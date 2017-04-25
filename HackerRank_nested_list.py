

def nested_lst(lst):
    students = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        student = [name, score]
        students.append(student)

    lowest = min(item[1] for item in students)
    next_lowest = min(item[1] for item in students if item[1] != lowest)
    name = [item[0] for item in students if item[1] == next_lowest]

    for item in sorted(name):
        print item


# Input:
# 4
# Prashant
# 32
# Pallavi
# 36
# Dheeraj
# 39
# Shivam
# 40


# Output:
# Pallavi



# Input:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39


# Output:
# Berry
# Harry