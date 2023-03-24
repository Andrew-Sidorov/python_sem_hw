Class PhoneBook:


def __int__(self, path: str):
    self.path = path
    self.phone_list = []
    self.open()


def open(self):
    with open(self.path, 'r', encoding="UTF-8") as file:
        data = file.readlines()
    for contact in data:
        new_cont = contact.strip().split(':')
        self.phone_list.append(Contact(*new_cont))


def save(self):
    data = '\n'.join([contact.to_str() for contact in self.phone_list])
    with open(self.path, 'w', encoding="UTF-8") as file:
        file.write(data)


def main_menu(self):
    return '''Glavnoe menu:
    1. Vse contact
    2. Sozdat contact
    3. Nayti contact
    4. Izmenit contact
    5. Delete contact
    6. Save contact
    7. Exit'''


def new_contact(self, name: str, phone: str | int, comment: str):
    self.phone_list.append(Contact(name, phone, comment))
