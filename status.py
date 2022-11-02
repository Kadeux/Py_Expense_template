from expense import get_expenses
from user import get_users


def show_status():
    """synthesizing who owes who and how much"""
    expenses = get_expenses()
    users = get_users()
    debts = {}
    for expense in expenses:
        for user in expense['refunders']:
            if user != expense['spender']:
                if user not in debts:
                    debts[user] = []
                debts[user].append({expense['spender']: expense['amount'] / len(expense['refunders'])})
    for user in users:
        if user not in debts:
            debts[user] = []
    # synthetize all debts between users
    for user in debts:
        for debtor in debts[user]:
            debtor_name = list(debtor.keys())[0]
            for debtor2 in debts[debtor_name]:
                # check if the debtor owes money
                for user2 in debtor2:
                    if user2 == user:
                        if debtor[debtor_name] > debtor2[user2]:
                            debtor[debtor_name] -= debtor2[user2]
                            debtor2[user2] = 0
                        else:
                            debtor2[user2] -= debtor[debtor_name]
                            debtor[debtor_name] = 0
                    elif synergie(user2, debts[user]):
                        if debtor[debtor_name] > debtor2[user2]:
                            tmp = debtor[debtor_name]
                            debtor[debtor_name] -= debtor2[user2]
                            for i in debts[user]:
                                if list(i.keys())[0] == user2:
                                    i[user2] += tmp - debtor[debtor_name]
                                    break
                            debtor2[user2] = 0
                        else:
                            tmp = debtor2[user2]
                            debtor2[user2] -= debtor[debtor_name]
                            for i in debts[user]:
                                if list(i.keys())[0] == user2:
                                    i[user2] += tmp - debtor2[user2]
                                    break
                            debtor[debtor_name] = 0
    # print all debts
    for user in debts:
        for debtor in debts[user]:
            debtor_name = list(debtor.keys())[0]
            if debtor[debtor_name] != 0:
                print(user, "owes", debtor_name, debtor[debtor_name])

def synergie(user, array):
    for i in array:
        if user == list(i.keys())[0]:
            return True
    return False