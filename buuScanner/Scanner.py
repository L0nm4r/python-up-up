import requests

url="http://baidu.com/"

# 加载字典,模式匹配
def LoadDicts(filepath=''):
    Dicts=[]
    dictsFile=open(filepath,'r')
    
    for path in dictsFile:
        path = path.strip()
        Dicts.append(path)
    dictsFile.close()
    return Dicts

# 直接扫描
def Scan(url='',dicts=[]):
    results=[]
    for path in dicts:
        r = requests.get(url=url+path)
        print(r.status_code,url+path)
        if r.status_code in [200,302]:
            results.append(url+path)
    return results

# 结果展示
def showResults(results):
    for res in requests:
        print(res)

if __name__ == '__main__':
    Dicts=LoadDicts('test.txt')
    results=Scan(url,Dicts)
    showResults(results)