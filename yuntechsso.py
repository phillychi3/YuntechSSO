import requests
from bs4 import BeautifulSoup
from typing import Union

__all__ = ["YuntechSSO"]

class YuntechSSO:
    def __init__(self,username:str,password:str) -> None:
        self.ssourl = "https://webapp.yuntech.edu.tw/YunTechSSO/Account/Login"
        self.session = requests.Session()
        self.cookie = ""
        self.__RequestVerificationToken = ""
        self.username = username
        self.password = password
        self.universalheaders = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "webapp.yuntech.edu.tw",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

    def __beforelogin(self):
        req = self.session.get(self.ssourl, headers=self.universalheaders)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "html.parser")
            self.__RequestVerificationToken = soup.find(
                "input", {"name": "__RequestVerificationToken"}
            )["value"]
            self.cookie = req.cookies
            return True
        else:
            return False

    def __login(self):
        data = {
            "pLoginName": self.username,
            "pLoginPassword": self.password,
            "pRememberMe": True,
            "redirectUrl": "",
            "RedirectTo": "",
            "__RequestVerificationToken": self.__RequestVerificationToken,
        }
        ssoreq = self.session.post(
            self.ssourl, headers=self.universalheaders, data=data
        )
        if ssoreq.status_code == 302 or ssoreq.status_code == 200:
            self.cookie = ssoreq.headers["Set-Cookie"]
        else:
            raise Exception("登入失敗")

    def init(self):
        self.__beforelogin()
        self.__login()


    def get(self,url:str) -> str:
        headers = self.universalheaders.copy()
        headers.update({"Cookie": self.cookie})
        home = self.session.get(url, headers=headers)
        if home.status_code == 200:
            return home.text
        else:
            match home.status_code:
                case 404:
                    raise Exception("404 找不到網頁")
                case 500:
                    print("500 伺服器錯誤 嘗試重新登入")
                    self.init()
                    return self.get(url)
                case _:
                    raise Exception("未知錯誤")
            

