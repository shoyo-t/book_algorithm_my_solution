def func(chars):
    br_stack = []
    pr_stack = []
    pairs = []

    for i, char in enumerate(chars):
        if char == '(':
            br_stack.append(')')
            pr_stack.append(i)
        elif char == ')':
            if not br_stack:
                return {'judge': False, 'pairs': []}
                
            if char != br_stack.pop():
                return {'judge': False, 'pairs': []}
            else:
                pairs.append((pr_stack.pop(), i))
        
    if br_stack:
        return {'judge': False, 'pairs': []}

    return {'judge': True, 'pairs': pairs}

if  __name__ == '__main__':
    chars = '(()(())())(()())'
    print(func(chars))
