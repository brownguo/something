import requests
import coloredlogs
import sys
import logging
import time

class bj_hospital_registration(object):

    def __init__(self):
        pass

    def getDuty(self):
        # list_url = 'https://www.114yygh.com/web/product/list?_time={}'.format(int(time.time() * 1000))

        url = 'https://www.114yygh.com/web/product/detail?_time={}'.format(int(time.time() * 1000))
        print(url)
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "119",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": "hyde_session=L6qMa71caG58DM3SiGCK7SF52Qb6ySxF_5358918; "
                      "hyde_session=L6qMa71caG58DM3SiGCK7SF52Qb6ySxF_5358918; _"
                      "_jsluid_s=9125fbdfd130083aa7a89af522114cea; pgv_pvi=4550084608;"
                      " pgv_si=s3445782528; secure-key=1127cb18-bb29-44b3-a706-2e711215d85f; "
                      "cmi-user-ticket=Sxc9anWGhvW7FounLhmS5uvNRcMDLAWFR6IkJQ..; "
                      "hyde_session=Y5iZ4Jj7XTOlm1MexKSoy0EUkVF64VKf_5358920; hyde_session_tm={}".format(int(time.time() * 1000)),
            "Host": "www.114yygh.com",
            "Origin": "https://www.114yygh.com",
            "Referer": "https://www.114yygh.com/hospital/142/b4a4701c87a767a7ec671591c5af5297/200047440/source",
            "Request-Source": "PC",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        }
        session = requests.session()
        response = session.post(url=url, headers=headers)
        print(response.text)


if __name__ == '__main__':
    if not sys.platform.startswith('win'):
        coloredlogs.install('INFO')
        start = bj_hospital_registration()
        start.getDuty()