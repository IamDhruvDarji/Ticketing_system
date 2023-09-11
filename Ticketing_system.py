from Ticket import Ticket

Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[95m"
Cyan = "\033[36m"
LightGray = "\033[37m"
LightYellow = "\033[93m"
Reset = "\033[0m"
Bold = "\033[1m"
Underline = "\033[4m"
ResetBold = "\033[21m"
ResetUnderlined = "\033[24m"


class Ticketing_system:

    def __init__(self):
        self.tickets = []
        self.counter = 2000
        self.open_tickets = 0
        self.total_tickets = 0

        # t1 = Ticket(self.counter, "Dhruv", "DDD",
        #             "d@gmail.com", "pc not working")
        # self.tickets.append(t1)
        # self.counter += 1

        # t2 = Ticket(self.counter, "Graham", "GGG", "g@gmail.com",
        #             "Parking not available")
        # self.tickets.append(t2)
        # self.counter += 1

        # t3 = Ticket(self.counter, "Marina", "MMM",
        #             "m@gmail.com", "Wifi is slow")
        # self.tickets.append(t3)
        # self.counter += 1

    def Submit_ticket(self):
        Ticket_id = self.counter
        print("◤━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◥")
        staff_id = input(
            f"{Bold}{Magenta}Enter Your Staff ID : {ResetBold}{Reset}")
        name = input(
            f"{Bold}{Magenta}Enter Your name : {ResetBold}{Reset}")
        email = input(
            f"{Bold}{Magenta}Enter Your E-mail ID : {ResetBold}{Reset}")
        issue = input(
            f"{Bold}{Magenta}What is the issue : {ResetBold}{Reset}")

        ticket = Ticket(Ticket_id, name, staff_id, email, issue)
        self.tickets.append(ticket)
        self.counter += 1
        if ticket.status == "Open":
            self.open_tickets += 1
            self.total_tickets += 1
        print("◣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◢")
        print("")
        print(f"{Green}Your ticket is submitted successfully{Reset}")

    # def Display(self):
    #     print("*** ALL TICKETS ***")

    #     for t in self.tickets:
    #         t.display()

    def Display_tickets(self):
        for ticket in self.tickets:
            print("")
            print(Magenta, "・・★・★・★・・", Reset, Red, "TICKET",
                  Reset, Magenta, "・・★・★・★・・", Reset)
            print("")
            print(LightYellow, "Ticket ID : ", Reset, ticket.ticket_id)
            print(LightYellow, "Name : ", Reset, ticket.name)
            print(LightYellow, "Staff ID : ", Reset, ticket.staff_id)
            print(LightYellow, "e-mail : ", Reset, ticket.email)
            print(LightYellow, "Issue : ", Reset, ticket.issue)
            print(LightYellow, "Response : ", Reset, ticket.response)
            print(LightYellow, "Status : ", Reset, Red, ticket.status, Reset)
            print(Magenta, "︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿", Reset)

    # def Generate_new_Password(self, Ticket):
    #     if "Change password" in Ticket.issue:
    #         return Ticket.staff_id[:2] + Ticket.name[:3]
    #     else:
    #         return "Not applicable"

    def Response_ticket(self):
        try:
            TID = int(input("Ticket id :"))
        except:
            print(Red, Bold, "Incorrect ticket ID", ResetBold, Reset)
            return

        for t in self.tickets:
            if TID == t.ticket_id:
                resp = input("Enter Response: ")
                t.response = resp
                t.status = f"{Green}Closed{Reset}"
                self.open_tickets -= 1
                t.response = f"{Green}The issue has been resolved{Reset}"
                break

    def Reopen_ticket(self):
        try:
            TID = int(input("Ticket Id: "))
        except ValueError:
            print(f"{Red}Incorrect Ticket ID{Reset}")
            return
        for t in self.tickets:
            if TID == t.ticket_id:
                t.status = f"{Red}Reopened{Reset}"
                self.open_tickets += 1
                break

    # def Resolve_ticket(self):
    #     if self.status == "Open":
    #         self.status = "Closed"

    # def Reopen_ticket(self):
    #     if self.status == "Closed":
    #         self.status = "Reopened"

    # def Show_response(self, response):
    #     self.response = response

        # loop through the list of tickets
        # if ticketID == t.ticket_id
        # input respose
        # change the status

    def Statistics(self):
        print(Green, "Open Tickets : ", Reset, self.open_tickets)
        print(Red, "Closed Tickets : ", Reset,
              self.total_tickets - self.open_tickets)
        print("Total Tickets : ", self.total_tickets)

    def main_manu(self):
        print("")
        print(Green, "Welcome to Dhruv's Ticketing System !!!!", Reset)
        while True:
            print(Yellow, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", Reset)
            print(Blue)
            print("1. SUBMIT A TICKET")
            print("2. DISPLAY TICKET")
            print("3. RESPOND TO A TICKET")
            # print("4. CHANGE PASSWORD")
            print("4. REOPEN A TICKET")
            print("5. SHOW STATISTICS")
            print("6. EXIT")
            print("PLEASE CHOOSE A NUMBER FROM 1 TO 6")
            print(Reset)
            print(Yellow, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", Reset)
            print(Cyan)
            choice = input("YOUR CHOICE : ")
            print(Reset)
            if choice == "1":
                self.Submit_ticket()
            elif choice == "2":
                self.Display_tickets()
            elif choice == "3":
                self.Response_ticket()
            # elif choice == "4":
            #     self.Generate_new_Password
            elif choice == "4":
                self.Reopen_ticket()
            elif choice == "5":
                self.Statistics()
            elif choice == "6":
                print(Green, Bold, "Thank you for using My ticketing system!",
                      Red, "Byeee...!", ResetBold, Reset)
                break
            else:
                print(
                    Red, "Invalid input, Please choose number between 1 to 6 !!!", Reset)


ts = Ticketing_system()
# ts.Submit_ticket()
# ts.Submit_ticket()
# ts.Display_tickets()
ts.main_manu()
