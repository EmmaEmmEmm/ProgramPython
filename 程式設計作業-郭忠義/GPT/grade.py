def parse_input():
    M = int(input())  # 課程數
    courses = {}

    for _ in range(M):
        course_info = input().split()
        course_code, term_code, student_count = course_info[:3]
        student_count = int(student_count)
        students = []

        for _ in range(student_count):
            student_data = input().split()
            student_id = student_data[0]
            if len(student_data) == 3:  # 有會考成績
                term_score = int(student_data[1]) if student_data[1] != 'w' else 'w'
                exam_score = int(student_data[2]) if student_data[1] != 'w' else 'w'
                score = None if term_score == 'w' else int((term_score * 0.7) + (exam_score * 0.3) + 0.5)
            else:  # 無會考成績
                term_score = int(student_data[1]) if student_data[1] != 'w' else 'w'
                score = None if term_score == 'w' else term_score
            students.append((student_id, term_score, score))

        courses[(course_code, term_code)] = students

    search_course = input()
    return courses, search_course

def calculate_statistics(courses, search_course):
    # 存放統計結果
    department_stats = {}
    course_stats = {}
    search_results = {}

    for (course_code, term_code), students in courses.items():
        year = int(term_code[:3])
        department_data = {}
        valid_scores = []
        
        for student_id, term_score, score in students:
            print(term_code)
            department = student_id[3:6]
            if score is not None:
                valid_scores.append((student_id, score))
                if department not in department_data:
                    department_data[department] = []
                department_data[department].append((student_id, score))

        valid_scores.sort(key=lambda x: (-x[1], x[0]))  # 按成績排序，若成績相同按學號排序

        if course_code == search_course:
            search_results[year] = valid_scores[:2]  # 取前兩名

        highest_score = max(valid_scores, key=lambda x: x[1])[1] if valid_scores else 0
        lowest_score = min(valid_scores, key=lambda x: x[1])[1] if valid_scores else 0
        avg_score = sum(score for _, score in valid_scores) // len(valid_scores) if valid_scores else 0
        withdraw_rate = (len(students) - len(valid_scores)) * 100 // len(students) if students else 0

        course_stats[(course_code, year)] = {
            "highest": highest_score,
            "lowest": lowest_score,
            "average": avg_score,
            "withdraw_rate": withdraw_rate,
            "top_students": valid_scores[:3],
        }

    # 搜尋最多人數的科系編碼
    course_students = {}
    for (course_code, _), students in courses.items():
        for student_id, _, _ in students:
            department = student_id[3:6]
            if course_code not in course_students:
                course_students[course_code] = {}
            if department not in course_students[course_code]:
                course_students[course_code][department] = 0
            course_students[course_code][department] += 1

    max_dept = max(course_students[search_course].items(), key=lambda x: x[1])[0]

    return department_stats, course_stats, search_results, max_dept

def print_results(department_stats, course_stats, search_results, max_dept):
    # 第一部分：學生成績統計
    for department, years in sorted(department_stats.items()):
        for year, data in sorted(years.items()):
            print(department, year)
            for student_id, avg_score, rank_percent, withdraw_percent in data:
                print(student_id, avg_score, rank_percent, withdraw_percent)

    # 第二部分：課程成績統計
    for (course_code, year), stats in sorted(course_stats.items()):
        print(course_code, year)
        print(stats["highest"], stats["average"], stats["lowest"], stats["withdraw_rate"])
        for student_id, score in stats["top_students"]:
            print(student_id, score)

    # 第三部分：搜尋結果
    top_students = search_results[max(search_results.keys())]
    print(*[student_id for student_id, _ in top_students], max_dept)

if __name__ == "__main__":
    courses, search_course = parse_input()
    department_stats, course_stats, search_results, max_dept = calculate_statistics(courses, search_course)
    
    print_results(department_stats, course_stats, search_results, max_dept)
