----------------------------------------------------------------------- Submission is All You Need ------------------------------------------------------------------------------
----------------------------------------------------------------------time limit per test:1 second ------------------------------------------------------------------------------------
-------------------------------------------------------------------memory limit per test:256 megabytes------------------------------------------------------------------------------------
For a multiset T consisting of non-negative integers, we define:sum(T) is the sum of all elements in T. For example, if T={0,1,1,3}, then sum(T)=0+1+1+3=5.
mex(T) is the smallest non-negative integer not in T. For example, if T={0,1,1,3}, then mex(T)=2 because 2 is the smallest non-negative integer not present in T.
You are given a multiset S of size n consisting of non-negative integers. At first, your score is 0. You can perform the following operations any number of times in any order (possibly zero):
Select a subset S′⊆S (i.e., S′ contains some of the elements currently in S), add sum(S′) to your score, and then remove S′ from S.
Select a subset S′⊆S, add mex(S′) to your score, and then remove S′ from S
Find the maximum possible score that can be obtained.
  
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤103). The description of the test cases follows.
The first line of each test case contains a single integer n (1≤n≤50).
The second line of each test case contains n integers S1,S2,…,Sn (0≤Si≤50).

Output
For each test case, print a single integer — the maximum possible score that can be obtained.

Example
Input
2
3
0 1 1
3
1 2 3
Output
3
6
Note
In the first test case, a possible optimal strategy is as follows:

Select S′={0,1}, add mex(S′)=mex({0,1})=2 to your score, and then remove S′ from S. Currently, your score is 2 and S={1}.
Select S′={1}, add sum(S′)=sum({1})=1 to your score, and then remove S′ from S. Currently, your score is 3 and S=∅.
After that, you cannot do any further operations. It can be proven that 3 is the maximum possible score that can be obtained.

  -----------------------------------------------------------------------Solution----------------------------------------------------------------------------------
Assuming that choosing mex(S') is optimal, there are no duplicate numbers in S′. And thers is not a number greater than mex(S'). Otherwise, we can easily construct a better answer.

Consider S={0,1,...,x}. We can see mex(S')>max(S') when x is 0 or 1. And mex({0,1})=mex({0})+sum({1}). Thus, we only use mex operation for each single 0.

The answer is sum(S) add the number of 0 in S.
######################################################################### Code ############################################################################
t=int(input())
for _ in range(t):
  n=int(input())
  x=list(map(int, input().split()))
  z=sum(x)
  for i in range(len(x)):
      
      if x[i]==0:
        z=z+1
  print(z)
  


