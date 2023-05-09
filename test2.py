class PhoneBook:
    contacts = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def add_contact(cls, contact_str):
        name, phone_number = contact_str.split()
        contact = cls(name, phone_number)
        cls.contacts.append(contact)
        print(f"Contact {name} has been added to the phone book.")

    @classmethod
    def change_phone(cls, name, new_phone_number):
        for contact in cls.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                print(f"Phone number for {name} has been updated to {new_phone_number}.")
                break
        else:
            print(f"No contact with name {name} found.")

    @classmethod
    def print_contacts(cls):
        print("Phone book:")
        for contact in cls.contacts:
            print(f"Name: {contact.name}, Phone number: {contact.phone_number}")

    @classmethod
    def search_contact(cls, name):
        for contact in cls.contacts:
            if contact.name == name:
                print(f"Phone number for {name}: {contact.phone_number}")
                break
        else:
            print(f"No contact with name {name} found.")