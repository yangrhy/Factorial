def Factorial(n):
    if n <= 1:
        return 1
    else:
        return n * Factorial(n-1)

def Main():
    
    # initialized to y to start program
    userChar = 'y' 
    
    # loops if userChar is y, anything else will exit program
    while userChar == 'y': 
        try:
            userNum = int(input('Enter a number to find the factorial: '))
            print('{}! = {}'.format(userNum, Factorial(userNum)))
            userChar = input('Do you wish to enter another number (y/n)?')
        except:
            print('Please enter an integer')
    print('Goodbye!')
    
Main()
