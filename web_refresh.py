import webbrowser as web
import time
import threading

lock = threading.RLock()

def refresh(url, number):
    global lock

    print 'begin refresh %s' % url
    i = 0
    while i < number:
        try:
            web.open_new_tab(url)
        except:
            print 'Failed!!!------ %s' % url
        else:
            time.sleep(5)
            lock.acquire()
            i = i + 1
            lock.release()
    print 'finish the url %s' % url


def main():

    urls = [
            "http://www.jjl.cn/article/16160.html",
            "http://www.jjl.cn/article/16154.html",
            "http://www.jjl.cn/article/16147.html",
            "http://www.jjl.cn/article/16142.html",
            "http://www.jjl.cn/article/16129.html",
            "http://www.jjl.cn/article/16115.html",
            "http://www.jjl.cn/article/16040.html",
            "http://www.jjl.cn/article/15924.html",
            "http://www.jjl.cn/article/10368.html",
            "http://www.jjl.cn/article/10350.html",
            "http://www.jjl.cn/article/4496.html",
            "http://www.jjl.cn/article/4409.html",
            "http://www.jjl.cn/article/4247.html",
            "http://www.jjl.cn/article/3781.html"
            ]

    for url in urls:
        t = threading.Thread(target=refresh,args=(url,10000))
        t.start()

if __name__=="__main__":
    main()