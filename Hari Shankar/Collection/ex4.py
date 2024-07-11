# student={'Name':'hari','age':19,'city':'kkdi'}
# # print(student)
# # print(student['Name'])
# for x in student:
#     print(x)
# for x in student.values():
#     print(x)
# print("--------------")
# for x in student.keys():
#     print(f'{x}-{student[x]}')
# print("---------")
# for x in student.items():
#     print(x)

student={}
for x in range(3):
    student[input("Enter the key:")]=input("Enter the Value:")
print(student)