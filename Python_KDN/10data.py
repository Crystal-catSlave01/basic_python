data = [1,2,3]
copy_data = data

print(id(data[1]))
print(id(copy_data[1]))
# print(copy_data)
copy_data[1] = 5
print(id(data[1]))
print(id(copy_data[1]))


# print(copy_data)

# print(data)