from UI.book_menu import BookMenu, MemberMenu,LoanMenu,LoanReport

def main():
    while True:
        print("""
==============================
LIBRARY MANAGEMENT SYSTEM
==============================
1. Book Management
2. Member Management
3. Loan Management
4. Reports
5. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            BookMenu().bookchoose_option()

        elif choice == "2":
            MemberMenu().Member_chooseOption()

        elif choice == "3":
            LoanMenu().Loan_chooseOption()

        elif choice == "4":
           LoanReport().Report_chooseOption()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()