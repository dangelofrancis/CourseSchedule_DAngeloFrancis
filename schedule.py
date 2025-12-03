
## PURPOSE: Defines the Schedule class to load
# store, search, and display the schedule

# schedule.py

from schedule_item import ScheduleItem
import csv

class Schedule:
    def __init__(self):
        """Creates empty dict for the schedule."""
        self.data = {}

    def add_entry(self, item):
        key = item.get_key()
        self.data[key] = item

    def print_header(self):
        print(f"{'Subject':<8} {'Catalog':<8} {'Section':<8} "
              f"{'Component':<10} {'Session':<6} {'Units':<5} "
              f"{'TotEnrl':<8} {'CapEnrl':<8} Instructor")

    def print(self):
        self.print_header()
        for item in self.data.values():
            item.print()

    def find_by_subject(self, subject):
        return [item for item in self.data.values() if item.subject == subject]

    def find_by_subject_catalog(self, subject, catalog):
        return [
            item for item in self.data.values()
            if item.subject == subject and item.catalog == catalog
        ]

    def find_by_instructor_last_name(self, last_name):
        last_name = last_name.lower().strip()

        results = []
        for item in self.data.values():
            csv_last = item.instructor.split(",")[0].lower().strip()

            # allow partial match (Anderson matches Anderson Jr.)
            if last_name in csv_last:
                results.append(item)

        return results


    def load_from_csv(self, filename):
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
