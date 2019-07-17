names = ['john', 'jacob', 'jingle']

user_name = input('What is your name?\n')

def display_name(): 
    for name in names: 
        if user_name == name: 
            return f'Hi, {name}'
    if user_name != name: 
        return 'Who goes there?'
    

print(display_name())