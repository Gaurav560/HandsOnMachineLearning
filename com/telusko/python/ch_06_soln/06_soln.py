#program to calculate the grade of a student from his marks from the following scheme
science=80
maths=94
sanskrit=64
hindi=89
english=92
computer=88
total_percentage=(100*(science+computer+maths+sanskrit+hindi+english))/600
print(total_percentage)
if total_percentage>=90:
    print("Ex")
elif 90 > total_percentage >= 80:
    print("A")
elif 80 > total_percentage >= 70:
    print("B")
elif 70 > total_percentage >= 60:
    print("C")
elif 60 > total_percentage >= 50:
    print("D")
else:
    print("F")