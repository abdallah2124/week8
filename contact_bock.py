from contact import Contact

class Contact_book:

    def __init__(self):

        self.contacts=dict()
        

    def add (self,contact):
        self.contacts[contact.id]=contact
