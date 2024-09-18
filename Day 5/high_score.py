# Finding the High Score
student_scores = [150,12,41,64,29,34,182, 199, 201, 20, 8, 19, 141]

bigger = 0
for score in student_scores:
    if bigger < score:
        bigger = score
print(bigger)