student = 5 #öğreci sayısını tutan değişkenim.
note_number = 3
name_info = 2
grades = [[0 for i in range(note_number)] for j in range(student)]
name = [[0 for i in range(name_info)] for j in range(student)]

for i in range(student):
    for j in range(note_number):
        try:
            grades[i][j] = int(input(f"Enter {i+1}. student's grade information:"))
        except:
            print("Please enter notes as numbers.")
            quit()

    for k in range(name_info):
            name[i][k] = (input(f"Enter {i+1}. student's name of information:"))

info = dict()
max_note = 0

for i in range(student):
    note = (grades[i][0] + grades[i][1] + grades[i][2]) / 3
    name_surname = (name[i][0], name[i][1])
    info[(name_surname)] = note
    if max_note < note:
        max_note = note
        max_student = (name[i][0], name[i][1])

print("Information:", info)
ranking = sorted(info.values())
print("Ranking:", ranking)
print("Congratulations:", max_student)
