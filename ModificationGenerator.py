#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
this is for python 2.7
this scripts use command:
git log tag1...tag2  git log tag1..HEAD
return:
create a log_update.txt file to record changes between two tags
如果使用 subprocess.Popen，就不使用 Popen.wait()，而使用 Popen.communicate() 来等待外部程序执行结束.
ps.communicate()就是阻塞当前线程来执行具体的语句.

subprocess.call()
Depending on how you want to work your script you have two options. If you want the commands to block and not do anything while it is executing,
you can just use subprocess.call.
subprocess.Popen()
If you want to do things while it is executing or feed things into stdin, you can use communicate after the popen call.

结论：如果使用 subprocess.Popen，就不使用 Popen.wait()，而使用 Popen.communicate() 来等待外部程序执行结束
'''
import getopt
import os
import subprocess
import sys
import time

# raw_input for python 2.7, 3.x use input()
# from __builtin__ import raw_input

__author__ = "qiancheng"

PWD = os.getcwd()


def shell(cmd, env=None):
    if sys.platform.startswith("linux"):
        sp = subprocess.Popen(['/bin/bash', '-c', cmd], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = sp.communicate()
    else:
        sp = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = sp.communicate()
    return sp.returncode, stdout, stderr


def tag_handler(tag1, tag2):
    repoc_flag = False
    os.chdir(PWD)
    if os.path.isfile("log_update.txt"):
        os.remove("log_update.txt")
    path_list = os.getcwd().split(os.path.sep)
    repo_path = "/".join(path_list[:3])
    os.chdir(os.path.join(repo_path,"bin"))
    if os.path.isfile("repoc"):
        repoc_flag = True
    os.chdir(PWD)
    with open("git_list.txt", "w+") as f:
        if repoc_flag:
            ret_code, stdout, stderr = shell("repoc list | awk '{print $1}'")
        else:
            ret_code, stdout, stderr = shell("repo list | awk '{print $1}'")
        if ret_code != 0:
            print(stderr)
            sys.exit(1)
        f.write(stdout)
        f.flush()
        time.sleep(1)
        f.seek(0,0)
        for line in f:
            line=line.strip()
            os.chdir(os.path.join(PWD, line))
            with open(r"{0}/log_update.txt".format(PWD), "a") as update_f:
                #ret_code, stdout, stderr = shell("git log --oneline {0}...{1}".format(tag1, tag2))
                ret_code, stdout, stderr = shell('git log  --pretty=format:"%an"\ "%h"\ "%s" {0}...{1}'.format(tag1, tag2))
                if ret_code != 0:
                    tag_ret_code,tag_stdout,tag_stderr = shell("git tag")
                    if tag1 not in tag_stdout:
                        print("new git repertory {0}".format(line))
                        update_f.write("######## NEW PATH:{0}".format(line) + "\n")
                        update_f.write("\n\n")
                        continue
                    else:
                        print(stderr)
                        sys.exit(1)
                else:
                    if stdout:
                        update_f.write("########PATH:{0}".format(line)+"\n")
                        update_f.write(stdout)
                        update_f.write("\n\n")


def show_tag_info():
    os.chdir(PWD)
    if os.path.isdir("wind"):
        os.chdir(os.path.join(PWD, "wind"))
        ret_code, stdout, stderr = shell("git tag")
        if ret_code != 0:
            print(stderr)
            sys.exit(1)
        else:
            print("请选择打入tag的节点:\n" + stdout)
            tagname1 = raw_input("\033[1;36m输入上一次节点:\033[0m").strip()
            tagname2 = raw_input("\033[1;36m输入本次节点,默认为HEAD:\033[0m").strip()
            if not tagname1 or tagname1 not in stdout:
                print("tagname is error,will exit!")
                sys.exit(1)
            if not tagname2:
                tagname2 = "HEAD"
            tag_handler(tagname1, tagname2)


if __name__ == '__main__':
    show_tag_info()
