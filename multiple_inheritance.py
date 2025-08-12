class dad:
    def dadFunction(self):
        print("i am dad class")


class mom():
    def momFunction(self):
        print("I am mom class")


class son(dad, mom):
    def sonFunction(self):
        print("I am son class")

    def dadFunction(self):
        print("i am overriden dad class in son class")

   # def momFunction(self):
   #     print("i am overriden mom class in son class")


print("son")
print("===")
s = son()
s.sonFunction()
s.dadFunction()
s.momFunction()

print("dad")
print("===")
d=dad()
d.dadFunction()

print("mom")
print("===")
m=mom()
m.momFunction()