def askAQuestion(question):
    response = input(question);
    print("\n" + '-' * 100);
    return response

def options():
    print('Pick one of the following!')
    print('1 - Add Two Numbers');
    print('2 - Subtract Two Numbers');
    print('3 - Multiply Two Numbers');
    print('4 - Divide Two Numbers');
    print('5 - Generate a Prime Sequence');
    print('6 - Generate the Fibonacci Sequence');
    option = int(askAQuestion("Which would you like to try out? "));

    optionPicked(option);

def optionPicked(option):
    if(option == 1):
        addTwo();
    elif(option == 2):
        subTwo();
    elif (option == 3):
        
    else:
            

print('Hello There! I am number bot! Welcome to the number app!');
name = askAQuestion("What's your name, stranger? ");

