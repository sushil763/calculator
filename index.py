from required_functions import *

print('Welcome to Calculator 1.0')
print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
main_expression = input('Enter the Mathematical Expression you want to calculate: ')
expression = string_validation(main_expression)
loop = True

while loop:

    if type(expression) == list:
        expression = tuple(expression)
        if bracket_validation(expression):
            print('\n  ==>>  Step-1: Brackets are balanced.')
            if operator_validation(expression):
                print('  ==>>  Step-2: Arithmetic Operators are valid.')
                postfix = postfix_convert(expression)
                result = solve_postfix(postfix)
                print('\n  ==>>  Result of your Mathematical Expression = {}\n'.format(result))
                next = input('Do you want to calculate another Mathematical Expression?\nEnter YES to continue and anything else to exit: ').upper()
                if next == 'YES':
                    clear()
                    print('Welcome to Calculator 1.0')
                    print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
                    main_expression = input('Enter the Mathematical Expression you want to calculate: ')
                    expression = string_validation(main_expression)
                    continue
                else:
                    loop = False
            else:
                clear()
                print('Welcome to Calculator 1.0')
                print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
                print('Mathematical Expression you entered is: {}\n'.format(main_expression))
                print('  ==>>  Arithmetic Operators are not valid.\n  ==>>  Please try again.\n')
                main_expression = input('Enter the Mathematical Expression you want to calculate: ')
                expression = string_validation(main_expression)
                continue
        else:
            clear()
            print('Welcome to Calculator 1.0')
            print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
            print('Mathematical Expression you entered is: {}\n'.format(main_expression))
            print('  ==>>  Brackets are not balanced.\n  ==>>  Please try again.\n')
            main_expression = input('Enter the Mathematical Expression you want to calculate: ')
            expression = string_validation(main_expression)
            continue
    elif expression == 401:
        clear()
        print('Welcome to Calculator 1.0')
        print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
        print('Mathematical Expression you entered is: {}\n'.format(main_expression))
        print('  ==>>  Mathematical Expressions can not contain alphabets.\n  ==>>  Please try again.\n')
        main_expression = input('Enter the Mathematical Expression you want to calculate: ')
        expression = string_validation(main_expression)
        continue
    elif expression == 402:
        clear()
        print('Welcome to Calculator 1.0')
        print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
        print('Mathematical Expression you entered is: {}\n'.format(main_expression))
        print('  ==>>  Mathematical Expressions can only contain numbers, spaces, brackets and arithmetic operators (+, -, *, /).\n  ==>>  Please try again.\n')
        main_expression = input('Enter the Mathematical Expression you want to calculate: ')
        expression = string_validation(main_expression)
        continue
    elif expression == 403:
        clear()
        print('Welcome to Calculator 1.0')
        print('This can only deal with arithmetic operators (+, -, *, /) and brackets.\n')
        print('Mathematical Expression you entered is: {}\n'.format(main_expression))
        print('  ==>>  Decimals must be in the form x.y (where x and y can be any number).\n  ==>>  Please try again.\n')
        main_expression = input('Enter the Mathematical Expression you want to calculate: ')
        expression = string_validation(main_expression)
        continue
