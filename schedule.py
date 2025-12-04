
# FILE NAME: schedule.py
# REQUIREMENTS: Defines the Schedule class to load
#               store, search, and display the schedule

from schedule_item import ScheduleItem
import csv

class Schedule:
    def __init__(self):
        """
            Pre: None

            Post: Creates empty dict for the schedule.    
        """
        self.data = {}

    def add_entry(self, item):
        """
            Pre: item is a ScheduleItem

            Post: Adds item to the schedule dict
        """
        key = item.get_key()
        self.data[key] = item

    def print_header(self):
        """
            Pre: None

            Post: Prints the formatted header
        """
        print(f"{'Subject':<8} {'Catalog':<8} {'Section':<8} "
              f"{'Component':<10} {'Session':<6} {'Units':<5} "
              f"{'TotEnrl':<8} {'CapEnrl':<8} Instructor")

    def print(self):
        """
            Pre: None

            Post: Prints all schedule items
        """
        self.print_header()
        for item in self.data.values():
            item.print()

    def find_by_subject(self, subject):
        """
            Pre: subject is a string

            Post: Returns list of ScheduleItems matching subject
        """
        return [item for item in self.data.values() if item.subject == subject]

    def find_by_subject_catalog(self, subject, catalog):
        """
            Pre: subject and catalog are strings

            Post: Returns list of ScheduleItems matching subject and catalog
        """
        return [
            item for item in self.data.values()
            if item.subject == subject and item.catalog == catalog
        ]

    def find_by_instructor_last_name(self, last_name):
        """
            Pre: last_name is a string

            Post: Returns list of ScheduleItems matching instructor last name
        """
        last_name = last_name.lower().strip()

        results = []
        for item in self.data.values():
            csv_last = item.instructor.split(",")[0].lower().strip()

            # allow partial match (Anderson matches Anderson Jr.)
            if last_name in csv_last:
                results.append(item)

        return results


    def load_from_csv(self, filename):
        """
            Pre: filename is a string

            Post: Loads schedule data from CSV file
        """
        with open(filename, encoding="utf-8-sig", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = ScheduleItem(
                    subject=row["Subject"],
                    catalog=row["Catalog"],
                    section=row["Section"],
                    component=row["Component"],
                    session=row["Session"],
                    units=int(row["Units"]),
                    totEnrl=int(row["TotEnrl"]),
                    capEnrl=int(row["CapEnrl"]),
                    instructor=row["Instructor"]
                )
                self.add_entry(item)
