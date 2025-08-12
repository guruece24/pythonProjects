class god:
    def godFunction(self):
        print("i am god class")

class dad(god):
    def dadFunction(self):
        print("i am dad class")

    #def godFunction(self):
       # print("i am god class overridden in dad class")


class mom(god):
    def momFunction(self):
        print("I am mom class")

    #def godFunction(self):
        #print("i am god class overridden in mom class")


class son(dad, mom):
    def sonFunction(self):
        print("I am son class")

    #def dadFunction(self):
    #    print("i am overriden dad class in son class")

    #def momFunction(self):
    #    print("i am overriden mom class in son class")


print("hybrid")
print("god")
print("===")
g=god()
g.godFunction()

print("dad")
print("===")
d=dad()
d.dadFunction()
d.godFunction()

print("mom")
print("===")
m=mom()
m.momFunction()
m.godFunction()

print("son")
print("===")
s = son()
s.sonFunction()
s.dadFunction()
s.momFunction()
s.godFunction()
