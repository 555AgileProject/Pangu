import datetime
from prettytable import PrettyTable

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
    def __init__(self,d):
        self.dir=d
        self.indi={}
        self.fam={}
        self._analyze_files()

    def _analyze_files(self):
        pass

    def pretty_print(self):
        pass


#This is Test branch
