def solution(arr):
    result_list = []
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            result_list.append(arr[i-1])
    result_list.append(arr[len(arr)-1])
    return result_list
