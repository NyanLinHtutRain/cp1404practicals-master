# function main()
#     get name
#     choice = ""
#
#     while choice != "Q"
#         display menu()
#         get choice
#
#         if choice == "H"
#             display name
#         else if choice == "G"
#             display name
#         else if choice == "Q"
#             display Finished
#         else
#             display Invalid
#
#
# function display menu()
#     display (H)ello
#     display (G)oodbye
#     display (Q)uit
#
#
# main()
#

def main():
    name = input("Enter name: ")
    choice = ""

    while choice.upper() != "Q":
        display_menu()
        choice = input(">>> ").upper()

        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        elif choice == "Q":
            print("Finished")
        else:
            print("Invalid choice")


def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


main()
