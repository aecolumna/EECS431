
studentScores = [943, 234, 654, 235, 654]

schoolSeats = [5, 3, 4, 6, 4]

studentPreferences = [[4, 2, 3], [1, 2, 4], [0, 1, 2] , [3, 4, 5], [4, 3,0]]

def f(studentScores, schoolSeats, studentPreferences):
    students = []

    for i in range(len(studentScores)):
        students.append([studentScores[i], studentPreferences[i]])

    # sort according to scores
    students.sort(reverse=True, key=lambda student : student[0] )

    studentsPlaced = 0

    for student in students:
        for school in student[1]:
            if schoolSeats[school] > 0:
                schoolSeats[school] -= 1
                studentsPlaced += 1
                break

    remainingSeats = sum(schoolSeats)

    return [studentsPlaced, remainingSeats]










