# import only system from os
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




# stack object

class Stack():

    def __init__(self):
        self.data = []
        self.top = -1

    def push(self,num):
        self.data.append(num)
        self.top += 1

    def pop(self):
        self.data.pop()
        self.top -=1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False




# this function check if the expression is valid or not
# it will return a list if epression is valid
# it will return False if expression is invalid

def string_validation(string):
    array = []

    if string[-1] == '.':
        return 403

    count = 0
    last_digit = False
    length = len(string)

    digit_continue = False

    for n in string:

        if n.isalpha():
            return 401

        count += 1

        if count == length:
            last_digit = True

        if not digit_continue:
            num = ''

        if not n.isdigit() and n not in '.(){}[]+-*/ ':
            return 402
        elif n.isdigit() or n == '.':
            if not digit_continue and n == '.':
                return 403
            digit_continue = True
            num += n
            if not last_digit:
                continue

        if n ==' ' and not last_digit:
            continue

        if digit_continue:
            if num.count('.') <= 1 and not num[-1] == '.':
                array.append(num)
                digit_continue = False
            else:
                return 403

        if not n.isdigit():
            array.append(n)

    return array





# this function check if the brackets are balanced or not
# it will return True if brackets are balanced
# it will return False if brackets are not balanced

def bracket_validation(exp):
    S = Stack()
    for n in exp:
        if n in ['(','{','[']:
            S.push(n)
        elif n == ')':
            if S.top >= 0:
                if S.data[S.top] == '(':
                    S.pop()
                else:
                    return False
            else:
                return False
        elif n == '}':
            if S.top >= 0:
                if S.data[S.top] == '{':
                    S.pop()
                else:
                    return False
            else:
                return False
        elif n == ']':
            if S.top >= 0:
                if S.data[S.top] == '[':
                    S.pop()
                else:
                    return False
            else:
                return False
        else:
            continue

    if S.top == -1:
        return True
    else:
        return False




# this function check if the operators are valid or not
# it will return True if operators are valid
# it will return False if operators are invalid


def operator_validation(exp):
    exp = list(exp)
    length = len(exp)
    count = 0
    rem = ['(','{','[',')','}',']']
    operators = ['+','-','*','/']

    while count < length:

        x = exp[count]
        if x in rem:
            exp.pop(count)
            length -= 1
            continue

        count += 1

    if exp[0] in operators or exp[-1] in operators:
        return False

    count = 0
    length = len(exp)
    term = 0

    while count < length:

        if exp[count] in operators:
            term += 1
        else:
            term = 0

        if term == 2:
            return False

        count += 1

    return True





# this function will convert infix to postfix

def postfix_convert(exp):
    final_exp = []
    S = Stack()
    operators = ['+', '-', '*', '/']
    prefference = {'*':2, '/':2, '+':1, '-':1}

    for n in exp:

        isfloat = False

        try:
            if float(n):
                isfloat = True
        except ValueError:
            isfloat = False


        if n.isdigit():
            final_exp.append(int(n))
        elif isfloat:
            final_exp.append(float(n))
        elif n in ['(','{','[']:
            S.push(n)
        elif n in operators:

            if S.isEmpty():
                S.push(n)
            else:
                if not S.data[S.top] in ['(','{','[']:
                    current_prefference = prefference[n]
                    top_prefference = prefference[S.data[S.top]]

                    while current_prefference <= top_prefference and not S.data[S.top] in ['(','{','[']:
                        final_exp.append(S.data[S.top])
                        S.pop()
                        if not S.isEmpty() and not S.data[S.top] in ['(','{','[']:
                            top_prefference = prefference[S.data[S.top]]
                        else:
                            break
                S.push(n)
        else:

            while not S.data[S.top] in ['(','{','[']:
                final_exp.append(S.data[S.top])
                S.pop()
            else:
                S.pop()

    while not S.isEmpty():
        final_exp.append(S.data[S.top])
        S.pop()

    return tuple(final_exp)



# this function will solve postfix operation

def solve_postfix(exp):
    S = Stack()

    for n in exp:
        if type(n) == int or type(n) == float:
            S.push(n)
        else:
            second_operand = S.data[S.top]
            S.pop()
            first_operand = S.data[S.top]
            S.pop()
            if n == '+':
                x = first_operand + second_operand
                S.push(x)
            elif n == '-':
                x = first_operand - second_operand
                S.push(x)
            elif n == '/':
                x = first_operand / second_operand
                S.push(x)
            elif n == '*':
                x = first_operand * second_operand
                S.push(x)

    return S.data[0]










