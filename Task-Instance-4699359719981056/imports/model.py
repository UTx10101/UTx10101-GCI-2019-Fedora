class Class:
    def __init__(self,teacher,subject,periNow):
        self.teacher = teacher
        self.subject = subject
        self.totalPeris = periNow
        self.perisLeft = periNow
        self.cells = [(-1,-1)]*self.totalPeris
    def __str__(self):
        return "Teacher-'{}' | Subject-'{}' | {} Periods Left \n".format(self.teacher,self.subject,self.perisLeft)
    def __repr__(self):
        return str(self)

class Teacher:
    def __init__(self,id,name,subject,amtofperi):
        self.id=id
        self.name=name
        self.subject=subject
        self.periods=amtofperi
    def __str__(self):
        return "ID-{} | Name-'{}' | Subject-'{}' | {} Periods \n".format(self.id,self.name,self.subject,self.periods)
    def __repr__(self):
        return str(self)

class Subject:
    def addSubject(self,sub,sub_id,subjects,_id,amt):
        if(_id not in subjects[sub]["teachers"]):
            subjects[sub]["teachers"].append(_id)
            subjects[sub]["periods"]+=amt