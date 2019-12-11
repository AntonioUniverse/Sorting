# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
   
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        for j in range(cur_index , len(arr)):
            
            if arr[smallest_index] > arr[j]:
                newsmall = arr[j]
                oldsmall = arr[smallest_index]
                arr[cur_index] = newsmall
                arr[j] = oldsmall





    return(arr)
selection_sort([1,4, 5, 8, 10, 3])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    length = len(arr)
    for i in range( length):

        for j in range(0, length -i -1):
             
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        

    print(arr)
         
      
    return arr

bubble_sort([1,4,3,6,8])
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
