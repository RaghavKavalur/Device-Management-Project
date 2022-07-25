ans = 'y'                       #ruby - main, repetition
print('Welcome to the Device Management System')
print('1.	view all devices')  #Raghav
print('2.	add a device')      #Vengie
print('3.	delete a device')   #Hetvi
print('4.	update a device')   #Neil
print('5.	exit the program')  #SEARCH for Bashir
while ans == 'y':
    option = int(input('Select one option from the list( 1, 2, 3, 4, or 5): '))
    if option == 1:
        print('====>>> execute View function here')
        ans = input('Do you want to continue?(y/n):')
    elif option == 2:
        print('====>>> execute Add function here')
        ans = input('Do you want to continue?(y/n):')
    elif option == 3:
        print('====>>> execute DELETE function here')
        ans = input('Do you want to continue?(y/n):')
    elif option == 4:
        print('====>>> execute UPDATE function here')
        ans = input('Do you want to continue?(y/n):')
    elif option == 5:
        print('====>>> EXIT here')
    else:
        print('Please choose only 1 to 5 options!!!')
        ans = input('Do you want to continue?(y/n):')
else:
    print('\nTHANKS FOR USING PYTEAM\'S DEVICE MANAGEMENT SYSTEM')
