## 路径下的所有图片
import os
import pandas as pd
import re
import shutil

df_sub = pd.DataFrame()
# 图床图片的本地路径
path = 'E:\\GooglePhoto\\'
imgtypes = ('png', 'jpg', 'webp', 'gif')
prefix = 'https://raw.githubusercontent.com/xwydq/picbed/master/'

# Markdown 笔记文件夹
md_odir = 'C:\\Users\\xwydq\\Google 云端硬盘\\note'
# Markdown 笔记文件夹替换img url
md_dir = 'C:\\Users\\xwydq\\Google 云端硬盘\\noteurl'


# copy本地文件
def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

copy_and_overwrite(md_odir, md_dir)


## list all img file path
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


#############
### 正则替换
## list md files
md_files = []
for r, d, f in os.walk(md_dir):
    for file in f:
        if file.lower().endswith('.md'):
            md_files.append(os.path.join(r, file))

## 按行读取单个 md 文件
# 每行循环进行正则替换
for md_file in md_files:
    with open(md_file, "r", encoding='utf-8') as f:
        md_lines = f.readlines()

    for li in range(len(md_lines)):
        line = md_lines[li]
        for fi in range(len(file_nm)):
            fd = file_nm[fi]
            ptn = r'\!\[.*\]\(.*' + fd + r'\)'
            if re.search(ptn, line):
                print(line)
                substr = re.sub(r'\(.*' + fd + r'\)',
                                r'(' + img_url[fi] + r')', line, count=0, flags=0)
                md_lines[li] = substr

    with open(md_file, "w", encoding='utf-8') as f:
        f.writelines(md_lines)


# with open(md_file, "r", encoding='utf-8') as f:
#     for line in f.readlines():
#         # print(line)
#         for fi in range(len(file_nm)):
#             fd = file_nm[fi]
#             # img_url[fi]
#         # for fd in file_nm:
#             ptn = r'\!\[.*\]\(.*' + fd + r'\)'
#             if re.search(ptn, line):
#                 print(line)
#                 substr = re.sub(r'\(.*' + fd + r'\)',
#                        r'(' + img_url[fi] + r')', line, count=0, flags=0)
#                 print(substr)







##################
## 关于反斜杠在正则表达式re
# import re
# string = '3\8'
# m = re.search(r'(\d+\\)', string)
# print(m.group(1))
#
# re.search('\!\[.*\]\(E:\\jdfhek.jpg\)', 'jksjdj![](E:\jdfhek.jpg)')
# re.search(r'\!\[.*\]\(E:\\jdfhek.jpg\)', 'jksjdj![](E:\jdfhek.jpg)')
