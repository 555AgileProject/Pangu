from datetime import datetime, timedelta
from prettytable import PrettyTable
from Project02 import file_reading_gen
from dateutil.relativedelta import relativedelta

class Individual:
    def __init__(self, id):
        """a new instance for a individual"""
        self.id = id
        self.name = ''
        self.gender = ''
        self.bday = 'NA'
        self.age = ''
        self.alive = True
        self.dday = 'NA'
        self.child = 'NA'
        self.spouse = 'NA'


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

    def update_age(self):
        for indi in self.indi.values():
            if indi.bday != 'NA' and indi.dday != 'NA':
                indi.age = indi.dday.year - indi.bday.year - (
                        (indi.dday.month, indi.dday.day) < (indi.bday.month, indi.bday.day))

                indi.alive = False
            elif indi.bday != 'NA':
                today = datetime.today()
                indi.age = today.year - indi.bday.year - (
                        (today.month, today.day) < (indi.bday.month, indi.bday.day))
                indi.alive = True
            else:
                indi.age = 'NA'

    def _analyze_files(self):
        indi_index = {'NAME': 'name', 'SEX': 'gender', 'BIRT': 'bday', 'DEAT': 'dday', 'FAMC': 'child',
                      'FAMS': 'spouse'}
        fam_index = {'MARR': 'mar_date', 'HUSB': 'hus_id', 'WIFE': 'wife_id', 'CHIL': 'child_id', 'DIV': 'div_date'}
        indi_buff = Individual(None)
        indi_date_buff = [False, False]  # 0 indicates bday 1 indicates dday
        fam_buff = Family(None, 'NA', 'NA', 'NA', 'NA', set())
        fam_date_buff = [False, False]  # 0 indicates div_date 1 indicates mar_date
        for eachrow in file_reading_gen(self.dir):
            readline = eachrow.split("|")
            if (readline[0] == '0'):
                if (indi_buff.id != None):
                    # condition 1 push the individual buffer
                    new_indi = indi_buff
                    if new_indi.id not in self.indi.keys():
                        self.indi[new_indi.id] = new_indi
                    indi_buff = Individual(None)  # clear the buffer
                    indi_date_buff = [False, False]  # 0 indicates bday 1 indicates dday
                elif (fam_buff.id != None):
                    # condition 2 push the family buffer
                    new_fam = fam_buff
                    if new_fam.id not in self.fam.keys():
                        self.fam[new_fam.id] = new_fam
                    fam_buff = Family(None, 'NA', 'NA', 'NA', 'NA', set())  # clear the buffer
                    fam_date_buff = [False, False]  # 0 indicates div_date 1 indicates mar_date
                if (indi_buff.id == fam_buff.id == None):
                    # condition 3 set the ?_buffer's id
                    if (readline[1] in ["INDI", "FAM"]):
                        # Create New Family and push existing into the respective function
                        orig = readline[1]
                        if (orig == "INDI"):
                            indi_buff.id = readline[2]  # pass the attributes of self.data to it
                        else:
                            fam_buff.id = readline[2]
                    elif readline[1] == 'NOTE':
                        pass  # Ignore the line when there is a note

            elif (readline[0] == '1'):
                if (indi_buff.id != None):
                    # condition 1 for update indi_buff
                    if (readline[1] in ['BIRT', 'DEAT']):
                        if readline[1] == 'BIRT':
                            indi_date_buff[0] = True
                        else:
                            indi_date_buff[1] = True
                    else:
                        setattr(indi_buff, indi_index[readline[1]], readline[2])

                elif (fam_buff.id != None):
                    # condition 2 for update fam_buff
                    if (readline[1] in ['DIV', 'MARR']):
                        if readline[1] == 'DIV':
                            fam_date_buff[0] = True
                        else:
                            fam_date_buff[1] = True
                    elif readline[1] == 'CHIL':
                        fam_buff.child_id.add(readline[2])
                    else:
                        setattr(fam_buff, fam_index[readline[1]], readline[2])

            elif (readline[0] == '2'):
                if (readline[1] == 'DATE'):
                    try:
                        the_date = datetime.strptime(readline[2], '%d %b %Y').date()
                    except Exception as E:
                        the_date = datetime.strptime(readline[2], '%Y').date()  #what if this raises exception?
                    if indi_date_buff[0]:
                        indi_buff.bday = the_date
                        indi_date_buff[0] = False
                        continue
                    elif indi_date_buff[1]:
                        indi_buff.dday = the_date
                        indi_date_buff[1] = False
                    elif fam_date_buff[0]:
                        fam_buff.div_date = the_date
                        fam_date_buff[0] = False
                        continue
                    elif fam_date_buff[1]:
                        fam_buff.mar_date = the_date
                        fam_date_buff[1] = False
        self.update_age()

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
            hus_name, wife_name = 'NA', 'NA'
            if d.hus_id in self.indi:
                hus_name = self.indi[d.hus_id].name
            if d.wife_id in self.indi:
                wife_name = self.indi[d.wife_id].name
            ptf.add_row(
                [key, d.mar_date, d.div_date, d.hus_id, hus_name, d.wife_id, wife_name, d.child_id])
        print(ptf.get_string(title="Families"))

    def us06(self):
        '''Divorce can only occur before death of both spouses'''
        l = []
        for k, f in self.fam.items():
            if f.div_date != 'NA':
                d1 = self.indi[f.hus_id].dday
                d2 = self.indi[f.wife_id].dday
                if d1 != 'NA' and f.div_date > d1:
                    print(f"ERROR: FAMILY: US06: {k}: Divorced {f.div_date} after husband's death on {d1}")
                    l.append(k)
                if d2 != 'NA' and f.div_date > d2:
                    print(f"ERROR: FAMILY: US06: {k}: Divorced {f.div_date} after wife's death on {d2}")
                    l.append(k)
        return l

    def us07(self):
        '''Death should be less than 150 years after birth for dead people,
        and current date should be less than 150 years after birth for all living people'''
        l = []
        for k, i in self.indi.items():
            if i.age!='NA' and i.age >= 150:
                s = f'ERROR: INDIVIDUAL: US07: {k} More than 150 years old at death - Birth {i.bday}'
                if i.dday != 'NA':
                    s += f': Death {i.dday}'
                print(s)
                l.append(k)
        return l

    def us02(self):
        """Birth should occur before marriage of an individual"""
        l = []
        for x,y in self.fam.items():
            if self.indi[y.hus_id].bday != "NA" and y.mar_date != "NA" and self.indi[y.wife_id].bday!="NA":       #both birthdates are available
                if(self.indi[y.hus_id].bday > y.mar_date and self.indi[y.wife_id].bday > y.mar_date):           #both of them werent born
                    print(f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before both of them were born")
                    l.append(x)
                elif(self.indi[y.hus_id].bday > y.mar_date):                    #Husband married before birth
                    print(f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.hus_id].name}")
                    l.append(x)
                elif(self.indi[y.wife_id].bday > y.mar_date):                    #wife married before birth
                    print(f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.wife_id].name}")
                    l.append(x)
            elif self.indi[y.hus_id].bday != "NA" and y.mar_date != "NA":
                if(self.indi[y.hus_id].bday > y.mar_date):                        #wife doesnt exits but husband is married before birth
                    print(f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.hus_id].name}")
                    l.append(x)
            elif self.indi[y.wife_id].bday != "NA" and y.mar_date != "NA":
                if (self.indi[y.wife_id].bday > y.mar_date):                     # husband id doesnt exist but wife is married before birth
                    print(f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.wife_id].name}")
                    l.append(x)
        return l


    def us03(self):
        """Birth should not occur before death of an individual"""
        l = []
        for x,y in self.indi.items():
            if y.dday != "NA" and y.bday != "NA":
                if(y.dday<y.bday):
                    print(f"ERROR: Indiidual US03:{y.name} has a death-date before birth-day")
                    l.append(x)
        return l

    def us09(self):
        """Birth before death of parents
        Child should be born before death of mother and before 9 months after death of father"""
        l = []
        for k, f in self.fam.items():
            for i in f.child_id:
                if self.indi[f.hus_id].dday != "NA":
                    d1 = self.indi[i].bday
                    d2 = self.indi[f.wife_id].dday
                    d3 = self.indi[f.hus_id].dday
                    d4 = d3 - relativedelta(months=9)
                    if d1 != "NA" and d2 != 'NA' and d3 != "NA" and d1 > d2 or d1 > d4:
                        print(f"ERROR: FAMILY: US09: {k} Birth {d1} before death of parents on {d2, d3}")
                        l.append(k)
        return l


    def us10(self):
        """Marriage after 14
        Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
        l = []
        for k, f in self.fam.items():
            if f.mar_date != "NA":
                d1 = self.indi[f.hus_id].bday
                d2 = self.indi[f.wife_id].bday
                d3 = f.mar_date
                d4 = d1 + relativedelta(years=14)
                d5 = d2 + relativedelta(years=14)
                if d1 != "NA" and d2 != "NA" and d3 < d4 or d3 < d5:
                    print(f"ERROR: FAMILY: US10: {k} Marriage {d3} before 14")
                    l.append(k)
        return l