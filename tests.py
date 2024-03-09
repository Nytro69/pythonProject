def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            if nums[j] + nums[i] == target:
                return [j, i]
    print("No solution")

print(twoSum([2, 7, 11, 15], 13))