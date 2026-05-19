import datetime
import os
os.system('cls')
while True:
    print('\n======WELCOME TO PERSONAL DIARY======\n')
    print(f'Date & Time: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
    print('MAIN MENU\n')
    print('What do you want to do?\n' \
    'a) Input data\n' \
    'b) Search by key\n' \
    'c) Delete entry ID\n' \
    'd) View all entries\n' \
    'e) Exit\n')
    choice=input()
    if choice.lower()=='e':
        break
    elif choice.lower()=='a':
        break
    elif choice.lower()=='b':
        break
    elif choice.lower()=='c':
        break
    elif choice.lower()=='d':
        break
    else:
        print('Invalid entry, try again.\n')
print('See you soon!')

