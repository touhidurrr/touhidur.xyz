from glob import glob
from functools import cmp_to_key as toKey

fileList = glob('**/*.*', recursive=True)

html = open('sitemap.html', mode = 'w', encoding = 'utf-8')
txt = open('sitemap.txt', mode = 'w', encoding = 'utf-8')

site = 'https://touhidur.xyz/'

html.write(
'''<!DOCTYPE html>
<html>
<head>
  <title>Sitemap</title>
</head>
<body>
''')

linkList = []

for file in fileList:
  link = site
  
  if file.startswith('build'): continue
  elif file.endswith('index.html'):
    link += file[:-10]
  elif file.endswith('.html'):
    link += file[:-5]
  else:
    link += file
  
  linkList.append(link)

def cmp(a, b):
  ac = a.count('/')
  bc = b.count('/')
  if  ac == bc:
    la = len(a)
    lb = len(b)
    if la == lb:
      if a < b: return -1
      if a == b: return 0
      return 1
    return la - lb
  return ac - bc

linkList.sort(key=toKey(cmp))

for link in linkList:
  if link == site:
    html.write('<a href="%s">Home</a><br>\n'%(link))
  else:
    html.write('<a href="%s">%s</a><br>\n'%(link, link.split('/')[-1]))
  txt.write(link + '\n')

html.write('</body>\n</html>\n')

html.close()
txt.close()
