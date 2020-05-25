# a = [0,1,2,3,4,5,6,7,8,9,10]
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[1:4])
# print(a[1:-2])

# print(sum(a))
# print(sum(a) / 10)
# print(sum(a) / len(a))
# a = [1,2,3,4,5,6,7,8,9]
# 3 -> 1
# 5 -> 2
# 7 -> 3
# 9 -> 4
# n -> (n-1)/2
# print(a[int((len(a)-1) / 2)])
# print(a[len(a) // 2])

# a = [3,4,5,6,7,8,9,10]
# n = len(a)
# i1 = n // 2 - 1
# i2 = n // 2
# m = (a[i1] + a[i2]) / 2
# print(m)

names = ['James','Bod','James']

# cnt = 0
# for i in range (len(names)):
#     print(cnt)
#     print(i)
#     print(names[i])
#     if names[i] == "James":
#         cnt += 1
#     print(cnt)
# print(cnt)

# cnt = 0
# for name in names:
#     # print(name)
#     if name == "Bod":
#         cnt += 1
# print(cnt)

# booleans = [True, False, True, False]

# floats = [1.0, 1.5, 2.0]

a2d = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10]
]
# print(len(a2d))
# print(len(a2d[0]))
# print(a2d[0][0])
# print(a2d[2][3])
# print(a2d[-1][-1])
# print(a2d[0][-1])
# print(a2d[-1][0])

# cnt = 0
# for i in range(len(a2d)):
#     row = a2d[i]
#     # print(row)
#     for j in range(len(row)):
#         # print(row[j])
#         if row[j] == 4:
#             cnt += 1
# print(cnt)

cnt = 0
for row in a2d:
    for e in row:
        if e == 4:
            cnt += 1
print(cnt)

# a = [1, 2, 3]
# print(a)
# a.append(4)
# print(a)
# a.insert(2, 5)
# print(a)
# a.pop()
# print(a)
# a.pop(2)
# print(a)

# a.reverse()
# print(a)
# a.sort()
# print(a)