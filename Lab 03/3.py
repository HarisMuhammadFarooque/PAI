def containsDuplicates(nums):
    set1 = set()
    for num in nums:
        if num in set1:
            return True
        else:
            set1.add(num)

    return False

nums = [1, 3, 7,3 ,2 , 8, 6, 0]
nums2 = [1, 3, 7, 10 ,2 , 8, 6, 0]

print(containsDuplicates(nums))
print(containsDuplicates(nums2))
