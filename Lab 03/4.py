def majorityElement(nums):
    n = len(nums)

    numsFreq = {}
    for num in nums:
        if num in numsFreq:
            numsFreq[num] += 1
        else:
            numsFreq[num] = 1

    for num, count in numsFreq.items():
        if count > n/2:
            return num

    return None

print(majorityElement([3, 3, 4]))        
print(majorityElement([2, 2, 1, 1, 1]))  
print(majorityElement([1, 2, 3]))        