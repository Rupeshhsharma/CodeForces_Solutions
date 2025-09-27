############################################################################ time limit per test :2 seconds ################################################################################
########################################################################## memory limit per test :256 megabytes ##############################################################################
There is a 2D-coordinate plane that ranges from (0,0) to (x,y). You are located at (0,0) and want to head to (x,y).

However, there are n horizontal lasers, with the i-th laser continuously spanning (0,ai) to (x,ai). Additionally, there are also m vertical lasers, with the i-th laser continuously spanning (bi,0) to (bi,y).

You may move in any direction to reach (x,y), but your movement must be a continuous curve that lies inside the plane. Every time you cross a vertical or a horizontal laser, it counts as one crossing. Particularly, if you pass through an intersection point between two lasers, it counts as two crossings.

For example, if x=y=2
, n=m=1
, a=[1]
, b=[1]
What is the minimum number of crossings necessary to reach (x,y)?
Output
For each test case, output the minimum number of crossings necessary to reach (x,y).
Example

Input
2
1 1 2 2
1
1
2 1 100000 100000
42 58
32

Output
2
3

###################################################################### Solution #######################################################################################
Since our path is continuous, whatever route we take will always pass through all vertical and horizontal lasers in the region from (0,0)
 to (x,y)
 since our movement is bounded inside the region. Therefore, the answer is simply n+m.

#################################################### CODE ##################################################################################3
t=int(input())
for _ in range(t):
   n,m,x,y= map(int, input().split())
   a=list(map(int, input().split()))
   b=list(map(int, input().split()))
   print(n+m)
