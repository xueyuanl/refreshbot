import urllib2
import time
import user_agent

def main():

    url = "http://xueyuanl.github.io/2017/12/05/BBC-%E7%BA%AA%E5%BD%95%E7%89%87%EF%BC%9ABule-Planet-II/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1',
    }

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    for i in range(0,2):
        req=urllib2.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53")
        file = urllib2.urlopen(req)
        print 'number' + str(i)
        print file.read()
        time.sleep(1)

if __name__=="__main__":
    main()