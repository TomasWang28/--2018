import urllib.request
import random
url = 'http://www.whatismyip.com.tw//'

iplist = ['61.155.164.106:3128','112.250.65.222:53281','113.68.189.221:9999']

proxy_support = urllib.request.ProxyHandler({'https':random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
