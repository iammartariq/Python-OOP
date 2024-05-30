class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_items(self, name, number, email):
        self.contacts.append({"Name":name, "Contact" : number, "Email" : email})

    def print_enteries(self):
        for contact in self.contacts:
            print(contact)

    def sort_enteries(self):
        self.contacts.sort(key= lambda x : x["Name"])

    def search(self, n):
        found = [contact for contact in self.contacts if n.lower() in contact["Name"].lower()]
        return found

a = Phonebook()
a.add_items("Ammar", "03303753291", "ammar@gmail.com")
a.add_items("Maham", "03313864762", "ammar@gmail.com")
a.print_enteries()
a.sort_enteries()
a.search("03313864762")