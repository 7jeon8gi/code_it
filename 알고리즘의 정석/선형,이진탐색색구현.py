def linear_search(element, some_list):
    answer = None
    for i in range(len(some_list)):
        if some_list[i] == element:
            answer = i
    return answer

def binary_search(element, some_list):
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
