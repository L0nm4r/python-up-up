官方文档: https://docs.python.org/zh-cn/3/library/hashlib.html

每种类型的 *hash* 都有一个构造器方法, 它们都返回一个具有相同的简单接口的 hash 对象

可以使用 `update()` 方法向这个对象输入字节类对象

example:

```python
>>> import hashlib
>>>
>>> m = hashlib.md5()
>>> m.update(b"admin123456")
>>> m.digest()
b'\xa6j\xbbV\x84\xc4Yb\xd8\x87VO\x084n\x8d'
>>> m.hexdigest()
'a66abb5684c45962d887564f08346e8d'
```

更简单的写法:

```python
>>> hashlib.md5(b"admin123456").hexdigest()
'a66abb5684c45962d887564f08346e8d'
```

加盐:

```python
import hashlib

salt='secret_value'#自定义加盐字符串
md5_str='test123456'#加密字符串

salt_md5=hashlib.md5((md5_str+salt).encode('utf-8')).hexdigest()
str_md5=hashlib.md5(md5_str.encode('utf-8')).hexdigest()

print("没有加盐："+str_md5)
print("加盐之后："+salt_md5)

#运行结果
没有加盐：47ec2dd791e31e2ef2076caf64ed9b3d
加盐之后：f9fc96fcf48eb7cbc5a20a025506a0e3
```

