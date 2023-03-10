import requests
import execjs
cookies = {
    'mk': 'ca100c68af3649c8b71a649ae87a4b72',
    'uk': '2087231893',
    '_m_h5_tk': '9b2cb87e6279789975e25bb50fd34b6e_1678382787189',
    '_m_h5_tk_enc': '8053ba7e6b085f8048e7172a7ddd5fdd',
    'imk': 'MjA4NzIzMTg5My0wLTE2NzgzNzk0NTc2MjQtMTY3ODQ2NTg1NzYyNA%3D%3D-D213E8DAA5F602F98F671A8F409544CE',
}

headers = {
    'authority': 'acs.laifeng.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mk=ca100c68af3649c8b71a649ae87a4b72; uk=2087231893; _m_h5_tk=9b2cb87e6279789975e25bb50fd34b6e_1678382787189; _m_h5_tk_enc=8053ba7e6b085f8048e7172a7ddd5fdd; imk=MjA4NzIzMTg5My0wLTE2NzgzNzk0NTc2MjQtMTY3ODQ2NTg1NzYyNA%3D%3D-D213E8DAA5F602F98F671A8F409544CE',
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


if __name__ == "__main__":
    params = {
        'jsv': '2.6.1',
        'appKey': '24679788',
        't': '1678380171003',
        'sign': 'c76632e5e3b3397de8d7f43d63682e0d',
        'api': 'mtop.youku.laifeng.rec.pc.attention.get',
        'dataType': 'json',
        'v': '1.0',
        'preventFallback': 'true',
        'type': 'originaljson',
        'data': '{"page":"1","pageSize":"9"}',
    }
    bro_cookies='mk=339201ea4efa4d25ac12010539b1ce4a; uk=2080306434; xlly_s=1; anchor-task-tips=vistived; fansTuan-tips=vistived; cna=NKWNHIfYgzcCAW8CWyb3taec; _m_h5_tk=e6099cf2a63171c02027e25d21f6fb34_1678415547138; _m_h5_tk_enc=8752b6179c76b95f7ecc5f9c66550974; isg=BJOTx03w87BV3bg71pM1er4DIhe9SCcKraQmm0WwdrLpxLJmzRl4WmJc-jSq5H8C; __ysuid=1678411168839Ipl; imk=MjA4MDMwNjQzNC0wLTE2Nzg0MTExNzAyNjMtMTY3ODQ5NzU3MDI2Mw%3D%3D-960F99893B38D34CDB89867DA1D47635'

    # 调用js
    with open('laifengsign.js', 'r', encoding='UTF-8') as f:
        js_code = f.read()
        context = execjs.compile(js_code)
        result = context.call("getSign", params["data"],bro_cookies).split("_")
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
        'type': 'originaljson',
        'data': '{"page":"1","pageSize":"9"}',
    }
        
        
    session=requests.Session()
    response = session.get(
        'https://acs.laifeng.com/h5/mtop.youku.laifeng.rec.pc.attention.get/1.0/',
        params=params,
        cookies=cookies,
        headers=headers,
    )


print(response.json())