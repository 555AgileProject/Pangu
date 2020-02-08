import datetime
from prettytable import PrettyTable

class Individual:
    def __init__(self, id):
        """a new instance for a individual"""
        self._id = id
        self._name = ''
        self._gender = ''
        self._bday = ''
        self._age = ''
        self._alive = True
        self._dday = 'N/A'
        self._child = 'N/A'
        self._spouse = 'N/A'

class Family:
    def __init__(self, id, married, divorced, hus, wife, child_id):
        self.id = id
        self.mar_date = married
        self.div_date = divorced
        self.hus_id = hus
        self.wife_id = wife
        self.child_id = child_id

class Repository:

#HelloWOrldS
