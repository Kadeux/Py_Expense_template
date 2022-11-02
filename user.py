from PyInquirer import prompt

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name: ",
    },
]


def get_users():
    users = []
    with open('users.csv', 'r') as file:
        for line in file:
            users.append(line.strip())
    return users


def add_user():
    infos = prompt(user_questions)
    with open('users.csv', 'a') as file:
        file.write(f"{infos['name']}\n")
    return
