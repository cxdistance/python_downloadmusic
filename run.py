from bs4 import BeautifulSoup
from DownLoad import DownloadResource
from selenium import webdriver
import time
import json


def CheckConf() -> dict:
    """
    :return ret: the json dict
    """
    print('checking "config.json"')
    flag = True
    conf = json.load(open('./conf.json', 'r', encoding='utf-8'))
    if not conf['executable_path']:
        print('undefined "executable_path",please check the "conf.json"')
        flag = False
    if not conf['url']:
        print('undefined "url",please check the "conf.json"')
        flag = False
    if not conf['download_path']:
        print('undefined "path",please check the "conf.json"')
        flag = False
    if conf['display'] == '':
        print('undefined "display",please check the "conf.json"')
        flag = False
    if flag:
        print('complete')
        return conf
    else:
        return {}


def RunProgram():
    ret = CheckConf()
    if not ret:
        return
    url = ret['url']
    browser = webdriver.Chrome(executable_path=ret['executable_path'])
    print('start searching')
    browser.get(url)
    time.sleep(5)
    page = BeautifulSoup(browser.page_source, 'html5lib')
    tag = page.find(name='audio', attrs={'src': True})
    browser.close()
    if not tag:
        print('No result')
    else:
        print('Find result :')
        print(tag)
        music_url = tag['src']
        print(music_url)
        answer = input(
            "Are you sure to download?\n 'y' to download or press any other keys to cancel\n ")
        if answer == 'Y' or answer == 'y':
            if ret['display']:
                DownloadResource(music_url, ret['download_path'], display=True)
            else:
                DownloadResource(music_url, ret['download_path'])
            print('complete')
        else:
            print('the task has been cancelled')


RunProgram()
