grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_list = list(students)
stud_list.sort()
aver_grade_0 = sum(grades[0]) / len(grades[0])
aver_grade_1 = sum(grades[1]) / len(grades[1])
aver_grade_2 = sum(grades[2]) / len(grades[2])
aver_grade_3 = sum(grades[3]) / len(grades[3])
aver_grade_4 = sum(grades[4]) / len(grades[4])
report_card = {stud_list[0]: aver_grade_0, stud_list[1]: aver_grade_1, stud_list[2]: aver_grade_2, stud_list[3]: round(aver_grade_3, 2), stud_list[4]: aver_grade_4}
print(report_card)
