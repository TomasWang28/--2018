import requests
import json

def open_url(url):
    headers ={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"}
    res = requests.get(url,headers=headers)

    return res

def main():
    url = input("请输入网址：")
    res = open_url(url)

    with open("res.txt","w",encoding="utf-8",errors="ignore")as file:
        file.write(res.text)

if __name__ == "__main__":
    main()
