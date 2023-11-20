import requests
import os

class AutoLogin():
    def __init__(self):
        #url = "http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanacip=192.168.132.254&wlanacname=JPL-ME60-1&mac=e9-c1-90-aa-68-43&enAdvert=0&queryACIP=0&loginMethod=1"
        url = "http://192.168.7.221:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=192.168.7.221&iTermType=1&wlanacip=192.168.132.254&wlanacname=JPL-ME60-1&mac=bd-64-5e-3a-bb-9b&enAdvert=0&queryACIP=0&loginMethod=1"

        # 请求头
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        # 账号、密码、时间戳写入payload报文
        #payload = f"opr=pwdLogin&userName={account}&pwd={pwd}&auth_tag={tag}&rememberPwd=1"
        data = (f"DDDDD=%2C0%2C008750&upass=Zx910918&R1=0&R2=0&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login=")

        # 提交登录
        res = requests.post(url, data=data, headers=headers)
        #print(res.text)

        self.states(res)

    def states(self, res):
        # login back
        if '<!--Dr.COMWebLoginID_3.htm-->' in res.text:
            print('Login Success!')
            self.msg = 'ok'
            return
        elif '<!--Dr.COMWebLoginID_2.htm-->' in res.text:
            print("信息页")
            self.msg = 'ok'
            return
        else:
            print("网络不通！登录后台查询")
            self.msg = 'error'
            return

def check_ping(ip, count=1, timeout=1000):
    cmd = 'ping -n %d -w %d %s > NUL' % (count, timeout, ip)
    res = os.system(cmd)
    return 'ok' if res == 0 else 'failed'

    # def __init__(self):
    #     # check internet state
    #     self.res
    #
    #     try:
    #         self.res = requests.get('https://www.baidu.com/', timeout=5)
    #     except requests.exceptions.RequestException as e:
    #         print('It timed out!')
    #     finally:
    #         self.status = True if self.res.status_code == 200 else False


if __name__ == "__main__":
    # internet connect
    status = True if check_ping("baidu.com") == 'ok' else False

    if status:
        print('Already connected to the Internet!')
    else:
        L = AutoLogin()
        print(L.msg)
