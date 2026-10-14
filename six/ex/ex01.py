class Student:
    def __init__(self, name, score) :
        self.name = name
        self.score = score

    def result(self):
        return "일반학생"
class ScholarshipStudent(Student):
    def result(self):
        if self.score >= 80:
          return "장학 대상"
        return "장학 제외"

s=ScholarshipStudent("지우", 92)
print(s.name, s.score, s.result())