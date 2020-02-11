from bs4 import BeautifulSoup
from DownLoad import DownloadResource
from selenium import webdriver
import time

url = 'http://www.jdlg.net/jingdianlaoge500shou/A563.html'
browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get(url)
time.sleep(5)
page = BeautifulSoup(browser.page_source, 'html5lib')
tag = page.find(name='audi', attrs={'src': True})
if not tag:
    print('No result')
else:
    print('Find result :\n')
    print(tag)
    print('\n')
    music_url = tag['src']
    print(music_url)
    answer = input("Are you sure to download?\n 'y' to download or press any other keys to cancel\n")
    if answer == 'Y' or answer == 'y':
        DownloadResource(music_url, './name.mp3')
    else:
        print('the task has been cancelled\n')
