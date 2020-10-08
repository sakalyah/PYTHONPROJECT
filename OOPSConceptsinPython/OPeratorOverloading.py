class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
S1 = Student(60,60)
S2 = Student (70,70)
S3 = S1+S2
S4 = Student("Harish","Sakalya")
print(S3.m1,S3.m2,S4)

