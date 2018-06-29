###.PyOS.0.1.2.4_DEV1.### #
# TO DO LIST
#
# Fix no internet crash                          x
#   
# 
#
#
#
#
lisence = '''
MIT License

Copyright (c) 2018 - 20xx Sam Forrester

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Encryption / Decryption code - https://www.blog.pythonlibrary.org/2016/05/18/python-3-an-intro-to-encryption/
Voice Recognition - https://pythonspot.com/speech-recognition-using-google-speech-api/
 ~~ Both of these codes have been modified, but the framework was based on these.
'''
######################
print("[  OS  ] Importing core modules...")
import os
os.system("clear")
os.system("cls")
print("[  OK  ] OS")
import time
print("[  OK  ] Time")
import platform
print("[  OK  ] Platform")
print("[  OK  ] Core modules imported")
print("[  OS  ] Checking System...")
print("[  OK  ] Machine type: " + platform.machine())
print("[  OS  ] Checking OS...")
wname = platform.system()
if ("Windows") in wname:
    print("[  OK  ] OS: " + wname)
    print("[  OK  ] Supported OS")
else:
    print("[  OS  ] OS: " + wname)
    print("You are using an unsupported OS!")
    print("Currently, PyOS is only supported on Windows.")
    print("Exiting in 5 seconds.")
    time.sleep(5)
    exit()
print("[  OK  ] Win Version: " + platform.platform())
print("[  OK  ] Machine supported")
import sys
print("[  OK  ] Sys")
import getpass
print("[  OK  ] Getpass")
import re
print("[  OK  ] Re")
import shutil
print("[  OK  ] Shutil")
import hashlib
print("[  OK  ] Hashlib")
import glob
print("[  OK  ] Glob")
import urllib.request
print("[  OK  ] Urllib.request")
import random
print("[  OK  ] Random")
##################################
##################################################
global credit
credit = '''
CREDIT
General Coding by Sam Forrester, (C) 2018 - 20xx
This program is protected under the MIT Lisence.
See source code for more info.

Encryption / Decryption and Voice Recognition code
referances can be found in the source code.

Thanks to Mike Atkinson and Stack Overflow for
other various tips.
'''
#######
if not os.path.exists("ske.dll"):
    print("[  OS  ] Checking for crash...")
    if os.path.exists("crashhandler.dll"):
        print("[      ]")
        print("[      ]")
        print("[  OS  ] A crash / unexpected shutdown was detected!")
        print("[  OS  ] If this was an error, Please report it on Github")
        print("[  OS  ] Include details of what you were doing, etc etc")
        print("[  OS  ] Boot will continue in 5 seconds")
        print("[      ]")
        time.sleep(1)
        print("[      ]")
        time.sleep(1)
        print("[      ]")
        time.sleep(1)
        print("[      ]")
        time.sleep(1)
        print("[      ]")
        time.sleep(1)
        print("[      ]")
    else:
        print("[  OK  ] No crash detected")
        if os.path.exists("crashhandlernull.dll"):
            os.rename("crashhandlernull.dll", "crashhandler.dll")
        else:
            os.system("echo crashhandler >> crashhandler.dll")
print("[  OS  ] Defining Variables")
global pyos_ver
global pyos_iden_ver
global pyos_upd_cc
global pyos_osn
global pyos_aun
global pyos_permaun
global pyver
global code
global password_write
global pyos_tempadm
global pyos_fallback
global connection
global config_resize
global config_autologin
global configbytes
global config_devmode
global config_forceadmin
global config_update
config_resize = "Resize1"
config_autologin = "Autologin0"
config_devmode = "Devmode0"
config_forceadmin = "Forceadmin0"
config_update = "Update1"
config_acccreate = "AccountCreation1"
try:
    update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyOS/master/PyOS.py')
    response = urllib.request.urlopen(update)
    newcode = response.read()
    master = newcode.decode()
    print("[  OK  ] Connection Established")
    connection = True
except:
    print("[  OK  ] No connection, updates disabled")
    connection = False
configbytes = 'PyOS Config//Resize1//Autologin0//Devmode0//Forceadmin1//Update0//AccountCreation1//PauseStart0' ##Used for config file
pyos_fallback = False ##used to determine how the program runs, with or without pycryptodomex essentially
code = 'pyosenckey' ##used for encryption/decryption - default is 'pyosenckey'. You can change this, but any existing passwords will not work. ##may be redundant now, can't be asked to check if it's still used anywhere
pyos_upd_cc = False ##used to check for updates 
pyos_ver = str("PyOS 0.1.2.4 Developer R2") ##used as title
pyos_osn = getpass.getuser() ##default user
pyos_tempadm = False ##used if user accesses admin account during session
pyver = platform.python_version() ##used to determine version
pyos_iden_ver = ("###.PyOS.0.1.2.4_DEV1.###") ##used to check for updates as well
pyos_aun = getpass.getuser() ##admin user (changes)
pyos_permaun = getpass.getuser() ##admin user (permanent)
password_write = 'pyos_pass_write_to_file_encryption_key' ##written to password files, helps prevent eL1T3 HaX0r5
print("[  OK  ] Done")
if pyver > ("3.6"):
    print("You are using an unsupported version of Python!")
    print("PyOS works best on Python 3.0 to 3.5")
    print("Thanks!")
    os.system("pause")
    pyos_exitscript()
if pyver <= ("2.9"):
    print("You are using an unsupported version of Python!")
    print("PyOS works best on Python 3.0 to 3.5")
    print("Thanks!")
    os.system("pause")
    pyos_exitscript()   
print("[  OK  ] Supported Python Version")
os.system("title " + pyos_ver)
if os.path.exists("UpdateClient.py"):
    os.remove("UpdateClient.py")
if os.path.exists("UpdateClientBK.py"):
    os.remove("UpdateClientBK.py")
if os.path.exists("update.pyd"):
    os.remove("update.pyd")
def pyos_exitscript():
    if os.path.exists("PyOS.py"):
        try:
            os.rename("crashhandler.dll", "crashhandlernull.dll")
        except:
            exit()
        exit()
    else:
        os.chdir("..")
        pyos_exitscript()
def pyos_boot():
    if os.path.exists("PyOS_Data"):
        os.chdir("PyOS_Data")
        if os.path.exists("config.bin"):
            with open('config.bin', 'rb') as config_read:
                config = config_read.read()
                config = bytes(config)
                config = config.decode('utf-8')
                config = config.split('//')
                for letter, number in enumerate(config):
                    print("[  OK  ]", number) ##What's that? Streamlined coding? Never heard of it ##Sidenote, it got worse
                global config_resize
                global config_autologin
                global config_devmode
                global config_forceadmin
                global config_update
                global config_acccreate
                global config_pausestart
                try:
                    config_resize = config[1]
                    config_autologin = config[2]
                    config_devmode = config[3]
                    config_forceadmin = config[4]
                    config_update = config[5]
                    config_acccreate = config[6]
                    config_pausestart = config[7]
                except:
                    config_read.close()
                    print("[  OK  ] Failed to assign config variables")
                    print("[  OK  ] Rewriting defaults")
                    os.system("attrib -s -h config.bin")
                    os.remove('config.bin')
                    with open('config.bin', 'wb') as config_write:
                        config_write.write(bytes(configbytes, "UTF-8"))
                        config_write.close()
                    os.system("attrib +s +h config.bin")
                    time.sleep(1)
                    print("[  OK  ] Reset")
                    print("[  OK  ] Retrying...")
                    time.sleep(1)
                    os.chdir('..')
                    pyos_boot()
        else:
            print("[  OK  ] Config not found")
        try:
            os.chdir(pyos_osn)
        except:
            pyos_set()
    pyos_dr = os.getcwd()
    if "PyOS_Data" in pyos_dr:
        print("[  OS  ] Checking Files...")
        if os.path.exists("data_pm.bin") or os.path.exists("psdef.bin"):
              print("[  OK  ] Assuming account exists")
              try:
                global RSA
                global AES
                global get_random_bytes
                global PKCSl_OAEP
                from Cryptodome.PublicKey import RSA
                print("[  OK  ] RSA Import")
                from Cryptodome.Cipher import PKCS1_OAEP
                print("[  OK  ] PKCSl_OAEP Import")
                from Cryptodome.Cipher import AES
                print("[  OK  ] AES Import")
                from Cryptodome.Random import get_random_bytes
                print("[  OK  ] Random Import")
              except:
                pyos_cryfail()
              if not os.path.exists("psdef.bin"):
                  pyos_0114setup()
              print("[  OK  ] Booting!")
              if os.path.exists("stp.dev"):
                  os.remove("stp.dev")
              if os.path.exists("stp.null"):
                    os.remove("stp.null")
              if config_pausestart == "PauseStart1":
                  print("[  OK  ] Start pause enabled")
                  os.system("pause >nul")
              if config_resize == "Resize1":
                  os.system("@mode con cols=50 lines=34")
              if config_autologin == "Autologin1":
                  print("Auto login enabled.")
                  print("Welcome, " + pyos_osn + ".")
                  pyos_os_ad()
              pyos_login()
        else:
            os.chdir('..')
            try:
                global RSA
                global AES
                global get_random_bytes
                global PKCSl_OAEP
                from Cryptodome.PublicKey import RSA
                print("[  OK  ] RSA Import")
                from Cryptodome.Cipher import PKCS1_OAEP
                print("[  OK  ] PKCSl_OAEP Import")
                from Cryptodome.Cipher import AES
                print("[  OK  ] AES Import")
                from Cryptodome.Random import get_random_bytes
                print("[  OK  ] Random Import")
            except:
                pyos_cryfail()
            pyos_set()
    else:
        os.mkdir("PyOS_Data")
        os.chdir("PyOS_Data")
        try:
            global RSA
            global AES
            global get_random_bytes
            global PKCS1_OAEP
            from Cryptodome.PublicKey import RSA
            print("[  OK  ] RSA Import")
            from Cryptodome.Cipher import AES
            print("[  OK  ] AES Import")
            from Cryptodome.Cipher import PKCS1_OAEP
            print("[  OK  ] PKCSl_OAEP Import")
            from Cryptodome.Random import get_random_bytes
            print("[  OK  ] Random Import")
        except:
            pyos_cryfail()
        print("[  OK  ] Assuming setup is required")
        print("[  OK  ] Booting!")
        if config_resize == "Resize1":
            os.system("@mode con cols=50 lines=34")
        pyos_set()
def pyos_0114setup():
    os.system("attrib -h -s prkey.bin")
    os.system("attrib -h -s pukey.bin")
    os.system("attrib -h -s data_pm.bin")
    os.system("cls")
    if config_resize == "Resize1":
        os.system("@mode con cols=50 lines=34")
    print("##################################################")
    print("")
    print("                      Py OS                       ")
    print("                     Account                      ")
    print("                     Manager                      ")
    print("")
    print("")
    print("###################################################")
    print("Welcome to PyOS 0.1.1.4!")
    print("Some security changes have been made,")
    print("so the admin must re-enter their password.")
    print("No accounts will be affected.")
    passwordcheck = getpass.getpass("")
    print("Please type your password again.")
    passwordre = getpass.getpass("")
    if passwordcheck == passwordre:
        try:
            with open('data_pm.bin', 'rb') as fobj:
                private_key = RSA.import_key(
                    open('prkey.bin').read(),
                    passphrase=code)
                enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                            for x in (private_key.size_in_bytes(), 
                                                            16, 16, -1) ]
                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        except:
            print("Failed to decrypt password.")
            print("Ensure the key is correct in the source code.")
            os.system("pause")
            pyos_0114setup()
        datat = data.decode('ascii')
        if datat == passwordcheck:
            if len(passwordcheck) == 0:
                print("Passwords can no longer be empty!")
                print("Enter a new password...")
                passwordcheck = getpass.getpass("")
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(passphrase=passwordcheck, pkcs=8, 
                    protection="scryptAndAES128-CBC")
            with open('privkey.bin', 'wb') as f:
                    f.write(encrypted_key)
                    os.system("attrib +h privkey.bin")
            with open('pubkey.bin', 'wb') as f:
                    f.write(key.publickey().exportKey())
                    os.system("attrib +h pubkey.bin")
            with open('psdef.bin', 'wb') as out_file:
                recipient_key = RSA.import_key(
                    open('pubkey.bin').read())
                session_key = get_random_bytes(16)
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                out_file.write(cipher_rsa.encrypt(session_key))
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                data = bytes(password_write, encoding='utf-8')
                ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                out_file.write(cipher_aes.nonce)
                out_file.write(tag)
                out_file.write(ciphertext)
                os.system("attrib +h psdef.bin")
            print("")
            print("Update complete.")
            print("Press any key to go to menu.")
            os.system("pause >nul")
            pyos_login()
        else:
            print("Incorrect password!")
            print("Update cannot be completed without it.")
            print("Please try again.")
            os.system("pause >nul")
            pyos_0114setup()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        pyos_0114setup()
def pyos_0114setupuser():
    os.system("attrib -h -s prkey.bin")
    os.system("attrib -h -s pukey.bin")
    os.system("attrib -h -s data_pm.bin")
    passwordcheck = getpass.getpass("")
    if passwordcheck == passwordcheck:
        try:
            with open('data_pm.bin', 'rb') as fobj:
                private_key = RSA.import_key(
                    open('prkey.bin').read(),
                    passphrase=code)
                enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                            for x in (private_key.size_in_bytes(), 
                                                            16, 16, -1) ]
                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        except:
            print("Failed to decrypt password.")
            print("Ensure the key is correct in the source code.")
            os.system("pause")
            pyos_0114setup()
        datat = data.decode('ascii')
        if datat == passwordcheck:
            if len(passwordcheck) == 0:
                print("Passwords can no longer be empty!")
                print("Enter a new password...")
                passwordcheck = getpass.getpass("")
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(passphrase=passwordcheck, pkcs=8, 
                    protection="scryptAndAES128-CBC")
            with open('privkey.bin', 'wb') as f:
                    f.write(encrypted_key)
                    os.system("attrib +h privkey.bin")
            with open('pubkey.bin', 'wb') as f:
                    f.write(key.publickey().exportKey())
                    os.system("attrib +h pubkey.bin")
            with open('psdef.bin', 'wb') as out_file:
                recipient_key = RSA.import_key(
                    open('pubkey.bin').read())
                session_key = get_random_bytes(16)
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                out_file.write(cipher_rsa.encrypt(session_key))
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                data = bytes(password_write, encoding='utf-8')
                ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                out_file.write(cipher_aes.nonce)
                out_file.write(tag)
                out_file.write(ciphertext)
                os.system("attrib +h psdef.bin")
            print("")
            print("Update complete.")
            print("Press any key to continue.")
            os.system("pause >nul")
            if pyos_osn == pyos_aun:
                os.system("cls")
                print("##################################################")
                print("                      Py OS                       ")
                print("                       Sys                        ")
                print("                      -USR-                       ")
                print("##################################################")
                checkforlog = glob.glob("*.log")
                if not len(checkforlog) == 0:
                    logam = len(checkforlog)
                    logam = str(logam)
                    print("You have " + logam + " new admin logs.")
                pyos_os_us()
            os.system("cls")
            print("##################################################")
            print("                      Py OS                       ")
            print("                       Sys                        ")
            print("                      -USR-                       ")
            print("##################################################")
            pyos_os_us()
        else:
            print("Incorrect password!")
            print("Update cannot be completed without it.")
            print("Please try again.")
            os.system("pause >nul")
            pyos_0114setupuser()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        pyos_0114setupuser()
def pyos_skeset():
    if os.path.exists("PyOS.py"):
        if os.path.exists("ske.dll"):
            os.rename("ske.dll", "ske.null")
            print("Disabled ske.")
            os.chdir("PyOS_Data")
            os.chdir(pyos_osn)
            pyos_devconsole()
        if os.path.exists("ske.null"):
            os.rename("ske.null", "ske.dll")
            print("Enabled ske.")
            os.chdir("PyOS_Data")
            os.chdir(pyos_osn)
            pyos_devconsole()
        else:
            os.system("echo PyOS >> ske.dll")
            print("Enabled ske.")
            os.chdir("PyOS_Data")
            os.chdir(pyos_osn)
            pyos_devconsole()
    else:
        os.chdir("..")
        pyos_skeset()
def pyos_dsacc():
    os.chdir('..')
    dirs = os.listdir(os.getcwd())
    for number, letter in enumerate(dirs):
        if "###.PyOS" in letter:
            continue
        if pyos_aun == letter:
            continue
        print(letter)
    print("Enter name of account to disable/enable...")
    accdis = input("")
    if accdis == pyos_permaun:
        print("Cannot disable admin account.")
        os.chdir(pyos_osn)
        pyos_devconsole()
    try:
        os.chdir(accdis)
    except:
        print("Invalid account!")
        os.chdir(pyos_osn)
        pyos_devconsole()
    if os.path.exists("dbm.bin"):
        if not os.path.exists("dbmnull.bin"):
            os.rename("dbm.bin", "dbmnull.bin")
        else:
            os.system("attrib -h dbm.bin")
            os.remove("dbm.bin")
        print("Enabled " + accdis)
        os.chdir('..')
        os.chdir(pyos_osn)
        pyos_devconsole()
    if os.path.exists("dbmnull.bin"):
        os.rename("dbmnull.bin", "dbm.bin")
        print("Disabled " + accdis)
        os.chdir('..')
        os.chdir(pyos_osn)
        pyos_devconsole()
    os.system("echo disableaccount >> dbm.bin")
    os.system("attrib +h dbm.bin")
    print("Disabled " + accdis)
    os.chdir('..')
    os.chdir(pyos_osn)
    pyos_devconsole()
def pyos_accrecover():
    os.system("cls")
    print("##################################################")
    print("")
    print("                      Py OS                       ")
    print("                     Account                      ")
    print("                     Manager                      ")
    print("")
    print("")
    print("###################################################")
    print("")
    passwordcheck = getpass.getpass("Enter New Pass: ")
    passwordre = getpass.getpass("Retype New Pass: ")
    if passwordcheck == passwordre:
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=passwordcheck, pkcs=8, 
                protection="scryptAndAES128-CBC")
        with open('privkey.bin', 'wb') as f:
                f.write(encrypted_key)
                os.system("attrib +h privkey.bin")
        with open('pubkey.bin', 'wb') as f:
                f.write(key.publickey().exportKey())
                os.system("attrib +h pubkey.bin")
        with open('psdef.bin', 'wb') as out_file:
            recipient_key = RSA.import_key(
                open('pubkey.bin').read())
            session_key = get_random_bytes(16)
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            out_file.write(cipher_rsa.encrypt(session_key))
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            data = bytes(password_write, encoding='utf-8')
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            out_file.write(cipher_aes.nonce)
            out_file.write(tag)
            out_file.write(ciphertext)
            os.system("attrib +h psdef.bin")
        print("")
        print("Setup is complete!")
        print("Press any key to go to menu.")
        os.system("pause >nul")
        pyos_login()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        pyos_accrecover()
def pyos_login():
    os.system("cls")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("")
    print("                      Py OS                       ")
    print("                      Login                       ")
    print("                      -----                       ")
    print("")
    print("")
    print("##################################################")
    if connection == True:
        update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyOS/master/PyOS.py')
        response = urllib.request.urlopen(update)
        newcode = response.read()
        master = newcode.decode()
        tvers = master.split(" ")
        updatedev = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyOS/developer/PyOSDEV.py')
        responsedev = urllib.request.urlopen(updatedev)
        newcodedev = responsedev.read()
        masterdev = newcodedev.decode()
        tversdev = masterdev.split(" ")
        for number, line in enumerate(tvers):
            tms = str(line)
            break
        for number, line in enumerate(tversdev):
            tmsdev = str(line)
            break
        if not tmsdev == pyos_iden_ver:
            if config_devmode == "Devmode1":
                print("A developer update is available.")
                global pyos_upd_cc
                pyos_upd_cc = True
        if config_devmode == "Devmode0":
            if not tms == pyos_iden_ver:
                print("An update is available.")
                global pyos_upd_cc
                pyos_upd_cc = True
    print("1} Log In as " + pyos_osn)
    print("2} Switch user")
    if config_acccreate == "AccountCreation0":
        print("3} Exit")
    else:
        print("3} Create new user")
        print("4} Exit")
    pyos_login_c = input("")
    if pyos_login_c == ("1"):
        if pyos_fallback == True:
            pyos_fallbacklogin()
        print("Please enter your password, " + pyos_osn)
        enterpass = getpass.getpass("")
        try:
            with open('psdef.bin', 'rb') as fobj:
                private_key = RSA.import_key(
                    open('privkey.bin').read(),
                    passphrase=enterpass)
                enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                            for x in (private_key.size_in_bytes(), 
                                                            16, 16, -1) ]
                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        except:
            print("Failed to unlock account.")
            print("Is your password correct?")
            os.system("pause >nul")
            pyos_login()
        datat = data.decode('ascii')
        if datat == password_write:
            if os.path.exists("dbm.bin"):
                print("Your account has been disabled.")
                print("Contact the admin (" + pyos_permaun + ") for help.")
                os.system("pause >nul")
                pyos_login()
            print("Password Accepted.")
            fobj.close()
            os.system("pause >nul")
            if pyos_osn == pyos_aun:
                os.system("cls")
                if connection == True:
                    timedate = time.strftime('%H:%M', time.gmtime())
                    print("Connected                                    " + timedate)
                else:
                    timedate = time.strftime('%H:%M', time.gmtime())
                    print("Not Connected                                " + timedate)
                print("##################################################")
                print("                      Py OS                       ")
                print("                       Sys                        ")
                print("                      -ADM-                       ")
                print("##################################################")
                checkforlog = glob.glob("*.log")
                if not len(checkforlog) == 0:
                    logam = len(checkforlog)
                    logam = str(logam)
                    print("You have " + logam + " new admin logs.")
                pyos_os_ad()
            os.system("cls")
            if connection == True:
                timedate = time.strftime('%H:%M', time.gmtime())
                print("Connected                                    " + timedate)
            else:
                timedate = time.strftime('%H:%M', time.gmtime())
                print("Not Connected                                " + timedate)
            print("##################################################")
            print("                      Py OS                       ")
            print("                       Sys                        ")
            print("                      -USR-                       ")
            print("##################################################")
            pyos_os_us()
        else:
            print("Failed to unlock account.")
            print("Ensure password_write has not been changed.")
            fobj.close()
            os.system("pause >nul")
            pyos_login()
    elif pyos_login_c == ("2"):
        if pyos_fallback == True:
            print("Disabled in fallback mode")
            os.system("pause >nul")
            pyos_login()
        os.chdir('..')
        dirs = os.listdir(os.getcwd())
        print("")
        for number, letter in enumerate(dirs):
            if "###.PyOS" in letter:
                continue
            if pyos_aun == letter:
                print(letter, "(admin)")
                continue
            print(letter)
        print("")
        print("Enter the NAME of the user you want to switch to.")
        logswitch = input("")
        if logswitch == ("admin"):
            logswitch = pyos_permaun
        try:
            os.chdir(logswitch)
        except:
            print("User not found!")
            os.system("pause >nul")
            os.chdir(pyos_osn)
            pyos_login()
        if os.path.exists("psdef.bin") or os.path.exists("data_pm.bin"):
            if not os.path.exists("psdef.bin"):
                global pyos_osn
                pyos_osn = (logswitch)
                print("")
                print("Welcome to PyOS 0.1.1.4!")
                print("To finish preparing this update,")
                print("Please enter your password again.")
                pyos_0114setupuser()
            print("Switched to " + logswitch)
            global pyos_osn
            pyos_osn = (logswitch)
            os.system("pause >nul")
            pyos_login()
        else:
            if os.path.exists("appdata"):
                print("Corrupted Account!")
                recover = input("Attempt To Recover account? [y/n] ")
                if recover == ("y"):
                    pyos_accrecover()
                else:
                    pyos_login()
            print("Invalid account!")
            os.chdir('..')
            os.chdir(pyos_osn)
            os.system("pause >nul")
            pyos_login()
    elif pyos_login_c == ("3"):
        if config_acccreate == "AccountCreation0":
            pyos_exitscript()
        if pyos_fallback == True:
            print("Disabled in fallback mode")
            os.system("pause >nul")
            pyos_login()
        os.chdir('..')
        print("Enter a new username...")
        newusern = input("")
        if os.path.exists(newusern):
            print("User already exists!")
            os.chdir(pyos_osn)
            os.system("pause >nul")
            pyos_login()
        global pyos_osn
        pyos_osn = (newusern)
        pyos_set()
    elif pyos_login_c == ("4"):
        if config_acccreate == "AccountCreation0":
            pyos_login()
        pyos_exitscript()
    elif pyos_login_c == ("cd"):
        pyos_tempcd = os.getcwd()
        print(pyos_tempcd)
        os.system("pause >nul")
        pyos_login()
    elif pyos_login_c == ("devff"):
        if pyos_fallback == True:
            print("Disabled in fallback mode.")
            os.system("pause >nul")
            pyos_login()
        print(devmess)
        os.system("pause >nul")
        pyos_cryfail()
    else:
        pyos_login()
def pyos_fallbacklogin():
    pyos_dr_fall = os.getcwd()
    if not "fallback" in pyos_dr_fall:
        if os.path.exists("fallback"):
            os.chdir("fallback")
        else:
            os.mkdir("fallback")
            os.chdir("fallback")
    os.system("cls")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("                      Py OS                       ")
    print("                       Sys                        ")
    print("                      -ADM-                       ")
    print("##################################################")
    checkforlog = glob.glob("*.log")
    if not len(checkforlog) == 0:
        logam = len(checkforlog)
        logam = str(logam)
        print("You have " + logam + " new admin logs.")
    pyos_os_ad()
def pyos_set():
    os.system("cls")
    pyos_dr = os.getcwd()
    if not "PyOS_Data" in pyos_dr:
        os.chdir("PyOS_Data")
    if not os.path.exists(pyos_osn):
        os.mkdir(pyos_osn)
        os.chdir(pyos_osn)
        os.mkdir('appdata')
    if os.path.exists(pyos_osn):
        os.chdir(pyos_osn)
        if not os.path.exists("appdata"):
            os.mkdir('appdata')
    if config_resize == "Resize1":
        os.system("@mode con cols=50 lines=34")
    if pyos_fallback == True:
        if connection == True:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Connected                                    " + timedate)
        else:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Not Connected                                " + timedate)
        print("##################################################")
        print("")
        print("                     WELCOME                      ")
        print("                       T O                        ")
        print("                      Py OS                       ")
        print("                    Fall back                     ")      
        print("                     M o d e                      ")
        print("##################################################")
    else:
        if connection == True:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Connected                                    " + timedate)
        else:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Not Connected                                " + timedate)
        print("##################################################")
        print("")
        print("                     WELCOME                      ")
        print("                       T O                        ")
        print("                      Py OS                       ")
        print("")      
        print("")
        print("##################################################")        
    print("Hi, " + pyos_osn + "!")
    if pyos_fallback == True:
        pyos_setpsf()
    print("Let's set up your account.")
    print("Please enter a password.")
    print("Keystrokes will not be echoed.")
    pyos_setps()
def pyos_setps():
    passwordcheck = getpass.getpass("Enter New pass: ")
    passwordre = getpass.getpass("Retype New Pass: ")
    if passwordcheck == passwordre:
        if len(passwordcheck) == 0:
            print("Password cannot be 0 characters!")
            pyos_setps()
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=passwordcheck, pkcs=8, 
                protection="scryptAndAES128-CBC")
        with open('privkey.bin', 'wb') as f:
                f.write(encrypted_key)
                os.system("attrib +h privkey.bin")
        with open('pubkey.bin', 'wb') as f:
                f.write(key.publickey().exportKey())
                os.system("attrib +h pubkey.bin")
        with open('psdef.bin', 'wb') as out_file:
            recipient_key = RSA.import_key(
                open('pubkey.bin').read())
            session_key = get_random_bytes(16)
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            out_file.write(cipher_rsa.encrypt(session_key))
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            data = bytes(password_write, encoding='utf-8')
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            out_file.write(cipher_aes.nonce)
            out_file.write(tag)
            out_file.write(ciphertext)
            os.system("attrib +h psdef.bin")
        print("")
        print("Setup is complete!")
        print("Press any key to go to menu.")
        os.system("pause >nul")
        pyos_login()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        pyos_setps()
def pyos_setpsf():
    if os.path.exists("fallback"):
        os.chdir("fallback")
    else:
        os.mkdir("fallback")
        os.chdir("fallback")
    print("")
    print("A seperate account has been created.")
    print("A password is not needed to access this account.")
    os.system("pause >nul")
    pyos_login() 
def pyos_prog():
    os.system("cls")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("PyOS Apps")
    if not os.path.exists("appdata"):
        os.mkdir('appdata')
    os.chdir("appdata")
    avapps = glob.glob("*.py")
    avapps.extend(glob.glob("*.exe"))
    maxnum = len(avapps)
    maxnumext = maxnum + 5
    maxnumstr = str(maxnumext)
    print("")
    for number, letter in enumerate(avapps):
        trnu = number + 1
        trnus = str(trnu)
        letterm = letter.replace(".py", "")
        letterm = letterm.replace(".exe", "")
        print(trnus + ":", letterm)
    print("")
    print("Enter number of the app you want to start,")
    print("or type 'ext' to go back to terminal.")
    startapp = input("")
    if startapp == ("ext"):
        os.chdir('..')
        if pyos_osn == pyos_aun:
            pyos_os_ad()
        else:
            pyos_os_us()
    if re.match("^[A-Za-z]*$", startapp):
        print("Please only use numbers!")
        os.system("pause >nul")
        os.chdir('..')
        pyos_prog()
    startapp = int(startapp)
    startapp = startapp - 1
    if startapp < 0:
        print("Invalid choice!")
        os.system("pause")
        os.chdir('..')
        pyos_prog()
    if startapp < maxnum:
        appcc = avapps[startapp]
        appccx = appcc.replace(".py", "")
        appccx = appcc.replace(".exe", "")
        print("What would you like to do?")
        print("[s]tart app")
        print("[u]ninstall app")
        appccd = input("")
        if appccd == ("s"):
            print("Starting " + appccx)
            os.startfile(appcc)
            os.chdir('..')
            pyos_prog()
        elif appccd == ("u"):
              print("Deleting...")
              try:
                 os.remove(appcc)
                 print("Deleted!")
                 os.system("pause")
                 os.chdir('..')
                 pyos_prog()
              except:
                  print("Could not delete.")
                  os.system("pause")
                  os.chdir('..')
                  pyos_prog()
        else:
              print("Cancelled.")
              os.system("pause")
              os.chdir('..')
              pyos_prog()
    else:
        print("Invalid choice!")
        os.system("pause")
        os.chdir('..')
        pyos_prog()
    pyos_os_us()
def pyos_mus():
          os.system("pause")
def pyos_browse():
          os.system("pause")
def pyos_os_us():
    global pyos_aun
    os_input = input(">>")
    if os_input == ("help"):
        print("PyOS Commands")
        print("help - Displays this menu")
        print("ext - Exits")
        print("lgt - Logs out of account")
        print("app - Displays list of available apps")
        print("cls - Clears screen")
        print("enc - Encryption Tool")
        print("dnc - Read Encrypted Files")
        print("typ - Word Processor")
        print("rdf - Read Files")
        print("lsf - List Files")
        print("ret - Return program / system info")
        print(" ~use ret [info]")
        print(" ~E.g, time, ver, date, etc")
        print("adm - Switch To Administrator")
        print("crd - Credits")
        pyos_os_us()
    if "ret" in os_input:
        osin = os_input.split(" ")
        if not len(osin) == 2:
            print("Usage: ret [info]")
            pyos_os_us()
        lookup = osin[1]
        if lookup == "time":
            print(time.strftime('%H:%M:%S', time.gmtime()))
            pyos_os_us()
        if lookup == "date":
            print(time.strftime('%m-%d-%Y', time.gmtime()))
            pyos_os_us()
        if lookup == "ver":
            print(pyos_ver + " Running on Python " + pyver)
            pyos_os_us()
        else:
            print("Unrecognized lookup")
            pyos_os_us()
    if os_input == ("crd"):
        print(credit)
        pyos_os_us()
    elif os_input == ("ext"):
        pyos_exitscript()
    elif os_input == ("lgt"):
        if pyos_osn == ("tmpacc"):
            print("Exiting...")
            os.system("pause >nul")
            pyos_exitscript()
        if pyos_aun == pyos_osn:
            pyos_tempadm = False
            pyos_aun = (getpass.getuser())
        print("Logging out...")
        os.system("pause >nul")
        pyos_login()
    elif os_input == ("app"):
        pyos_prog()
    elif os_input == ("cls"):
        os.system("cls")
        if connection == True:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Connected                                    " + timedate)
        else:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Not Connected                                " + timedate)
        print("##################################################")
        print("                      Py OS                       ")
        print("                       Sys                        ")
        print("                      -USR-                       ")
        print("##################################################")
        pyos_os_us()
    elif os_input == ("enc"):
        pyos_enc()
    elif os_input == ("dnc"):
        pyos_dnc()
    elif os_input == ("typ"):
        print("###")
        print("Start typing to begin...")
        pyos_word = input("")
        print("")
        print("Enter name for file (Do not include filetypes).")
        pyos_wordname = input("")
        pyos_wordb = pyos_word.encode()
        pyos_word_txt = (pyos_wordname + ".txt")
        try:
            with open(pyos_word_txt, 'wb') as pw:
                pw.write(pyos_wordb)
        except:
            print("Failed to save.")
            pyos_os_us()
        print("Saved!")
        pw.close()
        pyos_os_us()
    elif os_input == ("cps"):
        print("")
        if pyos_fallback == True:
            print("Disabled in fallback mode.")
            pyos_os_ad()
        print("Enter your current password...")
        enterpass = getpass.getpass("")
        if len(enterpass) == 0:
            print("Password cannot be 0 characters!")
        try:
            with open('psdef.bin', 'rb') as fobj:
                private_key = RSA.import_key(
                    open('privkey.bin').read(),
                    passphrase=enterpass)
                enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                            for x in (private_key.size_in_bytes(), 
                                                            16, 16, -1) ]
                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            datat = data.decode('ascii')
        except:
            print("Incorrect password!")
            fobj.close()
            pyos_os_ad()
        if not datat == password_write:
            print("Incorrect password!")
            fobj.close()
            pyos_os_us()
        fobj.close()
        os.remove("psdef.bin")
        os.remove('privkey.bin')
        os.remove('pubkey.bin')
        print("Enter a new password...")
        passwordcheck = getpass.getpass("")
        print("Please type your password again.")
        passwordre = getpass.getpass("")
        if passwordcheck == passwordre:
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(passphrase=passwordcheck, pkcs=8, 
                    protection="scryptAndAES128-CBC")
            with open('privkey.bin', 'wb') as f:
                    f.write(encrypted_key)
                    os.system("attrib +h privkey.bin")
            with open('pubkey.bin', 'wb') as f:
                    f.write(key.publickey().exportKey())
                    os.system("attrib +h pubkey.bin")
            with open('psdef.bin', 'wb') as out_file:
                recipient_key = RSA.import_key(
                    open('pubkey.bin').read())
                session_key = get_random_bytes(16)
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                out_file.write(cipher_rsa.encrypt(session_key))
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                data = bytes(password_write, encoding='utf-8')
                ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                out_file.write(cipher_aes.nonce)
                out_file.write(tag)
                out_file.write(ciphertext)
                os.system("attrib +h psdef.bin")
            print("")
            print("Password changed.")
            pyos_os_us()
        else:
            print("Passwords do not match!")
            os.system("pause >nul")
            pyos_os_us()
    elif os_input == ("rdf"):
        print("Enter file name to open (Do not include filetype).")
        pyos_read = input("")
        pyos_read_txt = (pyos_read + ".txt")
        if os.path.exists(pyos_read_txt):
            print(pyos_read + " Contains...")
            print("")
            with open(pyos_read_txt, 'rb') as pr:
                for line in pr:
                    datat = line.decode('ascii')
                    print(datat)
                    pr.close()
                    pyos_os_us()
        else:
            print("File not found!")
            pyos_os_us()
    elif os_input == ("lsf"):
        files = glob.glob("*.*")
        encfiles = glob.glob("*")
        print("")
        print("Files found:")
        for number, letter in enumerate(files):
            trnu = number + 1
            trnus = str(trnu)
            if (".bin") in letter:
                continue
            if ("_enc") in letter:
                continue
            if letter == "dbmnull.bin":
                continue
            if letter == "dbm.bin":
                continue
            print(letter)
        print("")
        print("Encrypted files found:")
        for number, letter in enumerate(encfiles):
            trnu = number + 1
            trnus = str(trnu)
            if not ("_enc") in letter:
                continue
            letter = letter.replace("_enc", "")
            print(letter)
        print("")
        pyos_os_us()
    elif os_input == ("adm"):
        if config_forceadmin == "Forceadmin1":
            print("Force admin enabled.")
            print("Switched to admin!")
            pyos_os_ad()
        pyos_aun = getpass.getuser()
        if pyos_osn == pyos_aun:
            print("Switched to admin!")
            pyos_os_ad()
        else:
            os.chdir('..')
            os.chdir(pyos_aun)
            tryswitch = getpass.getpass("Enter admin (" + pyos_aun + ")'s password...")
            if len(tryswitch) == 0:
                print("Password cannot be 0 characters!")
                pyos_os_us()
            try:
                with open('psdef.bin', 'rb') as fobj:
                    private_key = RSA.import_key(
                        open('privkey.bin').read(),
                        passphrase=tryswitch)
                    enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                                for x in (private_key.size_in_bytes(), 
                                                                16, 16, -1) ]
                    cipher_rsa = PKCS1_OAEP.new(private_key)
                    session_key = cipher_rsa.decrypt(enc_session_key)
                    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
                datat = data.decode('ascii')
            except:
                os.chdir('..')
                os.chdir(pyos_aun)
                timedate = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
                timedateformat = timedate.replace(":", ".")
                logfail = str("The user '" + pyos_osn + "' attempted accessing your account with the password '" + tryswitch + "' on/at '" + timedate + "'")
                logname = str("failedlogin " + timedateformat + ".log")
                with open(logname, 'w') as log:
                    log.write(logfail)
                    log.close()
                print("Incorrect password!")
                print(pyos_aun + " has been alerted.")
                os.chdir('..')
                os.chdir(pyos_osn)
                pyos_os_us()
            if datat == password_write:
                os.chdir('..')
                os.chdir(pyos_aun)
                timedate = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
                timedateformat = timedate.replace(":", ".")
                logsucc = str("The user '" + pyos_osn + "' accessed your account on/at '" + timedate + "'")
                logname = str("successlogin " + timedateformat + ".log")
                with open(logname, 'w') as log:
                    log.write(logsucc)
                    log.close()
                os.chdir('..')
                os.chdir(pyos_osn)
                pyos_tempaun = pyos_aun
                pyos_aun == pyos_osn
                global pyos_tempadm
                pyos_tempadm = True
                fobj.close()
                print("Temporary access granted.")
                print(pyos_tempaun + " has been alerted.")
                pyos_os_ad()
            os.chdir('..')
            os.chdir(pyos_aun)
            timedate = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            timedateformat = timedate.replace(":", ".")
            logfail = str("The user '" + pyos_osn + "' attempted accessing your account with the password '" + tryswitch + "' on/at '" + timedate + "'")
            logname = str("failedlogin " + timedateformat + ".log")
            with open(logname, 'w') as log:
                log.write(logfail)
                log.close()
            print("Incorrect password!")
            print(pyos_aun + " has been alerted.")
            os.chdir('..')
            os.chdir(pyos_osn)
            pyos_os_us()
    else:
        print(os_input + " - Bad Input")
        pyos_os_us()
def pyos_config(): ##Hey user, if you're reading this, prepare for the worst piece of code you'll ever read
    print("")
    print("Reading config file...")
    os.chdir('..')
    if pyos_fallback == True:
        os.chdir('..')
    if os.path.exists("config.bin"):
        os.system("attrib -s -h config.bin")
        with open('config.bin', 'rb') as config_read:
            config = config_read.read()
            config = bytes(config)
            config = config.decode('utf-8')
            config = config.split('//')
            for letter, number in enumerate(config):
                print(number) ##I know it should be letter but that returns the numbers?? Probably just me putting letter, number in the wrong order oops
        print("Enter change to be made...")
        conf_input = input("")
        if not "0" in conf_input:
            if not "1" in conf_input:
                print("Invalid Selection.")
                os.system("attrib +s +h config.bin")
                os.chdir(pyos_osn)
                if pyos_fallback == True:
                    os.chdir('fallback')
                pyos_os_ad()
            pass
        cf_temp = conf_input.split()
        if not len(cf_temp) == 2:
            print("No change.")
            print("Ensure you use [config] [number]")
            os.system("attrib +s +h config.bin")
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
        cf = conf_input.split(" ")
        if cf[1] == "1":
            cf_alt = "0"
        if cf[1] == "0":
            cf_alt = "1"
        cf_raw = "".join(cf)
        del cf[1]
        cf.extend(cf_alt)
        cf_altraw = "".join(cf)
        if not cf_raw in config:
            if not cf_altraw in config:
                print("No change.")
                os.system("attrib +s +h config.bin")
                os.chdir(pyos_osn)
                if pyos_fallback == True:
                    os.chdir('fallback')
                pyos_os_ad()
            cf_change = config.index(cf_altraw)
            del config[cf_change]
            config.insert(cf_change, cf_raw)
            config_read.close()
            config = "//".join(config)
            time.sleep(1)
            os.remove("config.bin")
            time.sleep(1)
            with open('config.bin', 'wb') as config_write:
                config_write.write(bytes(config, "UTF-8"))
                config_write.close()
            print("Changed " + cf_altraw + " to " + cf_raw)
            os.system("attrib +s +h config.bin")
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
        cf_change = config.index(cf_raw)
        del config[cf_change]
        config.insert(cf_change, cf_altraw)
        config_read.close()
        config = "//".join(config)
        time.sleep(1)
        os.remove("config.bin")
        time.sleep(1)
        with open('config.bin', 'wb') as config_write:
            config_write.write(bytes(config, "UTF-8"))
            config_write.close()
        print("Changed " + cf_raw + " to " + cf_altraw)
        os.system("attrib +s +h config.bin")
        os.chdir(pyos_osn)
        if pyos_fallback == True:
            os.chdir('fallback')
        pyos_os_ad()
        os.system("pause")
    else:
        print("Writing Defaults...")
        with open('config.bin', 'wb') as config_write:
            config_write.write(bytes(configbytes, "UTF-8"))
            config_write.close()
        os.system("attrib +s +h config.bin")
        time.sleep(1)
        os.chdir(pyos_osn)
        if pyos_fallback == True:
            os.chdir('fallback')
        pyos_config()
def pyos_update():
    if os.path.exists("UpdateClient.py"):
        os.startfile("UpdateClient.py")
        pyos_exitscript()
    else:
        os.system("echo import time >> UpdateClient.py")
        os.system("echo import os >> UpdateClient.py")
        os.system("echo import urllib.request >> UpdateClient.py")
        os.system("echo os.system('title PyOS Updater') >> UpdateClient.py")
        os.system("echo print('Collecting update from github...') >> UpdateClient.py")
        os.system("echo update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyOS/master/PyOS.py') >> UpdateClient.py")
        os.system("echo response = urllib.request.urlopen(update) >> UpdateClient.py")
        os.system("echo newcode = response.read() >> UpdateClient.py")
        os.system("echo master = newcode.decode() >> UpdateClient.py")
        os.system("echo with open('update.pyd', 'w') as u: >> UpdateClient.py")
        os.system("echo     u.write(master) >> UpdateClient.py")
        os.system("echo     u.close >> UpdateClient.py")
        os.system("echo print('Updating...') >> UpdateClient.py")
        os.system("echo time.sleep(2) >> UpdateClient.py")
        os.system("echo os.remove('PyOS.py') >> UpdateClient.py")
        os.system("echo with open('update.pyd', 'r') as u: >> UpdateClient.py")
        os.system("echo    with open('PyOS.py', 'w', encoding='utf-8', newline='') as p: >> UpdateClient.py")
        os.system("echo        p.write(master) >> UpdateClient.py")
        os.system("echo        p.close() >> UpdateClient.py")
        os.system("echo        u.close() >> UpdateClient.py")
        os.system("echo        os.remove('update.pyd') >> UpdateClient.py")
        os.system("echo print('Updated! Now restarting...') >> UpdateClient.py")
        os.system("echo time.sleep(2) >> UpdateClient.py")
        os.system("echo os.startfile('PyOS.py') >> UpdateClient.py")
        os.system("echo exit() >> UpdateClient.py")
        os.startfile("UpdateClient.py")
        pyos_exitscript()
def pyos_update_dev():
    if os.path.exists("UpdateClientDev.py"):
        os.startfile("UpdateClientDev.py")
        pyos_exitscript()
    else:
        os.system("echo import time >> UpdateClientDev.py")
        os.system("echo import os >> UpdateClientDev.py")
        os.system("echo import urllib.request >> UpdateClientDev.py")
        os.system("echo os.system('title PyOS Updater') >> UpdateClientDev.py")
        os.system("echo print('Collecting update from github...') >> UpdateClientDev.py")
        os.system("echo update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyOS/developer/PyOSDEV.py') >> UpdateClientDev.py")
        os.system("echo response = urllib.request.urlopen(update) >> UpdateClientDev.py")
        os.system("echo newcode = response.read() >> UpdateClientDev.py")
        os.system("echo master = newcode.decode() >> UpdateClientDev.py")
        os.system("echo with open('update.pyd', 'w') as u: >> UpdateClientDev.py")
        os.system("echo     u.write(master) >> UpdateClientDev.py")
        os.system("echo     u.close >> UpdateClientDev.py")
        os.system("echo print('Updating...') >> UpdateClientDev.py")
        os.system("echo time.sleep(2) >> UpdateClientDev.py")
        os.system("echo os.remove('PyOS.py') >> UpdateClientDev.py")
        os.system("echo with open('update.pyd', 'r') as u: >> UpdateClientDev.py")
        os.system("echo    with open('PyOS.py', 'w', encoding='utf-8', newline='') as p: >> UpdateClientDev.py")
        os.system("echo        p.write(master) >> UpdateClientDev.py")
        os.system("echo        p.close() >> UpdateClientDev.py")
        os.system("echo        u.close() >> UpdateClientDev.py")
        os.system("echo        os.remove('update.pyd') >> UpdateClientDev.py")
        os.system("echo print('Updated! Now restarting...') >> UpdateClientDev.py")
        os.system("echo time.sleep(2) >> UpdateClientDev.py")
        os.system("echo os.startfile('PyOS.py') >> UpdateClientDev.py")
        os.system("echo exit() >> UpdateClientDev.py")
        os.startfile("UpdateClientDev.py")
        pyos_exitscript()
def pyos_localback():
    if os.path.exists("UpdateClientBK.py"):
        os.startfile("UpdateClientBK.py")
        pyos_exitscript()
    else:
        os.system("echo import time >> UpdateClientBK.py")
        os.system("echo import os >> UpdateClientBK.py")
        os.system("echo os.system('title PyOS Backup Restore') >> UpdateClientBK.py")
        os.system("echo print('Restoring...') >> UpdateClientBK.py")
        os.system("echo time.sleep(2) >> UpdateClientBK.py")
        os.system("echo os.remove('PyOS.py') >> UpdateClientBK.py")
        os.system("echo with open('backup_restore.dat', 'rb') as u: >> UpdateClientBK.py")
        os.system("echo    with open('PyOS.py', 'w', encoding='utf-8', newline='') as p: >> UpdateClientBK.py")
        os.system("echo        x = u.read() >> UpdateClientBK.py")
        os.system("echo        x = x.decode('ascii') >> UpdateClientBK.py")
        os.system("echo        p.write(x) >> UpdateClientBK.py")
        os.system("echo        p.close() >> UpdateClientBK.py")
        os.system("echo        u.close() >> UpdateClientBK.py")
        os.system("echo        os.remove('backup_restore.dat') >> UpdateClientBK.py")
        os.system("echo print('Restored!') >> UpdateClientBK.py")
        os.system("echo time.sleep(2) >> UpdateClientBK.py")
        os.system("echo os.startfile('PyOS.py') >> UpdateClientBK.py")
        os.system("echo exit() >> UpdateClientBK.py")
        os.startfile("UpdateClientBK.py")
        pyos_exitscript()
def pyos_devconsole():
    pyos_dev = input("$>> ")
    if pyos_dev == ("help"):
        print("help - Display this menu")
        print("ske - Skip boot error check")
        print("dsb - Disable user accounts")
        print("acu - Access user account")
        print("mod - Install mod pkg (not implemented)")
        print("ext - Exit dev mode")
    if pyos_dev == ("ske"):
        pyos_skeset()
    if pyos_dev == ("dsb"):
        pyos_dsacc()
    if pyos_dev == ("acu"):
        pyos_accessuser()
    if pyos_dev == ("ext"):
        pyos_os_ad()
    else:
        print("null")
        pyos_devconsole()
def pyos_accessuser():
    os.chdir('..')
    dirs = os.listdir(os.getcwd())
    for number, letter in enumerate(dirs):
        if "###.PyOS" in letter:
            continue
        print(letter)
    print("Enter name of account to access...")
    access = input("")
    try:
        os.chdir(access)
    except:
        print("Invalid account!")
        os.chdir(pyos_osn)
    pyos_osn == access
    print("Now accessing " + access + "'s account.")
def pyos_vdc():
    try:
        import speech_recognition as sr
    except:
        print("Failed to import modules.")
        print("For voice dictation to work, please use...")
        print("pip install SpeechRecognition")
        print("pip install PyAudio")
        pyos_os_ad()
    print("Initialising...")
    try:
        mic = sr.Recognizer()
        xtest = sr.Microphone()
    except:
        print("Failed to initialise microphone.")
        pyos_os_ad()
    print("Done!")
    os.system("cls")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("Welcome to PyOS Voice Dictation.")
    print("1} Use in live mode")
    print("2} Use in type mode")
    print("3} Return")
    print("")
    vdcin = input("")
    if vdcin == ("1"):
        print("Start speaking now.")
        print("Say 'finished' to return.")
        pyos_vdc_live()
    if vdcin == ("2"):
        print("Start speaking now.")
        print("Say 'finished' to save text.")
        global speechlist
        speechlist = []
        pyos_vdc_type()
    if vdcin == ("3"):
        print("Returning...")
        pyos_os_ad()
    else:
        print("Bad input!")
        os.system("pause >nul")
        pyos_vdc()
def pyos_vdc_live():
    import speech_recognition as sr
    mic = sr.Recognizer()
    with sr.Microphone() as listen:
        audio = mic.listen(listen)
    try:
        speech = mic.recognize_google(audio)
        if speech == ("finished"):
            print("Returning...")
            time.sleep(1)
            pyos_vdc()
        print(speech)
        pyos_vdc_live()
    except sr.UnknownValueError:
        print("Could not understand.")
        pyos_vdc_live()
    except sr.RequestError as e:
        print("Failed to communicate with Google API.")
        pyos_vdc_live()
def pyos_vdc_type():
    import speech_recognition as sr
    mic = sr.Recognizer()
    with sr.Microphone() as listen:
        audio = mic.listen(listen)
    try:
        speech = mic.recognize_google(audio)
        if speech == ("finished"):
            final = " ".join(speechlist)
            print(final)
            print("Enter name for file.")
            pyos_wordname = input("")
            if (".") in pyos_wordname:
                final = final.encode()
                try:
                    with open(pyos_wordname, 'wb') as pw:
                        pw.write(final)
                except:
                    print("Failed to save.")
                    pyos_os_ad()
                print("Saved!")
                pw.close()
                pyos_os_ad()
            else:
                final = final.encode()
                pyos_word_txt = (pyos_wordname + ".txt")
                try:
                    with open(pyos_word_txt, 'wb') as pw:
                        pw.write(final)
                except:
                    print("Failed to save.")
                    pyos_os_ad()
                print("Saved!")
                pw.close()
                pyos_os_ad()
        print(speech)
        speech += ""
        speechlist.extend([speech])
        pyos_vdc_type()
    except sr.UnknownValueError:
        print("Could not understand.")
        pyos_vdc_live()
    except sr.RequestError as e:
        print("Failed to communicate with Google API.")
        pyos_vdc_live()
def pyos_os_ad():
    os_input = input(">>")
    if os_input == ("help"):
        print("PyOS Commands")
        print("help - Displays this menu")
        print("ext - Exits")
        print("lgt - Logs out of account")
        print("cps - Change Password")
        print("app - Displays list of available apps")
        print(" ~~Use 'app [appname]' to launch direct")
        print("cls - Clears screen")
        if pyos_fallback == False:
            print("enc [filename] [passphrase] - Encryption Tool")
            print("dnc [filename] [passphrase] - Read Encrypted Files")
        print("typ - Word Processor")
        print("rdf - Read Files")
        print("upd - Check For Update")
        print(" ~~Use 'upd a' to force update")
        print("cmd - Command Prompt")
        print("ist - Install Apps")
        print("run - Run Files")
        print(" ~~Use 'run [file]' to launch direct")
        print("lsf - List files")
        print(" ~~Use 'lsf a' to return all filetypes")
        print("log - See admin logs")
        print(" ~~Use 'log a' to see archived logs")
        print(" ~~Use 'log r' to auto print all unread logs")
        print("rib - Reinstall PyOS backup")
        print("crb - Create Backup")
        print("vdc - Voice dictation")
        print("ret - Return program / system info")
        print(" ~use ret [info]")
        print(" ~E.g, time, ver, date")
        print("adm - Admin tools")
        print("set - PyOS Settings")
        print(" ~~Use 'set d' to reset config file")
        print(" ~~Recommended after updates!")
        print("crd - Credits")
        pyos_os_ad()
    if "ret" in os_input:
        osin = os_input.split(" ")
        if not len(osin) == 2:
            print("Usage: ret [info]")
            pyos_os_ad()
        lookup = osin[1]
        if lookup == "time":
            print(time.strftime('%H:%M:%S', time.gmtime()))
            pyos_os_ad()
        if lookup == "date":
            print(time.strftime('%m-%d-%Y', time.gmtime()))
            pyos_os_ad()
        if lookup == "ver":
            print(pyos_ver + "\nRunning on " + platform.platform() + "\nwith Python " + pyver)
            pyos_os_ad()
        else:
            print("Unrecognized lookup")
            pyos_os_ad()
    if os_input == ("set"):
        if not pyos_osn == pyos_permaun:
            print("Access denied.")
            pyos_os_ad()
        print("Caution!")
        print("Changing these settings may cause security flaws.")
        print("Use at your own risk.")
        pyos_config()
    if os_input == ("set d"):
        if not pyos_osn == pyos_permaun:
            print("Access denied.")
            pyos_os_ad()
        print("Resetting...")
        os.chdir('..')
        os.system("attrib -s -h config.bin")
        os.remove('config.bin')
        with open('config.bin', 'wb') as config_write:
            config_write.write(bytes(configbytes, "UTF-8"))
            config_write.close()
        os.system("attrib +s +h config.bin")
        time.sleep(1)
        os.chdir(pyos_osn)
        print("Reset.")
        pyos_os_ad()
    if os_input == ("adm"):
        if not pyos_osn == pyos_permaun:
            print("Access denied.")
            pyos_os_ad()
        if pyos_fallback == True:
            print("Disabled in fallback mode.")
            pyos_os_ad()
        pyos_devconsole()
    if os_input == ("crd"):
        print(credit)
        pyos_os_ad()
    if os_input == ("crb"):
            os.chdir('..')
            if pyos_fallback == True:
                os.chdir('..')
            if os.path.exists(pyos_iden_ver):
                print("Backup already exists for this version.")
                os.chdir(pyos_osn)
                if pyos_fallback == True:
                    os.chdir('fallback')
                pyos_os_ad()
            else:
                print("Creating backup...")
                if os.path.exists(pyos_iden_ver):
                    os.chdir(pyos_iden_ver)
                else:
                    os.mkdir(pyos_iden_ver)
                    os.chdir(pyos_iden_ver)
                os.chdir('..')
                os.chdir('..')
                pyos_iden_ver_file = str(pyos_iden_ver + ".bkp")
                os.system("type PyOS.py >> " + pyos_iden_ver_file)
                copydir = ("PyOS_Data/" + pyos_iden_ver)
                shutil.copy2(pyos_iden_ver_file, copydir)
                os.remove(pyos_iden_ver_file)
                os.chdir("PyOS_Data")
                os.chdir(pyos_osn)
                if pyos_fallback == True:
                    os.chdir('fallback')
                print("Backup Created!")
                pyos_os_ad()
    if os_input == ("rib"):
        print("Finding backups...")
        os.chdir('..')
        if pyos_fallback == True:
            os.chdir('..')
        trubacks = []
        checkbackups = glob.glob('*')
        if len(checkbackups) == 0:
            print("No backups!")
            print("You can create one by using 'cbk'")
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
        print("")
        print("Found these backups.")
        print("Choose one to revert to.")
        print("Enter anything else to cancel.")
        print("Reverting to an old version does not delete data.")
        print("")
        for number, letter in enumerate(checkbackups):
            trnu = number + 1
            trnus = str(trnu)
            if not ("###.PyOS.") in letter:
                continue
            trubacks.extend([letter])
        for number, letter in enumerate(trubacks):
            trnu = number + 1
            trnus = str(trnu)
            letter = letter.replace("###", "")
            letter = letter.replace(".", " ")
            print(trnus + ":", letter)            
        choosebak = input()
        try:
            cbk = int(choosebak)
        except:
            print("Cancelled.")
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
        cbk = cbk - 1
        try:
            cbk = trubacks[cbk]
        except:
            print("Cancelled.")
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
        print(cbk)
        print("Preparing to restore...")
        os.chdir('..')
        if os.path.exists("backup_restore.dat"):
            os.remove("backup_restore.dat")
        if os.path.exists("UpdateClientBK.py"):
            os.remove("UpdateClientBK.py")
        if os.path.exists(cbk):
            try:
                os.remove(cbk)
            except:
                pass
        pypath_1 = os.getcwd()
        os.chdir('PyOS_Data')
        os.chdir(cbk)
        bkpfile = glob.glob("*.bkp")
        if len(bkpfile) == 0:
            print("Failed to locate restore file.")
            os.chdir('..')
            try:
                os.remove(cbk)
            except:
                pass
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
        bkpfile_move = bkpfile[0]
        shutil.copy2(bkpfile_move, pypath_1)
        os.chdir('..')
        os.chdir('..')
        os.rename(bkpfile_move, "backup_restore.dat")
        print("Ready to restore. Continue? [y/n]")
        recc = input("")
        if recc == ("y"):
            pyos_localback()
        else:
            print("Cancelled.")
            if os.path.exists("backup_restore.dat"):
                os.remove("backup_restore.dat")
            if os.path.exists("UpdateClientBK.py"):
                os.remove("UpdateClientBK.py")
            if os.path.exists(cbk):
                os.remove(cbk)
            os.chdir('PyOS_Data')
            os.chdir(pyos_osn)
            if pyos_fallback == True:
                os.chdir('fallback')
            pyos_os_ad()
    if os_input == ("vdc"):
        print("PyOS Voice Input")
        pyos_vdc()
    if os_input == ("log"):
        checklogs = glob.glob("*.log")
        if len(checklogs) == 0:
            print("No new logs!")
            print("Other user's actions will appear here.")
            print("")
            pyos_os_ad()
        print("")
        print("Unread logs...")
        print("")
        for number, letter in enumerate(checklogs):
            trnu = number + 1
            trnus = str(trnu)
            print(trnus + ":", letter)
        print("")
        print("Enter number of log to read...")
        logchoice_r = input("")
        try:
            logchoice = int(logchoice_r)
        except:
            print("Illegal characters used!")
            pyos_os_ad()
        logchoice = logchoice - 1
        try:
            logchoice = checklogs[logchoice]
        except:
            print("Failed to open log requested.")
            pyos_os_ad()
        if os.path.exists(logchoice):
            with open(logchoice, 'r') as rlo:
                for line in rlo:
                    print(line)
            print("")
            print("Log archived.")
            logrename = logchoice.replace(".log", "")
            logrename = (logrename + "_archive.alg")
            os.rename(logchoice, logrename)
            if not os.path.exists("archlogs"):
                os.mkdir("archlogs")
            shutil.move(logrename, "archlogs")
            rlo.close()
            pyos_os_ad()
        else:
            print("Failed to open log requested.")
            pyos_os_ad()
    elif os_input == ("log a"):
        if not os.path.exists("archlogs"):
            print("No archived logs!")
            print("Logs are auto archived when read.")
            pyos_os_ad()
        os.chdir("archlogs")
        checklogs = glob.glob("*.alg")
        if len(checklogs) == 0:
            print("No archived logs!")
            print("Logs are auto archived when read.")
            os.chdir('..')
            pyos_os_ad()
        print("")
        print("Archived logs...")
        print("")
        for number, letter in enumerate(checklogs):
            trnu = number + 1
            trnus = str(trnu)
            print(trnus + ":", letter)
        print("")
        print("Enter number of log to read...")
        logchoice_r = input("")
        try:
            logchoice = int(logchoice_r)
        except:
            print("Illegal characters used!")
            os.chdir('..')
            pyos_os_ad()
        logchoice = logchoice - 1
        try:
            logchoice = checklogs[logchoice]
        except:
            print("Failed to open log requested.")
            os.chdir('..')
            pyos_os_ad()
        if os.path.exists(logchoice):
            with open(logchoice, 'r') as rlo:
                for line in rlo:
                    print(line)
                    os.system("pause >nul")
            rlo.close()
            os.chdir('..')
            pyos_os_ad()
        else:
            print("Failed to open log requested.")
            os.chdir('..')
            pyos_os_ad()
    elif os_input == ("log r"):
        checklogs = glob.glob("*.log")
        if len(checklogs) == 0:
            print("No new logs!")
            print("Other user's actions will appear here.")
            print("")
            pyos_os_ad()
        loglen = len(checklogs)
        print(loglen, "Unread Logs.")
        for log in range(loglen):
            checklogs = glob.glob("*.log")
            logchoice = checklogs[0]
            with open(logchoice, 'r') as rlo:
                for line in rlo:
                    print(line)
            print("")
            print("Log archived.")
            print("")
            logrename = logchoice.replace(".log", "")
            logrename = (logrename + "_archive.alg")
            os.rename(logchoice, logrename)
            if not os.path.exists("archlogs"):
                os.mkdir("archlogs")
            shutil.move(logrename, "archlogs")
            rlo.close()
        pyos_os_ad()
    elif os_input == ("log a"):
        if not os.path.exists("archlogs"):
            print("No archived logs!")
            print("Logs are auto archived when read.")
            pyos_os_ad()
        os.chdir("archlogs")
        checklogs = glob.glob("*.alg")
        if len(checklogs) == 0:
            print("No archived logs!")
            print("Logs are auto archived when read.")
            os.chdir('..')
            pyos_os_ad()
        print("")
        print("Archived logs...")
        print("")
        for number, letter in enumerate(checklogs):
            trnu = number + 1
            trnus = str(trnu)
            print(trnus + ":", letter)
        print("")
        print("Enter number of log to read...")
        logchoice_r = input("")
        try:
            logchoice = int(logchoice_r)
        except:
            print("Illegal characters used!")
            os.chdir('..')
            pyos_os_ad()
        logchoice = logchoice - 1
        try:
            logchoice = checklogs[logchoice]
        except:
            print("Failed to open log requested.")
            os.chdir('..')
            pyos_os_ad()
        if os.path.exists(logchoice):
            with open(logchoice, 'r') as rlo:
                for line in rlo:
                    print(line)
                    os.system("pause >nul")
            rlo.close()
            os.chdir('..')
            pyos_os_ad()
        else:
            print("Failed to open log requested.")
            os.chdir('..')
            pyos_os_ad()        
    elif os_input == ("upd"):
        if connection == False:
          print("You're offline!")
          print("Restart to try and establish a connection.")
          pyos_os_ad()
        if config_update == "Update0":
            print("Updates have been disabled.")
            pyos_os_ad()
        print("Checking for update...")
        if pyos_upd_cc == False:
            print("No update required")
            pyos_os_ad()
        if config_devmode == "Devmode1":
            print("Creating version backup...")
            os.chdir('..')
            if os.path.exists(pyos_iden_ver):
                os.chdir(pyos_iden_ver)
            else:
                os.mkdir(pyos_iden_ver)
                os.chdir(pyos_iden_ver)
            os.chdir('..')
            os.chdir('..')
            pyos_iden_ver_file = str(pyos_iden_ver + ".bkp")
            os.system("type PyOS.py >> " + pyos_iden_ver_file)
            copydir = ("PyOS_Data/" + pyos_iden_ver)
            shutil.copy2(pyos_iden_ver_file, copydir)
            os.remove(pyos_iden_ver_file)
            pyos_update_dev()
        else:
            print("Creating version backup...")
            os.chdir('..')
            if os.path.exists(pyos_iden_ver):
                os.chdir(pyos_iden_ver)
            else:
                os.mkdir(pyos_iden_ver)
                os.chdir(pyos_iden_ver)
            os.chdir('..')
            os.chdir('..')
            pyos_iden_ver_file = str(pyos_iden_ver + ".bkp")
            os.system("type PyOS.py >> " + pyos_iden_ver_file)
            copydir = ("PyOS_Data/" + pyos_iden_ver)
            shutil.copy2(pyos_iden_ver_file, copydir)
            os.remove(pyos_iden_ver_file)
            pyos_update()
    elif os_input == ("upd a"):
        if config_update == "Update0":
            print("Updates have been disabled.")
            pyos_os_ad()
        print("Forcing update...")
        os.chdir('..')
        os.chdir('..')
        pyos_update()
    elif os_input == ("cps"):
        print("")
        if pyos_fallback == True:
            print("Disabled in fallback mode.")
            pyos_os_ad()
        print("Enter your current password...")
        enterpass = getpass.getpass("")
        if len(enterpass) == 0:
            print("Password cannot be 0 characters!")
        try:
            with open('psdef.bin', 'rb') as fobj:
                private_key = RSA.import_key(
                    open('privkey.bin').read(),
                    passphrase=enterpass)
                enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                            for x in (private_key.size_in_bytes(), 
                                                            16, 16, -1) ]
                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            datat = data.decode('ascii')
        except:
            print("Incorrect password!")
            fobj.close()
            pyos_os_ad()
        if not datat == password_write:
            print("Incorrect password!")
            fobj.close()
            pyos_os_ad()
        fobj.close()
        os.remove("psdef.bin")
        os.remove('privkey.bin')
        os.remove('pubkey.bin')
        print("Enter a new password...")
        passwordcheck = getpass.getpass("")
        print("Please type your password again.")
        passwordre = getpass.getpass("")
        if passwordcheck == passwordre:
            key = RSA.generate(2048)
            encrypted_key = key.exportKey(passphrase=passwordcheck, pkcs=8, 
                    protection="scryptAndAES128-CBC")
            with open('privkey.bin', 'wb') as f:
                    f.write(encrypted_key)
                    os.system("attrib +h privkey.bin")
            with open('pubkey.bin', 'wb') as f:
                    f.write(key.publickey().exportKey())
                    os.system("attrib +h pubkey.bin")
            with open('psdef.bin', 'wb') as out_file:
                recipient_key = RSA.import_key(
                    open('pubkey.bin').read())
                session_key = get_random_bytes(16)
                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                out_file.write(cipher_rsa.encrypt(session_key))
                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                data = bytes(password_write, encoding='utf-8')
                ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                out_file.write(cipher_aes.nonce)
                out_file.write(tag)
                out_file.write(ciphertext)
                os.system("attrib +h psdef.bin")
            print("")
            print("Password changed.")
            pyos_os_ad()
        else:
            print("Passwords do not match!")
            pyos_os_ad()
    elif os_input == ("ext"):
        pyos_exitscript()
    elif os_input == ("lgt"):
        if pyos_fallback == True:
            print("Logging out...")
            os.system("pause >nul")
            os.chdir('..')
            pyos_login()
        print("Logging out...")
        os.system("pause >nul")
        pyos_login()
    elif ("run") in os_input:
        if os_input == ("run"):
            print("Usage: run [filename]")
            pyos_os_ad()
        else:
            try:
                pyos_runfile = os_input.replace('run ', '')
                os.startfile(pyos_runfile)
                pyos_os_ad()
            except:
                os_input_txt = (os_input + ".txt")
                try:
                    os_inputx = os_input_txt.replace('run ', '')
                    os.startfile(os_inputx)
                    pyos_os_ad()
                except:
                    print("File not found!")
                    pyos_os_ad()
            pyos_os_ad()
    elif ("app") in os_input:
        if os_input == ("app"):
            pyos_prog()
        os_in_app = os_input.replace("app ", "")
        try:
            os.chdir("appdata")
            os_in_app = (os_in_app + ".py")
            os.startfile(os_in_app)
            os.chdir('..')
        except:
            os_in_app = (os_in_app.replace(".py", ""))
            print("No app named " + os_in_app)
            os.chdir('..')
            pyos_os_ad()
        print("Launched " + os_in_app)
        pyos_os_ad()
    elif os_input == ("cls"):
        os.system("cls")
        if connection == True:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Connected                                    " + timedate)
        else:
            timedate = time.strftime('%H:%M', time.gmtime())
            print("Not Connected                                " + timedate)
        print("##################################################")
        print("                      Py OS                       ")
        print("                       Sys                        ")
        print("                      -ADM-                       ")
        print("##################################################")
        pyos_os_ad()
    elif ("enc") in os_input:
        if pyos_fallback == True:
            print("Disabled in fallback mode.")
            pyos_os_ad()
        encls = os_input.split()
        if not len(encls) == 3:
            print("Usage: enc [filename] [passphrase]")
            pyos_os_ad()
        pyos_enc_file = encls[1]
        passph = encls[2]
        passex = pyos_enc_file.split(".")
        if not len(passex) == 2:
            print("Specify Filetype!")
            pyos_os_ad()
        pyos_enc_file_txt = (pyos_enc_file)
        if os.path.exists(pyos_enc_file_txt):
            with open(pyos_enc_file_txt, 'rb') as pre:
                for line in pre:
                    if passph == (""):
                        print("Passphrase must be more than 0 characters!")
                        os.system("pause >nul")
                        pyos_enc()
                    print("Encrypting...")
                    pyos_encdir = (pyos_enc_file + "_enc")
                    if os.path.exists(pyos_encdir):
                        print("Encrypted file already exists!")
                        while True:
                            encr = random.randint(1, 99)
                            encr = str(encr)
                            pyos_encdir = (encr + pyos_encdir)
                            if os.path.exists(pyos_encdir):
                                continue
                            break
                        print("Encrypting as " + pyos_encdir)
                    os.mkdir(pyos_encdir)
                    with open(pyos_enc_file_txt, 'r') as x:
                        shutil.copy2(pyos_enc_file_txt, pyos_encdir)
                    x.close()
                    os.chdir(pyos_encdir)
                    key = RSA.generate(2048)
                    encrypted_key = key.exportKey(passphrase=passph, pkcs=8, 
                            protection="scryptAndAES128-CBC")
                    with open('privkey.file.bin', 'wb') as f:
                            f.write(encrypted_key)
                            os.system("attrib +h privkey.file.bin")
                    with open('pubkey.file.bin', 'wb') as f:
                            f.write(key.publickey().exportKey())
                            os.system("attrib +h pubkey.file.bin")
                    with open('data.file.bin', 'wb') as out_file:
                        recipient_key = RSA.import_key(
                            open('pubkey.file.bin').read())
                        session_key = get_random_bytes(16)
                        cipher_rsa = PKCS1_OAEP.new(recipient_key)
                        out_file.write(cipher_rsa.encrypt(session_key))
                        cipher_aes = AES.new(session_key, AES.MODE_EAX)
                        data = bytes(line)
                        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                        out_file.write(cipher_aes.nonce)
                        out_file.write(tag)
                        out_file.write(ciphertext)
                        os.system("attrib +h data.file.bin")
                        try:
                            os.remove(pyos_enc_file_txt)
                        except:
                            print("Failed to delete file.")
                            print("Encryption succeeded, but original file was not deleted.")
                            print("Most likely permission error.")
                        f.close()
                        out_file.close()
                        pre.close()
                        print("Encrypted!")
                        os.chdir('..')
                        os.remove(pyos_enc_file_txt)
                        pyos_os_ad()
        else:
            print("File not found!")
            pyos_os_ad()
    elif ("dnc") in os_input:
        if pyos_fallback == True:
            print("Disabled in fallback mode.")
            pyos_os_ad()
        dncls = os_input.split()
        if not len(dncls) == 3:
            print("Usage: dnc [filename] [passphrase]")
            pyos_os_ad()
        pyos_dnc_file = dncls[1]
        passph = dncls[2]
        pyos_dnc_file_enc = (pyos_dnc_file + "_enc")
        if os.path.exists(pyos_dnc_file_enc):
            os.chdir(pyos_dnc_file_enc)
            with open('data.file.bin', 'rb') as fobj:
                try:
                    private_key = RSA.import_key(
                        open('privkey.file.bin').read(),
                        passphrase=passph)
                    enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                                for x in (private_key.size_in_bytes(), 
                                                                16, 16, -1) ]
                except:
                    print("Incorrect passphrase!")
                    os.chdir('..')
                    os.system("pause >nul")
                    if pyos_osn == pyos_aun:
                        pyos_os_ad()
                    else:
                        pyos_os_us()
                try:
                    cipher_rsa = PKCS1_OAEP.new(private_key)
                    session_key = cipher_rsa.decrypt(enc_session_key)
                    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
                except:
                    print("An error occured when decrypting.")
                    print("Please try again.")
                    os.system("Pause >nul")
                    os.chdir('..')
                    pyos_dnc()
            print("Decrypted file contents...")
            print("")
            datat = data.decode('ascii')
            print(datat)
            os.chdir('..')
            if pyos_osn == pyos_aun:
                pyos_os_ad()
            else:
                pyos_os_us()
        else:
            print("File not found!")
            print("-- If you encrypted your file after PyOS 0.1.1.2,")
            print("   Ensure you include filetype for decrypting.")
            if pyos_osn == pyos_aun:
                pyos_os_ad()
            else:
                pyos_os_us()
    elif os_input == ("typ"):
        print("")
        print("Start typing to begin...")
        print("")
        pyos_word = input("")
        print("")
        print("Enter name for file.")
        pyos_wordname = input("")
        if (".") in pyos_wordname:
            pyos_wordb = pyos_word.encode()
            try:
                with open(pyos_wordname, 'wb') as pw:
                    pw.write(pyos_wordb)
            except:
                print("Failed to save.")
                pyos_os_ad()
            print("Saved!")
            pw.close()
            pyos_os_ad()
        else:
            pyos_wordb = pyos_word.encode()
            pyos_word_txt = (pyos_wordname + ".txt")
            try:
                with open(pyos_word_txt, 'wb') as pw:
                    pw.write(pyos_wordb)
            except:
                print("Failed to save.")
                pyos_os_ad()
            print("Saved!")
            pw.close()
            pyos_os_ad()
    elif "rdf" in os_input:
        rdfls = os_input.split()
        if not len(rdfls) == 2:
            print("Usage: rdf [filename]")
            pyos_os_ad()
        pyos_read = rdfls[1]
        if (".") in pyos_read:
            if os.path.exists(pyos_read):
                print(pyos_read + " Contains...")
                print("")
                try:
                    with open(pyos_read, 'rb') as pr:
                        for line in pr:
                            try:
                                datat = line.decode('ascii')
                            except:
                                print("Unable to open file.")
                            print(datat)
                except:
                    print("Unable to open file.")
                pr.close()
                pyos_os_ad()
            else:
                print("File not found!")
                pyos_os_ad()
        else:
            pyos_read_txt = (pyos_read + ".txt")
            if os.path.exists(pyos_read_txt):
                print(pyos_read + " Contains...")
                print("")
                with open(pyos_read_txt, 'rb') as pr:
                    for line in pr:
                        datat = line.decode('ascii')
                        print(datat)
                        pr.close()
                        pyos_os_ad()
            else:
                print("File not found!")
                pyos_os_ad()
    elif os_input == ("cmd"):
        os.system("cls")
        os.system("@mode con cols=130 lines=34")
        print("##################################################")
        print("Windows Command Prompt Emulator.")
        print("Type 'return' to go back to PyOS.")
        pyos_adm_cmd()
    elif os_input == ("ist"):
        if connection == False:
          print("You're offline!")
          print("Restart to try and establish a connection.")
          pyos_os_ad()
        print("Enter name of app to download (Do not include filetypes).")
        appinst = input("")
        appinst = (appinst + ".py")
        appinstlk = ('https://raw.githubusercontent.com/SimLoads/PyOS/pyos_apps/' + appinst)
        try:
            update = urllib.request.Request(appinstlk)
            response = urllib.request.urlopen(update) 
            newcode = response.read() 
            master = newcode.decode()
        except:
            print("Could not find app!")
            print("To see list of apps, go to...")
            print("https://github.com/SimLoads/PyOS/tree/pyos_apps")
            os.system("pause")
            pyos_os_ad()
        print("Downloaded!")
        print("Install for who?")
        print("[m]yself")
        print("[o]ther user")
        installin = input("")
        if installin == ("m"):
            print("Installing...")
            if os.path.exists("appdata"):
                os.chdir('appdata')
            else:
                os.mkdir('appdata')
                os.chdir('appdata')
            with open(appinst, 'w', encoding='utf-8') as app:
                app.write(master)
            print("Installed!")
            app.close()
            os.chdir('..')
            pyos_os_ad()
        if installin == ("o"):
            os.chdir('..')
            dirs = os.listdir(os.getcwd())
            print("")
            for number, letter in enumerate(dirs):
                trnu = number + 1
                trnus = str(trnu)
                print(trnus + ":", letter)
            print("")
            print("Enter the NAME of the user you want to switch to.")
            userinstall = input("")
            try:
                os.chdir(userinstall)
            except:
                print("User not found!")
                os.chdir(pyos_osn)
                pyos_os_ad()
            print("Installing for " + userinstall)
            if os.path.exists("appdata"):
                os.chdir('appdata')
            else:
                os.mkdir('appdata')
                os.chdir('appdata')
            with open(appinst, 'w', encoding='utf-8') as app:
                app.write(master)
            print("Installed!")
            app.close()
            os.chdir('..')
            os.chdir('..')
            os.chdir(pyos_osn)
            pyos_os_ad()
        else:
            print("Cancelled.")
            pyos_os_ad()
    elif os_input == ("lsf"):
        files = glob.glob("*.*")
        encfiles = glob.glob("*")
        print("")
        print("Files found:")
        for number, letter in enumerate(files):
            trnu = number + 1
            trnus = str(trnu)
            if (".bin") in letter:
                continue
            if (".log") in letter:
                continue
            if ("_enc") in letter:
                continue
            print(letter)
        print("")
        print("Encrypted files found:")
        for number, letter in enumerate(encfiles):
            trnu = number + 1
            trnus = str(trnu)
            if not ("_enc") in letter:
                continue
            letter = letter.replace("_enc", "")
            print(letter)
        print("")
        pyos_os_ad()
    elif os_input == ("lsf a"):
        filesa = glob.glob("*")
        print("")
        print("Files found:")
        for number, letter in enumerate(filesa):
            print(letter)
        print("")
        pyos_os_ad()
    elif "echo" in os_input:
        out = os_input.replace("echo ", "")
        print(out)
        pyos_os_ad()
    elif "add" in os_input:
        add = os_input.split()
        if not len(add) == 3:
            print("Missing integers!")
            pyos_os_ad()
        try:
            num = float(add[1]) + float(add[2])
        except:
            print("Use Numbers!")
            pyos_os_ad()
        print(num)
        pyos_os_ad()
    elif "sub" in os_input:
        sub = os_input.split()
        if not len(sub) == 3:
            print("Missing integers!")
            pyos_os_ad()
        try:
            num = float(sub[1]) - float(sub[2])
        except:
            print("Use Numbers!")
            pyos_os_ad()
        print(num)
        pyos_os_ad()
    elif "mul" in os_input:
        mul = os_input.split()
        if not len(mul) == 3:
            print("Missing integers!")
            pyos_os_ad()
        try:
            num = float(mul[1]) * float(mul[2])
        except:
            print("Use Numbers!")
            pyos_os_ad()
        print(num)
        pyos_os_ad()
    elif "div" in os_input:
        mul = os_input.split()
        if not len(mul) == 3:
            print("Missing integers!")
            pyos_os_ad()
        try:
            num = float(mul[1]) / float(mul[2])
        except:
            print("Use Numbers!")
            pyos_os_ad()
        print(num)
        pyos_os_ad()
    else:
        print(os_input + " - Bad Input")
        pyos_os_ad()
def pyos_adm_cmd():
    pyos_cmd_dr = os.getcwd()
    pyos_cmd_in = input(pyos_cmd_dr + ">")
    if pyos_cmd_in == ("return"):
        if config_resize == "Resize1":
            os.system("@mode con cols=50 lines=34")
        pyos_os_ad()
    else:
        try:
            os.system(pyos_cmd_in)
            pyos_adm_cmd()
        except:
            print("Unrecognised command")
            pyos_adm_cmd()
def pyos_enc():
    os.system("cls")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("Enter file name (Do not include filetype).")
    pyos_enc_file = input("")
    pyos_enc_file_txt = (pyos_enc_file + ".txt")
    if os.path.exists(pyos_enc_file_txt):
        with open(pyos_enc_file_txt, 'rb') as pre:
            for line in pre:
                print("Enter new encryption passphrase.")
                passph = getpass.getpass("")
                if passph == (""):
                    print("Passphrase must be more than 0 characters!")
                    os.system("pause >nul")
                    pyos_enc()
                print("Encrypting...")
                pyos_encdir = (pyos_enc_file + "_enc")
                os.mkdir(pyos_encdir)
                with open(pyos_enc_file_txt, 'r') as x:
                    shutil.copy2(pyos_enc_file_txt, pyos_encdir)
                x.close()
                os.chdir(pyos_enc_file + "_enc")
                key = RSA.generate(2048)
                encrypted_key = key.exportKey(passphrase=passph, pkcs=8, 
                        protection="scryptAndAES128-CBC")
                with open('privkey.file.bin', 'wb') as f:
                        f.write(encrypted_key)
                        os.system("attrib +h privkey.file.bin")
                with open('pubkey.file.bin', 'wb') as f:
                        f.write(key.publickey().exportKey())
                        os.system("attrib +h pubkey.file.bin")
                with open('data.file.bin', 'wb') as out_file:
                    recipient_key = RSA.import_key(
                        open('pubkey.file.bin').read())
                    session_key = get_random_bytes(16)
                    cipher_rsa = PKCS1_OAEP.new(recipient_key)
                    out_file.write(cipher_rsa.encrypt(session_key))
                    cipher_aes = AES.new(session_key, AES.MODE_EAX)
                    data = bytes(line)
                    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                    out_file.write(cipher_aes.nonce)
                    out_file.write(tag)
                    out_file.write(ciphertext)
                    os.system("attrib +h data.file.bin")
                    os.remove(pyos_enc_file_txt)
                    f.close()
                    out_file.close()
                    pre.close()
                    print("Encrypted!")
                    os.chdir('..')
                    os.remove(pyos_enc_file_txt)
                    if pyos_osn == pyos_aun:
                        pyos_os_ad()
                    else:
                        pyos_os_us()
    else:
        print("File not found!")
        if pyos_osn == pyos_aun:
            pyos_os_ad()
        else:
            pyos_os_us()
def pyos_dnc():
    os.system("cls")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("Enter file name (Do not include filetype).")
    pyos_dnc_file = input("")
    pyos_dnc_file_enc = (pyos_dnc_file + "_enc")
    if os.path.exists(pyos_dnc_file_enc):
        os.chdir(pyos_dnc_file_enc)
        print("Enter encryption passphrase.")
        passph = getpass.getpass("")
        with open('data.file.bin', 'rb') as fobj:
            try:
                private_key = RSA.import_key(
                    open('privkey.file.bin').read(),
                    passphrase=passph)
                enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
                                                            for x in (private_key.size_in_bytes(), 
                                                            16, 16, -1) ]
            except:
                print("Incorrect passphrase!")
                os.chdir('..')
                os.system("pause >nul")
                if pyos_osn == pyos_aun:
                    pyos_os_ad()
                else:
                    pyos_os_us()
            try:
                cipher_rsa = PKCS1_OAEP.new(private_key)
                session_key = cipher_rsa.decrypt(enc_session_key)
                cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
                data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            except:
                print("An error occured when decrypting.")
                print("Please try again.")
                os.system("Pause >nul")
                os.chdir('..')
                pyos_dnc()
        print("Decrypted file contents...")
        print("")
        datat = data.decode('ascii')
        print(datat)
        os.system("pause >nul")
        os.chdir('..')
        if pyos_osn == pyos_aun:
            pyos_os_ad()
        else:
            pyos_os_us()
    else:
        print("File not found!")
        os.system("pause >nul")
        if pyos_osn == pyos_aun:
            pyos_os_ad()
        else:
            pyos_os_us()
def pyos_func():
    os.system("pause")
def pyos_cryfail():
    os.system("cls")
    if config_resize == "Resize1":
        os.system("@mode con cols=50 lines=34")
    if connection == True:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Connected                                    " + timedate)
    else:
        timedate = time.strftime('%H:%M', time.gmtime())
        print("Not Connected                                " + timedate)
    print("##################################################")
    print("")
    print("Failed Import!")
    print("")
    print("##################################################")
    print("Cryptodome could not be found!")
    print("Install it with CMD using...")
    print("pip install pycryptodomex")
    print("")
    print("1} Boot into fallback mode")
    print("2} Attempt to install Cryptodome now")
    print("3} Exit")
    cryfail = input("")
    if cryfail == ("cd"):
        print(os.getcwd())
        os.system("pause >nul")
        pyos_cryfail()
    if cryfail == ("2"):
        os.system("pip install pycryptodomex")
        print("")
        print("")
        print("If install failed, try adding Pip to PATH")
        print("If it worked, try booting.")
        print("Now restarting...")
        os.system("pause >nul")
        pyos_boot()
    if cryfail == ("3"):
        exit()
    elif cryfail == ("1"):
        print("")
        print("PyOS will now boot w/o encryption services.")
        global pyos_fallback
        os.system("title " + pyos_ver  + " Fallback Mode")
        pyos_fallback = True
        os.system("pause")
        pyos_set()
    else:
        pyos_cryfail()
###########
devmess = ('''
PyOS 0.1.0.4 ----
- Bug fixes, around the login screen where PyOS backups would be listed as accounts
  and trying to log in to them would cause the program to navigate to the wrong directory
- Fixed massive security flaw with crd
- Added successful login logs for admins
- Added some more admin tools, like disabling user accounts.
- Plans for future - ssh with clients connecting to admin remotely, more admin tools, deeper intergration with other python scripts.

PyOS 0.1.0.6 ----
- More bug fixes, including failing to switch directories after crb returns "backup already created"
- Edited encryption / decryption for admins
- Added ability to restore corrupted accounts
- Changed account disable method
- Slightly edited some commands
- Plans for future - Same as before lol

PyOS 0.1.0.8 ----
- Changed no log message to better suit how logs now work
- Fixed updater trying to exit with pyos_exitscript()
- Made rdf in line
- Changed run error message
- Added "log r" function
- Fixed setup sequence??? Apparently had issues creating first account, I wonder how many problems that caused oops

PyOS 0.1.1.0 ----
- Increased support for fallback mode, including fixing the backup system and incorrect directory changes
- Disabled admin tools in fallback mode

PyOS 0.1.1.2 ----
- Added workaround for duplicate encryption files
- Encryption now supports all filetypes
- Decryption "file not found" message changed
- Added add, subtract, multiply and divide features.

PyOS 0.1.1.4 ----
- Completely changed how passwords work, now they work much more like enc and dnc, making them much more secure.
  Now passwords aren't actually stored - password files are just a default value
  and the password is the key to decrypt it. If it's wrong, the output is garbage.
  This means security is heightened massively. Even though the source code is open lol
- Few tiny bug fixes I can't actually remember
- Added an update page, kinda. Also backwards compatibilty is still there, surprisingly. That took some work.

PyOS 0.1.1.6 ----
- Fixed a flaw with user logins on first time setup from PyOS <0.1.1.4 oops

PyOS 0.1.1.8 ----
- Added a configuration file, where things can be changed program-wide. Used to do this with files being made, now theres an actual file for it.
- Allow for users to skip password checks, download developer updates, disable window resize, disable updates altogether and force admin for all users.
- Fixed disable accounts
- Fixed adm being allowed on first-time login from update to 0.1.1.4 for users

PyOS 0.1.1.8X ----
- HOTFIX CAUSE I'M AN IDIOT AND FORGOT TO MAKE SOME VARIABLES

PyOS 0.1.2.0 ----
- lol welcome to 100kb
- Added a semi-permanent status bar that never updates unless you cls or go somewhere else in the program
- Fixed crash when not connected to internet
- Added system info command (ret)

PyOS 0.1.2.2 ----
- Fixed the config system cause I'm an idiot and basically made the whole thing redundant
- Added some more config file features, now that it works
- Moved STP to config file

PyOS 0.1.2.4_DEV1 ----
- Update testing for developer mode
- Added further support for fallback mode

:)
''')
pyos_boot()
