#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
根据record.log判断是否为efuse版本
把版本放到特定文件中
对文件进行打包,并且生成md5校验
checkmd5并且释放(manifest 和更改点一并释放)
'''
import hashlib
import os
import logging
import fileinput
import re
import shutil
import subprocess
import sys
import time
import zipfile
from zipfile import ZipFile

PWD = os.getcwd()
TOOLS_DIR = '/home/qiancheng/code/workspace/SCM_script'
buffer_size = 10240
DATE = time.strftime('%Y%m%d')
# owner = shell()

def shell(cmd, env=None):
    if sys.platform.startswith('linux'):
        p = subprocess.Popen(['/bin/bash', '-c', cmd], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return p.returncode, stdout, stderr


def log_config():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s---%(lineno)d---%(message)s'
    )


def parse_parameter():
    os.chdir(PWD)
    if os.path.exists("build-log"):
        for fi in fileinput.input("build-log/record.log"):
            if len(re.findall(r'efuse', fi)):
                sign_flag = False
            else:
                sign_flag = True
    logging.info("sign flag is: %s" % sign_flag)
    return sign_flag


def modify_release_file():
    for fi in fileinput.input('release_version_efuse.sh', inplace=True):
        logging.debug("efuse find /data/mine/test/MT6572: %s" % re.findall(r'/data/mine/test/MT6752', fi))
        if len(re.findall(r'/data/mine/test/MT6572', fi)):
            content = re.sub(r'/data/mine/test/MT6572/\$MY_NAME', 'archivement',fi)
            sys.stdout.write(content)
        else:
            sys.stdout.write(fi)


def zip_file(source,target):
    zipf = ZipFile(target,'w',allowZip64=True,compression=zipfile.ZIP_DEFLATED)
    for img in os.listdir(source):
        zipf.write(source + os.path.sep + img)
    zipf.close()


def do_checksum(route):
    logging.info("current dir %s" % os.getcwd())
    origin_dir = os.getcwd()
    os.chdir(route)
    '''
    目前shell下的CheckSum_Gen并不支持这样做checksum.
    所以现在只能用折中的方法,手动执行.
    '''
    # shutil.copy(TOOLS_DIR + os.path.sep + 'checksum.zip', '.')
    # ret,stdout,stderr = shell('unzip {0}'.format('checksum.zip'))
    # if ret != 0:
    #     print('unzip error')
    # sp = subprocess.Popen('./CheckSum_Gen',shell=True)
    # sp.wait()
    # # rm CheckSum_Gen.exe  FlashTool* CheckSum_Gen* libflashtool* checksum.zip
    # rm_list = ['CheckSum_Gen','CheckSum_Gen.ilk','CheckSum_Gen.pdb','checksum.zip']
    shutil.copy(TOOLS_DIR + os.path.sep + 'CheckSum_Gen.zip', '.')
    ret, stdout, stderr = shell('unzip {0}'.format('CheckSum_Gen.zip'))
    if ret != 0:
        print('unzip Checksum error')
        sys.exit(1)
    else:
        print('\033[0;32m %s \033[0m' % '请手动到当前路径的archivement里面手动执行checksum')
        while True:
            if os.path.exists('Checksum.ini'):
                sys.stdout.write(os.linesep)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(0.5)
    time.sleep(1)
    rm_list = ['CheckSum_Gen.exe','CheckSum_Gen.zip']
    for file in os.listdir('.'):
        if file.startswith('FlashToolLib') or file in rm_list:
            logging.info('delete file >> %s' % file)
            os.remove(file)
    os.chdir(origin_dir)

def release_file_handler(flag):
    os.chdir(PWD)
    if os.path.exists('archivement'):
        shutil.rmtree('archivement')
    os.mkdir('archivement')

    with open('version','r') as f:
        data = f.read()
        matcher = re.search(r'INVER=(.*)',data)
        logging.info('dl_name %s' % matcher.group(1))
        if matcher.group(1):
            dl_name =matcher.group(1)
        else:
            print('match err')

    if flag:
        shutil.copy('./tools/wind/release_version_efuse.sh', './')
        modify_release_file()
        # ret, stdout, stderr = shell('./release_version_efuse.sh A460 ota')
        sp = subprocess.Popen('./release_version_efuse.sh A460 ota',shell=True)
        sp.wait()
        # logging.info('./release_version_efuse.sh',stdout)
    else:
        modify_release_file()
        sp = subprocess.Popen('./release_version.sh A460 ota',shell=True)
        sp.wait()

    os.chdir('archivement')
    os.mkdir(dl_name)
    file_list = os.listdir('.')
    for file in file_list:
        if file.startswith('full_A460-ota'):
            os.rename(file, 'update.zip')
        elif file.startswith('full') or file.startswith('vmlinux') or file.startswith('update'):
            continue
        else:
            shutil.move(file,dl_name)

    do_checksum(dl_name)
    logging.info('now ready to zip DL imgages,plz hold on')
    zip_file(dl_name,dl_name + '.zip')

    origin_dir = os.getcwd()
    os.chdir(PWD)
    sp = subprocess.Popen("repoc manifest -ro manifest-{0}_{1}.xml".format(dl_name,DATE),shell=True)
    sp.wait()
    shutil.copy("{0}_{1}.xml".format(dl_name,DATE),'archivement')
    # os.chdir(origin_dir)

    # 生成log_update.csv
    # os.chdir(TOOLS_DIR)
    snapshots = []
    shutil.copy('{0}/shell_script/get_snapshot_commit_diff.sh'.format(TOOLS_DIR),'.')
    for file in os.listdir('.'):
        if file.startswith('manifest'):
            snapshots.append(file)
            snapshots = sorted(snapshots,key=lambda x:os.path.getctime(file),reverse=True)
            logging.info("snapshots sorted %s" % snapshots)
    shell('./get_snapshot_commit_diff.sh {1} {0}'.format(snapshots[0],snapshots[1]))
    if os.path.exists('log_update.csv'):
        shutil.copy('log_update.csv','./archivement')
    else:
        print('execute get_snapshot_commit_diff.sh error!')
    if os.path.exists('updateB2C.zip'):
        shutil.copy('updateB2C.zip','./archivement')

def do_md5():
    os.chdir(os.path.join(PWD, "archivement"))
    md5_list = []
    md5_info = {}
    for img in os.listdir('.'):
        if img.endswith('zip'):
            md5_list.append(img)
    logging.info('md5list >>%s' % md5_list)
    for file in md5_list:
        file_hash = hashlib.md5()
        with open(file,'rb') as hf:
            while True:
                b = hf.read(buffer_size)
                if not b:
                    break
                file_hash.update(b)
        # file_hash.hexdigest()
        md5_info[file] = file_hash.hexdigest()

    with open('checklist.md5','w') as chf:
        chf.write('/*'+os.linesep)
        chf.write('* wind-mobi md5sum checklist'+ os.linesep)
        chf.write('*/' + os.linesep)
        for key in md5_info:
            chf.write(md5_info[key] + ' *' + key + os.linesep)



def release_file_to_routeway():
    os.chdir(os.path.join(PWD, "archivement"))

    ret,stdout,stderr = shell('whoami')
    if ret != 0:
        print(stderr)
    else:
        my_name = stdout
    out_path = '/data/mine/test/MT6572/{0}'.format(my_name)

    for img in os.listdir('.'):
        if img.endswith('zip'):
            shutil.copy(img,out_path)
        if img.endswith('xml') or img.endswith('csv') or img.endswith('md5'):
            shutil.copy(img,out_path)


if __name__ == '__main__':
    log_config()
    sign_flag = parse_parameter()
    release_file_handler(sign_flag)
    do_md5()
    release_file_to_routeway()
