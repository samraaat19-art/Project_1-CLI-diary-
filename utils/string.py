def string_cleaner_lowercase(string):
    string=string.strip()
    return string.lower()

def string_checker(string):
    if not string:
        return None
    else:
        return string