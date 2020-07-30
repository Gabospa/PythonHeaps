#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    heapq.heapify(A)
    ops = 0
    while len(A) > 1 and A[0] < k:
        c1, c2 = heapq.heappop(A), heapq.heappop(A)
        heapq.heappush(A, c1 + (2*c2))
        ops += 1
    if A[0] < k:
        return -1
    return ops
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()