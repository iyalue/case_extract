import requests
from bs4 import BeautifulSoup
import time
#登录系统需要两次获得cookie
#或得cookie1

def setcookie1():
    print("开始请求登入系统，获得第一次cookie!\n")
    import requests
    url = "http://192.168.8.90:9080/htweb/do?module=Sys&action=Shell&method=getShellUpdateDescriptor&updatePackageURL=sys/shell/HTShellUpdate.zip"
    r = requests.get(url)
    if(r.status_code!=200):
        print("error")
    cookie = r.headers
    cookie = cookie["Set-Cookie"]
    print("获得第一次cookies成功！\n")
    return cookie

#第一次登入系统
def log_in(cookie):
    print("开始使用lzb登入系统:\n")
    import requests
    url = "http://192.168.8.90:9080/htweb/do?module=User&action=Login&method=login"
    header = {"Cookie":cookie,"Accept":"*/*","Content-Type":"application/x-www-form-urlencoded;","Referer":"http://192.168.8.90:9080/htweb/","Accept-Language":"zh-cn","Accept-Encoding":"gzip, deflate","User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)","Host":"192.168.8.90:9080","Content-Length":"102","Connection":"Keep-Alive","Pragma":"no-cache","Cookie":cookie}
    data = {"WayOflogin":"1","user":"lzb","password":"439c3dd44ce03d75e686c914a37fbe2a","ipid":"","registerSn":"","loadFlag":"","checkUser":""}
    r = requests.post(url,headers = header,data = data)
    r.encoding = "uft-8"
    print(r.text)
    return r

#获得cookie2
#后续操作必须传入cookie2
def setcookie2(cookie1):
    print("第二次进入系统，获得第2次cookie!\n")
    url = "http://192.168.8.90:9080/htweb/do?module=User&action=Login&method=login"
    header = {"Accept":"*/*", \
              "Content-Type":"application/x-www-form-urlencoded;", \
              "Referer":"http://192.168.8.90:9080/htweb/", \
              "Accept-Language":"zh-cn", \
              "Accept-Encoding":"gzip, deflate", \
              "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)", \
              "Host":"192.168.8.90:9080", \
              "Content-Length":"102", \
              "Connection":"Keep-Alive", \
              "Pragma":"no-cache", \
              "Cookie":cookie1
              }
    data = {"WayOflogin":"1", \
            "user":"lzb", \
            "password":"439c3dd44ce03d75e686c914a37fbe2a", \
            "ipid":"","registerSn":"","loadFlag":"","checkUser":""}
    r = requests.post(url,headers = header,data = data)
    cookie2 = r.headers
    cookie2 = cookie2["Set-Cookie"]
    print("获得cookie2成功！\n")
    return cookie2
    

def search(cookie,page_num=""):
    url = "http://192.168.8.90:9080/htweb/do?module=adt&action=HistoryPatient&method=historyCasePatientListNew&zcSrc="
    if(page_num!=""):
        url = url+"&pageNum="+str(page_num)
    header = {"Cookie":cookie,"Accept":"*/*","Content-Type":"application/x-www-form-urlencoded;","Referer":"http://192.168.8.90:9080/htweb/do?module=adt&action=HistoryPatient&method=showHistoryCaseMain&urlMd5=337cdbbaf175a679a9a30b8fb7a4d165&tabNodeID=HistoryCase&tabNodeParentId=12&funcTree=Now","Accept-Language":"zh-cn","Accept-Encoding":"gzip, deflate","User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)","Host":"192.168.8.90:9080","Content-Length":"250","Connection":"Keep-Alive","Pragma":"no-cache"}
    data ="classCode=&department=&certID=&adminissionNo=&ipid=&startTime=2019-12-31&endTime=2021-12-12&patientName=&ryzd=&cyzd=%E8%84%93%E6%AF%92%E7%97%87&outStartTime=&outEndTime=&pid=&doctor=&mrStatus=&operationDate=&operationName=&checkOperationName=&operationCode=&icd=&groupD=" 
    r = requests.post(url,data = data,headers = header)
    return r


def choose_department(cookie):
    url = "http://192.168.8.90:9080/htweb/do?module=User&action=Login&method=showUserDuty"
    header = {"Accept":"image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*", \
              "Referer":"http://192.168.8.90:9080/htweb/do?module=User&action=Login&method=showUserDutyMain&pageNum=1", \
              "Accept-Language":"zh-cn", \
              "Content-Type":"application/x-www-form-urlencoded", \
              "Accept-Encoding":"gzip, deflate", \
              "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)", \
              "Content-Length":"33", \
              "Host":"192.168.8.90:9080", \
              "Connection":"Keep-Alive", \
              "Pragma":"no-cache", \
              "Cookie":cookie}
    data = {"dutyType":"MD","deptCode":"*","wardCode":"*"}
    r = requests.post(url,data= data,headers = header)
    return r

#查找历史病人信息
def search_history(cookies):
    print("开始查找病人历史信息！\n")
    url = "http://192.168.8.90:9080/htweb/do?module=adt&action=HistoryPatient&method=historyCasePatientListNew&zcSrc=" 
    header = {"Accept":"*/*", \
              "Content-Type":"application/x-www-form-urlencoded;", \
              "Referer":"http://192.168.8.90:9080/htweb/do?module=adt&acton=HistoryPatient&method=showHistoryCaseMain&urlMd5=337cdbbaf175a679a9a30b8fb7a4d165&tabNodeID=HistoryCase&tabNodeParentId=12&funcTree=Now", \
              "Accept-Language":"zh-cn", \
              "Accept-Encoding":"gzip, deflate", \
              "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)", \
              "Host":"192.168.8.90:9080", \
              "Content-Length":"270", \
              "Connection":"Keep-Alive", \
              "Pragma":"no-cache", \
              "Cookie":cookies}
    data = {"classCode":"", \
            "department":"", \
            "certID":"", \
            "adminissionNo":"", \
            "ipid":"", \
            "startTime":"2021-11-31", \
            "endTime":"2021-12-12", \
            "patientName":"", \
            "ryzd":"", \
            "cyzd":"", \
            "outStartTime":"", \
            "outEndTime":"", \
            "pid":"", \
            "doctor":"", \
            "mrStatus":"", \
            "operationDate":"", \
            "operationName":"", \
            "checkOperationName":"", \
            "operationCode":"", \
            "icd":"", \
            "groupD":""}
    r = requests.post(url,data = data,headers = header)
    print("病人历史信息查找完成！\n")
    return r

def search_all(cookie,num):
    list = []
    print("第1次搜索\n")
    result = search(cookie2)
    result.encoding = "utf-8"
    soup = BeautifulSoup(result.text, 'html.parser')
    a = soup.find_all('td')
    search(cookie)
    for i in a:
        list.append(i.text)
    for i in range(2,num):
        print("第",i,"次搜索\n")
        result = search(cookie,i)
        result.encoding = "utf-8"
        soup = BeautifulSoup(result.text, 'html.parser')
        a = soup.find_all('td')
        for j in a:
            list.append(j.text)
        print("第",i,"次搜索结束\n")
    return list

def save_file(result):
    import numpy as np
    import pandas as pd
    a = np.array(result)
    a = a.reshape((int(len(result)/20),20))
    pd.DataFrame(a).to_csv('sample.csv')


def start_manipulation():
    cookie1 = setcookie1()
    log_in(cookie1)
    cookie2 = setcookie2(cookie1)
    choose_department(cookie2)
    return cookie2

def log_out(cookie):
    url = "http://192.168.8.90:9080/htweb/do?module=User&action=Login&method=logout"
    headers = {"Accept":"*/*", \
              "Content-Type":"application/x-www-form-urlencoded;", \
              "Referer":"http://192.168.8.90:9080/htweb/do?module=Sys&action=Shell&method=showInitPage", \
              "Accept-Language":"zh-cn", \
              "Accept-Encoding":"gzip, deflate", \
              "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)", \
              "Host":"192.168.8.90:9080", \
              "Content-Length":"102", \
              "Connection":"Keep-Alive", \
              "Pragma":"no-cache", \
              "Cookie":cookie
              }
    requests.post(url,headers = headers)
    return
