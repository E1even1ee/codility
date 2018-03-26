# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

def solution(A):
    # write your code in Python 3.6
    # 看一下别人的解法
    temp = max(A)
    if temp <= 0:
    	return 1
    # 因为可能传进来[1,2,3]所以后面是max+2，都可以cover到
    check = {i:False for i in range(1, temp + 2)}
    for i in A:
    	check[i] = True
    for i in range(1, temp + 2):
    	if check[i] is True:
    		continue
    	else:
    		return i