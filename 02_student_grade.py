
test1 = float(input("Enter score for test 1: "))
test2 = float(input("Enter score for test 2: "))
test3 = float(input("Enter score for test 3: "))

average = (test1+test2+test3)/3

if average >= 90:
    grade = "A"
elif average >= 80 and average < 90 :
    grade = "B"
elif average >= 70 and average <80:
    grade = "C"
elif average >= 60 and average <70:
    grade = "D"
elif average <60:
    grade = "E"

print(f"The average score:{average}")
print(f"The letter grade: {grade}")