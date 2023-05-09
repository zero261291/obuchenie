class Phonebook:
    contacts = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def add_contact(cls, name, phone_number):
        contact = cls(name, phone_number)
        cls.contacts.append(contact)

    @classmethod
    def delete_contact(cls, name):
        for contact in cls.contacts:
            if contact.name == name:
                cls.contacts.remove(contact)

    @classmethod
    def change_phone(cls, name, new_phone_number):
        for contact in cls.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number

    @classmethod
    def print_contacts(cls):
        for contact in cls.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    @classmethod
    def search_contact(cls, name):
        for contact in cls.contacts:
            if contact.name == name:
                return contact.phone_number
        return None

#Здесь у меня затуп, не могу справиться

# создаем объекты контактов
contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact3)

# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()

# ищем контакт по имени
Phonebook.search_contact("Петр Петров")