import sys
print ("Please enter a, b, c, d, e or f as letter grade. Do not enter letter grades for general study courses")

#ask user to enter letter grade for first course
letter_grade = input("Please enter your letter grade for the following courses respectively, cbg211, btn211, chm213, mic211, fre135, zly211.")

if (letter_grade. lower() != "a", "b", "c", "d", "e", "f" ):
    def split (data):
        return [char for char in data]
    word = split(letter_grade)
    
#assign grade points to letter grades
def grade_point (data):
 if data == "a":
  return 5
 elif data == "b":
  return 4
 elif data == "c":
  return 3
 elif data == "d":
  return 2
 elif data == "e":
  return 1
 elif data == "f":
  return 0

#assign number of units to each course
cbg211 = 3
btn211 = 3
chm213 = 3
mic211 = 3
fre135 = 2
zly211 = 3

#assign value for total course units
total_units = cbg211 + btn211 + chm213 + mic211 + fre135 + zly211

#multiply the grade point assigned to the letter grade obtained in each course
#by the number of units assigned to the course to arrive at the weighted
#score for each course
weighted_score_cbg = grade_point(word[0])* cbg211
weighted_score_btn = grade_point(word[1])* btn211
weighted_score_chm = grade_point(word[2])* chm213
weighted_score_mic = grade_point(word[3])* mic211
weighted_score_fre = grade_point(word[4])* fre135
weighted_score_zly = grade_point(word[5])* zly211

#add together the weighted scores for all the courses
total_weighted_score = (weighted_score_cbg) + (weighted_score_btn) + (weighted_score_chm) + (weighted_score_mic) + (weighted_score_fre) + (weighted_score_zly)
print (total_weighted_score)
#divide theweighted score by the total number of units
gpa = total_weighted_score/total_units
gpa = round(gpa, 2)
print (gpa)
if (gpa > 3):
 print ("Good job! Your GPA is in good standing")
elif (gpa < 2):
 print (" Uh oh, your GPA is under 2.0")

#exit the code
sys.exit()
