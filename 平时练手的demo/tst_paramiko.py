#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.30.9',port=22,username='git_log',password='git_log')
stdin,stdout,stderr = ssh.exec_command('git log .')
if stderr != 0:
    print('error')
else:
    result = stdout.read()
ssh.close()