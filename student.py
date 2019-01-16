class Student(object):
    name = None
    skill = 0
    outgoing = 0
    grade = 0
    years = -1
    power = 0

    def __init__(self,name, skill, outgoing, grade, years):
        self.name = name
        self.skill = skill
        self.outgoing = outgoing
        self.grade = grade
        self.years = years
        self.power = 0  # TODO Add formula to compute power level

    def __compare__(self):
        return self.power

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
