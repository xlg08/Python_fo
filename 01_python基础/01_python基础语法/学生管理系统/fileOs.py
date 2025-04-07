STU_FILE_NAME = "students.txt"
students = []

def addStudentToFile(students):
    fileName = None
    try:
        # print(students)
        fileName = open(STU_FILE_NAME, "w", encoding="utf-8")
        for i in students:
            fileName.write(str(i) + "\n")
    except Exception as e:
        print("出现的异常是：" + e)
    finally:
        if fileName != None:
            fileName.close()


def getStudents():
    filename = None
    try:
        filename = open(STU_FILE_NAME, "r", encoding="utf-8")
        while True:
            c = filename.readline()
            c = c.replace("\n","")
            # print("信息为：", c)
            if c == "":
                break
            students.append(eval(c))

        return students
    except Exception as e:
        print("出现的异常为：", e)
    finally:
        if filename!=None:
            filename.close()

def delStudentFromFile():
    pass

