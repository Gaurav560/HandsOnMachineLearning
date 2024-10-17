# marks_obtained_in_subject_1 = int(input("Enter the marks obtained in subject 1: "))
#
# if marks_obtained_in_subject_1 >= 33:
#     marks_obtained_in_subject_2 = int(input("Enter the marks obtained in subject 2: "))
#
#     if marks_obtained_in_subject_2 >= 33:
#         marks_obtained_in_subject_3 = int(input("Enter the marks obtained in subject 3: "))
#
#         if marks_obtained_in_subject_3 >= 33:
#             total_marks = marks_obtained_in_subject_1 + marks_obtained_in_subject_2 + marks_obtained_in_subject_3
#
#             if total_marks > 120:  # This checks if total marks are more than 40%
#                 print("You have passed the exam. Your total marks are greater than 40%.")
#             else:
#                 print("You have not passed the exam as your total marks are less than 40%.")
#         else:
#             print("You have not passed the exam as marks in subject 3 are less than 33.")
#     else:
#         print("You have not passed the exam as marks in subject 2 are less than 33.")
# else:
#     print("You have not passed the exam as marks in subject 1 are less than 33.")


# another way
marks_in_science = int(input("Enter the number of marks in science: "))
marks_in_english = int(input("Enter the number of marks in english: "))
marks_in_maths = int(input("Enter the number of marks in maths: "))

total_percentage = (100 * (marks_in_maths + marks_in_science+ marks_in_english)) / 300
print(total_percentage)
if total_percentage >= 40 and marks_in_maths >= 33 and marks_in_science >= 33 and marks_in_english >= 33 and marks_in_maths >= 33:
    print("you have passed the examination!")
else:
    print("you have failed the examination!")
