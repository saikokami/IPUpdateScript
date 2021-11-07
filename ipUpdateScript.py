import requests # for receive the ip
import configparser # ini file handling
import ftplib # ftp handler

ip4 = requests.get('https://checkip.amazonaws.com').text.strip()
ip6 = requests.get('http://bennedikt.eu/download/test.php').text.strip() # Currently not avaible
cfg = configparser.ConfigParser()
cfg.read('C:/Users/benne/Documents/scripts/pyscripts/Website/config.ini')
cfg['be']['be_4'] = ip4
cfg['be']['be_6'] = ip6
with open('C:/Users/benne/Documents/scripts/pyscripts/Website/config.ini', 'w') as configfile:    # save
    cfg.write(configfile)

session = ftplib.FTP('********', '********', '********')
file = open('C:/Users/benne/Documents/scripts/pyscripts/Website/config.ini','rb') 
session.storbinary('STOR /html/download/secured/config.ini', file)
file.close()                                    
session.quit()
print('Upload Done')
