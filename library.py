# Global list to store data: Each book is a dict {'title': '...', 'author': '...', 'is_available': True} 
library = [] 
 
def add_book(): 
    # Input title, author -> append to library list 
    print("Book added successfully.") 
 
def view_books(): 
    # Loop through library list and print details 
    pass 
 
def search_book(): 
    # Input search query 
    # Loop and check if query is in book title 
    pass 
 
def main(): 
    while True: 
        print("\n--- LIBRARY MANAGEMENT SYSTEM ---") 
        print("1. Add New Book") 
        print("2. View All Books") 
        print("3. Search Book") 
        print("4. Exit") 
         
        choice = input("Enter your choice: ") 
         
        if choice == '1': 
            add_book() 
        elif choice == '2': 
            view_books() 
        elif choice == '3': 
            search_book() 
        elif choice == '4': 
            print("Exiting program.") 
            break 
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == "__main__": 
    main()