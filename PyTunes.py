### Pytunes Version 1.1.1.2 ###
# Hi user! Welcome to PyTunes! This is a fully standalone media player
# coded entirely in Python3. Only works in windows for now, I'm working on
# a linux edition. Hope you enjoy using it!
# MIT License
#
# Copyright (c) 2017 - 20xx Sam Forrester
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
## Version Numbers
#
#
#0.x Arcade
#1.x Tonic
#2.x Factory
#3.x Robot
#4.x Sub
#5.x Office
#6.x Rhythm
#
#####
# Changelog 24/01/18 - Ver 0.8.1.8 B4
# - Added window resize when creating playlist
# - Line 770 - Added check for sound effect to prevent crash for users who don't have it
# - Line 447 & 443 - Added mixer init to prevent crash if mixer not init before
#   attemtping to stop / rewind music
# - :::NOTE::: During testing the automated pygame exist check at the start
#   of the program returns a false positive on some machines. Looking into a fix
#   for this, whether it's my fault or pygame's I'm not sure. Maybe some users
#   have different install directories? Maybe specifying one specific dir is
#   the problem.
# - Added error catch if someone somehow boots into the login screen w/o login details
# - Removed progressbar altogether, just another thing users had to install that served no purpose
# - Removed 'import pygame' from the initial boot sequence because that was so dumb to have
#   an error catcher after trying to import it lol
# - Set all file extensions to .pyd instead of .ocr (Accounts will have to be remade sorry y'all)
# - Started doing a changelog cause I'm professional af
# - Added a 'import pygame' at the top of songsli() and playlistsli() because python is stupid and forgets it's imported sometimes
# - :::NOTE::: The reason there is a 'global' before each import of pygame in the preboot() cycle is because
#   that is the only way I could get any pygame function to actually work. I do not know why, the most confusing thing is that
#   pygame doesn't work without the global declaration before import HOWEVER python still throws up errors when defining it as global.
#####
# Changelog 26/01/18 - Ver 0.9.0.4 B6
# - The Import Update! Added the ability to import from your music folder OR a specified directory right from the music menu.
#   The function uses roughly the same script as the setup version but now you can specifiy directories. Take a look at it under def musimport()
# - General bug fixes, like actually exiting the program after an error catch in the login screen and changing unnecessary time.sleep() functions to os.system("pause >nul")
# - Refined the missing Pygame error screen so it is much less confusing and omits any mention of progressbar
# - Now on version 0.9 - We're nearly at 1.0 boys and girls! Plans for the future - Refining the boot process and error catching, adding custom playback speeds,
#   adding support for m4a files (if at all possible without forcing the user to install more modules - take this with a grain of salt)
#   and hopefully - this isn't guaranteed - making the program linux compatible. We'll have to see if I can be bothered. Any more bugs I find I should have fixed by next week. 
#####
# Changelog 26/01/18 PATCH - Ver 0.9.0.6 B7
# - Just gonna push this update tonight cause it's cool, added a 'now playing' in the songs menu. I know I've already pushed an update tonight but I got bored and carried on coding
#   for a while so here is version 0.9.0.6 :)
#####
# Changelog 27/01/18 - Ver 1.0.0.0 R1
# - Added updating! Thanks to being on github, the program can now access the raw section of github and update itself. Find the updater in settings.
# - That's literally all I've changed. also welcome to 1.0 everyone!
#####
# Changelog 27/01/18 - Ver 1.0.0.2 R1 HOTFIX
# - Fixed a referance bug during first time setup, nothing major, just annoying for new users.
#####
# Changelog 28/01/18 - Ver 1.0.0.4 R1
# - Added a new dev option, not that anyone would use it unless they're a dev
# - Removed import of some useless modules to (marginally) improve loading times
# - Planning an auto update system in the near future, that would be cools
#   of course by near future I mean I'll probably have it done by tonight :)
#####
# Changelog 28/01/18 - Ver 1.1.0.0 R1 
# - Added that auto updater I was talking about :)
# - Other subtle changes like re-adding that urllib module for the auto updater and
#   assigning the update manager a cmd title
#####
# Changelog 28/01/18 - Ver 1.1.0.2 R1 HOTFIX
# - Update manager had a huge bug, should be fixed now
# - Error code LxFExF fixed
#####
# Changelog 29/01/18 - Ver 1.1.0.4 R1
# - Bug fixes and stuff, nothing major
# - No real plans as to where to take this next? Will come up with something soon
#####
# Changelog 29/01/18 - Ver 1.1.0.6 R1 HOTFIX
# - Whoops accidentally broke the program, should be fixed now :)
#####
# Changelog 30/01/18 - Ver 1.1.0.8 R1
# - Added a record of every song played in the session, in the songs menu
# - Bigly things planned :)
#####
# Changelog 09/02/18 - Ver 1.1.1.0 R1
# - Hello! That big update is still on its way, I don't have a huge amount of free time though
#   so it'll be a while before it's out.
# - So apparently it was my fault that PyGame kept failing to install, the directory I specified
#   only seems to work for me and like no one else so I've patched that up!
# - Added some other useless dev stuff nobody will look at 
# - Removed Herobrine
#####
# Changelog 13/02/18 - Ver 1.1.1.2 R1
# - Hi there! I should probably mention that the big update isn't actually for PyTunes.
#   Instead, PyTunes will become part of a larger project I'm working on - PyOS.
#   PyOS is currently in development and you can pick up the latest version on my github.
#   Feel free to continue using PyTunes as is, but soon it will be part of a much larger thing!
# - Also bug fixes :)
#
####################### Total modules: 13
print("Importing...") #
import os             # (ONE) of which are currently dormant
import time           #
import getpass        #
import random         #
import shutil         #
import re             #
import glob           #
import sys            #    ¬ This one, it was used for a playlist function
import select         #    | to play a playlist in the background. 
import urllib.request #    | Function removed due to pygame being 
import pickle         #    | A dumbass and not working with the queue funtion.
import threading      # ---
import codecs         #
print("Import OK!")   #
#################################################################

#################################################################

####################### U S E R C H E C K #######################
os.system("@mode con cols=130 lines=34")
global programversion
programversion = str("PyTunes 1.1.1.2 Release 1 'Tonic'")
global todaysongs
todaysongs = []
os.system("title " + programversion)
def usercheck():
    print("[SC] User Check...")
    time.sleep(0.1)
    curdrs = os.getcwd()
    if os.path.exists("userfvg.pyd"):
        print("[OK] userfvg.pyd exists")
        global currentlyplaying
        currentlyplaying = ("Nothing")
        print("[OK] Song variable declared")
        print("[SC] Removing update files...")
        if os.path.exists("updatemanager.py"):
            os.remove("updatemanager.py")
        if os.path.exists("update.pyd"):
            os.remove("update.pyd")
        print("[OK] Done")
        print("[SC] Error Check...")
        time.sleep(0.1)
        if os.path.exists("userps2.pyd"):
            print("[FAIL] Error!")
            if os.path.exists("err.ogg"):
                pygame.mixer.music.load("err.ogg")
                pygame.mixer.music.play()
            time.sleep(0.5)
            print("[FAIL] Collecting Data...")
            time.sleep(1)
            os.system("cls")
            os.remove("userps.pyd")
            with open("userps2.pyd", 'r') as p:
                for lineusn in p:
                    with open("userps.pyd", 'w') as r: 
                        r.write(lineusn)
                        r.close()
                        p.close()
                        os.remove("userps2.pyd")
                        print(programversion)
                        print("0_0")
                        print("")
                        print("PyTunes ran into a problem and had to restart.")
                        print("If you contact the developer, please quote error code S2PDxE")
                        print("Your password has been changed to the one you entered.")
                        print("Please press any key to restart.")
                        os.system("pause >nul")
                        os.chdir('..')
                        os.startfile("PyTunes.py")
                        exit()
        else:
            print("[OK] userps2.pyd does not exist")
            print("[SC] Confirming User...")
            if not os.path.exists("username.pyd"):
                print("[FAIL] Error!")
                if os.path.exists("err.ogg"):
                    pygame.mixer.music.load("err.ogg")
                    pygame.mixer.music.play()
                time.sleep(0.5)
                print("[FAIL] Collecting Data...")
                time.sleep(1)
                os.system("cls")
                if os.path.exists("userfvg.pyd"):
                    os.remove("userfvg.pyd")
                if os.path.exists("userfva.pyd"):
                    os.remove("userfva.pyd")
                if os.path.exists("userps.pyd"):
                    os.remove("userps.pyd")
                if os.path.exists("userdob.pyd"):
                    os.remove("userdob.pyd")
                print(programversion)
                print("0_0")
                print("")
                print("PyTunes ran into a problem and had to restart.")
                print("If you contact the developer, please quote error code S3DAxE")
                print("Your password has been changed to the one you entered.")
                print("Please press any key to restart.")
                os.system("pause >nul")
                exit()
            else:
                print("[OK] No account deletion fails detected")
                print("[SC] Ensuring all files are locked...")
                os.system("attrib +s +h username.pyd")
                os.system("attrib +s +h userdob.pyd")
                os.system("attrib +s +h userps.pyd")
                os.system("attrib +s +h userfva.pyd")
                os.system("attrib +s +h userfvg.pyd")
                if os.path.exists("err.ogg"):
                    os.system("attrib +s +h err.ogg")
                if os.path.exists("iserrorskipon.pyd"):
                    os.system("attrib +s +h iserrorskipon.pyd")
                print("[OK] Attributed 'hidden' to all data files")
                print("[SC] Processing Songs...")
                presonglist = glob.glob("*.mp3")
                presonglist.extend(glob.glob("*.wav"))
                le = len(presonglist)
                prelestr = str(le)
                print("[OK] " + prelestr + " Songs [With Usable Formats] Found!")
                print("[OK] Songs Processed")
                print("[SC] Checking for update...")
                update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/PyTunes.py') 
                response = urllib.request.urlopen(update) 
                newcode = response.read() 
                master = newcode.decode()
                os.chdir('..')
                os.system("type PyTunes.py >> update2.pyd")
                os.system("attrib +s +h update2.pyd")
                with open('update.pyd', 'w') as u: 
                    u.write(master)
                    os.system("attrib +s +h update.pyd")
                    u.close
                with open('update.pyd', 'r') as u:
                    with open('update2.pyd', 'r') as r:
                        for lineu in u:
                            for liner in r:
                                print("[SC] Current Verison - ", liner)
                                print("[SC] Server Verison - ", lineu)
                                if (lineu) == (liner):
                                    print("[OK] No update needed!")
                                    u.close()
                                    r.close()
                                    os.remove("update.pyd")
                                    os.remove("update2.pyd")
                                    os.chdir(curdrs)
                                    redboot()
                                else:
                                    print("[OK] Update Required!")
                                    print("")
                                    u.close()
                                    r.close()
                                    os.remove("update.pyd")
                                    os.remove("update2.pyd")
                                    os.system("pause")
                                    updatecheck()
    if not os.path.exists("userfvg.pyd"):
        os.system("attrib +s +h err.ogg")
        os.system("attrib +s +h iserrorskipon.pyd")
        print("[OK] userfvg.pyd does not exist, assuming setup is required")
        print("[OK] Ready to boot!")
        if os.path.exists("deverb.pyd"):
            print("Auto boot disabled...")
            print("Waiting for user choice... [y/n/s]")
            verbin = input("")
            if verbin == ("y"):
                menu1()
            if verbin == ("n"):
                exit()
            if verbin == ("s"):
                print("Skip setup? Crash is likely unless files have been manually created [y/n]")
                verbinskip = input("")
                if verbinskip == ("y"):
                    menu2()
                if verbinskip == ("n"):
                    menu1()
                else:
                    menu2()
            else:
                print("Bad Input!")
                print("Booting to setup...")
                time.sleep(1)
                menu1()
        else:
            print("Auto boot enabled...")
            time.sleep(0.1)
            menu1()
def redboot():
    print("[OK] Ready to boot!")
    if os.path.exists("deverb.pyd"):
        print("Auto boot disabled...")
        print("Waiting for user choice... [y/n]")
        verbin = input("")
        if verbin == ("y"):
            if os.path.exists("skippass.pyd"):
                menu2c()
            else:
                boot()
        if verbin == ("n"):
            exit()
        else:
            print("Bad Input!")
            print("Booting...")
            time.sleep(1)
            menu2()
    else:
        print("Auto boot enabled...")
        if os.path.exists("skippass.pyd"):
            menu2c()
        else:
            boot()
def boot():
    time.sleep(0.1)
    time.sleep(0.1)
    print("######################")
    time.sleep(0.1)
    print("# |--|\- -/          #")
    time.sleep(0.1)
    print("# | _| \|/           #")
    time.sleep(0.1)
    print("# |_|  |_| T U N E S #")
    time.sleep(0.1)
    print("######################")
    time.sleep(0.1)
    print("")
    menu2()
####################### U S E R C H E C K #######################

    
#############################################################


####################### S E T U P #######################
def menu1():
    os.system("@mode con cols=100 lines=34")
    os.system("cls")
    time.sleep(0.1)
    print("######################")
    time.sleep(0.1)
    print("# |--|\- -/          #")
    time.sleep(0.1)
    print("# | _| \|/           #")
    time.sleep(0.1)
    print("# |_|  |_| T U N E S #")
    time.sleep(0.1)
    print("######################")
    time.sleep(0.1)
    print("")
    global trueusernm
    trueusernm = getpass.getuser()
    username = input("Welcome to PyTunes, " + trueusernm + "! We see this is your first time, so please enter your name: ")
    print("")
    for i in range(5):
        userps = input("Enter a password for your account: ")
        if userps == (""):
            print("Passwords cannot be 0 characters!")
            os.system("pause >nul")
            menu1()
        if not re.match("^[0-9A-Za-z]*$", userps):
            print("Illegal Characters! Please only use a-Z and 0-9.")
            os.system("pause >nul")
            menu1()
        elif len(userps) < 4:
            print("Error! Password too short! Please make it over 4 characters.")
            os.system("pause >nul")
            menu1()
        else:
            print("")
            userpsche = input("Re-enter your password: ")
            if userpsche == userps:
                print("Password accepted!")
                print("")
                userdob = input("Please enter the year you were born (YYYY): ")
                print("")
                with open("username.pyd", 'w') as f:
                    f.write(username)
                with open("userdob.pyd", 'w') as f:
                    f.write(userdob)
                with open("userps.pyd", 'w') as f:
                    f.write(userps)
                f.close()    
                setup()
            else:
                print("Passwords do not match!")
def setup():
    dircheck = input("Would you like PyTunes to check your songs library for music? [y/n] ")
    if dircheck == ("y"):
        global curdr
        curdr = os.getcwd()
        os.chdir("C:/Users/" + trueusernm + "/Music")
        songlist_copy = glob.glob("*.mp3")
        songlist_copy.extend(glob.glob("*.wav"))
        if songlist_copy == (""):
            print("No Files Found!")
            os.system("pause >nul")
            setupbreak()
        else:
            print("Found these songs...")
            maxnum = len(songlist_copy)
            maxnumext = maxnum + 5
            maxnumstr = str(maxnumext)
            os.system("@mode con cols=130 lines=" + maxnumstr)
            print("")
            for number, letter in enumerate(songlist_copy):
                trnu = number + 1
                trnus = str(trnu)
                letterm = letter.replace(".mp3", "")
                lettermm = letterm.replace(".wav", "")
                print(trnus + ":", lettermm)
            print("")
            print("Press any key to copy (Existing songs will be skipped) ")
            os.system("pause >nul")
            os.system("@mode con cols=130 lines=34")
            print("Copying...")
            dstsong = (curdr)
            srcsong = ("C:/Users/" + trueusernm + "/Music")
            for songlist_copy in songlist_copy:
                local = songlist_copy.split('"')
                dst_file_path = "%s\%s" % (dstsong,local[0])
                (root,file_name) = os.path.splitext(dst_file_path)
                src_file_path = os.path.normcase("%s/%s" % (srcsong,local[0]))
                shutil.copyfile(src_file_path,dst_file_path)
                print("Copying " + "" + local[0])
            print("Copied!")
            os.system("@mode con cols=130 lines=34")
            print("")
            os.chdir(curdr)
            setupbreak()
    else:
        setupbreak()
def setupbreak():
    userfva = input("Enter your favourite music artist: ")
    with open("userfva.pyd", 'w') as f:
        f.write(userfva)
        f.close() 
        setupcont()
def setupcont():
    print("")
    userfvg = input("Enter your favourite genre of music: ")
    with open("userfvg.pyd", 'w') as f:
        f.write(userfvg)
        print("")
        print("Finishing Up...")
        global currentlyplaying
        currentlyplaying = ("Nothing")
        print("")
        print("Setup complete! Going to main menu...")
        print("")
        time.sleep(1)
        f.close()
        dr = os.getcwd()
        time.sleep(0.1)
        os.system("attrib +s +h username.pyd")
        time.sleep(0.1)
        os.system("attrib +s +h userdob.pyd")
        time.sleep(0.1)
        os.system("attrib +s +h userps.pyd")
        time.sleep(0.1)
        os.system("attrib +s +h userfva.pyd")
        time.sleep(0.1)
        os.system("attrib +s +h userfvg.pyd")
        time.sleep(0.1)
        menu2()
####################### S E T U P #######################


#########################################################
        

####################### L O G I N #######################       
def menu2():
    os.system("cls")
    print("######################")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    print("")
    n = int(3)
    if os.path.exists("username.pyd"):
        with open("username.pyd", 'r') as f:
            for lineus in f:
                pswrd = getpass.getpass("Welcome back to PyTunes, " + lineus + "! Enter your password to continue... ")
        for loginloop in range(3):
            with open("userps.pyd", 'r') as f:
                for lineps in f:
                    if (pswrd) == (lineps):
                        print("Login Successful.")
                        os.system("pause >nul")
                        f.close()   
                        menu2c()
                    else:
                        time.sleep(2)
                        print("Could not verify password. Try Again...")
                        if os.path.exists("err.ogg"):
                            pygame.mixer.music.load("err.ogg")
                            pygame.mixer.music.play()
                        pswrd = getpass.getpass("Password: ")
    else:
        if os.path.exists("userfvg.pyd"):
            os.remove("userfvg.pyd")
        if os.path.exists("userfva.pyd"):
            os.remove("userfva.pyd")
        if os.path.exists("userps.pyd"):
            os.remove("userps.pyd")
        if os.path.exists("userdob.pyd"):
            os.remove("userdob.pyd")
        print(programversion)
        print("An error has occured. If you contact the developer, please quote error code LxFExF")
        print("Press any key to restart.")
        os.system("pause >nul")
        exit()
####################### L O G I N #######################


#########################################################
                    

#######################  M E N U  ####################### 
def menu2c():
    os.system("cls")
    print("######################")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    print("")
    print("1} Songs Library")
    print("2} Playlists")
    print("3} Settings")
    print("4} Log Out")
    print("Enter either 1, 2, 3 or 4 depending on what you want to do.")
    print("")
    menuch = input("")
    if menuch == ("1"):
        songsli()
    if menuch == ("2"):
        playlistsli()
    if menuch == ("3"):
        settingsli()
    if menuch == ("4"):
        print("Logging out...")
        os.system("pause >nul")
        pygame.mixer.music.stop()
        menu2()
    else:
        print("Bad Input! Please enter either 1, 2, 3 or 4 to naviagte to the selected menu.")
        os.system("pause >nul")
        menu2c()
#######################  M E N U  #######################


#############################################################
        

####################### S O N G S  L I S T #######################
def songsli():
    import pygame
    os.system("cls")
    print("######################")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    time.sleep(0.02)
    global currentlyplaying
    print("Songs List (Currently Playing - " + currentlyplaying + ")")
    print("")
    print("1} Restart Current Song")
    print("2} Stop Current Song")
    print("3} Choose Song From Library")
    print("4} Change Volume")
    print("5} Import Songs")
    print("6} Songs played today")
    print("7} Go Back")
    print("Press any key to play a random song.")
    print("")
    songschs = input("")
    if songschs == ("1"):
        pygame.mixer.init()
        pygame.mixer.music.rewind()
        songsli()
    if songschs == ("2"):
        pygame.mixer.init()
        pygame.mixer.music.stop()
        currentlyplaying = ("Nothing")
        songsli()
    if songschs == ("3"):
        #this songlist thing takes all the supported formats of pygame.mixer and lists them
        #excluding .ogg files because that would list the program's sound effects as playable songs
        songlist = glob.glob("*.mp3")
        songlist.extend(glob.glob("*.wav"))
        maxnum = len(songlist)
        maxnumext = maxnum + 5
        maxnumstr = str(maxnumext)
        os.system("@mode con cols=130 lines=" + maxnumstr)
        print("Current Songs In Library...")
        print("")
        #lists, however, aren't partiicularly user friendly. This little chunk sorts the list and numbers each list option.
        for number, letter in enumerate(songlist):
            #the 'trnu = number + 1' part is so the list starts at 1, not 0, for added user friendliness.
            trnu = number + 1
            #convert int to str for printing properly
            trnus = str(trnu)
            #remove the .mp3 part to make the printed title just the title and not title.mp3
            letterm = letter.replace(".mp3", "")
            #print [number on list]: [song title]
            print(trnus + ":", letterm)
        print("")
        print("Enter number of song you'd like to play...")
        choosesst = input("")
        if re.match("^[A-Za-z]*$", choosesst):
            os.system("@mode con cols=130 lines=34")
            print("Please type only the number of the song you want to play! [1, 2, 3 etc]")
            os.system("pause >nul")
            songsli()
        chooses = int(choosesst)
        truechoice = chooses - 1
        if truechoice < maxnum:
            choices = songlist[truechoice]
            choicename = choices.replace(".mp3", "")
            print("")
            print("Now Playing " + choicename + "...")
            global todaysongs
            todaysongs.extend([choicename])
            global currentlyplaying
            currentlyplaying = (choicename)
            pygame.mixer.pre_init()
            pygame.mixer.init()
            pygame.mixer.music.load(choices)
            pygame.mixer.music.play()
            os.system("pause >nul")
            os.system("@mode con cols=100 lines=34")
            songsli()
        if truechoice < 0:
            print("Choice too low!")
            os.system("pause >nul")
            os.system("@mode con cols=100 lines=34")
            songsli()            
        else:
            print("Choice too high!")
            os.system("pause >nul")
            os.system("@mode con cols=100 lines=34")
            songsli()
    if songschs == ("4"):
        volcha()
    if songschs == ("5"):
        musimport()
    if songschs == ("6"):
        maxnum = len(todaysongs)
        maxnumext = maxnum + 5
        maxnumstr = str(maxnumext)
        os.system("@mode con cols=130 lines=" + maxnumstr)
        print("")
        for number, letter in enumerate(todaysongs):
            trnu = number + 1
            trnus = str(trnu)
            letterm = letter.replace(".mp3", "")
            print(trnus + ":", letterm)
        os.system("pause")
        os.system("@mode con cols=100 lines=34")
        songsli()
    if songschs == ("7"):
        menu2c()
    else:
        songselector()
def musimport():
    import pygame
    trueusernm = getpass.getuser()
    curdr = os.getcwd()
    print("")
    newdir = input("Would you like to import from a custom directory? ('n' will set the directory as your music folder) [y/n]: ")
    if newdir == ("y"):
        srcsong = input("Paste the directory you want PyTunes to copy from: ")
        isdir = os.path.isdir(srcsong)
        isdirstr = str(isdir)
        if isdirstr == ("True"):
            os.chdir(srcsong)
            songlist_copy2 = glob.glob("*.mp3")
            songlist_copy2.extend(glob.glob("*.wav"))
            print("Found these songs...")
            maxnum = len(songlist_copy2)
            maxnumext = maxnum + 5
            maxnumstr = str(maxnumext)
            os.system("@mode con cols=130 lines=" + maxnumstr)
            print("")
            for number, letter in enumerate(songlist_copy2):
                trnu = number + 1
                trnus = str(trnu)
                letterm = letter.replace(".mp3", "")
                print(trnus + ":", letterm)
            print("")
            print("Press any key to copy (Existing songs will be skipped) ")
            os.system("pause >nul")
            pygame.mixer.init()
            pygame.mixer.music.stop()
            os.system("@mode con cols=130 lines=34")
            dstsong = (curdr)
            for songlist_copy2 in songlist_copy2:
                local = songlist_copy2.split('"')
                dst_file_path = "%s\%s" % (dstsong,local[0])
                (root,file_name) = os.path.splitext(dst_file_path)
                src_file_path = os.path.normcase("%s/%s" % (srcsong,local[0]))
                shutil.copyfile(src_file_path,dst_file_path)
                print("Copying " + "" + local[0])
            print("Songs Copied!")
            os.system("pause >nul")
            os.chdir(curdr)
            songsli()
        else:
            print("Invalid input - Not a directory!")
            os.system("pause")
            musimport()
    else:
        os.chdir("C:/Users/" + trueusernm + "/Music")
        songlist_copy2 = glob.glob("*.mp3")
        songlist_copy2.extend(glob.glob("*.wav"))
        print("Found these songs...")
        maxnum = len(songlist_copy2)
        maxnumext = maxnum + 5
        maxnumstr = str(maxnumext)
        os.system("@mode con cols=130 lines=" + maxnumstr)
        print("")
        for number, letter in enumerate(songlist_copy2):
            trnu = number + 1
            trnus = str(trnu)
            letterm = letter.replace(".mp3", "")
            print(trnus + ":", letterm)
        print("")
        print("Press any key to copy (Existing songs will be skipped) ")
        os.system("pause >nul")
        pygame.mixer.init()
        pygame.mixer.music.stop()
        os.system("@mode con cols=130 lines=34")
        srcsong = ("C:/Users/" + trueusernm + "/Music")
        dstsong = (curdr)
        for songlist_copy2 in songlist_copy2:
            local = songlist_copy2.split('"')
            dst_file_path = "%s\%s" % (dstsong,local[0])
            (root,file_name) = os.path.splitext(dst_file_path)
            src_file_path = os.path.normcase("%s/%s" % (srcsong,local[0]))
            shutil.copyfile(src_file_path,dst_file_path)
            print("Copying " + "" + local[0])
        print("Songs Copied!")
        os.system("pause >nul")
        os.chdir(curdr)
        songsli()
def volcha():
    print("")
    pygame.mixer.init()
    curvol = pygame.mixer.music.get_volume()
    curvolr = round(curvol, 2)
    curvolt = curvolr * 100
    curvolint = str(curvolt)
    curvolo = curvolint.replace(".0", "")
    print("Current Volume: " + curvolo)
    newvol = input("Enter new volume value: ")
    if newvol == (""):
            print("Cancelled")
            os.system("pause >nul")
            songsli()
    else:
        if re.match("^[A-Za-z]*$", newvol):
            print("Please do not use letters!")
            os.system("pause >nul")
            volcha()
        else:
            newvolint = float(newvol)
            newvolt = newvolint / 100
            pygame.mixer.music.set_volume(newvolt)
            songsli()
def songselector():
    dr = os.getcwd()
    rands = random.choice(os.listdir(dr))
    raco = ("0")
    if rands.endswith('.mp3'):
        randname = rands.replace(".mp3", "")
        print("")
        print("Now Playing " + randname + "...")
        global todaysongs
        todaysongs.extend([randname])
        global currentlyplaying
        currentlyplaying = (randname)
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.music.load(rands)
        pygame.mixer.music.play()
        os.system("pause >nul")
        songsli()
    else:
        songsli()
####################### S O N G S  L I S T #######################


#################################################################
        

####################### P L A Y L I S T S #######################
def playlistsli():
    import pygame
    os.system("cls")
    print("######################")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    print("|\-_-/          #")
    print("| \|/           #")
    print("  |_| T U N E S #")
    print("#################")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    print("/          #")
    print("           #")
    print(" T U N E S #")
    print("############")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    print("      #")
    print("      #")
    print("N E S #")
    print("#######")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    print("#")
    print("#")
    print("#")
    print("#")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    print("Playlists")
    print("")
    print("1} Play Playlist")
    print("2} Create New Playlist")
    print("3} Delete Playlist")
    print("4} Go Back")
    print("")
    playlistsch = input("")
    if playlistsch == ("1"):
        if os.path.exists("playlist.pyd"):
            backplay()
        else:
            print("You do not have a playlist! Create one first.")
            os.system("pause >nul")
            playlistsli()                
    if playlistsch == ("2"):
        createplaylist()
    if playlistsch == ("3"):
        if os.path.exists("playlist.pyd"):
            print("Are you sure you want to delete your playlist? [y/n] ")
            playdel = input("")
            if playdel == ("y"):
                print("Deleting...")
                os.remove("playlist.pyd")
                print("Deleted")
                os.system("pause >nul")
                playlistsli()
        else:
            print("No playlist to delete!")
            os.system("pause >nul")
            playlistsli()
    if playlistsch == ("4"):
        menu2c()
    else:
        print("Bad Input! Please enter either 1, 2, 3 or 4 to naviagte to the selected menu.")
        os.system("pause >nul")
        playlistsli()
def backplay():
    with open('playlist.pyd', 'rb') as f:
        playlist = pickle.load(f)
        pygame.mixer.init()
        maxnum = len(playlist)
        maxnumext = maxnum + 5
        maxnumstr = str(maxnumext)
        os.system("@mode con cols=130 lines=" + maxnumstr)
        print("Current Songs In Library...")
        print("")
        for number, letter in enumerate(playlist):
            trnu = number + 1
            trnus = str(trnu)
            letterm = letter.replace(".mp3", "")
            print(trnus + ":", letterm)
        print("")
        print("Enter number of song you'd like to play...")
        choosesst = input("")
        if re.match("^[A-Za-z]*$", choosesst):
            os.system("@mode con cols=130 lines=34")
            print("Please type only the number of the song you want to play! [1, 2, 3 etc]")
            os.system("pause >nul")
            f.close()
            playlistsli()
        chooses = int(choosesst)
        truechoice = chooses - 1
        if truechoice < maxnum:
            choices = playlist[truechoice]
            choicename = choices.replace(".mp3", "")
            print("")
            print("Now Playing " + choicename + "...")
            pygame.mixer.pre_init()
            pygame.mixer.init()
            pygame.mixer.music.load(choices)
            pygame.mixer.music.play()
            os.system("pause >nul")
            os.system("@mode con cols=100 lines=34")
            f.close()
            playlistsli()
        else:
            print("Choice too high!")
            os.system("pause >nul")
            os.system("@mode con cols=100 lines=34")
            f.close()
            playlistsli()
def createplaylist():
    global currentplay
    currentplay = []
    print("The program will now print a list of your songs. Type the numbers of the songs you want to include in the playlist, then type 'done' when you're finished.")
    os.system("pause >nul")
    createplaylister()
def createplaylister():
    songlist = glob.glob("*.mp3")
    songlist.extend(glob.glob("*.wav"))
    maxnum = len(songlist)
    maxnumext = maxnum + 5
    maxnumstr = str(maxnumext)
    os.system("@mode con cols=130 lines=" + maxnumstr)
    print("Current Songs In Library...")
    print("")
    for number, letter in enumerate(songlist):
        trnu = number + 1
        trnus = str(trnu)
        letterm = letter.replace(".mp3", "")
        print(trnus + ":", letterm)
    print("")
    print("Enter number of song you'd like to add...")
    choosesst = input("")
    if choosesst == ("done"):
        createpl2()
    else:
        if re.match("^[A-Za-z]*$", choosesst):
            os.system("@mode con cols=130 lines=34")
            print("Please type only the number of the song you want to add! [1, 2, 3 etc]")
            os.system("pause >nul")
            createplaylister()
        chooses = int(choosesst)
        truechoice = chooses - 1
        if truechoice < maxnum:
            choices = songlist[truechoice]
            choicestr = str(choices)
            currentplay.extend([choicestr])
            choicename = choices.replace(".mp3", "")
            print("")
            print("Added " + choicename + "...")
            os.system("pause >nul")
            os.system("@mode con cols=100 lines=34")
            createplaylister()
def createpl2():
    with open('playlist.pyd', 'wb') as f:
        currentplayst = str(currentplay)
        pickle.dump(currentplay, f)
        f.close()
        print("")
    print("Playlist Created!")
    os.system("pause >nul")
    playlistsli()
####################### P L A Y L I S T S #######################


#################################################################

        
#######################  S E T T I N G S  ####################### 
def settingsli():
    os.system("cls")
    print("######################")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("# |--|\-_-/          #")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("# | _| \|/           #")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("# |_|  |_| T U N E S #")
    print("######################")
    time.sleep(0.02)
    os.system("cls")
    print("######################")
    time.sleep(0.02)
    print("Settings")
    print("")
    print("1} See User Information")
    print("2} Change Password")
    print("3} Delete Account")
    print("4} Update Program")
    print("5} Go Back")
    print("")
    settingsch = input("")
    if settingsch == ("1"):
        pswrdui = getpass.getpass("Enter your account password... ")
        with open("userps.pyd", 'r') as f:
            for lineps in f:
                if (pswrdui) == (lineps):
                    print("Login Successful.")
                    time.sleep(1)
                    userinfo()
                else:
                    print("Incorrect Password!")
                    if os.path.exists("err.ogg"):
                        pygame.mixer.music.load("err.ogg")
                        pygame.mixer.music.play()
                    os.system("pause >nul")
                    settingsli()
    if settingsch == ("2"):
        pswdch()
    if settingsch == ("3"):
        pswrdui = getpass.getpass("Enter your account password... ")
        with open("userps.pyd", 'r') as f:
            for lineps in f:
                if (pswrdui) == (lineps):
                    f.close()
                    print("Login Successful.")
                    time.sleep(1)
                    delacc()
                else:
                    print("Incorrect Password!")
                    pygame.mixer.music.load("err.ogg")
                    pygame.mixer.music.play()
                    os.system("pause >nul")
                    settingsli()
    if settingsch == ("4"):
        os.chdir('..')
        updatecheck()
    if settingsch == ("5"):
        menu2c()
    if settingsch == ("27"):
        with open("username.pyd", 'r') as f:
            for lineps in f:
                if ("dev") == (lineps):
                    f.close()
                    print("")
                    print("Hello Dev!")
                    os.system("pause >nul")
                    devoptions()
                else:
                    f.close()
                    print("Bad Input! Please enter either 1, 2, 3 or 4 to naviagte.")
                    os.system("pause >nul")
                    settingsli()
    else:
        print("Bad Input! Please enter either 1, 2, 3 or 4 to naviagte.")
        settingsli()
def updatecheck():
    print("Starting update manager...")
    if os.path.exists("updatemanager.py"):
        os.startfile("updatemanager.py")
        exit()
    else:
        os.system("echo import time >> updatemanager.py")
        os.system("echo import os >> updatemanager.py")
        os.system("echo import urllib.request >> updatemanager.py")
        os.system("echo os.system('title PyTunes Update Manager') >> updatemanager.py")
        os.system("echo print('Collecting update from github...') >> updatemanager.py")
        os.system("echo update = urllib.request.Request('https://raw.githubusercontent.com/SimLoads/PyTunes.py/master/PyTunes.py') >> updatemanager.py")
        os.system("echo response = urllib.request.urlopen(update) >> updatemanager.py")
        os.system("echo newcode = response.read() >> updatemanager.py")
        os.system("echo master = newcode.decode() >> updatemanager.py")
        os.system("echo with open('update.pyd', 'w') as u: >> updatemanager.py")
        os.system("echo     u.write(master) >> updatemanager.py")
        os.system("echo     u.close >> updatemanager.py")
        os.system("echo print('Updating...') >> updatemanager.py")
        os.system("echo time.sleep(2) >> updatemanager.py")
        os.system("echo os.remove('PyTunes.py') >> updatemanager.py")
        os.system("echo with open('update.pyd', 'r') as u: >> updatemanager.py")
        os.system("echo    with open('PyTunes.py', 'w', encoding='utf-8', newline='') as p: >> updatemanager.py")
        os.system("echo        p.write(master) >> updatemanager.py")
        os.system("echo        p.close() >> updatemanager.py")
        os.system("echo        u.close() >> updatemanager.py")
        os.system("echo        os.remove('update.pyd') >> updatemanager.py")
        os.system("echo print('Updated! Now restarting...') >> updatemanager.py")
        os.system("echo time.sleep(2) >> updatemanager.py")
        os.system("echo os.startfile('PyTunes.py') >> updatemanager.py")
        os.system("echo exit() >> updatemanager.py")
        os.startfile("updatemanager.py")
        exit()
def devoptions():
    isdevon = str("a")
    isdevoff = str("b")
    iserrorskipon = str("c")
    iserrorskipoff = str("d")
    isskippasson = str("e")
    isskippassoff = str("f")
    if os.path.exists("deverb.pyd"):
        isdevon = ("Enable")
        isdevoff = ("Disabled")
    else:
        isdevon = ("Disable")
        isdevoff = ("Enabled")
    if os.path.exists("iserrorskipon.pyd"):
        iserrorskipon = ("Disable")
        iserrorskipoff = ("Enabled")
    else:
        iserrorskipon = ("Enable")
        iserrorskipoff = ("Disabled")
    if os.path.exists("skippass.pyd"):
        isskippasson = ("Disable")
        isskippassoff = ("Enabled")
    else:
        isskippasson = ("Enable")
        isskippassoff = ("Disabled")
    os.system("cls")
    print("## DEVELOPER OPTION ##")
    print(programversion)
    print("")
    print("1} " + isdevon + " Auto Boot [Currently " + isdevoff + "]")
    print("2} " + iserrorskipon + " Skip Boot Error Check [Currently " + iserrorskipoff + "]")
    print("3} Simulate Errors")
    print("4} Restart")
    print("5} " + isskippasson + " Skip Password Check [Currently " + isskippassoff + "]")
    print("9} Return")
    devop = input("")
    if devop == ("1"):
        if os.path.exists("deverb.pyd"):
            os.system("attrib -s -h deverb.pyd")
            os.remove("deverb.pyd")
            devoptions()
        else:
            os.system("echo autobootoff >> deverb.pyd")
            os.system("attrib +s +h deverb.pyd")
            devoptions()
    if devop == ("2"):
        if os.path.exists("iserrorskipon.pyd"):
            os.system("attrib -s -h iserrorskipon.pyd")
            os.remove("iserrorskipon.pyd")
            devoptions()
        else:
            os.system("echo errorskip >> iserrorskipon.pyd")
            os.system("attrib +s +h iserrorskipon.pyd")
            devoptions()
    if devop == ("5"):
        if os.path.exists("skippass.pyd"):
            os.system("attrib -s -h skippass.pyd")
            os.remove("skippass.pyd")
            devoptions()
        else:
            os.system("echo skippass >> skippass.pyd")
            os.system("attrib +s +h skippass.pyd")
            devoptions()
    if devop == ("3"):
        errorsim()
    if devop == ("4"):
        print("Restarting...")
        os.system("pause")
        os.chdir('..')
        os.startfile("PyTunes.py")
        exit()
    if devop == ("9"):
        if os.path.exists ("C:\Python34\Lib\site-packages\pygame"):
            settingsli()
        else:
            pyfail()
    else:
        devoptions()
def errorsim():
    print("1} Simulate Error S2PDxE")
    print("2} Simulate Error S3DAxE")
    print("9} Exit")
    print("")
    errorin = input("")
    if errorin == ("1"):
        print("Please note! Account will be deleted by simulating this error.")
        paserr = input("Continue? [y/n]")
        if paserr == ("y"):
            os.system("echo tespass >> userps2.pyd")
            os.remove("username.pyd")
            #username is removed and account is deleted because
            #for some reason trying to just print the user's password into a fake duplicate file causes
            #the password file to be 2 lines, so the program reads both lines as the password so
            #entering the password is impossible. Working on a fix.
            print("Simulating...")
            time.sleep(2)
            f.close()
            os.chdir('..')
            os.startfile("PyTunes.py")
            exit()
        else:
            devoptions()
    if errorin == ("2"):
        print("Please note! Account will be deleted by simulating this error.")
        delerr = input("Continue? [y/n] ")
        if delerr == ("y"):
            os.remove("username.pyd")
            print("Simulating...")
            time.sleep(2)
            os.chdir('..')
            os.startfile("PyTunes.py")
            exit()
    if errorin == ("9"):
        devoptions()
    else:
        devoptions()
def delacc():
    rand = random.randint(1,1001)
    print("Please enter this number to prove you're not a robot: ", rand)
    robche = int(input(""))
    if (robche) == (rand):
        print("Deleting account...")
        time.sleep(2)
        os.remove("username.pyd")
        os.remove("userdob.pyd")
        os.remove("userps.pyd")
        os.remove("userfva.pyd")
        os.remove("userfvg.pyd")
        print("Restarting...")
        time.sleep(2)
        os.chdir('..')
        os.startfile("PyTunes.py")
        exit()
    else:
        print("Abort.")
        pygame.mixer.music.load("err.ogg")
        pygame.mixer.music.play()
        os.system("pause >nul")
        settingsli()
def userinfo():
    os.system("cls")
    print("######################")
    print("")
    with open("username.pyd", 'r') as f:
        for lineusn in f:
            if ("dev") == (lineusn):
                print("You are a developer. Access developer options by entering 27 in settings.")
            else:
                print("Username: " + lineusn)
    with open("userdob.pyd", 'r') as f:
        for linedb in f:
            print("Date Of Birth: " + linedb)
    with open("userps.pyd", 'r') as f:
        for lineps in f:
            print("Password: " + lineps)
    with open("userfva.pyd", 'r') as f:
        for linefva in f:
            print("Favourite Artist: " + linefva)
    with open("userfvg.pyd", 'r') as f:
        for linefvg in f:
            print("Favourite Genre: " + linefvg)
    print("")
    os.system("  pause>nul|set/p =Press anything to return to settings...")
    settingsli()
def pswdch():
    pswrdcha = getpass.getpass("Enter your account password... ")
    with open("userps.pyd", 'r') as f:
        for lineps in f:
            if (pswrdcha) == (lineps):
                f.close()
                os.system("attrib -s -h userps.pyd")
                pwrdch()
            else:
                print("Incorrect Password!")
                pygame.mixer.music.load("err.ogg")
                pygame.mixer.music.play()
                os.system("pause >nul")
                settingsli()
def pwrdch():
    pswdch = getpass.getpass("Enter new password...")
    pswdchv = getpass.getpass("Verify new password...")
    if pswdch == pswdchv:
        with open("userps2.pyd", 'w') as i:
            i.write(pswdch)
            i.close()
            pwrewr()
    else:
        print("Passwords do not match!")
        os.system("pause >nul")
        settingsli()
def pwrewr():
    with open("userps2.pyd", 'r') as p:
        for lineps in p:
            os.remove("userps.pyd")
            with open("userps.pyd", 'w') as a:
                a.write(lineps)
                os.system("attrib +s +h userps.pyd")
                p.close()
                a.close()
                os.remove("userps2.pyd")
                print("Password Changed Successfully!")
                time.sleep(2)
                settingsli()
#######################  S E T T I N G S  #######################

####################################################################
                
#######################  P Y G A M E  F A I L  ######################
def pyfail():
    helpstart = str("Type 'end' to close program, or 'cmd' to enter a standard terminal.")
    pyfaildir = os.getcwd()
    print(helpstart)
    devinpy = input("PyTunes Dev Console> ")
    if devinpy == ("help"):
        print(helpstart)
        pyfail()
    elif devinpy == ("end"):
        exit()
    elif devinpy == ("cmd"):
        pyfailcm()
    elif devinpy == ("rundev"):
        print("Emulating dev options...")
        time.sleep(1)
        devoptions()
    elif devinpy == ("start"):
        print("Launching...")
        time.sleep(1)
        global todaysongs
        todaysongs = []
        global currentlyplaying
        currentlyplaying = ("Nothing")
        if os.path.exists("Songs"):
            os.chdir("Songs")
        menu2c()
    elif devinpy == ("install"):
        print("Attempting to install PyGame...")
        os.system("pip install pygame")
        pyfail() 
    elif devinpy == ("starte"):
        print("Launching into error check...")
        time.sleep(1)
        usercheck()
    else:
        try:
            print("Navigating...")
            (devinpy)()
        except:
            print("'" + devinpy + "' is not recognized as a PyTunes commnad, use 'cmd' to enter normal terminal")
            pyfail()
def pyfailcm():
    pyfaildir = os.getcwd()
    pyfailcm = input(pyfaildir + ">")
    print("")
    os.system(pyfailcm)
    pyfailcm()
#######################  P Y G A M E  F A I L  ######################

######################################################################
    
#######################  P R E  B O O T  P R E P #######################
def preboot():
    getdirtemp = os.getcwd()
    if getdirtemp == ("C:\WINDOWS\System32"):
        print("Error")
        os.system("pause")
        exit()
    if os.path.exists("Songs"):
        global pygame
        import pygame
        pygame.mixer.init()
        if os.path.exists("StartSnd.ogg"):
            pygame.mixer.music.load("StartSnd.ogg")
            pygame.mixer.music.play()
        os.chdir("Songs")
        if not os.path.exists("err.ogg"):
            os.chdir('..')
            if os.path.exists("err.ogg"):
                shutil.copy2('err.ogg', 'Songs')
            os.chdir("Songs")
        dr = os.getcwd()
        print(programversion)
        print("Current Dir... " + dr + " [THIS SHOULD BE THE DIRECTORY YOUR SONGS ARE IN]")
        if os.path.exists("iserrorskipon.pyd"):
            print("[OK] Error skip enabled")
            time.sleep(0.2)
            if os.path.exists("userps2.pyd"):
                print("[FAIL] Error!")
                if os.path.exists("err.ogg"):
                    pygame.mixer.music.load("err.ogg")
                    pygame.mixer.music.play()
                time.sleep(0.5)
                print("[FAIL] Collecting Data...")
                time.sleep(1)
                os.system("cls")
                os.remove("userps.pyd")
                with open("userps2.pyd", 'r') as p:
                    for lineusn in p:
                        with open("userps.pyd", 'w') as r: 
                            r.write(lineusn)
                            r.close()
                            p.close()
                            os.remove("userps2.pyd")
                            print("0_0")
                            print("")
                            print("PyTunes ran into a problem and had to restart.")
                            print("If you contact the developer, please quote error code S2PDxE")
                            print("Your password has been changed to the one you entered.")
                            print("Please press any key to restart.")
                            os.system("pause >nul")
                            os.chdir('..')
                            os.startfile("PyTunes.py")
                            exit()
            else:
                menu2()
        else:
            print("[OK] Error skip disabled")
            usercheck()
    else:
        try:
            import pygame
        except ImportError:
            print("Hi user!")
            print("We have detected you don't have pygame installed on your system.")
            print("Pygame is crucial for this program to function as intended.")
            print("You can continue to use PyTunes without it, however, many key functions WILL cause the program to crash.")
            print("")
            print("If you want to close PyTunes and install Pygame, press '1' followed by 'Enter'.")
            print("")
            print("If you belive this is an error, or would like to use the program anyway, press '2' followed by 'Enter'.")
            print("")
            print("If you want details on why PyTunes needs Pygame and how to install Pygame, press '3' followed by 'Enter'.")
            mench = input("")
            if mench == ("1"):
                exit()
            if mench == ("2"):
                print("Booting...")
                time.sleep(2)
                if os.path.exists("iserrorskipon.pyd"):
                    os.remove("iserrorskipon.pyd")
                if not os.path.exists("deverb.pyd"):
                    os.system("echo autobootoff >> deverb.pyd")
                if os.path.exists("Songs"):
                    os.chdir("Songs")
                    usercheck()
                usercheck()
            if mench == ("3"):
                print("")
                print("This program requires Pygame to play songs using the pygame.mixer.music function from pygame, ")
                print("And also to change volume and things using pygame.mixer.music.set_volume, things like that.")
                print("Logging out crashes the program as there is a pygame.mixer.music.stop() function embedded in the logout code, ")
                print("meaning the program will creash when a user tries to execute it. ")
                print("'progressbar' is also needed while the program is booting to relay the status of song loading")
                print("")
                os.system("pause")
                print("")
                print("You can install the modules using 'pip' which comes with python. To use 'pip', navigate to C:\Python34\Tools\Scripts ")
                print("and find a .py program called 'win_add2path.py'. It is usually at the bottom of the list. ")
                print("After executing, open an administrator command prompt window and type 'python3' to test if the script works.")
                print("If the output is 'Python 3.4.3' followed by some version numbers, it has worked.")
                print("Type 'exit()' to return to a normal command line, then type 'pip install pygame' and wait a while.")
                print("The window may seem unresponsive for a time.")
                print("After that has finished, type 'pip install progressbar' and wait until that finishes.")
                print("After that, the program should work as intended. If the pip installs fail, look online for other methods.")
                print("")
                os.system("pause")
                print("The program will now restart.")
                os.system("pause")
                os.startfile("PyTunes.py")
                exit()
            if mench == ("4"):
                pyfail()
            if mench == (""):
                print("Exiting...")
                time.sleep(2)
                exit()
##      ##      ##
##      ##      ##
        isquick = os.getcwd()
        if isquick == ("C:\WINDOWS\System32"):
            print("Hi user! Please don't run this program from Quick Access.")
            print("Place it in it's own folder to run correctly.")
            print("Type [y] to continue anyway (crash is very likely), or [n] to shutdown.")
            isquickin = input("")
            if isquickin == ("n"):
                exit()
            else:
                pygame.mixer.init()
                if os.path.exists("StartSnd.ogg"):
                    pygame.mixer.music.load("StartSnd.ogg")
                    pygame.mixer.music.play()
                os.mkdir("Songs")
                print("Directory Created")
                print("Performing first time setup...")
                if os.path.exists("err.ogg"):
                    shutil.copy2('err.ogg', 'Songs')
                os.chdir("Songs")
                dr = os.getcwd()
                print("Current Dir... " + dr + " [THIS SHOULD BE THE DIRECTORY YOUR SONGS ARE IN]")
                usercheck()
        else:
            pygame.mixer.init()
            if os.path.exists("StartSnd.ogg"):
                pygame.mixer.music.load("StartSnd.ogg")
                pygame.mixer.music.play()
            os.mkdir("Songs")
            print("Directory Created")
            print("Performing first time setup...")
            if os.path.exists("err.ogg"):
                shutil.copy2('err.ogg', 'Songs')
            os.chdir("Songs")
            dr = os.getcwd()
            print("Current Dir... " + dr + " [THIS SHOULD BE THE DIRECTORY YOUR SONGS ARE IN]")
            usercheck()
#######################  P R E  B O O T  P R E P #######################

########################################################################
preboot()
os.system("pause >nul") # :)
