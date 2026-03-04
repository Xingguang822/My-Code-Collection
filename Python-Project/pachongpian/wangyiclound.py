import requests
import json


def get_hot_comments(res):
    try:
        comments_json = json.loads(res.text)

        # 检查API返回的错误代码
        if 'code' in comments_json and comments_json['code'] != 200:
            print(f"API返回错误: {comments_json.get('message', '未知错误')}")
            return

        # 获取数据部分 - 这是关键修改
        data = comments_json.get('data', {})

        # 使用get方法安全访问键
        hot_comments = data.get('hotComments', [])

        # 如果没有热门评论，尝试获取普通评论
        if not hot_comments:
            print("未找到热门评论")
            # 尝试获取普通评论作为备选
            comments = data.get('comments', [])
            if comments:
                print(f"找到 {len(comments)} 条普通评论")
                # 取点赞数最高的10条评论作为"热门"评论
                comments_sorted = sorted(comments, key=lambda x: x.get('likedCount', 0), reverse=True)
                hot_comments = comments_sorted[:10]
            else:
                print("没有任何评论")
                return

        with open('hot_comments.txt', 'w', encoding='utf-8') as f:
            for comment in hot_comments:
                user_info = comment.get('user', {})
                nickname = user_info.get('nickname', '匿名用户')
                content = comment.get('content', '无评论内容')
                liked_count = comment.get('likedCount', 0)  # 获取点赞数

                f.write(f"{nickname} (👍 {liked_count}):\n\n")
                f.write(f"{content}\n")
                f.write('--------------------------------\n')

        print(f"成功保存 {len(hot_comments)} 条评论")

    except Exception as e:
        print(f"处理评论时出错: {str(e)}")
        # 保存原始响应用于调试
        with open('error_response.txt', 'w', encoding='utf-8') as f:
            f.write(res.text)


def get_comments(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        "referer": 'https://music.163.com/song?id=2711834126',
        "origin": "https://music.163.com",
        "content-type": "application/x-www-form-urlencoded"
    }

    params='4cS5M81NbKEDxmHrrO7QXIF+X5xV0bgWXzOpzAVRsAqEGmDTwXTzU1PUo+xw/aiY/bk746cPUpC9AozdMSGuss5cGvjfNu8q8lYAQ3zbHWx3d/5ekHw04+AhR4DXyPdSsSlQ5i8fa/H9T5HNAdhYuKoDJEsPhWrFPQ0Of1rKXbXAQCAhFfyyfVLfFCvV+YRncg1h1gV9oWYXF5CPve75chxtNttr4gpD0o8ll6mbKln16vQ/+gHdQn0aLXSr/jIS8TOe6OEkXU8miSsOistM1zWIzFEFZc6jw5Ae/574BjQpr6moGdH76YMuQ/HlsIkQ3HonKZ1ZWFEJcgnDvjqkAWtMy0jUV4D9rTLGWpbt05g='
    encSecKey= '8fbc2f6dcaf779625e98e001c276d0a01b409234c37a813e2e4c9afcaf39eeb98f88f475932c70feda3c28989062e3894023c22707ca5c5fe3ca176a676d6d667be70f5265d8cb1573454349097c40ab1e595f56b848527eb5fc024db229c807418d498c6bef6845094eb802edfdac84d204b25c683a9c709d136627bd5f2d35'
    post_data = {
        'params': params,
        'encSecKey': encSecKey
    }

    target_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

    res = requests.post(target_url, headers=headers, data=post_data)

    # 保存原始响应内容用于调试
    with open('api_response.json', 'w', encoding='utf-8') as f:
        f.write(res.text)

    if res.status_code != 200:
        print(f"请求失败，状态码: {res.status_code}")
        # 保存错误响应用于调试
        with open('error_response.html', 'w', encoding='utf-8') as f:
            f.write(res.text)

    return res


def main():
    url = 'https://music.163.com/#/song?id=2711834126'
    print("开始获取评论...")
    res = get_comments(url)
    if res and res.status_code == 200:
        try:
            # 尝试解析JSON以验证响应格式
            data = res.json()
            if 'code' in data and data['code'] != 200:
                print(f"API返回错误: {data.get('message', '未知错误')}")
            else:
                print("成功获取评论数据")
                get_hot_comments(res)
        except json.JSONDecodeError:
            print("响应不是有效的JSON格式")
            with open('invalid_response.txt', 'w', encoding='utf-8') as f:
                f.write(res.text)
    else:
        print("未能成功获取评论数据")


if __name__ == '__main__':
    main()