###Check Brackets in the Code###

def check_brackets(S):
    '''Test whether a string has its brackets balanced (ie., in the correct order).
    Examples:
    "(foo[bar])" is balanced.
    "((foo)foo" is not balanced.
    "]bar()" is not balanced.'''

    stack=[]
    leftover_stack=[]
    lefts=['(', '{', '[']
    rights = [')', '}', ']']
    def add_leftover(top_element, stack_element):
        if (top_element == '{' and stack_element != '}') \
        or (top_element == '[' and stack_element != ']') \
        or (top_element == '(' and stack_element != ')'):
            return False
            #stack1.append(top_element)
            #stack2.append(stack_element)
        else:
            return True
    for char in S:
        if char in lefts:
            stack.append(char)
        elif char not in lefts and char not in rights:
            #ignore non-bracket characters
            continue
        else:
            if char in rights:
            #the case where a right bracket appears before a left bracket, for example: ][
                if char == '}' and '{' not in stack \
                or char == ']' and '[' not in stack \
                or char == ')' and '(' not in stack:
                    return False
            top = stack.pop()
            #print (f'the top is {top} and the char is {char}')
            if add_leftover(top, char) == False:
                stack.append(top)
                leftover_stack.append(char)
            else:
                continue
    if (len(leftover_stack) == 0 and len(stack) == 0):
        return True
    elif len(leftover_stack) != len(stack):
        return False
    else:
        combined = stack + leftover_stack
        sep=''
        new_string = sep.join(combined)
        return (check_brackets(new_string))
if __name__ == '__main__':
    print (check_brackets(input()))
