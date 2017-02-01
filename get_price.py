import urllib.request as ur
import re

while True:

    sym=input("Enter the symbol: ")

    regex='<span id="yfs_l84_{}">(.+?)</span>'.format(sym)

    pattern=re.compile(regex)

    url='https://in.finance.yahoo.com/q?s={}'.format(sym)

    htmlfile=ur.urlopen(url)

    source=htmlfile.read()

    source=str(source)

    price=re.findall(pattern, source)

    print(price[0])
