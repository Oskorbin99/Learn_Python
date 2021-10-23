import time
from urllib import request

import io
word = u'<dd class="y">1970-01-01 08:00:00</dd>'
a = [2,8,0,0]
list = []
not_file = False
# Collect events until released
for i in range(200):
    if a[3] == 9:
        a[3] = 0
        a[2] += 1
    else:
        a[3] += 1
    if a[2] == 10:
        a[2] = 0
        a[1] += 1
    if a[1] == 10:
        a[1] = 0
        a[0] += 1
    urlData = "https://c.mi.com/space-uid-" + "636" + "".join(map(str, a)) + "665" + ".html"
    webURL  = request.urlopen(urlData).read().decode("utf-8")
    f = open('text.txt', 'w', encoding="utf-8")
    f.write(webURL)
    f.close()
    with io.open('text.txt', encoding='utf-8') as file:
        for line in file:
            if word in line:
                not_file = True
    if not not_file:
        print(urlData)
        list.append(urlData)
    else:
        not_file = False
    print (f" successfully {i}: {a}")

for i in list:
    print(i)
print(a)

