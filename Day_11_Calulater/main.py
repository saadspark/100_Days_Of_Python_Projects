from art import logo
print(logo)
should_continue = True
val_one = int(input("Enter Value : "))
while should_continue :
    print('Select Following Operation ')
    operation = {
        '+' : 'Addition',
        '-' : 'Subtraction',
        '*' : 'Multiplication',
        '/' : 'Division'
    }
    for key in operation:
        print(f'{key} : {operation[key]}')
    val_operation = input("Enter Operation : ")

    val_two = int(input("Enter Value : "))


    def calculator(val_one,val_operation,val_two):
        if val_operation == '+':
            return float(val_one) + float(val_two)
        elif val_operation == '-':
            return float(val_one) - float(val_two)
        elif val_operation == '*':
            return float(val_one) * float(val_two)
        elif val_operation == '/':
            return float(val_one) / float(val_two)
        else:
            return "Invalid Operation"

    answer = calculator(val_one,val_operation,val_two)
    print(f'{val_one} {val_operation} {val_two} = {answer}')

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y' :
        val_one = answer
    else:
        should_continue = False
        calculator()