#http://codeforces.com/contest/518/problem/B
#problem solved by Benegripe
#/usr/bin/py

s = [x for x in raw_input()]
r = [x for x in raw_input()]
dic = {}
for i in r:
    dic[i] = dic.get(i,0) + 1

yay = 0
for i in range(0,len(s)):
    if dic.get(s[i]) != None and dic.get(s[i]) != 0:
        dic[s[i]] -= 1
        yay += 1
        s[i] = '#'
whoops = 0
for i in s:
    if dic.get(i.lower()) != None and dic.get(i.lower()) != 0:
        dic[i.lower()] -= 1
        whoops += 1
    elif dic.get(i.upper()) != None and dic.get(i.upper()) != 0:
        dic[i.upper()] -= 1
        whoops += 1
print yay,whoops
