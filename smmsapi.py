#!python3
#encoding:utf-8
import os
import sys
import requests
def get_url(img):
    #print("请输入图片路径")
    #img = sys.stdin.readline().decode("utf-8")
    #print(img)
    name=str(os.path.basename(img)).replace("\n","").replace("截图","")
    print(name)
    url = "https://sm.ms/api/upload"
    files = {'smfile': ("%s"%name , open(img.replace("\n", ""), 'rb'), 'image/png')}
    print(files)
    sdata = {'ssl': 1}
    res = requests.post(url=url, data=sdata, files=files)
    the_json = res.text
    import json
    the_json = json.loads(the_json)
    print(the_json)
    # print the_json["data"]["delete"]  #删除图片链接
    print(the_json["data"]["url"])  # 图片链接
    print(the_json["data"]["filename"])  # 文件名
    import pyperclip
    mk = '![%s](%s )' % (the_json["data"]["filename"], the_json["data"]["url"])
    print(mk)
    pyperclip.copy(mk)
    print("已复制")
    f = open("图床记录.csv", "a+")
    f.write(the_json["data"]["filename"])
    f.write(",")
    f.write(the_json["data"]["url"])
    f.write(",")
    f.write(the_json["data"]["delete"])
    f.write("\r")
    f.close()


while(True):
    img = sys.stdin.readline()
    get_url(img)