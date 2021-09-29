class flop():
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
        return (3.14159 * (radius**2)) * height
    def volume_cone(radius, height):
        return (3.14159 * (radius**2)) * height/3
    def volume_sphere(radius):
        return ((4/3*3.14159) * (radius**3))

    def matrix(*args):
        # Matrix MAX SIZE == 3x3
        Matrix = [[args[0], args[1], args[2]], 
                 [args[3], args[4], args[5]],
                 [args[6], args[7], args[8]],]
        return Matrix
test = flop.matrix(1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,0)
print(test[1][2])

#print(flop.order_descending(test))



'''

[1, 2, 3, 2, 3, 4, 3, 4, 5]

A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19],
    [2, 5, 6]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[2][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

'''