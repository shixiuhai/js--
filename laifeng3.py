import requests
import execjs
cookies = {
    # 'mk': '339201ea4efa4d25ac12010539b1ce4a',
    # 'uk': '2080306434',
    # 'xlly_s': '1',
    # 'anchor-task-tips': 'vistived',
    # 'fansTuan-tips': 'vistived',
    # 'cna': 'NKWNHIfYgzcCAW8CWyb3taec',
    '_m_h5_tk': 'e6099cf2a63171c02027e25d21f6fb34_1678415547138',
    '_m_h5_tk_enc': '8752b6179c76b95f7ecc5f9c66550974',
    # 'isg': 'BJOTx03w87BV3bg71pM1er4DIhe9SCcKraQmm0WwdrLpxLJmzRl4WmJc-jSq5H8C',
    # '__ysuid': '1678411168839Ipl',
    # 'imk': 'MjA4MDMwNjQzNC0wLTE2Nzg0MTExNzAyNjMtMTY3ODQ5NzU3MDI2Mw%3D%3D-960F99893B38D34CDB89867DA1D47635',
}

headers = {
    'authority': 'acs.laifeng.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'cookie': 'mk=339201ea4efa4d25ac12010539b1ce4a; uk=2080306434; xlly_s=1; anchor-task-tips=vistived; fansTuan-tips=vistived; cna=NKWNHIfYgzcCAW8CWyb3taec; _m_h5_tk=e6099cf2a63171c02027e25d21f6fb34_1678415547138; _m_h5_tk_enc=8752b6179c76b95f7ecc5f9c66550974; isg=BJOTx03w87BV3bg71pM1er4DIhe9SCcKraQmm0WwdrLpxLJmzRl4WmJc-jSq5H8C; __ysuid=1678411168839Ipl; imk=MjA4MDMwNjQzNC0wLTE2Nzg0MTExNzAyNjMtMTY3ODQ5NzU3MDI2Mw%3D%3D-960F99893B38D34CDB89867DA1D47635',
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
    't': '1678411171790',
    'sign': 'd9e61f0aab26b0345917547ff0f3ead5',
    'type': 'originaljson',
    'dataType': 'jsonp',
    'api': 'mtop.youku.live.lf.gift.config.get',
    'v': '1.1',
}

bro_cookies='mk=339201ea4efa4d25ac12010539b1ce4a; uk=2080306434; xlly_s=1; anchor-task-tips=vistived; fansTuan-tips=vistived; cna=NKWNHIfYgzcCAW8CWyb3taec; _m_h5_tk=e6099cf2a63171c02027e25d21f6fb34_1678415547138; _m_h5_tk_enc=8752b6179c76b95f7ecc5f9c66550974; isg=BJOTx03w87BV3bg71pM1er4DIhe9SCcKraQmm0WwdrLpxLJmzRl4WmJc-jSq5H8C; __ysuid=1678411168839Ipl; imk=MjA4MDMwNjQzNC0wLTE2Nzg0MTExNzAyNjMtMTY3ODQ5NzU3MDI2Mw%3D%3D-960F99893B38D34CDB89867DA1D47635'

# 调用js
with open('laifengsign.js', 'r', encoding='UTF-8') as f:
    js_code = f.read()
    context = execjs.compile(js_code)
    result = context.call("getSign", '{"loginApp":1000,"roomId":"8122883"}',bro_cookies).split("_")
    print(result)
    sign=result[0]
    t=result[1]
    # print(t)
# 重新赋值param
params = {
    'jsv': '2.6.1',
    'appKey': '24679788',
    't': '%s'%t,
    'sign': '%s'%sign,
    'api': 'mtop.youku.laifeng.rec.pc.attention.get',
    'dataType': 'json',
    'v': '1.0',
    'preventFallback': 'true',
    'type': 'originaljson'
}
data = {
    'data': '{"loginApp":1000,"roomId":"8122883"}',
}

    
session=requests.Session()
response = session.get(
    'https://acs.laifeng.com/h5/mtop.youku.laifeng.rec.pc.attention.get/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)



print(response.cookies['_m_h5_tk'])