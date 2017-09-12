
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []
    
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        print('\nContact {} with phone {} and email {} successfuly added!'.format(name, phone, email))
        self._save()
    
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
    
    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(contact.name))
        print('Phone number: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * ---')

    def delete(self, name):
        # First option - only delete first occurence
        #for contact in self._contacts:
        #    if contact.name.lower() == name.lower():
        #        self._contacts.remove(contact)
        #        print('Contact {} removed!'.format(name))

        # Second option
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                print('Contact {} deleted!'.format(name))
                break
    
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
            else:
                self._not_found()
    
    def _not_found(self):
        print('******************')
        print('CONTACT NOT FOUND!')
        print('******************')


    def edit(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self._update_contact(idx)
                break
        else:
            print('Contact {} does not exists'.format(name))
    
    def _update_contact(self, idx):
        name = str(raw_input('New name: '))
        phone = str(raw_input('New phone number: '))
        email = str(raw_input('New email address: '))

        self._contacts[idx].name = name
        self._contacts[idx].phone = phone
        self._contacts[idx].email = email

        self._save()

        print('Contact updated!!!')

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )
def run():
    
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])


    while True:
        command = str(raw_input('''
            Choose an option:

            [a] Add contact
            [ac] Update contact
            [b] Search contact
            [e] Delete contact
            [l] Show contact list
            [s] Exit
        '''))

        if command == 'a':
            name = str(raw_input('Write contact name: '))
            phone = str(raw_input('Write contact phone: '))
            email = str(raw_input('Write contact email: '))
            
            contact_book.add(name, phone, email)
        elif command == 'ac':
            name = str(raw_input('Write contact name to update: '))

            contact_book.edit(name)
        elif command == 'b':
            name = str(raw_input('Contact name for search: '))

            contact_book.search(name)
        elif command == 'e':
            name = str(raw_input('Contact name for delete: '))

            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('Command not found')

if __name__ == '__main__':
    print('B I E N V E N I D O   A  L A   A G E N D A')
    run()