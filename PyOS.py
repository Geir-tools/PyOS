###.PyOS.0.0.9.0.### #
######################
import os            
os.system("cls")     
print("[  OK  ] OS")
import time
print("[  OK  ] Time")
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
import platform
print("[  OK  ] Platform")
import glob
print("[  OK  ] Glob")
import urllib.request
print("[  OK  ] Urllib.request")
##################################
#CREDIT#
#General Coding - Sam Forrester
#Encryption / Decryption code - https://www.blog.pythonlibrary.org/2016/05/18/python-3-an-intro-to-encryption/
#
#######
os.system("cls")
global pyos_ver
global pyos_iden_ver
global pyos_upd_cc
global pyos_osn
global pyos_aun
global pyver
global code
code = 'pyosenckey'
pyos_upd_cc = False
pyos_ver = str("PyOS 0.0.9.0")
pyos_osn = getpass.getuser()
pyver = platform.python_version()
pyos_iden_ver = ("###.PyOS.0.0.9.0.###")
if not ("3.4") in pyver:
    print("You are using an unsupported version of Python!")
    print("PyOS works best on Python 3.4.x")
    print("Thanks!")
    os.system("pause")
    exit()
print("[  OK  ] Supported Python Version")
pyos_aun = getpass.getuser()
os.system("title " + pyos_ver)
if os.path.exists("UpdateClient.py"):
    os.remove("UpdateClient.py")
def pyos_boot():
    if os.path.exists("PyOS_Data"):
        os.chdir("PyOS_Data")
        try:
            os.chdir(pyos_osn)
        except:
            pyos_set()
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
                print("[  OK  ] RSA Import")
                from Cryptodome.Cipher import PKCS1_OAEP
                print("[  OK  ] PKCSl_OAEP Import")
                from Cryptodome.Cipher import AES
                print("[  OK  ] AES Import")
                from Cryptodome.Random import get_random_bytes
                print("[  OK  ] Random Import")
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
        os.system("@mode con cols=50 lines=34")
        pyos_set()
def pyos_login():
    os.system("cls")
    print("##################################################")
    print("")
    print("                      Py OS                       ")
    print("                      Login                       ")
    print("                      -----                       ")
    print("")
    print("")
    print("##################################################")
    update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyOS/master/PyOS.py')
    response = urllib.request.urlopen(update)
    newcode = response.read()
    master = newcode.decode()
    tvers = master.split(" ")
    for number, line in enumerate(tvers):
        tms = str(line)
        break
    if not tms == pyos_iden_ver:
        print("An update is available.")
        pyos_upd_cc = True
    print("1} Log In as " + pyos_osn)
    print("2} Switch user")
    print("3} Create new user")
    print("4} Exit")
    pyos_login_c = input("")
    if pyos_login_c == ("1"):
        print("Please enter your password, " + pyos_osn)
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
        datat = data.decode('ascii')
        if datat == enterpass:
            print("Password Accepted.")
            fobj.close()
            os.system("pause >nul")
            if pyos_osn == pyos_aun:
                os.system("cls")
                print("##################################################")
                print("                      Py OS                       ")
                print("                       Sys                        ")
                print("                      -ADM-                       ")
                print("##################################################")
                pyos_os_ad()
            os.system("cls")
            print("##################################################")
            print("                      Py OS                       ")
            print("                       Sys                        ")
            print("                      -USR-                       ")
            print("##################################################")
            pyos_os_us()
        else:
            print("Incorrect Password!")
            fobj.close()
            os.system("pause >nul")
            pyos_login()
    elif pyos_login_c == ("2"):
        os.chdir('..')
        dirs = os.listdir(os.getcwd())
        print("")
        for number, letter in enumerate(dirs):
            trnu = number + 1
            trnus = str(trnu)
            print(trnus + ":", letter)
        print("")
        print("Enter the NAME of the user you want to switch to.")
        logswitch = input("")
        try:
            os.chdir(logswitch)
        except:
            print("User not found!")
            os.system("pause >nul")
            os.chdir(pyos_osn)
            pyos_login()
        if os.path.exists("data_pm.bin"):
            print("Switched to " + logswitch)
            global pyos_osn
            pyos_osn = (logswitch)
            os.system("pause >nul")
            pyos_login()
        else:
            print("Invalid / Corrupted Account!")
            os.chdir('..')
            os.system("pause >nul")
            pyos_login()
    elif pyos_login_c == ("3"):
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
        exit()
    elif pyos_login_c == ("cd"):
        pyos_tempcd = os.getcwd()
        print(pyos_tempcd)
        os.system("pause >nul")
        pyos_login()
    elif pyos_login_c == ("dev"):
        print(devmess)
        os.system("pause >nul")
        pyos_cryfail()
    else:
        pyos_login()
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
    print("Please type your password again.")
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
        print("Press any key to go to menu.")
        os.system("pause >nul")
        pyos_login()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        pyos_setps()
def pyos_prog():
    os.system("cls")
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
        print("adm - Switch To Administrator")
        pyos_os_us()
    elif os_input == ("ext"):
        exit()
    elif os_input == ("lgt"):
        if pyos_osn == ("tmpacc"):
            print("Exiting...")
            os.system("pause >nul")
            exit()
        print("Logging out...")
        os.system("pause >nul")
        pyos_login()
    elif os_input == ("app"):
        pyos_prog()
    elif os_input == ("cls"):
        os.system("cls")
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
        if pyos_osn == pyos_aun:
            print("Switched to admin!")
            pyos_os_ad()
        else:
            print(pyos_osn + " Is not an admin!")
            print("Please log in as " + pyos_aun + " for administrator tools.")
            pyos_os_us()
    else:
        print(os_input + " - Bad Input")
        pyos_os_us()
def pyos_update():
    if os.path.exists("UpdateClient.py"):
        os.startfile("UpdateClient.py")
        exit()
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
        exit()
def pyos_os_ad():
    os_input = input(">>")
    if os_input == ("help"):
        print("PyOS Commands")
        print("help - Displays this menu")
        print("ext - Exits")
        print("lgt - Logs out of account")
        print("app - Displays list of available apps")
        print(" ~~Type 'app [appname]' to launch direct")
        print("cls - Clears screen")
        print("enc - Encryption Tool")
        print("dnc - Read Encrypted Files")
        print("typ - Word Processor")
        print("rdf - Read Files")
        print("upd - Check For Update")
        print("cmd - Command Prompt")
        print("ist - Install Apps")
        print("run - Run Files")
        print(" ~~Type 'run [file] to launch direct")
        print("lsf - List files")
        print(" ~~Use 'lsfa' to return all filetypes")
        pyos_os_ad()
    elif os_input == ("ext"):
        exit()
    elif os_input == ("lgt"):
        print("Logging out...")
        os.system("pause >nul")
        pyos_login()
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
            print("No app named " + os_in_app)
            os.chdir('..')
            pyos_os_ad()
        print("Launched " + os_in_app)
        pyos_os_ad()
    elif os_input == ("cls") or ("clear"):
        os.system("cls")
        print("##################################################")
        print("                      Py OS                       ")
        print("                       Sys                        ")
        print("                      -ADM-                       ")
        print("##################################################")
        pyos_os_ad()
    elif os_input == ("enc"):
        pyos_enc()
    elif os_input == ("dnc"):
        pyos_dnc()
    elif os_input == ("typ"):
        print("")
        print("###")
        print("Start typing to begin...")
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
    elif os_input == ("rdf"):
        print("Enter file name to open.")
        pyos_read = input("")
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
    elif os_input == ("upd"):
        print("Checking for update...")
        if pyos_upd_cc == False:
            print("No update required")
            pyos_os_ad()
        else:
            os.chdir('..')
            os.chdir('..')
            pyos_update()
    elif os_input == ("cmd"):
        os.system("cls")
        os.system("@mode con cols=130 lines=34")
        print("##################################################")
        print("Windows Command Prompt Emulator.")
        print("Type 'return' to go back to PyOS.")
        pyos_adm_cmd()
    elif ("run") in os_input:
        if os_input == ("run"):
            print("Please specify file!")
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
    elif os_input == ("ist"):
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
    elif os_input == ("lsfa"):
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
    else:
        print(os_input + " - Bad Input")
        pyos_os_ad()
def pyos_adm_cmd():
    pyos_cmd_dr = os.getcwd()
    pyos_cmd_in = input(pyos_cmd_dr + ">")
    if pyos_cmd_in == ("return"):
        pyos_os_ad()
        os.system("@mode con cols=50 lines=34")
    else:
        try:
            os.system(pyos_cmd_in)
            pyos_adm_cmd()
        except:
            print("Unrecognised command")
            pyos_adm_cmd()
def pyos_enc():
    os.system("cls")
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
                with open('prkey.file.bin', 'wb') as f:
                        f.write(encrypted_key)
                        os.system("attrib +s +h prkey.file.bin")
                with open('pukey.file.bin', 'wb') as f:
                        f.write(key.publickey().exportKey())
                        os.system("attrib +s +h pukey.file.bin")
                with open('data.file.bin', 'wb') as out_file:
                    recipient_key = RSA.import_key(
                        open('pukey.file.bin').read())
                    session_key = get_random_bytes(16)
                    cipher_rsa = PKCS1_OAEP.new(recipient_key)
                    out_file.write(cipher_rsa.encrypt(session_key))
                    cipher_aes = AES.new(session_key, AES.MODE_EAX)
                    data = bytes(line)
                    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                    out_file.write(cipher_aes.nonce)
                    out_file.write(tag)
                    out_file.write(ciphertext)
                    os.system("attrib +s +h data.file.bin")
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
                    open('prkey.file.bin').read(),
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
    print("Failed to import Cryptodomex!")
    print("Install it with CMD by using the command")
    print("pip install pycryptodomex")
    cryfail = getpass.getpass("Press any key to continue...")
    if cryfail == ("dr"):
        print(os.getcwd())
        os.system("pause >nul")
        pyos_cryfail()
    if cryfail == ("bk"):
        os.chdir('..')
        pyos_cryfail()
    if cryfail == ("tmp"):
        if pyos_osn in (os.getcwd()):
            os.chdir('..')
        global pyos_osn
        if os.path.exists("tmpacc"):
            os.chdir("tmpacc")
        else:
            os.mkdir('tmpacc')
            os.chdir("tmpacc")
        pyos_osn = ("tmpacc")
        pyos_os_us()
    else:
        exit()



    
###########
devmess = ('''
:)
So a few of you might be wondering why I'm not doing a changelog for this
program. The answer is simple - I am. Just not yet. You see, changelogs are used
to log both significant and tiny changes to code. Since PyOS is still in
ridiculously early development, there is a lot of big and lil changes
like all the time, so noting each and every one down is for the most part
time wasting. To me, anyway.
I'll start making a changelog when we reach V 0.1.
Thanks! ''')
pyos_boot()
