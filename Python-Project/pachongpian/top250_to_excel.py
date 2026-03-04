import requests
import bs4
import openpyxl

def open_url(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    res=requests.get(url, headers=headers)
    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    movies = []
    targets=soup.find_all('div',class_='hd')
    for target in targets:
        movies.append(target.a.span.text)

    ranks=[]
    targets=soup.find_all('span',class_='rating_num')
    for target in targets:
        ranks.append(target.text)

    messages=[]
    targets=soup.find_all('div',class_='bd')
    for target in targets:
        try:
            messages.append(target.p.text.split('\n')[1].strip()+target.p.text.split('\n')[2].strip())
        except:
            continue

    result=[]
    length= min(len(movies), len(ranks), len(messages))
    for i in range(length):
        result.append([movies[i],ranks[i],messages[i]])

    return result

def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth=soup.find('span',class_='next').previous_sibling.previous_sibling.text
    return int(depth)

def save_to_excel(result):
    wb=openpyxl.Workbook()
    ws=wb.active
    ws.append(['电影名称','评分','资料'])
    for each in result:
        ws.append(each)

    wb.save("doubantop250.xlsx")


def main():
    host='https://movie.douban.com/top250'
    res=open_url(host)
    depth=find_depth(res)

    result=[]
    for i in range(depth):
        url=host+'?start='+str(25*i)
        res=open_url(url)
        result.extend(find_movies(res))

    save_to_excel(result)


if __name__ == '__main__':
    main()