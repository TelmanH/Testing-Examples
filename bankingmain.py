# Write your code here
import sqlite3
import random
import sys

conn = sqlite3.connect('card.s3db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS card(
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER);""")

#c.execute(('DROP TABLE card;'))
#c.fetchall()
conn.commit()


class BankingSystem():
    #all_card_info = {}

    def init(self):
        self.pin = ''
        self.card_number = ''
        #self.id_calc = id_calc

    def creatingaccount(self):

        random.seed()
        self.card_number = '400000'
        for i in range(9):
            self.card_number += str(random.randint(0, 9))
        self.pin_number = ''
        for i in range(4):
            self.pin_number += str(random.randint(0, 9))

        num = [self.card_number]
        num = list(map(int, num))[::-1]

        lista = []
        lista[:0] = self.card_number
        sum = 0
        for i in range(len(lista)):
            if i % 2 == 0:
                lista[i] = int(lista[i]) * 2
                if int(lista[i]) > 9:
                    lista[i] = int(lista[i]) - 9
            sum += int(lista[i])
        if sum % 10 == 0:
            self.card_number += '0'
        else:
            self.card_number += str(((sum // 10) + 1) * 10 - sum)

        print("Your card has been created")
        print("Your card number:")
        print(self.card_number)
        print("Your card PIN:")
        print(self.pin_number)
        #BankingSystem.all_card_info[self.card_number] = self.pin_number
        id_calc = len(c.fetchall()) + 1
        c.execute("INSERT INTO card (id, number, pin, balance) VALUES (?,?,?,?)", (id_calc, self.card_number, self.pin_number, 0))
        conn.commit()
        action()

    def loginaccount(self):
        print("Enter your card number:")
        cardnumber = input()

        print("Enter your PIN:")
        cardpin = input()

        c.execute('SELECT number, pin FROM card WHERE number=? AND pin=?', (cardnumber, cardpin))
        res = c.fetchone()

        if res:

            print('You have successfully logged in!')
            print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
            types2 = int(input())
            while types2 != 0:

                if types2 == 1:
                    c.execute('SELECT balance FROM card')
                    print("Balance: ", c.fetchone())
                    #print('Balance: 0')
                    conn.commit()
                elif types2 == 5:
                    print('You have successfully logged out!')
                    action()
                    break
                elif types2 == 2:
                    print('Enter income:')
                    income = int(input())
                    c.execute("SELECT balance FROM card WHERE number=?", (cardnumber,))
                    new_balance = (c.fetchall())[0][0] + income
                    c.execute("UPDATE card SET balance = ? WHERE number=?", (new_balance, cardnumber,))
                    conn.commit()
                    print('Income was added!')
                elif types2 == 3:
                    print("\n Transfer")
                    print("Enter card number:")
                    transfer_account = input()
                    c.execute("SELECT balance FROM card WHERE number=?", (cardnumber,))
                    balance = (c.fetchall())[0][0]
                    if cardnumber == transfer_account:
                        print("You can't transfer money to the same account!")
                    else :
                        num = transfer_account
                        #num = list(map(int, num))[::-1]


                        check = int(str(num)[-1])
                        num_list = [int(x) for x in str(num)[0:15]]
                        for i in range(len(num_list)):
                            if (i + 1) % 2 == 1:
                                num_list[i] *= 2
                            if num_list[i] > 9:
                                num_list[i] -= 9
                        luhn = (sum(num_list) + check)
                        if luhn % 10 == 0:

                            c.execute("SELECT number FROM card")
                            accounts = (c.fetchall())
                            accounts = [i[0] for i in accounts]
                            if transfer_account not in accounts:
                                print("Such a card does not exist.")
                            else:
                                print("Enter how much money you want to transfer:")
                                transfer_money = int(input())
                                if (balance - transfer_money) <= 0:
                                    print('Not enough money!')
                                else:
                                    new_balance = balance - transfer_money
                                    c.execute("UPDATE card SET balance = ? WHERE number=?",
                                                (new_balance, cardnumber,))
                                    conn.commit()
                                    c.execute("SELECT balance FROM card WHERE number=?", (transfer_account,))
                                    new_balance2 = (c.fetchall())[0][0] + transfer_money
                                    c.execute("UPDATE card SET balance = ? WHERE number=?",
                                                (new_balance2, transfer_account,))
                                    conn.commit()
                                    print('Success!\n')
                        else:
                            #self.card_number += str(((sum // 10) + 1) * 10 - sum)
                            print("Probably you made mistake in the card number. Please try again!\n")

                elif types2 == 4:
                    c.execute("SELECT balance FROM card WHERE number=?", (cardnumber,))
                    c.execute("DELETE FROM card WHERE number=?", (cardnumber,))
                    conn.commit()
                    print('The account has been closed!\n')



                print('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
                types2 = int(input())

            print('Bye!')
            sys.exit()

        else:
            print("Wrong card number or PIN!")
            action()


def action():
    print("""1. Create an account
2. Log into account
0. Exit""")
    types = int(input())

    if types == 1:

        BankingSystem().creatingaccount()

    elif types == 2:

        BankingSystem().loginaccount()

    else:

        print('Bye!')
        sys.exit()
        conn.close()


action()