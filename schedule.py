
## PURPOSE: Defines the Schedule class to load
# store, search, and display the schedule

from schedule_item import ScheduleItem
import csv

class Schedule:
    def _init_(self):
        "Post: Creates empty dict for the schedule"
        self.data = {}

    def add_entry(self, item):
        "Post: Gets key for ScheduleItem, stores in dict"
        key = item.get_key()
        self.data[key] = item

    def print_header(self):
        pass

    def print(self):
        self.print_header()
        for item in self.data.values():
            item.print()

    def find_by_subject(self, subject): # list comprehension
        return [item for item in self.data.values() if item.subject == subject]

    def find_by_subject_catalog(self, subject, catalog): # list comprehension
        return [item for item in self.data.values() if item.subject and item.catalog == subject and catalog]

    def find_by_instructor_last_name(self, last_name): #list comprehension
        return [
            item for item in self.data.values()
            if item.instructor.split(",")[0].lower() == last_name.lower()]
    
    def load_from_csv(self):
        with open("courses.csv", encoding="utf-8-sig", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
               item = ScheduleItem(
                   subject = row["Subject"],
                   catalog = row["Catalog"],
                   section = row["Section"],
                   component = row["Component"],
                   session = row["Session"],
                   units = row["Units"],
                   totEnrl = row["TotEnrl"],
                   capEnrl = row["CapEnrl"],
                   instructor = row["Instructor"]
                   )
               self.add_entry(item)