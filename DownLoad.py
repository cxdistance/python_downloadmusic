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
        answer = input(ret[-1] + " had already existed\n 'y' to replace it or 'n' to cancel\n ")
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
    """call back
    :param a: number of data blocks which have downloaded
    :param b:the size of a block
    :param c:total size
    """
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)
