def DownloadResource(url: str, pathname='./tmp.mp3', display=False):
    """
    :param url: resource url
    :param pathname: you path name with flie name
    :param display: show percent
    :return: void
    """
    from urllib.request import urlretrieve
    import os
    if os.path.exists(pathname):
        ret = pathname.split('/')
        answer = input(ret[-1] + " had already existed\n 'y' to replace it 'n' to cancel ")
        if answer == 'y' or answer == 'Y':
            if display:
                urlretrieve(url, pathname, cbk)
            else:
                urlretrieve(url, pathname)
        else:
            print("the task has been cancelled\n")
    else:
        if display:
            urlretrieve(url, pathname, cbk)
        else:
            urlretrieve(url, pathname)


def cbk(a, b, c):
    '''''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)
