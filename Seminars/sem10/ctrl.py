import phone_book
import view

pb = phone_book.PhoneBook('phone_db.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Viberetyi punkt menu: '))
    match choice:
        case 1:
            view.print_pb(pb)
        case 2:
            name = input('Vvedite name: ')
            phone = input('Vvedite phone: ')
            comment = input('Vvedite comment: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Vvedite poiskovoi zapros: ')
            view.print_pb(pb.search(word))
        case 4:
            view.print_pb(pb)
            index = int(input('Vvedite index kontatov: '))
            name = input('Vvedite name (ili Enter - bez izmeneniy): ')
            phone = input('Vvedite phone (ili Enter - bez izmeneniy): ')
            comment = input('Vvedite comment (ili Enter - bez izmeneniy): ')
            pb.change(index-1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Vvedite index contactov, kotoryi delete: '))
            pb.delete(index-1)
        case 6:
            pb.save()
        case 7:
            break
