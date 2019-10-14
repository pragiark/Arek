class User():
    """Class user"""

    def __init__(self, first_name, last_name, login, password, email):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.email = email

    def describe_user(self):
        print("Dane uzytkownika: \n" + self.first_name + " " + self.last_name + "\n" + self.login + "\n" + \
        self.password + "\n" + self.email)

    def greet_user(self):
        print("Witaj " + self.first_name + " " + self.last_name +"." + " Twój login to: " + self.login
        + ", hasło to Twoje tajemnicze hasło")

user_arek = User("Arek", "Pragier", "arkpra", "as", "as@as.pl")
#user_arek.describe_user()
user_arek.greet_user()
user_paulina = User("Paulina", "Pragier", "pulus20", "qwertyas", "pa@pa.pl")
#user_paulina.describe_user()
user_paulina.greet_user()

user_celina = User("Celina", "Pragier", "celka", "asd", "cela@cela.pl")
user_celina.greet_user()

user_michalina = User("Michalina", "Pragier", "misia", "123", "misi@as.pl")
user_michalina.greet_user()