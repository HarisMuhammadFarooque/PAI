def isAnagram(s, t):
    s = s.lower()
    t = t.lower()

    if len(s) != len(t):
        return False

    freqS = {}
    for ch in s:
        if ch in freqS:
            freqS[ch] += 1
        else:
            freqS[ch] = 1

    freqT = {}
    for ch in t:
        if ch in freqT:
            freqT[ch] += 1
        else:
            freqT[ch] = 1

    return freqS == freqT


print(isAnagram("listen", "silent"))  
print(isAnagram("hello", "world"))   