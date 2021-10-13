#############################
### Flop Settings Manager ###
#############################
class Settings:
    def __init__(self, StartUp, pieDefine):
        self.startupState = StartUp
        self.pi = pieDefine
    def startup(self):
            global PI
            PI = self.pi
    def changeCurrent(self):
        global PI
        PI = self.pi

#############################
### Main Section of Flop ####
#############################
class Parent():
    class matrix():
        def __init__(self, *args):
            self.args = args
            self.Matrix =   [[self.args[0], self.args[1], self.args[2]], 
                            [self.args[3], self.args[4], self.args[5]],
                            [self.args[6], self.args[7], self.args[8]],]
        def fancy(self):
            print(str(self.Matrix[0]) + "\n" + str(self.Matrix[1]) + "\n" + str(self.Matrix[2]))
            return self.Matrix
    class math():        
        def exponents(num, power):
            return num ** power
        def root(sqrNum):
                squareroot = sqrNum ** 0.5
                return squareroot

        def compare(intA, intB, operator, **kwargs):
                if operator == ">":
                    return intA > intB
                elif operator == "<":
                    return intA < intB
                elif operator == "=":
                    return intA == intB

        def order_descending(*args):
            list_args = []
            for index in range(len(args)):
                if type(args[index]) == list:
                    list_args.extend(args[index])
                else:
                    list_args.append(args[index])
            return sorted(list_args, reverse=True)

        def order_ascending(*args):
            list_args = []
            for index in range(len(args)):
                if type(args[index]) == list:
                    list_args.extend(args[index])
                else:
                    list_args.append(args[index])
            return sorted(list_args, reverse=False)
            
        def volume_cylinder(radius, height):
            return (PI * (radius**2)) * height
        def volume_cone(radius, height):
            return (PI * (radius**2)) * height/3
        def volume_sphere(radius):
            return ((4/3*PI) * (radius**3))
#############################
### Search Section of Flop ##
#############################
# function as class
class Search(Parent):
    def integer(int, lookfor):
        if type(int) == list:
            for iterate in range(len(int)):
                if lookfor in int[iterate]:
                    return True
                else:
                    return False
        elif type(int) == type(1):
            while (int>0):
                n = int%10
                int = int//10

                if n==lookfor:
                    return True         
            return False
        else:
            print("Flop currently only has support for type int and list!")

