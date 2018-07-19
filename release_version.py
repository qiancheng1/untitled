import fileinput
import os
import re
import shutil
import subprocess
import sys
import logging

'''
./release_version.py A460 all zip
'''
ROOT = os.getcwd()
MY_NAME = subprocess.Popen("whoami", shell=True)
BUILD_PROP = "out/target/product/A460/system/build.prop"
INNER_VER = ""
ZIP_FLAG = False
OUTPATH = "out/target/product"
release_project = "A460"
release_type = "all"


def logging_info():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s-%(lineno)d-%(message)s"
    )


def shell(cmd, env=None):
    if sys.platform.startswith("linux"):
        p = subprocess.Popen(["/bin/bash", "-c", cmd], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr, stdout = p.communicate()
    return p.returncode, stdout, stderr


def check_parameter(params):
    global ZIP_FLAG
    global release_type
    global release_project
    project_list = ["A460", "A515"]
    release_type_list = ["ota", "otapackge", "all", "diff"]
    for param in params:
        if param in project_list:
            release_project = param
        elif param in release_type_list:
            release_type = param
        elif param not in release_type_list:
            release_type = "all"
        elif param == "zip":
            ZIP_FLAG = True
        else:
            print("error! release project is null!")
            sys.exit(1)


def process_release_version():
    os.chdir(ROOT)
    if os.path.exists("version_package"):
        shutil.rmtree("version_package")
    os.mkdir("version_package")


def process_ota_file():
    pass


def process_diff_file():
    pass


def parse_args():
    args_list = sys.argv[1:]
    if len(args_list) != 0:
        args_set = set(args_list)
        logging.info("args set:", args_set)
        check_parameter(args_set)
        for param in args_set:
            if param == "all":
                process_release_version()
            elif param == "ota" or param == "otapackage":
                process_ota_file()
            elif param == "diff":
                process_diff_file()


def get_version_info():
    os.chdir(ROOT)
    global INNER_VER
    if os.path.exists(BUILD_PROP):
        for fi in fileinput.input(BUILD_PROP):
            match = re.search(r"(ro\.build\.version\.plan\.inner=)(.*)", fi)
            INNER_VER = match.group(2)


def check_build_status():
    # 截取最后50行内容
    os.chdir(os.path.join(ROOT, "build-log"))
    with open("build.log", "r") as f:
        offset = -80
        while True:
            f.seek(offset, -2)
            data_list = f.readlines()
            if len(data_list) < 50:
                offset += -80
            else:
                result = re.findall(r"successfully", data_list, re.I)
                if result:
                    succ_flag = True
                else:
                    succ_flag = False
                break
    return succ_flag


def init_config():
    logging.info("start to init config")
    global OUTPATH
    if release_project == "A460":
        HARDWARE_VER = "S01"
        OUTPATH = OUTPATH + os.path.sep + "A460"
        PLATFORM = "MT6739"
    elif release_project == "A515":
        HARDWARE_VER = "S01"
        OUTPATH = OUTPATH + + os.path.sep + "A515"
        PLATFORM = "MT6739"

    if os.path.exists(BUILD_PROP):
        retcode, stdout, stderr = shell('grep -n "ro.product.hardware=*" {0} | cut -d "=" -f 2'.format(BUILD_PROP))
        HARDWARE_VER = stdout

    os.chdir(OUTPATH)
    if os.path.exists("Modem_Database_ulwctg"):
        release_list = ["logo.bin", "{0}_Android_scatter.txt", "preloader_{1}.bin", "AP_Database",
                        "Modem_Database_ulwtg", "boot.img", "secro.img",
                        "userdata.img", "lk.img", "recovery.img", "cache.img", "mcupmfw.img", "md1dsp.img",
                        "loader_ext.img", "spmfw.img", "tee.img", "md1img.img", "odmdtbo.img", "vendor.img",
                        "system.img".format(PLATFORM, release_project)]
    elif os.path.exists("Modem_Database_ulwtg"):
        release_list = ["logo.bin", "{0}_Android_scatter.txt", "preloader_{1}.bin", "AP_Database",
                        "Modem_Database_ulwctg", "boot.img", "secro.img",
                        "userdata.img", "lk.img", "recovery.img", "cache.img", "mcupmfw.img", "md1dsp.img",
                        "loader_ext.img", "spmfw.img", "tee.img", "md1img.img", "odmdtbo.img", "vendor.img",
                        "system.img".format(PLATFORM, release_project)]
    else:
        release_list = ["logo.bin", "{0}_Android_scatter.txt", "preloader_{1}.bin", "AP_Database",
                        "Modem_Database_ulwctg", "boot.img", "secro.img",
                        "userdata.img", "lk.img", "recovery.img", "cache.img", "mcupmfw.img", "md1dsp.img",
                        "loader_ext.img", "spmfw.img", "tee.img", "md1img.img", "odmdtbo.img", "vendor.img",
                        "system.img".format(PLATFORM, release_project)]


if __name__ == "__main__":
    logging_info()
    result = check_build_status()
    if result:
        get_version_info()
    else:
        logging.error("compile error, see build.log for more information")
        sys.exit(1)
    parse_args()
    init_config()
