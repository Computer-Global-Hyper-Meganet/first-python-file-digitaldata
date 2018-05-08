first = int(input("Enter first number : "));
second = int(input("Enter second number: "));

operation = input("Do you want to add, subtract, multiply or divide the two numbers?");

if(operation.lower() == "add"):
    sumof = first+second;
    print("the sum of ",first," and ",second," is ",sumof);
    
