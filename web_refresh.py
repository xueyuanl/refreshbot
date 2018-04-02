import webbrowser as web
import time
import threading

def refresh(url, number):
    print 'begin refresh %s' % url
    i = 0
    while i < number:
        try:
            web.open(url)
        except:
            print 'Failed!!!------ %s' % url
        else:
            i = i + 1
            time.sleep(1)
    print 'finish refreshing the url %s as %s times' % (url, i)

class Task(threading.Thread):
    def __init__(self, functor, param):
        super(Task, self).__init__()
        self.functor = functor
        self.param = param

    def run(self):
        try:
            self.functor(*self.param)
        except Exception as error:
            print error


def main():

    params = [
            ("http://www.jjl.cn/article/16160.html",10),
            ("http://www.jjl.cn/article/16154.html",10)
    ]

    for param in params:
        #param is the parameters of the function refresh
        task = Task(refresh, param)
        task.start()

    # for param in params:
    #     t = threading.Thread(target=refresh,args=param)
    #     t.start()

if __name__=="__main__":
    main()