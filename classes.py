class Cars:
    variable1 = "yes"
    variable2 = "yes"
    variable3 = "no"

    def __init__(self):

        def changeVariable1(yesOrNo):
            variable1 = yesOrNo



suv = Cars()

print(suv.variable1)
yesOrNo = "no"
suv.changeVariable1(yesOrNo)
print(suv.variable1)
