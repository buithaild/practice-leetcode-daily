# hash =  {2: 0, 11: 1}
# print(">>>: ", hash[2])
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

ret = []

# print(matrix[0])
# if matrix and matrix[0]:
#     for row in matrix:
#         ret.append(row.pop())

if matrix and matrix[0]:
    for row in matrix[::-1]:
        ret.append(row.pop(0))

print(ret)