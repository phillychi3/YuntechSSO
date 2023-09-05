# 雲林科技大學單一登入

## 簡介

我也不知道為啥要寫這個，肚子太痛了打發時間

## 使用方法

安裝

```bash
$ pip install -r requirements.txt
```

使用

```python
from yuntechsso import YuntechSSO
from sites import Site

wow = YuntechSSO("username", "password") # 帳號密碼
wow.init()
site = wow.get(Site.Home) # 裡面的網站可以自己打
print(site)
```

拿到之後就可以做其他事情，比如課表之類的~
