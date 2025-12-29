class employee_signup:
    company="regex"
    c_mail="regex@gmail.com"
    turnover=("100 cr")

    def information(self):
        print("Employee information :",self.c_mail, self.c_mail.split("@")[1])

e1=employee_signup()
e1.information()
print(e1.turnover)
