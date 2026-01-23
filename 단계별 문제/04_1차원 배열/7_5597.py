# sample = list(range(1,31))
# students = []
# absent = []
# for _ in range(28):
#     students.append(int(input()))

# print(min(list(set(sample)-set(students))))
# print(max(list(set(sample)-set(students))))      

# 다른 풀이
sample = set(range(1,31))
students = set()

for _ in range(28):
    students.add(int(input()))

answer = sorted(sample-students)
print(answer[0])
print(answer[1])