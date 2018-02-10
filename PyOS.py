### PyOS 0.0.0.0 ###
######################
print("Importing...")#
import os            #
import time          #
import sys           #
import getpass       #
######################
#CREDIT#
#General Coding - Sam Forrester
#Encryption / Decryption code - https://www.blog.pythonlibrary.org/2016/05/18/python-3-an-intro-to-encryption/
#
#######
global pyos_ver
global pyos_osn
global code
code = 'pyosenckey'
pyos_ver = str("PyOS 0.0.0.1")
pyos_osn = getpass.getuser()
def pyos_boot():
    if os.path.exists("PyOS_Data"):
        os.chdir("PyOS_Data")
    pyos_dr = os.getcwd()
    if "PyOS_Data" in pyos_dr:
        print("[  OS  ] Checking Files...")
        if os.path.exists("data_pm.bin"):
              print("[  OK  ] Assuming account exists")
              try:
                global RSA
                global AES
                global get_random_bytes
                global PKCSl_OAEP
                from Cryptodome.PublicKey import RSA
                from Cryptodome.Cipher import AES, PKCS1_OAEP
                from Cryptodome.Random import get_random_bytes
              except:
                pyos_cryfail()
              print("[  OK  ] Booting!")
              os.system("@mode con cols=50 lines=34")
              pyos_login()
        else:
            os.chdir('..')
            try:
                global RSA
                global AES
                global get_random_bytes
                global PKCSl_OAEP
                from Cryptodome.PublicKey import RSA
                from Cryptodome.Cipher import AES, PKCS1_OAEP
                from Cryptodome.Random import get_random_bytes
            except:
                pyos_cryfail()
            pyos_set()
    else:
        try:
            global RSA
            global AES
            global get_random_bytes
            global PKCS1_OAEP
            from Cryptodome.PublicKey import RSA
            from Cryptodome.Cipher import AES
            from Cryptodome.Cipher import PKCS1_OAEP
            from Cryptodome.Random import get_random_bytes
        except:
            pyos_cryfail()
        print("[  OK  ] Assuming setup is required")
        print("[  OK  ] Booting!")
        pyos_set()
def pyos_login():
    os.system("cls")
    print("##################################################")
    print("")
    print("                     WELCOME                      ")
    print("                       T O                        ")
    print("                      Py OS                       ")
    print("")
    print("")
    print("##################################################")
    print("Enter password to continue...")
    enterpass = getpass.getpass("")
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
    datas = str(data)
    for letter in datas:
        datatru = datas.replace("b", "")
        datatr = datatru.replace("'", "")
    if datatr == enterpass:
        print("Password Accepted.")
        fobj.close()
        os.system("pause >nul")
        exit()
    else:
        print("Incorrect Password!")
        fobj.close()
        pyos_login()
def pyos_main():
          os.system("pause")
def pyos_set():
    os.system("cls")
    if not os.path.exists("PyOS_Data"):
        os.mkdir("PyOS_Data")
        os.chdir("PyOS_Data")
    if os.path.exists("PyOS_Data"):
        os.chdir("PyOS_Data")
    os.system("@mode con cols=50 lines=34")
    print("##################################################")
    print("")
    print("                     WELCOME                      ")
    print("                       T O                        ")
    print("                      Py OS                       ")
    print("")
    print("")
    print("##################################################")
    print("Hi, " + pyos_osn + "!")
    print("We're going to create an account for you.")
    print("Please enter a password.")
    print("Keystrokes will not be echoed.")
    pyos_setps()
def pyos_setps():
    passwordcheck = getpass.getpass("")
    passwordre = getpass.getpass("")
    if passwordcheck == passwordre:
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=code, pkcs=8, 
                protection="scryptAndAES128-CBC")
        with open('prkey.bin', 'wb') as f:
                f.write(encrypted_key)
                os.system("attrib +s +h prkey.bin")
        with open('pukey.bin', 'wb') as f:
                f.write(key.publickey().exportKey())
                os.system("attrib +s +h pukey.bin")
        with open('data_pm.bin', 'wb') as out_file:
            recipient_key = RSA.import_key(
                open('pukey.bin').read())
            session_key = get_random_bytes(16)
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            out_file.write(cipher_rsa.encrypt(session_key))
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            data = bytes(passwordcheck, encoding='utf-8')
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            out_file.write(cipher_aes.nonce)
            out_file.write(tag)
            out_file.write(ciphertext)
            os.system("attrib +s +h data_pm.bin")
        print("")
        print("Setup is complete!")
        os.system("pause >nul")
        pyos_login()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        pyos_setps()
def pyos_prog():
          os.system("pause")
def pyos_mus():
          os.system("pause")
def pyos_browse():
          os.system("pause")
def pyos_os():
          os.system("pause")
def pyos_func():
          os.system("pause")
def pyos_cryfail():
          print("Failed to import Cryptodome!")
          os.system("pause")
          exit()



    
###########
pyos_boot()
