# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

# Assume that:

# N is an integer within the range [1..2,147,483,647].
# Complexity:

# expected worst-case time complexity is O(log(N));
# expected worst-case space complexity is O(1).

def solution(N):
    # write your code in Python 3.6
    
    binaryRepresent = list()
    while N >= 1:
        binaryRepresent.append(N % 2)
        N //= 2
    # !!!一开始输出的是反向的，比如6则是[0,1,1]，直接用自带函数就可以，复杂度还是 O(logN)
    binaryRepresent.reverse()
    result = 0
    temp = 0
    for i in range(len(binaryRepresent)):
        if binaryRepresent[i] == 1:
        	# 判断要放在上面，防止末尾是零这种情况
        	if temp > result:
        		result = temp
        	temp = 0
        else:
            temp += 1
    return result