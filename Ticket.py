

from os import name

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


class Ticket():

    # ticket_id: 2000
    # name: None
    # staff_id: None
    # email: None
    # issue: None

    def __init__(self, ticket_id, name, staff_id, email, issue):
        self.ticket_id = ticket_id
        self.name = name
        self.staff_id = staff_id
        self.email = email
        self.issue = issue
        self.response = "Not Provided"
        self.status = "Open"

        if self.issue.find("change") > -1 and self.issue.find("password") > -1:
            password = staff_id[:2] + name[:3]
            self.response = f"{Bold}Your new password is -> {ResetBold}{password}{ResetUnderlined}"
            self.status = f"{Green}Closed{Reset}"
