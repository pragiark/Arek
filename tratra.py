def sum_of_cubes(nums):

    total = 0
    for i in nums:
        total = total +  i**3
        print(total)
    return total

x = sum_of_cubes([1, 5, 9])
print(x)