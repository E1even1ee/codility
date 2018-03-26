# You are given N counters, initially set to 0, and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:

#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.

# Write a function:

# def solution(N, A)

# that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of integers representing the values of the counters.

# The sequence should be returned as:

# a structure Results (in C), or
# a vector of integers (in C++), or
# a record Results (in Pascal), or
# an array of integers (in any other programming language).
# For example, given:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

# Assume that:

# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].
# Complexity:

# expected worst-case time complexity is O(N+M);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

# 别人的答案
# 核心思路就是不要每一次循环遇到MAX的时候都[MAX]*N，事实证明这个操作为O(N)所以就会出现部分O(M*N)的情况，而是把这些操作都统一挪到最后进行
# 而这样就要知道，小于最后统一最大值的那些就要直接赋值最大
# 分为两类，统一赋值前加的（会一起变），后加的（要先赋值再加）
def solution(N, A):
    counter = [0]*(N+1)
    current_counter_max = 0
    total_max = 0
    for command in A:
        if 1 <= command <= N:
            # 所以加了这一步，意思就是你只要小于统一赋值，先统一再加，因为这个位置之后由于它比较大就不需要再加了
            if counter[command] < current_counter_max:
                counter[command] = current_counter_max
            counter[command] += 1
            if total_max < counter[command]:
                total_max = counter[command]
        else:
            current_counter_max = total_max
    for i in range(len(counter)):
        if counter[i] < current_counter_max:
            counter[i] = current_counter_max
    return counter[1:]