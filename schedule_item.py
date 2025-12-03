
## PURPOSE: Defines the ScheduleItem class
## to hold individual course information

from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    totEnrl: int
    capEnrl: int
    instructor: str

    def get_key(self) -> str: 
        " Post: Returns a unique string key"
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        " Post: Prints the formatted details"
        print(f"{self.subject:<8} {self.catalog:<8} {self.section:<8} "
              f"{self.component:<10} {self.session:<6} {self.units:<5} "
              f"{self.totEnrl:<8} {self.capEnrl:<8} {self.instructor}")
       