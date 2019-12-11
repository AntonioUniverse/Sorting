# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-Do
    sorted_list = []
    indexA = indexB = 0
    if elements == 0:
        return 

    while len(sorted_list) < elements:
    
     if arrA[indexA] <= arrB[indexB]:
           sorted_list.append(arrA[indexA])
       
           indexA += 1
     else:
           sorted_list.append(arrB[indexB])
       
           indexB += 1
     if indexB == len(arrB):
            # Reached the end of right
            # Append the remainder of left and break
            sorted_list += arrA[indexA:]
            break
            
     elif indexA == len(arrA):
            # Reached the end of left
            # Append the remainder of right and break
            sorted_list += arrB[indexB:]
            break
            
     
    return sorted_list


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    arr_len = len(arr)
    #find my mid point 
    mid = len(arr)//2 
    #split my array at each midpoint 
    left = arr[mid:]
    right  = arr[:mid]
    
    if arr_len <= 1: 
        # returns the arr if length is less than or equal to one 
        return arr
    else:
        # merge takes in array and combines them
        #merge_sort is called to split the array again
        return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
