""" Task
You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
Input Format
The first line contains an integer .  is the total number of integers in the list.
The second line contains the space separated list of  integers."""


# Enter your code here. Read input from STDIN. Print output to STDOUT


N = int(raw_input())
lst = raw_input()


lst = [ int(x) for x  in lst.split()]

if all([item > 0 for item in lst]) and any([item < 10 for item in lst]):
    print True

else:
    print False