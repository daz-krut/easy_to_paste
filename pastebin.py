#!/usr/bin/env python3
# coding: utf-8
# 
# ------------------
# By: Keika.H
# https://ir1s.com/
# ------------------
 
import os
from getpass import getpass
import requests
import sys
 
base_url = 'https://pastebin.com/api/api_post.php'
dev_key = 'Change here to your unique developer api key. See https://pastebin.com/api'
login_base_url = 'https://pastebin.com/api/api_login.php'
 
__doc__ = """
Usage:
   {file} <file> If you don't use options, the file will be uploaded as gest.
   {file} [-f | --file] [-t | --title] [-s | --syntax] [-e | --expire] [-l | --login] [-p | --private]
   {file} [-h | --help]
 
Options:
   -f --file <file>        File you want to paste to Pastebin.com
   -t --title <string>     The name or title of your paste
   -s --syntax <string>    Your paste format.
   -e --expire <string>    The expiration date of your paste.
                           N = Never, 10M = 10 mins, 1H = 1 hour, 1D = 1 day, 2W = 2 weeks,
                           1M = 1 month, 6M = 6 months, 1Y = 1 year.
   -l --login <int>        You login and your paste belongs to your account.
   -p --private <int>      1 -> Private, 2 -> Unlisted, 0 -> Public. (Default:0)
 
Examples:
   {file} test.php
   {file} -f ~/test.php -t test.php -s php -e 10M -l -p 1
""".format(file=__file__)
 
 
def Login():
    info = {'api_dev_key': dev_key, 'api_user_name': '', 'api_user_password':''}
 
    info['api_user_name'] = input('User Name: ')
    info['api_user_password'] = getpass()
 
    raw_resp = requests.post(login_base_url, info)
    resp = raw_resp.text
 
    if resp.find('Bad') != -1 :
        print(resp)
        exit()
   
    # User Key
    return resp
 
def parse():
    argv = sys.argv
    argc = len(argv)
 
    info = {'api_dev_key':dev_key}
 
    if(argc < 2):
        print(__doc__)
        exit()
 
    # did the user input -h?
    if(argc == 2):
        if('-h' in argv or '--help' in argv):
            print(__doc__)
            exit()
        else: # Paste
            if(os.path.exists(argv[1]) == False): # ファイルが存在しない
                print('{} doesn\'nt exist.'.format(argv[1]))
                print(__doc__)
                exit()
 
    # Get paste text when user didn't use option -h
    for i in argv:
        if(os.path.exists(i) == True):
            with open(i, 'r') as f:
                info['api_paste_code'] = f.read()
 
    # Paste text
    if('-f' in argv or '--file' in argv):
        index = 0
        if('-f' in argv):
            index = argv.index('-f') + 1
        if('--file' in argv):
            index = argv.index('--file') + 1
        with open(argv[index], 'r') as f:
            info['api_paste_code'] = f.read()
 
    q = (lambda c: argv.index(c) + 1)
    # Paste title
    if('-t' in argv or '--title' in argv):
        if('-t' in argv):
            info['api_paste_name'] = argv[q('-t')]
        if('--title' in argv):
            info['api_paste_name'] = argv[q('--title')]
 
    # Paste format
    if('-s' in argv or '--syntax' in argv):
        if('-s' in argv):
            info['api_paste_format'] = argv[q('-s')]
        if('--syntax' in argv):
            info['api_paste_format'] = argv[q('--syntax')]
 
    # Paste expire
    if('-e' in argv or '--expire' in argv):
        if('-e' in argv):
            info['api_paste_expire_date'] = argv[q('-e')]
        if('--expire' in argv):
            info['api_paste_expire_date'] = argv[q('--expire')]
 
    # login
    if('-l' in argv or '--login' in argv):
        info['api_user_key'] = Login()
   
    # Private, unlisted or listed
    if('-p' in argv or '--private' in argv):
        if('-p' in argv):
            info['api_paste_private'] = int(argv[q('-p')])
        if('--private' in argv):
            info['api_paste_private'] = int(argv[q('--private')])
 
    info['api_option'] = 'paste'
 
    return info
 
if __name__ == '__main__':
    info = parse()
   
    raw_resp = requests.post(base_url, info)
    resp = raw_resp.text
 
    print(resp)
