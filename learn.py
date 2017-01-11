#coding:utf-8
#!/usr/bin/python
# Filename: map.py
from PIL import Image

1. # 类的使用 #
class Student(object):
    def __init__(self, name, age):     
        self.__name=name
        self.age=age

    def getname(self):
        print self.__name

james = Student("james", 15)
mike = Student("mike", 20)

2. # @property的使用 #
class Screen(object):

    @property
    def width(self):
        print self._width

    @width.setter
    def width(self,value):
        self._width=value

s = Screen()
s.width=100
s.width          # 输出100

3. # 运用模组 从网上下载图片到本地
import random
import urllib.request

def dlweb(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

dlweb('http://xxxxxxx')

4. #读写文件
fw = open('sample.txt', 'w')
fw.write('writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

5. #下载csv文件，本地保存
from urllib import request

url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=9&c=2016&d=0&e=9&f=2017&g=d&ignore=.csv'

def dl(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

dl(url)

6. #线程
import threading


class abc(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

th1 = abc(name='this is 1')               #结果：th1，th2同时进行
th2 = abc(name='this is 2')
th1.start()
th2.start()     

7. #Python 程序： 提取网页高频词
import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'lxml')
    for post_text in soup.find_all('a', {'class': 'Fw(b)'}):
        content = post_text.string
        words = str(content).lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = '!.@#$%^&*();:,~<>'
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 0:
            clean_word_list.append(word)
    create_dict(clean_word_list)

def create_dict(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for k, v in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(k, v)

start('https://ca.yahoo.com/')
