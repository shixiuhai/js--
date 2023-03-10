import requests

cookies = {
    'mk': '339201ea4efa4d25ac12010539b1ce4a',
    'uk': '2080306434',
    'xlly_s': '1',
    'anchor-task-tips': 'vistived',
    'fansTuan-tips': 'vistived',
    'cna': 'NKWNHIfYgzcCAW8CWyb3taec',
    '_m_h5_tk': 'e6099cf2a63171c02027e25d21f6fb34_1678415547138',
    '_m_h5_tk_enc': '8752b6179c76b95f7ecc5f9c66550974',
    'isg': 'BAEBfOidAVqCUWqxMHWHoLANEE0bLnUg09pUkWNW_YhnSiEcq36F8C9YKr4M2Q1Y',
    '__ysuid': '1678413341369tef',
    'imk': 'MjA4MDMwNjQzNC0wLTE2Nzg0MTMzNDU0MTgtMTY3ODQ5OTc0NTQxOA%3D%3D-8BE01DF063243D7A646B6FAA0ADF2197',
}

headers = {
    'authority': 'acs.laifeng.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mk=339201ea4efa4d25ac12010539b1ce4a; uk=2080306434; xlly_s=1; anchor-task-tips=vistived; fansTuan-tips=vistived; cna=NKWNHIfYgzcCAW8CWyb3taec; _m_h5_tk=e6099cf2a63171c02027e25d21f6fb34_1678415547138; _m_h5_tk_enc=8752b6179c76b95f7ecc5f9c66550974; isg=BAEBfOidAVqCUWqxMHWHoLANEE0bLnUg09pUkWNW_YhnSiEcq36F8C9YKr4M2Q1Y; __ysuid=1678413341369tef; imk=MjA4MDMwNjQzNC0wLTE2Nzg0MTMzNDU0MTgtMTY3ODQ5OTc0NTQxOA%3D%3D-8BE01DF063243D7A646B6FAA0ADF2197',
    'origin': 'https://v.laifeng.com',
    'referer': 'https://v.laifeng.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

params = {
    'jsv': '2.6.1',
    'appKey': '24679788',
    't': '1678413347504',
    'sign': 'd7cf3d66c7172e00051acaf43e361b23',
    'type': 'originaljson',
    'dataType': 'json',
    'api': 'mtop.youku.laifeng.live.center.liveplaycontrol',
    'v': '1.0',
    'data': '{"liveId":"8122883","ccode":"live05010101laifeng","app":"Pc"}',
}

response = requests.get(
    'https://acs.laifeng.com/h5/mtop.youku.laifeng.live.center.liveplaycontrol/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)