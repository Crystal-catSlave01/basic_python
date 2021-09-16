arr = []
for i in range(10):
    n = int(input())
    arr.append(n%42)
arr = set(arr)
print(len(arr))


# n = []
# cnt = 0

# for i in range(10):
#     n.append(int(input()))
#     if n[i] % 42 == 0:
#         pass
#     else:
#         cnt += 1

# print(cnt)
# print(len(n))