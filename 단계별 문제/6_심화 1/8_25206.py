import sys

grade_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0']
subject_num = 0
grade_sum = 0

for _ in range(20):
    subject, num, grade = sys.stdin.readline().split()
    
    if grade == 'P':
        pass
    elif grade == 'F':
        subject_num += float(num)
    else:
        grade_sum += float(num) * (grade_list.index(grade) * -0.5 + 4.5)
        subject_num += float(num)

print(f'{(grade_sum / subject_num):.6f}')