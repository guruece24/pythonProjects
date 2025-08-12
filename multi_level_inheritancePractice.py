class grandfather():
    def grandfatherFunction(self):
        print("i am grandfather class")


class dad:
    def dadFunction(self):
        print("i am dad class")

    def grandfatherFunction(self):
        print("i am grandfather class overriden in dad class")

    def testFunction(self):
        print("I am test class")

class son(dad):
    def sonFunction(self):
        print("I am son class")

    def dadFunction(self):
        print("i am overriden dad class")

    def grandfatherFunction(self):
        print("i am grandfather class overriden in son class")



print("son")
print("===")
s = son()
s.sonFunction()
s.dadFunction()
s.grandfatherFunction()
print("\n")

print("dad")
print("===")
d=dad()
d.dadFunction()
d.grandfatherFunction()
print("\n")

print("grandfather")
print("======")
g=grandfather()
g.grandfatherFunction()
print("\n")

