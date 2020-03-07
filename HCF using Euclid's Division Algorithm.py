#This is a comment
#Comments help you to understand my code

#Program to return HCF of 2 numbers, num1 and num2
#using Euclid's Division Algorithm

#num1 ---> Number 1
#num2 ---> Number 2
#showSteps ---> Whether to show steps or not
#If showSteps = 0, HCF without steps
#If showSteps = 1, HCF with steps
#num1 % num2 means num1 mod num2 or num1 modulus num2
#modulus gives the remainder after division

#Function to return HCF of num1 and num2
#with or without steps
def HCF(num1, num2, showSteps):

    #Case 1 :- num1 > num2
    if num1 > num2:

        #Case 1(a) :- num1 not divisible by num2
        if num1 % num2 != 0:
            
            #Case 1(a)(i) :- showSteps = 1
            if showSteps == 1:
                
                #Print steps
                print('HCF of', num1, 'and', num2,
                      'is equal to HCF of',
                      (num1 % num2), 'and', num2)

                #Return HCF with steps
                return HCF(num1 % num2, num2, 1)

            #Case 1(a)(ii) :- showSteps = 0
            else:

                #Return HCF without steps
                return HCF(num1 % num2, num2, 0)

        #Case 1(b) :- num1 divisible by num2
        else:

            #Case 1(b)(i) :- showSteps = 1
            if showSteps == 1:

                #Print steps
                print('HCF of', num1, 'and', num2,
                      'is equal to HCF of',
                      num2, 'and', num2)

                #Return HCF with steps
                return 'HCF of ' + str(
                    num2) + ' and ' + str(
                    num2) + ' which is equal to '+ str(
                        num2)

            #Case 1(b)(ii) :- showSteps = 0
            else:

                #Return HCF without steps
                return str(num2)

        
    #Case 2 :- num1 = num2
    elif num1 == num2:

        #Return num1
        return str(num1)

    #Case 3 :- num1 < num2
    else:

        #Case 3(a) :- num2 not divisible by num1
        if (num2 % num1) != 0:

            #Case 3(a)(i) :- showSteps = 1
            if showSteps == 1:

                #Print steps
                print('HCF of', num1, 'and', num2,
                      'is equal to HCF of',
                      num1, 'and', (num2 % num1))

                #Return HCF with steps
                return HCF(num1, num2 % num1, 1)
            
            #Case 3(a)(ii) :- showSteps = 0
            else:

                #Return HCF without steps
                return HCF(num1, num2 % num1, 0)

        #Case 3(b) :- num2 divisible by num1
        else:

            #Case 3(b)(i) :- showSteps = 1
            if showSteps == 1:

                #Print steps
                print('HCF of', num2, 'and', num1,
                      'is equal to HCF of', num1,
                      'and', num1)

                #Return HCF with steps
                return 'HCF of ' + str(
                    num1) + ' and ' + str(
                    num1) + ' which is equal to '+ str(
                        num1)

            #Case 3(b)(ii) :- showSteps = 0
            else:

                #Return HCF without steps
                return str(num1)
#Main function
def main():

    #Ask user whether to show steps or not
    showSteps = int(input(
        'Show steps to find HCF (1 - Yes, 0 - No): '))

    #Loop forever
    while True:
        
        #If showSteps not equal to 0 and
        #showSteps not equal to 1
        if (showSteps != 0) and (showSteps != 1):

            #Loop while showSteps not equal to 0 and
            #showSteps not equal to 1
            while (showSteps != 0) and (showSteps != 1):

                #Display a helpful message to enter 0 or 1
                print('Please enter 0 or 1')

                #Ask user whether to show steps or not again
                showSteps = int(input(
            'Show steps to find HCF (1 - Yes, 0 - No): '))
                
        #If showSteps == 0 or showSteps == 1        
        else:
            
            #Break loop
            break
        
    #Ask num1 input from user                    
    num1 = int(input('Please enter the first number: '))

    #Ask num2 input from user
    num2 = int(input('Please enter the second number: '))

    #Print HCF of num1 and num2 
    print('HCF of', num1, 'and', num2,'is equal to', HCF(
        num1, num2, showSteps))

#If program is started as main process
#instead of being imported
if __name__ == '__main__':

    #Execute the main function
    main()
