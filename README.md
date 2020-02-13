# python_downloadmusic
python爬虫下载音乐 selenium+beautifulsoup
测试平台酷狗音乐

本程序在 `python3` 下运行 

### 需要环境: 
`python3` &nbsp; `selenium` &nbsp; `beautifulsoup4`

### todu:
编写使用说明

*  ### 一、配置`conf.json` :

<img src="./guide/pic1.png">

1. `executable_path` 参数 :浏览器驱动的路径
> 注: 若未安装浏览器驱动，请自行下载，示例程序使用 `chrome` 浏览器且仅支持 `chrome` ，版本`80.0.3987.100` ,请根据自己的浏览器版本自行下载 。下载地址 https://sites.google.com/a/chromium.org/chromedriver/home

2. `url` : 目标网址

3. `download_path` : 下载到本地的路径和名字（目录必须存在）

4. `display` : 若为 `true` 则会显示下载进度，若为 `false` 则不显示下载进度

* ### 二、 运行：
在当前目录下运行 `run.py` 即可