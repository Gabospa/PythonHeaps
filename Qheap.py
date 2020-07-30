#Fuction for build heap, from  node [len(arr)//2]


#Function to apply min-heap property 
def sink(arr, i):
    #compare i to left and right and swap if child is min
    flag_swap = 0
    while left(i) < len(arr):
        if arr[left(i)] < i:
            arr[left(i)], arr[i] = arr[i], arr[left(i)]
            flag_swap = 1
        if right(i) < len(arr) and arr[right(i)] < i:
            arr[right(i)], arr[i] = arr[i], arr[right(i)]
            flag_swap = 2
        #if swap happened, swap 
        if flag_swap == 1:
            sink(arr, left(i, arr))
        if flag_swap == 2:
                sink(arr,right(i, arr))

#Find left index of i, if i is a leaf return i         
def left(i):
    return (2*i + 1)

#Find right index of i
def right(i, arr):
    return (2*i + 2)

#Find parent of i
def parent(i):
    return (i-1)//2

#Function to insert new node
def insert(arr, v):
    arr.append(v)
    i = len(arr) - 1
    while i > 0 and arr[parent(i)] > v:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)
    
#Fuction to delete indicated value
def delete(arr, v):
    
    for i in range(len(arr)-1):
        if arr[i] == v:
            arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
            arr.pop()
            sink(arr, i)

#Function to retun min value of heap
def find_min(arr):
    print (arr[0])

if __name__ == '__main__':
    arr = []
    number_queries = int(input())
    for i in range (number_queries):
        query = list(map(int,input().strip().split()))
        if query[0] == 1:
            insert(arr, query[1])
        elif query[0] == 2:
            delete(arr, query[1])
        else:
            find_min(arr)