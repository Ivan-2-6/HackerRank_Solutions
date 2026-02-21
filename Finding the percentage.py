if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        query_scores = student_marks[query_name]
        average = sum(query_scores)/ len(query_scores)
        
        print(f"{average:.2f}")
