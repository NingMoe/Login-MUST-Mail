# coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.PhantomJS()
url = "https://mail.student.must.edu.mo/?_task=login"

def login(user,pwd):
    # 访问登陆页
    driver.get(url)
    # 填写邮箱与密码登陆
    driver.find_element_by_id ("rcmloginuser").send_keys (user)
    driver.find_element_by_id ("rcmloginpwd").send_keys (pwd)
    driver.find_element_by_id ("rcmloginsubmit").submit ( )
    return driver

    # 检测登陆状态
def islogin():
    soup = BeautifulSoup (driver.page_source, "html.parser")
    if '收件箱' in soup.text:
        print ('login successful')
        return True
    else:
        print ('Login failed')
        quit ()

#定位tbody
def tbody():
    soup = BeautifulSoup (driver.page_source, "lxml")
    mlist = soup.find (id="messagelist").find ('tbody')
    return mlist
#定位寄件人
def nameadd():
    madrr = tbody().select('[class="rcmContactAddress"]')
    return madrr

def INBOX():
    ij = ''.join (str (tbody ( )))
    sj = ij.replace ('><', '>,<').replace ('> <', '>,<').replace ('[', '').replace (']', '')
    ij1 = sj.split (',')
    return (ij1)


def ID():
    subject = []
    for i in INBOX ():
        if str ('rcmrow') in i:
            ids = i.replace ('<', '').replace ('>', '').replace ('rcmrow', '').replace ('id=', '').replace ('"','').split (' ')
            subject.append (ids[2])
    return subject

def title():
    sslist = tbody().select('[class="subject"]')
    subject = []
    for ss in sslist:
        subject.append (ss.get_text ( ).replace (u'\xa0', u''))
    return subject

def name():
    subject = []
    for ss in nameadd ():
        subject.append (ss.get_text ( ))
    return subject

def add():
    subject = []
    for a in nameadd ():
        subject.append (a.get ('title'))
    return subject

def date():
    list = tbody().select ('[class="date"]')
    subject = []
    for ss in list:
        subject.append (ss.get_text ( ).replace (u'\xa0', u''))
    return subject

def size():
    list = tbody().select ('[class="size"]')
    subject = []
    for ss in list:
        subject.append (ss.get_text ( ).replace (u'\xa0', u''))
    return subject



#-------testing part---------

username = **
password = **

login(username,password)

print(ID())
print (title ())
print(add())
print(date())
print(size())
