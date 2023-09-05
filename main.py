from yuntechsso import YuntechSSO
from sites import Site

username = input("請輸入學號:")
password = input("請輸入密碼:")
wow = YuntechSSO(username, password)
wow.init()
with open("test.html", "w", encoding="utf-8") as f:
    f.write(wow.get(Site.Home))


