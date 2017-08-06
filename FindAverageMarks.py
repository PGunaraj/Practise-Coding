def averageMarksOfAStudent():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    scores = student_marks[query_name]
    SumOfScores = sum(scores)
    l = len(student_marks[query_name])
    Average = SumOfScores / l
    print("%.2f" % Average)

    # Instead of doing the above 5 lines, You can do the below 1 line code
    print("%.2f"%(sum(student_marks[query_name])/len(student_marks[query_name])))

averageMarksOfAStudent()