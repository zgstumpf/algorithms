from typing import List, Union

def countSegments(inputList: List[Union[int, None]]) -> int:
    """
    Given an `inputList` where each element is either an `int` or `None`, return
    the number of segments. A segment is a group of ints separated by Nones or cut off by
    the start or end of the list.
    
    Examples:
        
    [None, 1, 2, None, 3] -> 2 (1, 2 form the first segment, the final 3 forms 
    the second segment.)
    
    [1] -> 1 (No elements are next to the 1 because before 1 is the start of the list
    and after 1 is the end of the list.)
    
    [1, None] -> 1
    
    [None, 3, None] -> 1
    
    [2, 3] -> 1
    
    [2, 3, None, 4, 1] -> 2
    
    [None, None, None] -> 0
    
    [2, None, 3] -> 2
    
    [2, 3, 2, None, 2, 1, 2, None, 4, 6] -> 3
    """
    
    numSegments = 0
    isSegment = False
    
    for i in range(len(inputList)):
        if not isSegment and inputList[i] is not None:
            # if last position is not None, it is guaranteed end of a segment
            if i == len(inputList) - 1: 
                return numSegments + 1
            isSegment = True
        elif isSegment and (inputList[i] is None or i == len(inputList) - 1):
            isSegment = False
            numSegments += 1
            
    return numSegments
    

if __name__ == "__main__":
    tests = (
        ([None, 1, 2, None, 3], 2),
        ([1], 1),
        ([1, None], 1),
        ([None, 3, None], 1),
        ([2, 3], 1),
        ([2, 3, None, 4, 1], 2),
        ([None, None, None], 0),
        ([2, None, 3], 2),
        ([2, 3, 2, None, 2, 1, 2, None, 4, 6], 3),
    )
    
    for test, answer in tests:
        assert countSegments(test) == answer
    print("All tests passed")
