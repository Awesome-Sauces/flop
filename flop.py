class Parent():
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
volume = Parent.volume_sphere(4)
print(volume)