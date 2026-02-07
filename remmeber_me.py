import json



def greet_user():
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        username = input('whats is your name: ')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back, {username}")
    else:
        print(f' welcome back, {username}')


greet_user()