def func(str_expression):
    stack = []
    for s in str_expression:
        if s == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(y + x)
        elif s == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif s == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(y * x)
        elif s == '/':
            x = stack.pop()
            y = stack.pop()
            stack.append(y / x)
        else:
            stack.append(int(s))
    return stack.pop()

if __name__ == '__main__':
    expression = '34+12-*'
    print(func(expression))
