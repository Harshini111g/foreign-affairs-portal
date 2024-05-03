class ForeignAffairsPortal:
    def __init__(self):
        self.data = {}

    def create_entry(self, country, information):
        if country in self.data:
            print("Entry already exists. Use update function to modify.")
        else:
            self.data[country] = information
            print(f"Entry for {country} created successfully.")

    def read_entry(self, country):
        if country in self.data:
            print(f"Information for {country}: {self.data[country]}")
        else:
            print("Entry does not exist.")

    def update_entry(self, country, information):
        if country in self.data:
            self.data[country] = information
            print(f"Information for {country} updated successfully.")
        else:
            print("Entry does not exist. Use create function to add.")

    def delete_entry(self, country):
        if country in self.data:
            del self.data[country]
            print(f"Entry for {country} deleted successfully.")
        else:
            print("Entry does not exist.")

def main():
    portal = ForeignAffairsPortal()

    while True:
        print("\nForeign Affairs Information Portal")
        print("1. Create Entry")
        print("2. Read Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            country = input("Enter the country name: ")
            information = input("Enter information about the country: ")
            portal.create_entry(country, information)
        elif choice == '2':
            country = input("Enter the country name to read: ")
            portal.read_entry(country)
        elif choice == '3':
            country = input("Enter the country name to update: ")
            information = input("Enter updated information: ")
            portal.update_entry(country, information)
        elif choice == '4':
            country = input("Enter the country name to delete: ")
            portal.delete_entry(country)
        elif choice == '5':
            print("Exiting the portal.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
