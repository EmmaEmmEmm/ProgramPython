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
                if score != 'w':
                    students.append((student_id[3:6], student_id, score))
            else:  # 無會考成績
                term_score = int(student_data[1]) if student_data[1] != 'w' else 'w'
                score = None if term_score == 'w' else term_score
                if term_score != 'w':
                    students.append((student_id[3:6], student_id, term_score))
        courses[(course_code, term_code)] = students

    search_course = input()
    return courses, search_course

def course(c, ser):
    re_de = {}
    department_stats = {}
    course_stats = {}
    search_results = {}

    # print(c)
    #part1
    for (class_code, year), student in c.items():
        year = year[:3]
        print(year)
        d = {}
        v = [[]]
        y_s = [[]]
        a = 0
        num = student[0][0]
        for i in student:
            if num == i[0]:
                v[a].append(i)  
            else:
                a += 1
                v.append([])
                num = i[0]
                v[a].append(i)
        num = student[0][1][:3]
        a = 0
        for x in v:
            for y in x:
                if num == y[1][:3]:
                    y_s[a].append(y)  
                else:
                    a += 1
                    y_s.append([])
                    num = y[1][:3]
                    y_s[a].append(y)
        for t in y_s:
            d[(t[0][0], t[0][1][:3], year)] = t
        for (sys, y, year), stu in d.items():
            if (sys, y, year) not in department_stats.keys():
                department_stats[(sys, y, year)] = stu
            else:
                re_de[(sys, y, year)] = stu
            if (sys, y, year) in department_stats and (sys, y, year) in re_de:
                v = []
                for i in department_stats[(sys, y, year)]:
                    for j in re_de[((sys, y, year))]:
                        if i[1] == j[1]:
                            v.append((i[0], i[1], int((i[2]+j[2])//2+0.5)))
                            
            
                
    #part2
    #   
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
    print(department_stats)
    return department_stats, course_stats, search_results, max_dept
courses, search_course = parse_input()
course(courses, search_course)
