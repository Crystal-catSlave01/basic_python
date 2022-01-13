import copy

print(dir(copy))

data = [[1,2], [3,4]]
copy_data = copy.deepcopy(data)
print(id(data[0][1]))
print(id(copy_data[0][1]))
copy_data[0][1] = 5
print(id(data[0][1]))
print(id(copy_data[0][1]))

print(data)
print(copy_data)