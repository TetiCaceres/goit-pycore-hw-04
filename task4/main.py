# Splits input into command and arguments
def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, *args

# Check if phone is digits only, optionally starting with '+'
def is_valid_phone(phone):
    return phone.isdigit() or (phone.startswith("+") and phone[1:].isdigit())

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Usage: add [name] [phone]"
    name, phone = args
    if not is_valid_phone(phone):
        return "Invalid phone number. Use only digits, optionally starting with +."
    contacts[name] = phone
    return "Contact added."

#Change an existing contact's phone number
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid arguments. Usage: change [name] [new_phone]"
    name, new_phone = args
    if not is_valid_phone(new_phone):
        return "Invalid phone number. Use only digits, optionally starting with +."
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."
    
  
#Show the phone number of a given contact    
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]."
    
    name = args[0]
    phone = contacts.get(name)
    if phone :
        return f"{name}'s phone: {phone}"
    else:
        return f"No contact found for {name}"

#Show all contacts in the dictionary.
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{i+1}. {name}: {phone}" for i, (name, phone) in enumerate(contacts.items()))


#Handles user input and executes commands
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")          
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            elif command == "":
                # Empty input, ignore
                continue
            else:
                print("Invalid command.")
        
        except Exception as e:
            # Catch any unexpected errors to prevent crash
            print(f"Unexpected error: {e}")
           


if __name__ == "__main__":
    main()
