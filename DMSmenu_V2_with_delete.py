import re

def view_function():
    with open("devicelist.txt", 'r') as f:
        lines = f.read()
        print(lines)
#ADD function by VENGIE
def write_to_file(text):
    with open('devicelist.txt', 'a') as file:
        file.writelines('\n' + text)
#ADD function by VENGIE
def add_function():
    with open('devicelist.txt') as file:
        text = input("Add new device name and device code separated by space: ")
        fileList = file.read().split()
        if text not in fileList:
            fileList.append(text)
            write_to_file(text)
            # with open('devicelist.txt','a') as file:
            #     file.writelines('\n'+text)
            print('new device {} has been added'.format(text))
            view_function()
        else:
            msg = input('You have entered device {} that is already existed in device list.'
                        'Do you want to continue adding? ')
            if msg == "Yes" or "YES":
                write_to_file(text)
                print('new device {} has been added'.format(text))
            else:
                msg == "No" or "NO"
            print(fileList)
def delete_function(string):
    try:
        with open('devicelist.txt', 'r') as f1:
            delete = string
            lines = f1.readlines()
            with open("devicelist.txt", 'w') as f2:
                for line in lines:
                    if line.strip('\n') != delete:
                        f2.write(line)
        print("The device has been deleted")
    except:
        print("Oops! something error")
#Update function by NEIL
def update_function(string):
    with open("devicelist.txt", 'r+') as f:
        text1 = string
        text = f.read()
        update = str(input('The update device is: '))
        text = re.sub(text1,update,text)
        f.seek(0)
        f.write(text)
        f.truncate()
        print('The device is updated')

def main():
    file1 = open("devicelist.txt")
    ans = 'y'                       #ruby - main, repetition, compiling all functions
    print('Welcome to the Device Management System')
    print('1.	view all devices')  #Raghav, github (OK)
    print('2.	add a device')      #Vengie (DONE)
    print('3.	delete a device')   #Hetvi
    print('4.	update a device')   #Neil (DONE)
    print('5.	exit the program')  #SEARCH for Bashir
    while ans == 'y':
        option = int(input('Select one option from the list( 1, 2, 3, 4, or 5): '))
        if option == 1:
            print('VIEWING ALL DEVICES')
            view_function()
            ans = input('Do you want to continue?(y/n):')
        elif option == 2:
            print('ADDING NEW DEVICE')
            add_function()
            ans = input('Do you want to continue?(y/n):')
        elif option == 3:
            print('====>>> execute DELETE function here')
            view_function()
            string1 = input("Enter full device info to be deleted: ")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if string1 in line:
                    flag = 1
                    break
            if flag == 0:
                print('The device you have entered does not exist')
            else:
                delete_function(string1)
            ans = input('Do you want to continue?(y/n):')
        elif option == 4:
            print('UPDATING DEVICE from below...')
            view_function()     #Update function by NEIL
            string1 = input("Enter full device info to be updated: ")
            flag = 0
            index = 0
            for line in file1:
                index += 1
                if string1 in line:
                    flag = 1
                    break
            if flag == 0:
                print('The device you have entered does not exist')
            else:
                update_function(string1)
            ans = input('Do you want to continue?(y/n):')
        elif option == 5:
            print('\nTHANKS FOR USING PYTEAM\'S DEVICE MANAGEMENT SYSTEM..Bye!')
            break
        else:
            print('Please choose only 1 to 5 options!!!')
            ans = input('Do you want to continue?(y/n):')
    else:
        print('\nTHANKS FOR USING PYTEAM\'S DEVICE MANAGEMENT SYSTEM..Bye!')
    file1.close()
main()
