#A porgramme that registers biodata and courses for 3 students in your set and calculate their cgpa


#The program will run three times which is for three students
def getGPA():
    students_data = []
    for i in range(1,4):
        #Create a dict to hold a student info
        student = {}
        #Accept Student name from user
        name = input(f'Enter the full name of student{i}: ')
        #Append student name to student dict
        student['name'] = name
        #ask student for number of courses offering
        number_of_courses = int(input(f'How many courses does {name} offers: '))
        #An empty dict to hold the courses offered by a student
        courses = {}
        #An empty dict to hold the info about a course
        course = {}
        #Total score in a subject
        total_score = 0
        #Total units of courses offered by the student
        total_units = 0
        #Current gpa
        gpa = 0
        #A list that will contain student name and gpa
        student_gpa = {}
        student_gpa['name'] = name
        students_data_gpa = []
        #Loop to get details of courses
        for i in range(1,number_of_courses+1):
            #Ask for course name
            course_name = input(f'input the name of course{i}: ')
            #Append it to course dict
            course['course_name'] = course_name
            #Ask for course unit
            course_unit = int(input(f'How many unit course is {course_name}: '))
            #will add the course unit to the total unit
            total_units += course_unit
            #Append it to the course dict
            course['course_unit'] = course_unit
            #Ask for course grade
            course_grade = str(input(f'Whats your grade in {course_name}: '))
            #Append it to course dict
            course['course_grade'] = course_grade
            #Current course score
            course_score = 0
            '''
            The following conditional statement will figure out the course score and add it to the total score
            '''
            if course_grade.lower() == 'a':
                course_score = 5 * course_unit
                total_score += course_score
                course['course_score'] = course_score
            elif course_grade.lower == 'b':
                course_score = 4 * course_unit
                total_score += course_score
                course['course_score'] = course_score
            elif course_grade.lower() == 'c':
                course_score = 3 * course_unit
                total_score += course_score
                course['course_score'] = course_score
            elif course_grade.lower == 'd':
                course_score = 2 * course_unit
                total_score += course_score
                course['course_score'] = course_score
            elif course_grade.lower() == 'e':
                course_score = 1 * course_unit
                total_score += course_score
                course['course_score'] = course_score
            elif course_grade.lower() == 'f':
                course_score = 0 * course_unit
                total_score += course_score
                course['course_score'] = course_score
            #Will find the gpa by dividing total score by total units
            gpa = total_score / total_units
            #will add course dict to course dict
            courses[f'course{i}'] = course
            #will add the student courses to the student variable
            student['courses'] = courses
            #will append the student gpa
            student['gpa'] = gpa
            #will add the gpa of student to the student_gpa list
            student_gpa['gpa'] = gpa
        #will add the student gpa containing name and the gpa to the students_data_gpa
        #students_data_gpa.append(student_gpa)
        #will append the student to the students which hold all students
        students_data.append(student_gpa)
    return students_data

# This will get the GPA of each student and append it to students_final_data
students_final_data = []
for i in range(1, 3):
    print('\n')
    print(f'The is for semester{i}\n')
    students_final_data.append(getGPA())


# Function to get CGPA of each students    
def getCGPA(x):
    students_cgpa = []
    student1_cgpa = {}
    student2_cgpa = {}
    student3_cgpa = {}
    if x[0][0]['name'] == x[1][0]['name']:
        student1_cgpa['name'] = x[0][0]['name']
        gpa = (x[0][0]['gpa'] + x[1][0]['gpa']) / 2
        student1_cgpa['gpa'] = gpa
    if x[0][1]['name'] == x[1][1]['name']:
        student2_cgpa['name'] = x[0][1]['name']
        gpa =  (x[0][1]['gpa'] + x[1][1]['gpa']) / 2
        student2_cgpa['gpa'] = gpa
    if x[0][2]['name'] == x[1][2]['name']:
        student3_cgpa['name'] = x[0][2]['name']
        gpa =  (x[0][2]['gpa'] + x[1][2]['gpa']) / 2  
        student3_cgpa['gpa'] = gpa  
    students_cgpa.append(student3_cgpa) 
    students_cgpa.append(student1_cgpa)
    students_cgpa.append(student2_cgpa)
    for i in range(len(students_cgpa)):
        print(students_cgpa[i])      
    return students_cgpa


# Function to get Highest CGPA
def getHighestCGPA(x):
    x = getCGPA(students_final_data)
    list_of_cgpa = []
    list_of_names = []
    for i in range(len(x)):
        list_of_cgpa.append(x[i]['gpa'])
        list_of_names.append(x[i]['name'])
    max_cgpa = max(list_of_cgpa)

    val_index = list_of_cgpa.index(max_cgpa)
    name = list_of_names[val_index]
    print('The highest CGPA is scored by '+ name + ' which is', max_cgpa)

getHighestCGPA(students_final_data)