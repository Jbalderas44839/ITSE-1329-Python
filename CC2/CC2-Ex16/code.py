grades = [98, 79, 85, 75, 93, 63, 82, 90, 82, 84, 74]

highest_so_far = -1

for grades in grades:
    if grades > highest_so_far:
        highest_so_far = grades
print('Highest grade is', highest_so_far)
