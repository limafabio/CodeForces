#http://codeforces.com/contest/519/problem/B
#problem solved by Benegripe
#/usr/bin/py
S = lambda: sum(map(int,raw_input().split()))
n = int(raw_input())
er1 = S()
er2 = S()
er3 = S()
print er1 - er2
print er2 - er3
