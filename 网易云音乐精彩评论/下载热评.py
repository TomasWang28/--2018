import requests
import json

def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open("hot_comments.txt","w",encoding="utf-8")as file:
        for each in hot_comments:
            file.write(each['user']['nickname']+"：\n\n")
            file.write(each['content']+'\n')
            file.write("---------------------------------------------------\n")

def get_comments(url):
    # 给它传个 referer 以免服务器疑神疑鬼的@_@
    # 当然，你这有时间的话将headers头部填写完整，那样妥妥会更好一些……
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
        'referer': 'http://music.163.com/song?id=418603077'
        }

    params = "5iCPzP/xsmpQBjA9zZrP81vFjYyqf69+6O+/MQPpNJUIG9aVZLAGWZ6QberDvEsDP+tc6QBkr3SId2M02zk3nHiAxpQueSfgQbyDd00J4HJfhGZ7Xshij9iZiI57k9BKJCBoyXMAMS9sHVCnpC74G0iCjzOLYaNhcQpXzoZjKPvVtfCkPcIUNe2pUQ9NcnP7"
    encSecKey = "d983b4c22666b3b29c0cc7913794a50f0654c71609c3d36d5893381897d627ed417702c2f5910d213709a88ce550149f51b80707b52efb9561a8545b9f783b68fdcafd654f35d4c4822a79e4b4defa3f00b63249debb57689291cc7043cfc406fb3ae2dd95327108903f25d0956c514e2571592953e7968d0a796d4365a2c641"
    data = {
        "params":params,
        "encSecKey":encSecKey
    }

    name_id = url.split('=')[1]
    target_url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s?csrf_token=/" % name_id

    res = requests.post(target_url,headers=headers,data=data)

    return res

def main():
    url = input("请输入链接地址：")
    res = get_comments(url)
    get_hot_comments(res)

if __name__=="__main__":
    main()
