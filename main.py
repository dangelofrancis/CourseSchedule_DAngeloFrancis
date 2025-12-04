
# PROJECT TITLE: Course Schedule
# PROGRAMMER: D'Angelo Francis
# DUE DATE: 11/21/2025
# REQUIREMENTS: 

# FILE NAME: main.py 
# REQUIREMENTS: Drives the program and contains a menu system

from schedule import Schedule

def main():
    schedule = Schedule()
    schedule.load_from_csv("courses.csv")

    while True:
        print("\nMENU:")
        print("1. Display All")
        print("2. Search by Subject")
        print("3. Search by Subject + Catalog")
        print("4. Search by Instructor")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            schedule.print()

        elif choice == "2":
            subject = input("Enter Subject: ").upper()
            results = schedule.find_by_subject(subject)
            schedule.print_header()
            for item in results:
                item.print()

        elif choice == "3":
            subject = input("Enter Subject: ").upper()
            catalog = input("Enter Catalog: ")
            results = schedule.find_by_subject_catalog(subject, catalog)
            schedule.print_header()
            for item in results:
                item.print()

        elif choice == "4":
            last_name = input("Enter Instructor Last Name: ")
            results = schedule.find_by_instructor_last_name(last_name)
            schedule.print_header()
            for item in results:
                item.print()

        elif choice == "5":
            print("Exiting Program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
