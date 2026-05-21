from utils import date_time,string,json_function
import os
os.system('cls')
while True:
    print('\n======WELCOME TO PERSONAL DIARY======\n')
    print(f'Date & Time: {date_time.date_time_now()}')
    print('MAIN MENU\n')
    print('What do you want to do?\n' \
    'a) Input data\n' \
    'b) Search by key\n' \
    'c) Delete entry ID\n' \
    'd) View all entries\n' \
    'e) Exit\n')
    choice=input()
    choice=string.string_cleaner_lowercase(choice)
    if choice=='e':
        break
    elif choice=='a':
        json_function.data_input()
    elif choice=='b':
        json_function.data_search()
    elif choice=='c':
        json_function.delete_entry()
    elif choice=='d':
        json_function.view_all()
    else:
        print('Invalid entry, try again.\n')
print('See you soon!')

