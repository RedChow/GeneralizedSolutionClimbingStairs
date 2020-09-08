<h1>LeetCode Problem: Climbing Stairs</h1>
<p>
The problem description states that you are climbing a stair case. It takes <i>n</i> steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
(The problem can be found at <a href="https://leetcode.com/problems/climbing-stairs/">https://leetcode.com/problems/climbing-stairs/</a>.)
</p>

<p>
I found this problem really interesting, because the heart of the problem is combinatorics.
There are ways of solving this problem without using combinatorial algorithms, but combinatorics can solve the bigger more general problem of
climbing stairs using any length of steps less than <i>n</i>.
</p>
<h2>Solution for Original Problem</h2>
<p>
We first make the observation that we are permuting a multiset of <i>n</i> elements where the number of 1s and 2s are the multiplicities of the objects 1 and 2.
For example, if <i>n</i>=3, and the number of 1s and 2s are 1 and 1, then we want the number of permutations of arranging 1 and 2.
Since we have two distinct objects, 1 and 2, and each object has multiplicity 1, we have:
  <img src="https://raw.githubusercontent.com/RedChow/GeneralizedSolutionClimbingStairs/images/first_eqn.gif" />
  </p>
![2 choose 1, 1](/images/first_eqn.gif?raw=true "2 choose 1,1")
![Alt text](/screenshots/getting_data.png?raw=true "Getting Data")
