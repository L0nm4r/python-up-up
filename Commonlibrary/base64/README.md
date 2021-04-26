编码:
```python
import base64
content = "flag"
content = content.encode('utf-8') # b'flag'
b64content = base64.b64encode(content) # b'ZmxhZw=='
b64content = b64content.decode() # ZmxhZw==
```
解码:
```python
import base64
b64content = "ZmxhZw=="
b64content = b64content.encode('utf-8') # b'ZmxhZw=='
content = base64.b64decode(b64content) # b'flag'
content = content.decode() # flag
```