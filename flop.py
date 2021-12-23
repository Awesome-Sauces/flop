#############################
### Flop Settings Manager ###
#############################
'''
Manages Global variables
Changes them
And can declare them
'''
class Settings:
    def __init__(self, StartUp, pieDefine, fancyShow=True):
        self.startupState = StartUp
        self.pi = pieDefine
        self.fancy = fancyShow
    def startup(self):
            global PI
            global FS
            PI = self.pi
            FS = self.fancy
    def changeCurrent(self):
        global PI
        global FS
        PI = self.pi
        FS = self.fancy

#############################
### Main Section of Flop ####
#############################
'''
Parent Class of Flop!
contains matrix, math and will have much more added!

'''
class Parent():
    class matrix():
        def __init__(self, *args):
            self.args = args
            self.Matrix =   [[self.args[0], self.args[1], self.args[2]], 
                            [self.args[3], self.args[4], self.args[5]],
                            [self.args[6], self.args[7], self.args[8]],]
        def fancy(self):
            if FS == True:
                print(str(self.Matrix[0]) + "\n" + str(self.Matrix[1]) + "\n" + str(self.Matrix[2]))
                return self.Matrix
            elif FS == False:
                return self.Matrix
            else:
                raise TypeError("Please Enter a Boolean Value!")
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
            for iterate in range(len(args)):
                if type(args[iterate]) == type(Parent.matrix(0,0,0,0,0,0,0,0,0)):
                    matrice_args_final = args[iterate].fancy()
                    matrice_args = []
                    for matrice_index in range(len(matrice_args_final)):
                            matrice_args.extend(matrice_args_final[matrice_index])
                    return sorted(matrice_args, reverse=True)
                else:
                    list_args = []
                    for index in range(len(args)):
                        if type(args[index]) == list:
                            list_args.extend(args[index])
                        else:
                            list_args.append(args[index])
                    return sorted(list_args, reverse=True)

        def order_ascending(*args):
            for iterate in range(len(args)):
                if type(args[iterate]) == type(Parent.matrix(0,0,0,0,0,0,0,0,0)):
                    matrice_args_final = args[iterate].fancy()
                    matrice_args = []
                    for matrice_index in range(len(matrice_args_final)):
                            matrice_args.extend(matrice_args_final[matrice_index])
                    return sorted(matrice_args, reverse=False)
                else:
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
        def one_step_equations():
            return
#############################
### Search Engine of Flop ###
#############################
'''
Flop Search engine
allows search inside matrice!
and normal lists aswell.
helps shorten syntax when doing searches!
'''
class Search(Parent):
    def integer(int, lookfor):
        if type(int) == type(1):
            while (int>0):
                n = int%10
                int = int//10

                if n==lookfor:
                    return True         
            return False
        else:
            raise ValueError("Enter a Integer!")
    def list(Floplst, lookfor):
        if type(Floplst) == list:
            for iterate in range(len(Floplst)):
                if lookfor in Floplst[iterate]:
                    return True
        else:
            raise ValueError("Enter a List!")
    def string(string, lookfor):
        if type(string) == str:
                if lookfor in string:
                    return True
                else:
                    return False
        else:
            raise ValueError("Enter a String!")





# BETA
from dataclasses import dataclass
@dataclass
class DataClassCard:
    rank: str
    suit: str
    def output(self):
        print(self.rank)
queen_of_hearts = DataClassCard('Q', 'Hearts')
queen_of_hearts.output()