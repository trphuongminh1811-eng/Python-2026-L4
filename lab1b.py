list_students = []
list_courses = []
dict_marks = {}

def add_student():
    n = int(input("how many students? "))
    for i in range(0, n):
        id = input("id: ")
        name = input("name: ")
        dob = input("dob: ")
        # make dictionary
        st = {"id": id, "name": name, "dob": dob}
        list_students.append(st)

def add_course():
    n = int(input("how many courses? "))
    for i in range(0, n):
        id = input("course id: ")
        name = input("course name: ")
        crs = {"id": id, "name": name}
        list_courses.append(crs)

def add_mark():
    c_id = input("enter course id to add mark: ")
    
    # check if course exists
    found = False
    for i in range(len(list_courses)):
        if list_courses[i]["id"] == c_id:
            found = True
            
    if found == False:
        print("course not found!!!")
        return
        
    dict_marks[c_id] = {}
    
    for i in range(len(list_students)):
        st = list_students[i]
        m = float(input("mark for " + st["name"] + ": "))
        dict_marks[c_id][st["id"]] = m

def print_students():
    print("--- students ---")
    for i in range(len(list_students)):
        print(list_students[i]["id"] + " - " + list_students[i]["name"])

def print_courses():
    print("--- courses ---")
    for i in range(len(list_courses)):
        print(list_courses[i]["id"] + " - " + list_courses[i]["name"])

def print_marks():
    c_id = input("enter course id to see marks: ")
    if c_id in dict_marks:
        for st_id in dict_marks[c_id]:
            print("student " + st_id + " got " + str(dict_marks[c_id][st_id]))
    else:
        print("no marks")

add_student()
add_course()
add_mark()
print_students()
print_courses()
print_marks()
