import requests
import time
from torrequest import TorRequest

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
}

url = "http://www.jjl.cn/article/16040.html"
times = 100


def run():
    response = tr.get(site, headers=headers,verify=False)
    #     time.sleep(10)
    #     print(response.text)
    print "["+str(i)+"]" + " Blog View Added With IP:" +  tr.get('http://ipecho.net/plain').content
    tr.reset_identity()



if __name__ == '__main__':
    with TorRequest() as tr:
        for i in range(blog):
            run()


