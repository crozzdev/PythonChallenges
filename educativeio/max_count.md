# Maximum Number of Integers to Choose from a Range I

## Instructions

Given an integer array banned and two integers n and max_sum, determine the maximum number of integers you can choose while adhering to the following rules:

1. The selected integers must fall within the range $[1,n]$

2. Each integer can be chosen at most once.

3. No selected integer can be present in the banned array.

4. The sum of the selected integers must not exceed max_sum.

Your goal is to return the maximum count of integers that can be chosen while satisfying all the above constraints.

Constraints:

1. $1≤banned.length ≤10^3$
2. $1=<banned[i],n<=10^3$
3. $1=<max\_sum<=10^6$
