#Name:Cesar Giner
#Class: CS101L-005L
#Lab 5
#Date: 9/30/2022







#function to get field of study(school) of library card input
def get_school(string):
    if int(string[5]) == 1:
        school = 'School of Computing and Engineering SCE'
    elif int(string[5]) == 2:
        school = 'School of Law'
    elif int(string[5]) == 3:
        school = 'College of Arts and Sciences'
    else:
        school = 'Invalid School'

    return school

#function to get year student is in of library card
def get_grade(string):
    if int(string[6]) == 1:
        grade = 'Freshman'
    elif int(string[6]) == 2:
        grade = 'Sophmore'
    elif int(string[6]) == 3:
        grade = 'Junior'
    elif int(string[6]) == 4:
        grade = 'Senior'
    else:
        grade ='Invalid Grade'

    return grade

#function to reset value of A-Z to 0-25
def cv(character):
    if character.isalpha() == True:
        value = ord(character)
        value = value - 65
    if character.isdigit() == True:
        value = int(character)
        
    return value

#function to calculate the last digit of the library card
def get_check_digit(string):
    a = cv(string[0]) * 1
    b = cv(string[1]) * 2
    c = cv(string[2]) * 3
    d = cv(string[3]) * 4
    e = cv(string[4]) * 5
    f = cv(string[5]) * 6
    g = cv(string[6]) * 7
    h = cv(string[7]) * 8
    i = cv(string[8]) * 9

    x = a+b+c+d+e+f+g+h+i
    cd = x%10

    return cd

#function to verify the vailidity of the library card input
def verify_check_digit(string):
    if len(string) != 10:
        error = 'The length of the number given must be 10'
        return False,error
        
        
    elif string[0:4].isalpha() == False:
        error = 'The first five characters must be A-Z'
        return False,error
        
        
    elif int(string[5]) > 3 or int(string[5]) < 1:
        error = 'The sixth character must be 1,2, or 3'
        return False,error
       
        
    elif int(string[6]) > 4 or int(string[6]) < 1:
        error = 'The seventh character must be 1,2,3, or 4'
        return False,error
        
    elif int(string[9]) != get_check_digit(string):
        error = 'Check Digit {} does not match calculated value {}'.format(string[9],get_check_digit(string))
        return False,error
        
    #input is valid,     
    else:
        error = ''
        return True,error
        

    

    

#MAIN
#MAIN
#MAIN
#MAIN



#Outputting to user the program they are about to interact with
#Centering the program message
print('Linda Hall'.center(75,' '))
print('Library Card Check'.center(75,' '))
print('='.center(75,'='))
print()


#setting up a while loop for user to exit when their input is 'E'
#setting initital value of librar_card_num to 0 to start the loop
library_card_num = 0
while library_card_num != 'E':

    #user input
    library_card_num = input("Enter Library Card. Hit 'E' to Exit ==> ")

    #is user input is 'E', end program
    if library_card_num == 'E':
        break

    #calling function to get validity of user input, if invalid, why that is
    valid,message = verify_check_digit(library_card_num)

    #if input invalid, output it, restart loop
    if valid == False:
        print('Library card is invalid.')
        print(message)
        print()
    #if input valid, call functions to get grade and school(field of study) and output them
    elif valid == True:
        print('Library card is valid.')
        school = get_school(library_card_num)
        grade = get_grade(library_card_num)
        print('The card belong to a {} in {}.'.format(grade,school))
        print()
    else:
        continue
                                       
        



    
    
    
        
    

    
