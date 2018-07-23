# Kadanes
The Kadanes algorithm is used to solve the Maximum subarray problem which asks to find the contigous subarray that has a maximal sum.
Kadanes algorithm uses a dynamic programming technique to calculate its answer.
If for position i in the array we have the sum of the maximum subarray stored in B[i] then can we can find the sum of the subarray at position i + 1.
Either this  i + 1 position contains B[i] as a prefix or it doesn't.
We therefore take B[i] to be the max of A[i] or A[i] + B[i - 1]. 
The runtime of this algorithm is O(n) because it iterates over the list of n elements one time.