import operations as op

def instaSolve (val,arg):
    if arg == 'pc':
        return op.percent(val)
    elif arg == 'in':
        return op.inverse(val)
    elif arg == 'sq':
        return op.square(val)
    elif arg == 'sr':
        return op.sqroot(val)
    else:
        print("Error in single value operation.")
        pass
def solve(operations):
    x = operations.pop(0)
    y = 0

    for i in operations:
        print(operations)
        print("Resultado parcial: ",x)
        op = operations.pop(0)
        y = operations.pop(0)

        if op == '+':
            x += y

        elif op == '-':
            x -= y

        elif op == '*':
            x *= y

        elif op == '/':
            x /= y

    return x