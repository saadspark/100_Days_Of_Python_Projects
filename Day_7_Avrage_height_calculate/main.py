# Input a Python list of student heights
student_heights = input().split()
count = 0;
total_hight = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_hight += student_heights[n]
  count += 1

print(f'total height = {total_hight}')
print(f'number of students = {count}')
Avg = round(total_hight/count)
print(f'average height = {Avg}')