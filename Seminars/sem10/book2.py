def new_contact(self, name: str, phone: str | int, comment: str):
    self.phone_list.append(Contact(name, phone, comment))


def search(self, find: str):
    result = []
    for contact in self.phone_list:
        if find in contact.to_str():
            result.append(f'{contact}')
    return '\n'.join(result)


def change(self, index: int, name: str, phone: str, comment: str):
    name = name if name != '' else self.phone_list[index].name
    phone = phone if phone != '' else self.phone_list[index].phone
    comment = comment if comment != '' else self.phone_list[index].comment
    self.phone_list[index] = Contact(name, phone, comment)


def delete(self, index: int):
    self.phone_list.pop(index)


def __str__(self)
 result = ''
  i = 0
   for contact in self.phone_list:
        i += 1
        result += f'{i}. {contact}\n'
    return result[:-2]
