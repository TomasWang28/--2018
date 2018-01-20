import urllib.request
import re
from bs4 import BeautifulSoup


def main():
    url = "http://baike.baidu.com/view/284853.htm"
    response = urllib.request.urlopen(url)
    html = response.read()
    #使用解析器
    soup = BeautifulSoup(html,"html.parser")

    with open("Save File.txt",'w',encoding="utf-8")as f:
        if f:
            pass
        else:
            f.write(soup.prettify())

    for each in soup.find_all(href=re.compile("item")):
        print(each.text,'->',''.join(["http://baike.baidu.com",each["href"]]))
    

if __name__ == '__main__':
    main()
