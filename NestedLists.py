def main():
    records = []
    for _ in range(int(input())):
        names = input()
        score = float(input())

        records.append([names,score])
        
    
    
    records_of_scores = [i[1] for i in records]
    

    min_no = min(records_of_scores)
    
    my_set = set(records_of_scores)
    my_set.remove(min_no)
    
    new_min_no = min(my_set)

    target_names = sorted([name for name , score in records if score == new_min_no])
    
    for i in target_names:
        print(i)

if __name__ == "__main__":
    main()
-----------------------------------------------------------------------

def main():
    # 1. Use a descriptive name, avoiding the built-in 'list' keyword
    student_records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_records.append([name, score])
        
    # Extract unique scores using a set comprehension
    unique_scores = {score for name, score in student_records}
    
    # 2. Handle the edge case where a second score doesn't exist
    if len(unique_scores) < 2:
        print("Not enough unique scores to evaluate.")
        return
        
    # 3. Find the target score (assuming Second Lowest)
    unique_scores.remove(min(unique_scores))
    target_score = min(unique_scores) 
    
    # Target second highest instead? Swap min() for max() above.

    # Extract names that match the target score and sort them alphabetically
    target_names = sorted([name for name, score in student_records if score == target_score])

    # 4. Print names line by line as expected by most automated graders
    for name in target_names:
        print(name)

if __name__ == '__main__':
    main()
