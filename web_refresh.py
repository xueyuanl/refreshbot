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

class Task(threading.Thread):
    def __init__(self, functor, param):
        super(Task, self).__init__()
        self.functor = functor
        self.param = param

    def run(self):
        try:
            self.functor(*self.param)
        except Exception as error:
            #traceback.print_exc()
            print error

for param in iter(params):
    thrd = self.Task(self.desc, self.functor, param)
    thrd.start()

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

    params = [
            ("http://www.jjl.cn/article/16160.html",10000),

    ]

    for param in params:
        task = Task(refresh, param)
        task.start()

    for url in urls:
        t = threading.Thread(target=refresh,args=(url,10000))
        t.start()

if __name__=="__main__":
    main()