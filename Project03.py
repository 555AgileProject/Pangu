import datetime
from prettytable import PrettyTable
from Project02 import file_reading_gen


class Individual:
    def __init__(self, id):
        """a new instance for a individual"""
        self.id = id
        self.name = ''
        self.gender = ''
        self.bday = ''
        self.age = ''
        self.alive = True
        self.dday = 'N/A'
        self.child = 'N/A'
        self.spouse = 'N/A'


class Family:
    def __init__(self, id, married, divorced, hus, wife, child):
        self.id = id
        self.mar_date = married
        self.div_date = divorced
        self.hus_id = hus
        self.wife_id = wife
        self.child_id = child


class Repository:
    def __init__(self, d):
        self.dir = d
        self.indi = {}
        self.fam = {}
        self._analyze_files()

    def _analyze_files(self):
        array = []
        for eachrow in file_reading_gen(self.dir):
            readline = eachrow.split("|")

            if (readline[1] in ["INDI", "FAM"]):
                # Create New Family and push existing into the respective function
                orig = readline[1]
                if (orig == "INDI"):
                    Individual()  # pass the attributes of self.data to it
                else:
                    Family()
                array = []
            else:
                # Add the details to existing Repo and continue iteration
                # array.append(readline)
                if (orig == "condition"):
                    pass
                    # check and add to the self.parameter.

    def pretty_print(self):
        """ print out the pretty table of individual summary and family summary"""
        pti = PrettyTable(
            field_names=['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
        for key, d in self.indi.items():
            pti.add_row([key, d.name, d.gender, d.bday, d.age, d.alive, d.dday, d.child, d.spouse])
        print(pti.get_string(title="Individuals"))

        ptf = PrettyTable(
            field_names=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
        for key, d in self.fam.items():
            pti.add_row(
                [key, d.mar_date, d.div_date, d.hus_id, self.indi[d.hus_id].name, d.wife_id, self.indi[d.wife_id].name,
                 d.child_id])
        print(ptf.get_string(title="Families"))


# This is Test branch
Repository("C:\\Users\\arunn\\Desktop\\Masters!\\SSW-555_Agile\\TeamProject\\proj02test.ged")
