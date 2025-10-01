----------------------------------------------------------------------------- In the Dream ---------------------------------------------------------------------------------------
-------------------------------------------------------------------------time limit per test1 second-----------------------------------------------------------------------------
-----------------------------------------------------------------------memory limit per test256 megabytes-------------------------------------------------------------------------------
Two football teams, the RiOI team and the KDOI team, are about to have a football match. A football match consists of two halves — the first half and the second half. At the beginning of the match, both teams have a score of 0.

As a fan of both teams, Aquawave knows that the two teams have similar levels, so neither team will score three consecutive goals in the same half.
Aquawave had a dream the night before the match, in which:
The score at the end of the first half was a:b, where a
 is the score of the RiOI team, and b
 is the score of the KDOI team;
And, the score at the end of the second half was c:d
, where c is the score of the RiOI team, and d is the score of the KDOI team.
You have to determine whether Aquawave's dream can come true according to the above information.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤1000). The description of the test cases follows.

The only line of each test case contains four integers a, b, c, and d (0≤a≤c≤100, 0≤b≤d≤100) — the score at the end of the first half and the score at the end of the second half.

Output
For each test case, print "YES" if Aquawave's dream can come true. Otherwise, print "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
Input
11
1 4 1 4
4 1 4 1
1 4 2 5
0 100 0 100
1 4 2 9
3 1 13 5
8 11 17 36
19 41 30 50
20 38 30 60
0 0 0 0
100 100 100 100
Output
YES
YES
YES
NO
NO
YES
NO
NO
YES
YES
YES
Note
We will use R
 to represent the RiOI team's goal, and K
 to represent the KDOI team's goal.

In the first test case, the only goal order is:
First half: KKRKK. At the end of the first half, the score is 1:4;
Second half: No goals. At the end of the second half, the score is still 1:4.
In the second test case, the only goal order is:
First half: RRKRR. At the end of the first half, the score is 4:1;
Second half: No goals. At the end of the second half, the score is still 4:1.
In the third test case, one possible goal order is:
First half: KKRKK. At the end of the first half, the score is 1:4;
Second half: KR. At the end of the second half, the score is 2:5.
In the fourth test case, at the end of the first half, the KDOI team has scored 100 goals, while the RiOI team did not score any goals. Thus, in Aquawave's dream, the KDOI team scored 100 consecutive goals in the first half, which is impossible.

###################################################################################### Solution ################################################################################################
And, the score at the end of the second half was c:d which mwans it is total so second half is (c-a),(d-b).
Step 1: Think about spacing
Suppose RiOI scored x goals.
We must place these x Rs in the half.
Now we ask: how many Ks can we squeeze in without making KKK?

Step 2: Where can we place Ks?
Between each pair of Rs, we can place at most 2 Ks (because 3 in a row is not allowed).
So if there are x Rs:
Gaps between them = x - 1.
Each gap can hold at most 2 Ks.
That gives us 2 * (x - 1) Ks inside.
We can also place Ks before the first R and after the last R.
At most 2 at the start.
At most 2 at the end.
Step 4: Add them up

Total max Ks = inside gaps + edges =
2 * (x - 1) + 4
= 2x + 2
That’s the formula.
So:
If RiOI scored x, then KDOI can score at most 2x + 2.
Symmetrically, if KDOI scored y, then RiOI can score at most 2y + 2.
max(x, y) ≤ 2 * min(x, y) + 2
so yes it is possibe
############################################################################# Code ###############################################################################################
t=int(input())
for _ in range(t):
   a,b,c,d=map(int, input().split())
   if max(a,b)>2*min(a,b)+2:
      print("NO")
   elif max((c-a),(d-b))>2*min((c-a),(d-b))+2:
      print("NO")
   else:
      print("YES")
---------------------------------------------------------------Problem Tag--------------------------------------------------------
greedy,math,800











