class Student:
    def __init__(self, name, branch, marks):
        self.name = name
        self.branch = branch
        self.marks = marks
    def calc_percent(self):
        if self.branch.upper() == 'CSE':
            total_marks = 750
            marks_obtained = self.marks
            percentage = (marks_obtained * 100) / total_marks
        elif self.branch.upper() == 'ECE':
            total_marks = 850
            marks_obtained = self.marks
            percentage = (marks_obtained * 100) / total_marks
        elif self.branch.upper() == 'EEE':
            total_marks = 600
            marks_obtained = self.marks
            percentage = (marks_obtained * 100) / total_marks
        else:
            percentage = 'No details found for ' + self.branch
        self.percentage = percentage
        return self.percentage

    def calc_grade(self):
        if 80 <= self.percentage < 100:
            self.grade = 'A1'
        elif 70 <= self.percentage < 80:
            self.grade = 'A2'
        elif 55 <= self.percentage < 70:
            self.grade = 'B'
        elif 40 <= self.percentage < 55:
            self.grade = 'C'
        elif self.grade < 40:
            self.grade = 'Fail'
        else:
            self.grade = 'Not Assigned'
        return self.grade

    def student_details(self):
        print('Student name - ', self.name.title())
        print('Branch - ', self.branch.upper())
        print('Marks - ', self.marks)
        print('Percentage -', self.calc_percent(), '%')
        print('Grade obtained - ', self.calc_grade())


student1 = Student('shaNNu', 'cSe', 687)
student1.student_details()
student2 = Student('vasanth', 'cse', 654)
student2.student_details()