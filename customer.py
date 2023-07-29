class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class CustomerManagementSystem:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_customers(self):
        print("Customer List: harish")
        for idx, customer in enumerate(self.customers, 1):
            print(f"{idx}. Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

    def search_customer(self, name):
        found_customers = [customer for customer in self.customers if customer.name.lower() == name.lower()]
        if found_customers:
            print("Search Results:")
            for idx, customer in enumerate(found_customers, 1):
                print(f"{idx}. Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")
        else:
            print("No customers found with the given name.")

def main():
    customer_system = CustomerManagementSystem()

    while True:
        print("\nCustomer Management System Menu:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone number: ")
            customer = Customer(name, email, phone)
            customer_system.add_customer(customer)
            print("Customer added successfully!")

        elif choice == "2":
            customer_system.view_customers()

        elif choice == "3":
            name = input("Enter customer name to search: ")
            customer_system.search_customer(name)

        elif choice == "4":
            print("Exiting the Customer Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
