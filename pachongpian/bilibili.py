import requests
import bs4

def open_url(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    res=requests.get(url, headers=headers)
    return res

def find_message(res):
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    titles=soup.find_all('div',class_='bili-video-card__info')
    for each in titles:
        print(each.h3['title'])

def main():
    host='https://search.bilibili.com/all?vt=62898395&keyword=%E7%BC%96%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007&search_source=5'
    res=open_url(host)
    find_message(res)

if __name__ == '__main__':
    main()