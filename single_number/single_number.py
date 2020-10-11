'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # loop through the numbers in the array
    # add first number in the array to new array
    # if index is already in the array array.delete index

    newList = []
    

    for num in arr:
        if num in newList:
            newList.remove(num)
        else:
            newList.append(num)
    

    return int(newList[0])


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")