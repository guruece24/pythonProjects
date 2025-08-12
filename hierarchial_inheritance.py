
class dad:
    def dadFunction(self):
        print("i am dad class")

    def testFunction(self):
        print("I am test class")

class son1(dad):
    def sonFunction(self):
        print("I am son1 class")

    def dadFunction(self):
        print("i am overriden dad class in son1 class")

class son2(dad):
    def sonFunction(self):
        print("I am son2 class")

   # def dadFunction(self):
   #     print("i am overriden dad class in son2 class")


s1 = son1()
s1.sonFunction()
s1.dadFunction()

s2=son2()
s2.sonFunction()
s2.dadFunction()
