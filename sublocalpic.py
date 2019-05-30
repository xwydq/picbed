## 路径下的所有图片
import os
import pandas as pd
import re

df_sub = pd.DataFrame()

path = 'E:\\GooglePhoto\\'
imgtypes = ('png', 'jpg', 'webp', 'gif')
prefix = 'https://github.com/xwydq/picbed/blob/master/'
prefix = 'https://raw.githubusercontent.com/xwydq/picbed/master/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file.lower().endswith(imgtypes):
            files.append(os.path.join(r, file))

file_dirnm = files
file_nm = [os.path.basename(f) for f in files]
img_url = [prefix + os.path.basename(f) for f in files]
resub_pre = [r'\!\[.*\]\(' + f + '\)' for f in file_dirnm]
resub_after = ['\!\[.*\]\(' + u + '\)' for u in img_url]

df_sub = pd.DataFrame({
    'file_dirnm': file_dirnm,
    'file_nm': file_nm,
    'img_url': img_url,
    'resub_pre': resub_pre,
    'resub_after': resub_after
})

df_sub.to_csv('img_path_url_4md.csv', index=False)

## 正则替换

## list md files
md_dir = 'E:\\testPros\\note\\'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(md_dir):
    for file in f:
        if file.lower().endswith('.md'):
            files.append(os.path.join(r, file))

## 按行读取单个 md 文件
# 每行循环进行正则替换
md_file = 'E:\\testPros\\note\\superset\\superset.md'

with open(md_file, "r", encoding='utf-8') as f:
    for line in f.readlines():
        # print(line)
        for fi in range(len(file_nm)):
            fd = file_nm[fi]
            # img_url[fi]
        # for fd in file_nm:
            ptn = r'\!\[.*\]\(.*' + fd + r'\)'
            if re.search(ptn, line):
                print(line)
                substr = re.sub(r'\(.*' + fd + r'\)',
                       r'(' + img_url[fi] + r')', line, count=0, flags=0)
                print(substr)


##################
## 关于反斜杠在正则表达式re
import re

string = '3\8'
m = re.search(r'(\d+\\)', string)
print(m.group(1))

re.search('\!\[.*\]\(E:\\jdfhek.jpg\)', 'jksjdj![](E:\jdfhek.jpg)')
re.search(r'\!\[.*\]\(E:\\jdfhek.jpg\)', 'jksjdj![](E:\jdfhek.jpg)')




r'\!\[.*\]\(' + 'E:\\jdfhek.jpg' + r'\)'


re.search(re.compile(ptn), 'jksjdj![](jdfhek.jpg)')

'\\!\\[.*\\]\\(E:\\GooglePhoto\\4f54e63f817c4293b8f71adb15b1e3f7.webp\\)'.replace(r'\\','\\')



for f in files:
    print(f)
    print(os.path.basename(f))
    print(prefix + os.path.basename(f))
    file_dirnm = f
    file_nm = os.path.basename(f)
    img_url = prefix + os.path.basename(f)
    df_sub = pd.DataFrame(
        file_dirnm=file_dirnm,
        file_nm=file_nm,
        img_url=img_url,
        resub_pre='![.*]\(\)'
    )
