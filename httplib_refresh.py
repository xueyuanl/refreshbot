import httplib

httpClient = None

headers = {
           'Content-type': 'application/json',
           'Cookie': None,
           'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
           }

httpClient = httplib.HTTPConnection('www.jjl.cn', 80, timeout=30)

httpClient.request('GET', '/article/16040.html',headers=headers)

response = httpClient.getresponse()

print response.status

print response.getheaders()

