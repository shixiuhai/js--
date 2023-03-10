import requests
import execjs
import json
class LF:
    def __init__(self) -> None:
        # 默认传递使用的cookie
        self.broCookies={
            'mk': '339201ea4efa4d25ac12010539b1ce4a',
            'uk': '2080306434',
            'xlly_s': '1',
            'anchor-task-tips': 'vistived',
            'fansTuan-tips': 'vistived',
            'cna': 'NKWNHIfYgzcCAW8CWyb3taec',
            '_m_h5_tk': 'e6099cf2a63171c02027e25d21f6fb34_1678415547138',
            '_m_h5_tk_enc': '8752b6179c76b95f7ecc5f9c66550974',
            'isg': 'BJOTx03w87BV3bg71pM1er4DIhe9SCcKraQmm0WwdrLpxLJmzRl4WmJc-jSq5H8C',
            '__ysuid': '1678411168839Ipl',
            'imk': 'MjA4MDMwNjQzNC0wLTE2Nzg0MTExNzAyNjMtMTY3ODQ5NzU3MDI2Mw%3D%3D-960F99893B38D34CDB89867DA1D47635',
        }   
    def dicToStrCookies(self)->str:
        strCookies=""
        for key in self.broCookies:
            strCookies=strCookies+(key+"="+self.broCookies[key]+";")
        return strCookies[:-1]
    # 获取主播信息
    def getAnchor(self):
        pass
    # 获取主播房间信息
    def getAnchorRoom(self):
        pass
    
    # 获取sign函数
    def getSign(self,cookies:str,requestData:dict)->type:
        # 调用js
        with open('laifengsign.js', 'r', encoding='UTF-8') as f:
            js_code = f.read()
            context = execjs.compile(js_code)
            result = context.call("getSign",json.dumps(requestData),cookies).split("_")
            # print(result)
            sign=result[0]
            t=result[1]
        return (sign,t)
    
    # 获取主播视频流信息
    def getAnchorVideo(self,data:dict):
        # '{"liveId":"8122883","ccode":"live05010101laifeng","app":"Pc"}'
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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        # 第一次请求
        sign,t = self.getSign(self.dicToStrCookies(),data)
        
        params = {
            'jsv': '2.6.1',
            'appKey': '24679788',
            't': '%s'%t,
            'sign': '%s'%sign,
            'type': 'originaljson',
            'dataType': 'json',
            'api': 'mtop.youku.laifeng.live.center.liveplaycontrol',
            'v': '1.0',
            'data': json.dumps(data),
        }
        response = requests.get(
            'https://acs.laifeng.com/h5/mtop.youku.laifeng.live.center.liveplaycontrol/1.0/',
            params=params,
            cookies=self.broCookies,
            headers=headers,
        )
        # print(response.cookies)
        if response.json()['ret']==['FAIL_SYS_TOKEN_EXOIRED::令牌过期']:
            print("token 过期")
            # 重新赋值cookies的关键参数
            self.broCookies['_m_h5_tk']=response.cookies['_m_h5_tk']
            self.broCookies['_m_h5_tk_enc']=response.cookies['_m_h5_tk_enc']
            # 重新获取sign和t参数
            sign,t = self.getSign(self.dicToStrCookies(),data)
            # 第一次请求失败第二次请求
            params = {
                'jsv': '2.6.1',
                'appKey': '24679788',
                't': '%s'%t,
                'sign': '%s'%sign,
                'type': 'originaljson',
                'dataType': 'json',
                'api': 'mtop.youku.laifeng.live.center.liveplaycontrol',
                'v': '1.0',
                'data': json.dumps(data),
            }
            
            response = requests.get(
                'https://acs.laifeng.com/h5/mtop.youku.laifeng.live.center.liveplaycontrol/1.0/',
                params=params,
                cookies=self.broCookies,
                headers=headers,
            )
            return response.json()
        else:
            return response.json()
        
        
obj=LF()
# print(obj.dicToStrCookies())
print(obj.getAnchorVideo({"liveId":"8122883","ccode":"live05010101laifeng","app":"Pc"}))
print(obj.getAnchorVideo({"liveId":"8122883","ccode":"live05010101laifeng","app":"Pc"}))

print(obj.getAnchorVideo({"liveId":"8122883","ccode":"live05010101laifeng","app":"Pc"}))
