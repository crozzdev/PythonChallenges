def find_target(arr:list[int], target:int) -> list[int] | str:
    length = len(arr)

    for i in range(length-1):
        for j in range(i+1, length):
            if arr[i] + arr[j] == target:
                return [i, j]

    return "Target not found"