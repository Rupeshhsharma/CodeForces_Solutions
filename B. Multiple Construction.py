------------------------------------------------------------------Multiple Construction----------------------------------------------------
-------------------------------------------------------------time limit per test:1 second----------------------------------------------------------
---------------------------------------------------------memory limit per test:256 megabytes-----------------------------------------------------------------------
You are given an integer n. Your task is to construct an array of length 2⋅n such that:
Each integer from 1 to n appears exactly twice in the array.
For each integer x (1≤x≤n), the distance between the two occurrences of x is a multiple of x. In other words, if px and qx are the indices of the two occurrences of x, |qx−px| must be divisible by x.
It can be shown that a solution always exists.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.
Each of the next t lines contains a single integer n (1≤n≤2⋅105).
It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, print a line containing 2⋅n integers — the array that satisfies the given conditions.
If there are multiple valid answers, print any of them.

Example
Input
3
2
3
1
Output
1 2 1 2
1 3 1 2 3 2
1 1
Note
Visualizer link

In the first test case:
The number 1 appears at positions 1 and 3: the distance is 2, which is divisible by 1.
The number 2 appears at positions 2 and 4: the distance is 2, which is divisible by 2.
In the second test case:
The number 1 appears at positions 1 and 3: the distance is 2, which is divisible by 1.
The number 2 appears at positions 4 and 6: the distance is 2, which is divisible by 2.
The number 3 appears at positions 2 and 5: the distance is 3, which is divisible by 3.
In the third test case, the two occurrences of 1 are at positions 1 and 2, so the distance between them is 1, which is a multiple of 1.
-----------------------------------------------------------------------------------Solution--------------------------------------------------------------------------------
There are multiple ways to solve this problem. We believe the easiest one is based on the following construction:[ n, n-1, n-2, ..., 3, 2, 1, n, 1, 2, 3, ..., n-2, n-1 ]
It's easy to see that both occurrences of n are at a distance of n, and all the other values appear at a distance of twice their value. In other words, we place the two n
's at the first position and at the (n+1)-th position, then we use the second n as a pivot to place numbers from 1 to n−1 in order.
There exist other constructions as well. For example, for n odd, we can use:[ 1, n-2, n-4, ..., 3, n, 1, 3, 5, ..., n-2, n-1, n-3, ..., 2, n, 2, ..., n-3, n-1 ]
For n even, the pattern is similar but we adjust the positions of n−1 and n−2 accordingly.
A greedy algorithm also works: we go from n to 1, and try to place each number in the leftmost possible position. Note that this greedy algorithm follows the same pattern as the first construction.
##################################################################################### Code #################################################################
t=int(input())
for _ in range(t):
  n = int(input())    
  for i in range(n, 0, -1):
    print(i, end=" ")
  print(n,end=" ")   
  for i in range(1, n):
    print(i, end=" ")
  print()

