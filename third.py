str = input('enter your full name: ');
firstName = "";
lastName = "";
isLastName = False;

for i in range(len(str)):
    if(str[i] is " "):
        isLastName = True;
    else:
        if(not isLastName):
            firstName += str[i];
        else:
            lastName += str[i];

print('First Name: ' + firstName);
print('Last Name: ' + lastName);

        
