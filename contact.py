class Contact :

    def __init__(self,user_name,f_name,l_name):
        self.user_name=user_name
        self.f_name=f_name
        self.l_name=l_name
        self.id=""
        self.email=list()
        self.phone_number=dict()
        self.avatar_url=""
        self.friends=set()

        print(f"Hi {self.f_name}  ")


def __str__(self):
    return f"""contact info : {self.f_name.title()}'' {self.l_name} & ==> {self.phone_number}    """


def set_user_name(self,user_name):
    self.user_name=user_name
    print(f"your user name has been  changed to {self.user_name}")

def set_f_name(self,f_name):
    self.f_name=f_name
    print(f"your first name has been  changed to {self.f_name}")


def set_l_name(self,l_name):
    self.l_name=l_name
    print(f"your last name has been  changed to {self.l_name}")


def set_phone_number(self,phone_number):
    self.phone_number=phone_number
    print(f"your phone number has been  changed to {self.phone_number}")

def get_user_name(self):
    return self.user_name

def get_f_name(self):
    return self.f_name


def get_l_name(self):
    return self.l_name

def get_phone_number(self):
    return self.phone_number

