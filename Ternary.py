def Ternary(value1, value2, value3):
    if value1 == True:
        return value2
    else:
        return value3
def run(var_1, var_2, var_3, var_4):
    if var_1 == False or var_2 == False or var_3 == False or var_4 == False:
        return 'There is one or more not number inputs'
    else:
        return Ternary(var_1==2, 0, (Ternary(var_2==4, 15, 0) + Ternary(var_2==3, 5, 0) - Ternary(var_4==2, 0, 5) + Ternary(var_3==3, 5, 0)))

def validate(var):
    try:
        int(var)
        return int(var)
    except ValueError:
        return False

var_1 = input('var_1: ')
var_2 = input('var_2: ')
var_3 = input('var_3: ')
var_4 = input('var_4: ')

print('Result: ' + str(run(validate(var_1), validate(var_2), validate(var_3), validate(var_4))))

input('Press any key to continue... ')