import urllib.request as ur
import re

urls=['http://google.com', 'http://youtube.com']

regex = '<title>(.+?)</title>'

patterns = re.compile(regex)

for i in range(len(urls)):
    htmlfile=ur.urlopen(urls[i])
    source=htmlfile.read()
    source = str(source)    #because we've got string pattern to match with source
    title=re.findall(patterns, source)
    print(title)
