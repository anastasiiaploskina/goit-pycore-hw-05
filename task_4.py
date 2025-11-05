
import re


TOTAL_WIDTH = 120
COMMAND_COLUMN_WIDTH = 25
FORMAT_COLUMN_WIDTH = 30


# Stores all the commands available in the bot (used in get_help() function)
COMMAND_REGISTRY = [
    {
        "command": "hello",
        "format": "hello",
        "description": "Ask 'How can I help you?'"
    },
    {
        "command": "add <NAME> <PHONE>",
        "format": "add Anna +380633727223",
        "description": "Add new contact to your contacts list."
    },
    {
        "command": "change <NAME> <PHONE>",
        "format": "change Daniil +380637927223",
        "description": "Change a specified contact's phone number."
    },
    {
        "command": "phone <NAME>",
        "format": "phone John",
        "description": "Return a specified contact's phone number."
    },
    {
        "command": "all",
        "format": "all",
        "description": "Return all contacts as a box."
    },
    {
        "command": "help",
        "format": "help",
        "description": "Return help for commands as a box."
    }
]


# KeyError, ValueError, IndexError
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Missing arguments. Please provide both name and phone number."
        except KeyError:
            return "Contact not found. Please check the name and try again."
        except IndexError:
            return "Insufficient arguments. Please provide the required information."
    return inner


# Parse an user input to receive command and other arguments
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Add new contact
@input_error
def add_contact(args, contacts):
    name, phone = args
    pattern = r'^\+380\d{9}$'
    match = re.fullmatch(pattern, phone)

    if not match:
        return "Invalid phone number format. Please try again starting with +380."

    contacts[name] = phone
    return "Contact added."


# Change phone number 
@input_error
def change_number(args, contacts):
    name, phone = args
    pattern = r'^\+380\d{9}$'
    match = str(re.search(pattern, phone))

    if name not in contacts:
        raise KeyError

    if not match:
        return "Invalid phone number format. Please try again starting with +380."

    contacts.update({name: phone})
    return "Contact changed."


# Show phone number of a specified contact
@input_error
def show_phone(args, contacts):
    name = args
    user = "".join(name)

    if user not in contacts:
        raise KeyError

    phone = contacts.get(user)
    return f"{user}'s phone number is {phone}."


# Show all contacts within a box, if there are no contacts show empty box
@input_error
def show_all_contacts(contacts):
    users_lines = []

    num_contacts = len(contacts)
    header_text = f"CONTACTS LIST ({num_contacts} Contacts)".center(TOTAL_WIDTH)
    users_lines.append("╔" + "═" * TOTAL_WIDTH + "╗")
    users_lines.append("║" + header_text + "║")
    users_lines.append("╟" + "─" * TOTAL_WIDTH + "╢")

    for name, phone in contacts.items():
        user_info = f"{name}'s phone number is {phone}.".ljust(TOTAL_WIDTH - 1)
        middle_section = "║ " + user_info + "║"
        users_lines.append(middle_section)

    users_lines.append("╚" + "═" * TOTAL_WIDTH + "╝")

    return "\n".join(users_lines)


# Dynamic help box, assosiated with COMMAND REGISTRY constant
def get_help():
    help_lines = []

    help_lines.append("╔" + "═" * TOTAL_WIDTH + "╗")
    header_text = "ASSISTANT BOT'S HELP".center(TOTAL_WIDTH)
    help_lines.append("║" + header_text + "║")
    help_lines.append("╟" + "─" * TOTAL_WIDTH + "╢")

    utility_line = ("Command".ljust(COMMAND_COLUMN_WIDTH) +
                    "Example".ljust(FORMAT_COLUMN_WIDTH) +
                    "Description")

    help_lines.append("║" + utility_line.ljust(TOTAL_WIDTH) + "║")
    help_lines.append("╟" + "─" * TOTAL_WIDTH + "╢")

    for item in COMMAND_REGISTRY:
        command = item["command"].ljust(COMMAND_COLUMN_WIDTH)
        example = item["format"].ljust(FORMAT_COLUMN_WIDTH)
        description = item["description"]

        line = f"{command}{example}{description}".ljust(TOTAL_WIDTH)
        help_lines.append("║" + line + "║")

    help_lines.append("╚" + "═" * TOTAL_WIDTH + "╝")

    return "\n".join(help_lines)


# Operate the whole program, store all contacts, ask for an input,
# match commands to execute them
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_number(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command == "help":
            print(get_help())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
