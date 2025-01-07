import math
from collections import defaultdict

# Store course data
courses = {}

# Store student data
students = defaultdict(lambda: defaultdict(dict))

# Read input data
def process_input():
    m = int(input())  # Number of courses
    for _ in range(m):
        course_info = input().split()
        course_code, term_code, student_count = course_info[0], course_info[1], int(course_info[2])
        courses[course_code] = {
            'term_code': term_code,
            'students': []
        }
        for _ in range(student_count):
            student_data = input().split()
            student_id = student_data[0]
            if len(student_data) == 3:
                term_score, exam_score = map(int, student_data[1:])
                score = math.ceil(term_score * 0.7 + exam_score * 0.3)
            elif student_data[1].lower() == 'w':
                score = 'w'
            else:
                score = int(student_data[1])
            courses[course_code]['students'].append((student_id, score))

            # Add to student dictionary
            year = student_id[:3]
            dept_code = student_id[3:6]
            students[dept_code][year][student_id] = students[dept_code][year].get(student_id, [])
            students[dept_code][year][student_id].append((course_code, score))

    # Course to search
    search_course = input()
    return search_course

# Calculate rank percentage
def calculate_rank_percentage(ranks):
    total = len(ranks)
    percentages = []
    for i, rank in enumerate(ranks, 1):
        percentage = math.ceil((i / total) * 100)
        percentages.append(f"{percentage}%")
    return percentages

# Process and output
search_course = process_input()

# Output for part 1
part1_output = []
for dept_code in sorted(students):
    for year in sorted(students[dept_code]):
        for term_code in sorted({courses[course]['term_code'] for course in courses}):
            part1_output.append(f"{dept_code} {year} {term_code}")

            # Collect students for this term
            yearly_students = [
                (student, sum(course_score for course_code, course_score in data if course_score != 'w'))
                for student, data in students[dept_code][year].items()
            ]
            yearly_students = sorted(yearly_students, key=lambda x: (-x[1], x[0]))

            # Get top 3
            top_students = yearly_students[:3]

            for i, (student_id, avg_score) in enumerate(top_students, 1):
                rank_percentages = calculate_rank_percentage(yearly_students)
                dropped_courses = sum(1 for course_code, score in students[dept_code][year][student_id] if score == 'w')
                total_courses = len(students[dept_code][year][student_id])
                drop_percentage = math.floor((dropped_courses / total_courses) * 100)

                part1_output.append(f"{student_id} {avg_score} {rank_percentages[i - 1]} {drop_percentage}%")

print('\n'.join(part1_output))

# Further processing for parts 2 and 3 (not shown here, but can be added similarly)
