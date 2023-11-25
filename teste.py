import re
url = 'pteste.com'

rex = re.compile(r'http')
res = bool(rex.search(url))
print(res)