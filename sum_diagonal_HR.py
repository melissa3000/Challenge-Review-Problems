"""Explanation:
Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output
15


The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15 """




import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum1 = 0
sum2 = 0

i = 0
for item in a:
    sum1 += a[i][i]
    i += 1


b = 0

for item in a:
    sum2 += a[b][n-1]
    b += 1
    n -= 1

print abs(sum2 - sum1)



