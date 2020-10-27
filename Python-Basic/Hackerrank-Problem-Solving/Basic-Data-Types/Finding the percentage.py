if __name__ == '__main__':
    n = int(input())
    z=0.0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        for j in range(3):
            scores = list(map(float, line))
            z=z+scores[j]
            #print('z=',z)
        student_marks[name] =(z/3.0)
        z=0
        #print(student_marks[name])
    query_name = input()
    print("%.2f" % student_marks[query_name])
