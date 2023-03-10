# import requests
# # https://www.52pojie.cn/thread-1479898-1-1.html 优酷逆向
# cookies = {
#     'mk': 'faed16388a0e4075a28afe3ade5d7f77',
#     'uk': '2088554432',
#     'cna': 'FW1KHIn+0SECASe8CfjwqTwx',
#     'xlly_s': '1',
#     'anchor-task-tips': 'vistived',
#     'fansTuan-tips': 'vistived',
#     '_m_h5_tk': 'b1097315d7c535cc065d380438743a0a_1678374643479',
#     '_m_h5_tk_enc': '3ba733421c9672893d9205b80dec092d',
#     '__ysuid': '1678369766166SVk',
#     'imk': 'MjA4ODU1NDQzMi0wLTE2NzgzNjk5MTkxNzItMTY3ODQ1NjMxOTE3Mg%3D%3D-0926E042F083BFFF8A0DD3DEDA6876F1',
#     'isg': 'BMnJJxofyXFzwbUFGgr1a9rA2PUjFr1Ia3KseWs--7DvsurEs2YdGMuj9BYE6lWA',
# }

# headers = {
#     'authority': 'acs.laifeng.com',
#     'accept': 'application/json',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'content-type': 'application/x-www-form-urlencoded',
#     # 'cookie': 'mk=faed16388a0e4075a28afe3ade5d7f77; uk=2088554432; cna=FW1KHIn+0SECASe8CfjwqTwx; xlly_s=1; anchor-task-tips=vistived; fansTuan-tips=vistived; _m_h5_tk=b1097315d7c535cc065d380438743a0a_1678374643479; _m_h5_tk_enc=3ba733421c9672893d9205b80dec092d; __ysuid=1678369766166SVk; imk=MjA4ODU1NDQzMi0wLTE2NzgzNjk5MTkxNzItMTY3ODQ1NjMxOTE3Mg%3D%3D-0926E042F083BFFF8A0DD3DEDA6876F1; isg=BMnJJxofyXFzwbUFGgr1a9rA2PUjFr1Ia3KseWs--7DvsurEs2YdGMuj9BYE6lWA',
#     'origin': 'https://v.laifeng.com',
#     'referer': 'https://v.laifeng.com/',
#     'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
# }

# params = {
#     'jsv': '2.6.1',
#     'appKey': '24679788',
#     't': '1678370419726',
#     'sign': 'e47b854e7bfa5bbb8a615ee2e6beb218',
#     'api': 'mtop.youku.laifeng.rec.pc.attention.get',
#     'dataType': 'json',
#     'v': '1.0',
#     'preventFallback': 'true',
#     'type': 'originaljson',
#     'data': '{"version":0}',
# }
# def abc():
#     print("hell word")

# response = requests.get(
#     'https://acs.laifeng.com/h5/mtop.youku.laifeng.rec.pc.attention.get/1.0/',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )

# print(response.json())
from requests_html import HTMLSession
from fake_useragent import UserAgent
import requests
session=requests.Session()
def scrape_prices():
    ua = UserAgent().chrome  #随机获取请求头
    print(ua)
    headers = {'User-Agent':ua}
    session = HTMLSession()
    url="https://v.laifeng.com"
    r = session.get(url,headers=headers)
    r.html.html
    print(r.cookies.get_dict())
scrape_prices()
# def get_Cookies0():
#     ua = UserAgent().ie  #随机获取请求头
#     headers = {'User-Agent':ua}
#     url = 'https://v.laifeng.com/'
#     session = requests.session()
#     session.get(url,headers = headers)
#     session.get(url="https://v.laifeng.com/622?spm=a2h55.8996835.0.0#/")
#     cookie = session.cookies
#     a = cookie.get_dict()
#     print(a)
# get_Cookies0()

# from requests_html import HTMLSession
# def scrape_prices():
#     session = HTMLSession()
#     url = 'https://opensea.io/collection/wonderpals? 
#         search[sortBy]=PRICE&search[sortAscending]=true&search[toggles]. 
#         [0]=BUY_NOW'
#     r = session.get(url)
#     r.html.render(sleep=1, keep_page=True, scrolldown=100)
#     substring = "<div class=" + '"' + "AssetCardFooter--name" + '"'
#     item_numbers = r.html.find(substring)