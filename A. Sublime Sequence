###################################################################################### time limit per test :1 second ###############################################################################################
################################################################################### memory limit per test :256 megabytes ##############################################################################################

Farmer John has an integer x. He creates a sequence of length n by alternating integers x and −x, starting with x.
For example, if n=5, the sequence looks like: x,−x,x,−x,x.
He asks you to find the sum of all integers in the sequence.
Input
The first line contains an integer t
 (1≤t≤100)  — the number of test cases.

The only line of input for each test case is two integers x
 and n (1≤x,n≤10).

Output
For each test case, output the sum of all integers in the sequence.
Example
Input
4
1 4
2 5
3 6
4 7
Output
0
2
0
4
############################################################################################ Solution ##############################################################################
There are n element and alternate number so it means divide by 2 .if the n is even so there sum will be zero because all cancel each but if the n is odd the pair number will cancle out and only last element will left so the 
output will be the number we are using (x).
######################################################################################### Code ##############################################################################
t=int(input())
for _ in range(t):
   x, n = map(int, input().split())
   if n%2 !=0:
      print(x)
   else:
      print("0")
