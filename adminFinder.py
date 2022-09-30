import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", help="target url", dest='target')

args = parser.parse_args()

target = args.target

print("""
      
    '##::::::::'##:::'##:'####:::::::'###::::'########::'##::::'##:'##:::'##:
    ##:::'##:: ##::'##::. ##:::::::'## ##::: ##.... ##: ###::'###:. ##:'##::
    ##::: ##:: ##:'##:::: ##::::::'##:. ##:: ##:::: ##: ####'####::. ####:::
    ##::: ##:: #####::::: ##:::::'##:::. ##: ########:: ## ### ##:::. ##::::
    #########: ##. ##:::: ##::::: #########: ##.. ##::: ##. #: ##:::: ##::::
    ...... ##:: ##:. ##::: ##::::: ##.... ##: ##::. ##:: ##:.:: ##:::: ##::::
    :::::: ##:: ##::. ##:'####:::: ##:::: ##: ##:::. ##: ##:::: ##:::: ##::::
    ::::::..:::..::::..::....:::::..:::::..::..:::::..::..:::::..:::::..::::: 
    
    -------------------------------------------------------------------------
    
    
                ____ ___ ____  _____ ___ ____  _____ 
                |  _ \_ _|  _ \|  ___|_ _|  _ \| ____|
                | | | | || |_) | |_   | || |_) |  _|
                | |_| | ||  _ <|  _|  | ||  _ <| |___
                |____/___|_| \_\_|   |___|_| \_\_____|
    
    """)

try:
    target = target.replace('https://', '')
except:
    print ('\033[1;31m[-]\033[1;m python adminFinder.py -u Target')
    quit()

target = target.replace('http://', '')
target = target.replace('/', '')
target = 'http://' + target 

def scan(links):
    for link in links:
        link = target + link 
        r = requests.get(link)
        http = r.status_code
        if http == 200:
            print ('  \033[1;32m[+]\033[0m Admin panel found: %s'% link)
            f = open("log.txt", "a")
            f.write(link + "\n")
            f.close()
        elif http == 404: 
            print ('  \033[1;31m[-]\033[1;m %s'% link)
        elif http == 302:
            print ('  \033[1;32m[+]\033[0m Try Again : ' + link)
        else:
            print ('  \033[1;31m[-]\033[1;m %s'% link)
    
                     
paths = []

def get_paths():
    try:
        with open('admin.txt','r') as wordlist:
            for path in wordlist:
                path = str(path.replace("\n",""))
                paths.append(path)
    except IOError:
        print ('\033[1;31m[-]\033[1;m Wordlist not found!')
        quit()

get_paths()
links = paths
scan(links)
