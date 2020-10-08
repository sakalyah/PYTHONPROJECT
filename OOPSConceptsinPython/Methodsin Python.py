class Student:
    school = "DAV"
    def __init__(self,m1,m2,m3):
        self.m1 =m1
        self.m2=m2
        self.m3=m3
    def avg(self):#Instance Method
        return (self.m1+self.m2+self.m3)/3
    def get(self):#Accessor Method
        return self.m1
    def set(self,value):#Mutator Method
        self.m1 = value
    @classmethod #Class Method to access Class variables and also called Decorator.Without the annotation this method will not execute
    def info(cls):
        return cls.school
    @staticmethod #Without this annotation to the static method we can see COmpile time error
    def harish():
        print("I am a static Method")
S1 = Student(25,35,45)
S2 = Student(22,33,44)
S1.harish()
S2.harish()
print(S1.avg(),S2.avg(),S1.info(),S2.harish())


