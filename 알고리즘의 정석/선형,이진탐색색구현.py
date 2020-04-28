def linear_search(element, some_list):
    """선형 탐색 구현"""
    answer = None
    for i in range(len(some_list)):
        if some_list[i] == element:
            answer = i
    return answer

def binary_search(element, some_list):
    """이진 탐색 구현"""
    lower = 0
    upper = len(some_list)-1
    
    while lower <= upper:
        mid = (lower + upper)//2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] < element:
            lower = mid + 1
        elif some_list[mid] > element:
            upper = mid -1
        mid = (lower + upper)//2
        
    return None
print(binary_search(2, [2, 3, 5, 7, 11]))

num_list = [33, 3, 5, 9, 0, 4, 44,500,2,21,222,55000000,1]

def selection_sort(some_list):
    """선택 정렬 구현"""
    for i in range(len(some_list)):
        min_val = some_list[i]

        for j in range(i,len(some_list)):
            if min_val > some_list[j]:
                min_val = some_list[j]
                min_index = j

        some_list[i], some_list[min_index] = min_val, some_list[i]

    return some_list
print(selection_sort(num_list))

def insertion_sort(some_list):
    """ 삽입 정렬 구현"""
    for i in range(len(some_list)):
        val = some_list[i]
        
        for j in range(i-1,-1,-1):
            if val < some_list[j]:
                some_list[j+1], some_list[j] = some_list[j], some_list[j+1]
    return some_list

insertion_sort([6,2,3,10,1])
