from PyInquirer import prompt, Separator
import json
from user import get_users

refunders = {
    'type': 'checkbox',
    'message': 'Select users who participated in the expense',
    'name': 'refunders',
    'transformer': lambda x: f"{len(x)} selected",
    'choices': [
        Separator('= Who participate ? ='),
    ],

    'validate': lambda answer: 'You must choose at least one user !' \
        if len(answer) == 0 else True
}

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "validate": lambda answer: 'You must enter a number !' \
            if not answer.isnumeric() else True,
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": get_users(),
    },
    refunders
]


def new_expense(*args):
    # This is because we need to recompute users during the runtime
    expense_questions[2]['choices'] = get_users()
    expense_questions[3]['choices'] = expense_questions[3]['choices'][:1]
    for i in list(map(lambda x: {"name": x, "checked": True}, get_users())):
        refunders['choices'].append(i)

    infos = prompt(expense_questions)

    print(infos)

    try:
        with open('expense_report.json', 'r') as file:
            expenses = json.load(file)
    except:
        expenses = []
    new_expense = {
        'amount': int(infos['amount']),
        'label': infos['label'],
        'spender': infos['spender'],
        'refunders': infos['refunders']
    }
    expenses.append(new_expense)
    with open('expense_report.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    return True

def get_expenses():
    try:
        with open('expense_report.json', 'r') as file:
            expenses = json.load(file)
    except:
        expenses = []
    return expenses