import random
while True:
    #EVA = 0
    x = random.randint(-1000,1000)
    def one_step(V1, EVA, operator, **kwargs):
        if operator == "*":
            if (V1 * x == EVA):
                print("SUCCESS!")
                quit()
        elif operator == "+":
            if (V1 + x == EVA):
                print("SUCCESS!")
                quit()
        elif operator == "/":
            if (V1 / x == EVA):
                print("SUCCESS!")
                quit()
        elif operator == "-":
            if (V1 - x == EVA):
                print("SUCCESS!")
                quit()
    one_step(V1=23, operator="+", EVA=230)
