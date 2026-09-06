def topKFrequent(nums, k):
    numsFreq = {}
    for num in nums:
        if num in numsFreq:
            numsFreq[num] += 1
        else:
            numsFreq[num] = 1

    ranked = sorted(numsFreq.items(), key = lambda x : x[1], reverse=True)
    return ranked[: k]

print(topKFrequent([1, 5, 4 , 7, 2, 5, 4 , 2 , 5, 6], 4))

