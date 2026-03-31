class StudentDetails :
    def __init__ (self, name) :
        self.name = name
    
class FetchMarks (StudentDetails) :
    def __init__ (self, name) :
        super().__init__ (name)
        self.total_marks = 0
        self.totalSubjects = 0
        self.marks = []

    def getMarks (self) :
        self.totalSubjects = int(input("ENTER YOUR NUMBER OF SUBJECTS : "))

        for i in range(0, self.totalSubjects) :
            mark = int(input(f"ENTER {i + 1} SUBJECT : "))
            self.marks.append(mark)
            self.total_marks += self.marks[i]

        print(f"YOUR NAME IS {self.name}")
        print(f"YOUR SUBJECTS ARE {self.totalSubjects}")
        print(f"YOUR NAME IS {self.total_marks}")

    def gradeChecker (self) :
        if ((self.total_marks >= 90) and (self.total_marks <= 80)) : print("GRADE : A")
        elif ((self.total_marks >= 70) and (self.total_marks <= 60)) : print("GRADE : B")
        elif ((self.total_marks >= 50) and (self.total_marks <= 40)) : print("GRADE : C")
        else : print("GRADE : FAIL")

    def totalAverage (self) :
        average = self.total_marks / self.totalSubjects
        print(f"THE AVERAGE IS {average}")

name = str(input("ENTER YOUR NAME : ").strip().upper())
getDetails = FetchMarks(name)
getDetails.getMarks()
getDetails.gradeChecker()
getDetails.totalAverage()