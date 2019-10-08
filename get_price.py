import urllib.request as ur
import re

while True:

    sym=input("Enter the symbol: ")

    regex='<span id="yfs_l84_{}">(.+?)</span>'.format(sym)

    pattern=re.compile(regex)

    url='https://in.finance.yahoo.com/q?s={}'.format(sym)

    price=re.findall(pattern, str(ur.urlopen(url).read()))[0]

    print(price)
