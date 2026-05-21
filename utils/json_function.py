
from utils import date_time,string,integer
import json
def data_empty_checker():
    with open('data/diary.json','r') as f:
        file_content=f.read()
        if file_content=='[]' or file_content=='':
            return None
        else:
            return file_content
        

def data_input():
    while True:
        title=input('Enter the title of the input.\n')
        mood=input('Enter the mood.\n')
        content=input('Enter the contents.\n')

        if string.string_checker(title) is None:
            print('Invalid Title. try again.\n')
        elif string.string_checker(mood) is None:
            print('Invalid mood, try again.\n')
        elif string.string_checker(content) is None:
            print('Invalid data, try again.\n')
        else:
            break
    file_content=data_empty_checker()
    if file_content is None:
        ID=1
    else:
        entries=json.loads(file_content)
        ID=max(entry['id'] for entry in entries)+1
    dic={}
    dic['ISO']=date_time.date_time_now()
    dic['id']=ID
    dic['Title']=title
    dic['Mood']=mood
    dic['Content']=content
    if file_content:
        entries.append(dic)
    else:
        entries=[]
        entries.append(dic)

    with open('data/diary.json','w') as f:
        json.dump(entries,f,indent=4)
    print('Successful!\n')
    pause=input('Press ENTER to go back to the main menu.')


def data_search():
    while True:
        content=data_empty_checker()
        if content is None:
            print('Diary is empty!')
            pause=input('Press ENTER to go back to the main menu.')
            break
        else:
            while True:
                search_key=input('Enter the ID you want to search: ')
                if integer.valid_integer(search_key) is None:
                    print('Enter a valid integer ID.\n')
                else:
                    search_key=integer.valid_integer(search_key)
                    break
            entries=json.loads(content)
            keys=[]
            for entry in entries:
                keys.append(entry['id'])
            if search_key not in keys:
                print('No entry with this specific key, try again with a different key.\n')
            else:
                for entry in entries:
                    if entry['id']==search_key:
                        print(f"Id: {entry['id']}")
                        print(f"ISO: {entry['ISO']}")
                        print(f"Title: {entry['Title']}")
                        print(f"Mood: {entry['Mood']}")
                        print(f"Content: {entry['Content']}")
                pause=input('Press ENTER to go back to the main menu.')
                break

def view_all():
    content=data_empty_checker()
    if content is None:
        print('Diary is empty!')
    else:
        entries=json.loads(content)
        for entry in entries:
            print(f"Id: {entry['id']}")
            print(f"ISO: {entry['ISO']}")
            print(f"Title: {entry['Title']}")
            print(f"Mood: {entry['Mood']}")
            print(f"Content: {entry['Content']}")
            print()
    pause=input('Press ENTER to go back to the main menu.')

def delete_entry():
    while True:
        content=data_empty_checker()
        if content is None:
            print('Diary is empty!')
            pause=input('Press ENTER to go back to the main menu.')
            break
        else:
            while True:
                search_key=input('Enter the ID you want to delete: ')
                if integer.valid_integer(search_key) is None:
                    print('Enter a valid integer ID.\n')
                else:
                    search_key=integer.valid_integer(search_key)
                    entries=json.loads(content)
                    break
            keys=[]
            for entry in entries:
                keys.append(entry['id'])
            if search_key not in keys:
                print('No entry with this specific key, try again with a different key.\n')
            else:
                for entry in entries:
                    if entry['id']==search_key:
                        entries.remove(entry)
                        break
                with open('data/diary.json','w') as f:
                    json.dump(entries,f,indent=4)
                print('Deleting successful!')
                pause=input('Press ENTER to go back to the main menu.')
                break


