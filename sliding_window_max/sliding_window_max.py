'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from collections import deque
def sliding_window_max(nums, k):


    max_vals = []

    q = deque()

    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]:
            q.pop()

        q.append(n)

        window_range = i - k + 1 

        if window_range >= 0:
            max_vals.append(q[0])

            if nums[window_range] == q[0]:
                q.popleft()
    return max_vals

    
    
    # max_values = []

    # n = 0

    # if len(nums) <= k:
    #     return max(nums)

    # while n <= len(nums) -k:
    #     window = nums[n:k + n]
    #     n +=1
    #     max_values.append(sliding_window_max(window,k))

    # return max_values



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
