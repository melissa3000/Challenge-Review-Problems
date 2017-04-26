#Write a program to produce a pattern of hash symbols shaped like a sideways triangle:
#
##
###
####
###
##
#

def sideways_triangle(n):
    i = 1
    while i <= n - 1:
        print '#' * i
        i +=1
    while i > 0:
        print '#' * i
        i -=1



sideways_triangle(4)
