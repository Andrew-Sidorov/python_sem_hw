import model
import view


def start():
    while True:
        pd = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранён')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pd, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index(
                        'Введите номер изменяемого контакта')
                    contact = view.change_contact(pd, index)
                    model.change_contact(contact, index)
                    view.show_message(
                        f'Контакт{model.get_phone_book()[index-1].get("name")} успешно изменён')
            case 6:
                search = view.input_search('Введите искомый элемент ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты не найдены')
            case 7:
                return            
