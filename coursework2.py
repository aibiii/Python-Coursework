#I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1941174
# Date: 24/11/2022

totalInputs = 0
progressCount = 0
trailerCount = 0
retrieverCount = 0
failCount = 0
progress_list = []
outcome_list = []
            

def histogram1():
    list0 = (progressCount, trailerCount, retrieverCount, failCount)
    list1 = ('Progress ', 'Trailer ', 'Retriever ', 'Excluded ')
    print()
    print('-' * 40)
    print('Horizontal Histogram')

    for i in range(len(list0)):
        print(list1[i], list0[i],':', end='')
        for j in range(list0[i]):
            print('*', end='')
        print('')

    print()
    print(totalInputs, ' outcomes in total')
    print("-" * 40)

def histogram2():
    print()
    print('List Histogram - Part 2')

    j = 0
    for i in range(len(outcome_list)):
        print(f'{outcome_list[i]} {progress_list[j:j+3]}', end="\n")        
        j += 3
        
def histogram3():
    print()
    print('List Histogram - Part 3')
    j = 0
    for i in range(len(outcome_list)):
        print(f'{outcome_list[i]} {progress_list[j:j+3]}', end="\n")        
        j += 3
    
    file = open('data_file.txt','w')
    j = 0
    for i in range(len(outcome_list)):
        file.write(f'{outcome_list[i]} {progress_list[j:j+3]}')
        file.write('\n')
        j += 3
    file.close()

while True:
    total = 0

    while True:
        userPass = input('Please enter your credits at pass: ')

        try:
            userPass = int(userPass)
            if int(userPass) > 120 or int(userPass) % 20 != 0:
                print('Out of range. Try again.')
            else:
                total += userPass
                break
        except ValueError:
            print('Integer required')


    while True:
        userDefer = input('Please enter your credits at defer: ')

        try:
            userDefer = int(userDefer)
            if int(userDefer) > 120 or int(userDefer) % 20 != 0:
                print('Out of range. Try again.')
            else:
                total += userDefer
                break
        except ValueError:
            print('Integer required')

    while True:
        userFail = input('Please enter your credits at fail: ')

        try:
            userFail = int(userFail)
            if int(userFail) > 120 or int(userFail) % 20 != 0:
                print('Out of range. Try again.')
            else:
                total += userFail
                break
        except ValueError:
            print('Integer required')


    
    if total == 120:
        totalInputs += 1
        if userPass == 120:
            print('Progress')
            progressCount += 1
            outcome_list.append('Progress -')
            progress_list.append(userPass)
            progress_list.append(userDefer)
            progress_list.append(userFail)
        elif userPass == 100:
            print('Progress (module trailer)')
            trailerCount += 1
            outcome_list.append('Progress (module trailer) -')
            progress_list.append(userPass)
            progress_list.append(userDefer)
            progress_list.append(userFail)
        elif userFail > (userPass + userDefer):
            print('Exclude')
            failCount += 1
            outcome_list.append('Exclude -')
            progress_list.append(userPass)
            progress_list.append(userDefer)
            progress_list.append(userFail)
        else:
            print('Do not Progress – module retriever')
            retrieverCount += 1
            outcome_list.append('Do not Progress – module retriever -')
            progress_list.append(userPass)
            progress_list.append(userDefer)
            progress_list.append(userFail)
            
    else:
        print("Total incorrect")



    print()
    print('Would you like to enter another set of data?')
    response = input("Enter 'y' to yes and 'q' to quit and view results: ").lower()
    if response == 'y':
        
        continue
    elif response == 'q':
        histogram1()
        histogram2()
        histogram3()
        
        break
    
    else:
        response = input("Please, enter 'y' to yes and 'q' to quit: ")
        
        




