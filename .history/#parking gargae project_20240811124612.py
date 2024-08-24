#parking gargae project
#enter and recieve ticket / decrease overall ticekts by 1
#spaces decrease by 1
#lp to indicate which car is parking
# how long will you park 
#return ticket 
#payment 
#exit 
#veh class
import math


class Parking:
    def __init__(self, total_spaces):
        # self.total_spaces = total_spaces
        self.available_spaces = total_spaces
        self.tickets = []
        self.current_ticket = {}

    def ticket(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            ticket_num = len(self.tickets) + 1
            # self.tickets.append({"ticket_num": ticket_num, "paid": False})
            # print(f"ticket {ticket_num}, please park.")
            self.current_ticket[ticket_num] = {"paid":False}
            self.tickets.append(self.current_ticket)
            print(f'your ticket is {ticket_num} DONT FORGET IT!!')

        else:
            print("we're full, come back another time")

    def paid_parking(self, ticket_num):
        for ticket in self.tickets:
            if ticket["ticket_num"] == ticket_num:
                print(f'')
            else:
                print(f"ticket {ticket_num} is paid.")
            return
            print(f"ticket {ticket_num} invalid.")

    def exit(self, ticket_num):
        for ticket in self.tickets:
            if ticket["ticket_num"] == ticket_num and ticket["paid"]:
                self.available_spaces += 1
                self.tickets.remove(ticket)
                print(f"thank you, drive safe.")
                return
        print("try again")


def main():
    garage = Parking(10)

    while True:
        choice = input("What would you like to do? 1:park 2: pay for parking 3: leave garage type 1,2,3! ")
        if choice ==1:
            garage.ticket()
        elif choice ==2:
            ticket_num input()
        elif choice ==3:
        else:


