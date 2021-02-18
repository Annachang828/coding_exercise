# 解法一: 若有兩個以上的第一高分則會出現bug

# def second_highest(students):
#     grades = [s[1] for s in students]
#     grades = sorted(grades, reverse=True)
#     second = grades[1]
#     second_high_students = [s[0] for s in students if s[1] == second]
#     for student in second_high_students:
#         print(student)

# second_highest([['Jerry', 88], ['Justine', 84], ['Tom', 90], ['Akriti', 94], ['Harsh', 94]])


# 解法二

def second_highest(students): 
    scores = set([s[1] for s in students]) # set是數學的"集合"，把清單變成集合就是只留下不重複的項目，所以最高分，第二高分，都會只有一個了，這樣就可以很確定scores[1]會是第二高分。
    scores = sorted(scores, reverse=True)
    highest_score = scores[0]
    second_highest = [s[0] for s in students if s[1] == scores[1]]
    for students in second_highest:
      print(students)

second_highest([['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90], ['Amanda', 92]])
