#!/usr/bin/python3

from glob import glob

fileList = glob('**/*', recursive=True)

html = open('sitemap.html', mode = 'w', encoding = 'utf-8')
txt = open('sitemap.txt', mode = 'w', encoding = 'utf-8')

site = 'https://' + glob('../*.*/.git', recursive=True)[0][3:-4]

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
  
  if file.startswith('build/'): continue
  elif file.endswith('index.html'):
    link += file[:-10]
  elif file.endswith('.html'):
    link += file[:-5]
  else:
    link += file
  
  linkList.append(link)

linkList.sort()

for link in linkList:
  if link == site:
    html.write('<a href="%s">Home</a>Home<br>\n'%(link))
  else:
    html.write('<a href="%s">%s</a><br>\n'%(link, link.split('/')[-1]))
  txt.write(link + '\n')

html.write('</body>\n</html>\n')

html.close()
txt.close()
