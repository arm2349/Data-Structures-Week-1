###Check Brackets in the Code###

def check_brackets(S):
    '''Test whether a string has its brackets balanced (ie., in the correct order).
    Examples:
    "(foo[bar])" is balanced.
    "((foo)foo" is not balanced.
    "]bar()" is not balanced.'''
    success = 'Success'
    stack=[]
    lefts=['(', '{', '[']
    rights = [')', '}', ']']
    opens = []
    if len(S)==1 and (S[0] in lefts or S[0] in rights):
        return 1
    def is_balanced(top_element, stack_element):
        if (top_element == '{' and stack_element != '}') \
        or (top_element == '[' and stack_element != ']') \
        or (top_element == '(' and stack_element != ')'):
            return False
        else:
            return True

    i=0
    for char in S:
        if char in lefts:
            stack.append(char)
            opens.append(i)
            i+=1
        elif char not in lefts and char not in rights:
            #not a bracket character, ignore it
            i+=1
            continue
        else:
            #the case where a right bracket appears before a left bracket, for example: ][
            #if char in rights and len(stack)==0:
            #    return False
            if len(stack)==0:
                return i + 1
            top = stack.pop()
            if is_balanced(top, char) == False:
                return i + 1
            else:
                i+=1
                opens=opens[0:-1]

    if len(stack)!=0:
        if len(opens)==0:
            return i
        else:
            return 1 + opens[-1]
    return success
if __name__ == "__main__":
    s=input()
    assert 1<=len(s)<=10**5
    print (check_brackets(s))
