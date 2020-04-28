def linear_search(element, some_list):
    answer = None
    for i in range(len(some_list)):
        if some_list[i] == element:
            answer = i
    return answer
