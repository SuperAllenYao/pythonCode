import urllib.request
import urllib.error
import json

address = input('Enter your URL: ')
uh = urllib.request.urlopen(address)
data = uh.read().decode()

js = json.loads(data)
js = js['comments']

sums = 0
for i in js:
    for k, v in i.items():
        # print(k,v)
        if k == 'count':
            a = int(v)
            sums += a
        else:
            continue
print(sums)
