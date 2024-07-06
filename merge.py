#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

def merge(nums: List[int]) -> List[int]:
    """
    Given an unsorted list of integers `nums`, repetitively merge all pairs of like integers
    `n, n` into `n + 1` until no more merges are possible, meaning all integers
    in the list are unique. The returned list may be in any order.
    
    Examples:
        
    [2, 2] -> [3]
    
    [2, 2, 3, 3] -> [3, 4] or [4, 3]
    
    [5, 5, 5] -> [6, 5] or [5, 6]
    
    [5, 5, 5, 5] -> [6, 6] -> [7]
    
    [3, 2, 2] -> [3, 3] -> [4]

    """
    
    numSet = set()
    for num in nums:
        while num in numSet:
            numSet.remove(num)
            num += 1
        else:
            numSet.add(num)
        
    return list(numSet)
            
        
    
if __name__ == "__main__":
    tests = (
        ([], []),
        ([1], [1]),
        ([2, 2], [3]),
        ([2, 2, 3, 3], [3, 4]),
        ([5, 5, 5], [6, 5]),
        ([5, 5, 5, 5], [7]),
        ([3, 2, 2], [4]),
        ([3, 2, 2, 3, 3], [5]),
        ([5, 5, 4, 2, 2, 4, 3, 7], [4, 5, 6, 7])
    )
    
    for test, answer in tests:
        assert set(merge(test)) == set(answer)
    print("All tests passed")
