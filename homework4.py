"""
SEARCH IN MATRIX
--------
"""
positiion = 0
def search_in_matrix(matrix, target):
    if len(matrix) == 0:
        return -1

    for line_index,line in enumerate(matrix):
        lower_bound=0
        upper_bound=len(line)-1

        while lower_bound < upper_bound:
            mid = (lower_bound + upper_bound) // 2
            # print(f'is {target} on {line_index} at position{mid}?')

            if line[mid] == target:
                globals()['position'] = mid
                # print('yes')
                return [line_index,mid]
            else:
                if line[mid] < target:
                    if lower_bound == mid:
                        lower_bound = upper_bound
                        if line[upper_bound] == target:
                            # print('yes')
                            return [line_index,upper_bound]
                    else:
                        lower_bound = mid
                else:
                    upper_bound = mid
                # print('no')

target = 44
matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

found_pos = search_in_matrix(matrix,target)
if found_pos:
    print('Found in:', found_pos)
else:
    print('Found in:',[-1,-1])









