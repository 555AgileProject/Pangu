from datetime import datetime, timedelta, date
from prettytable import PrettyTable
from Project02 import file_reading_gen
from dateutil.relativedelta import relativedelta
from collections import defaultdict

import logging


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
        self.pretty_print()

    def update_age(self):
        for indi in self.indi.values():
            if indi.bday != 'NA' and indi.dday != 'NA':
                indi.age = int(indi.dday.year - indi.bday.year - (
                        (indi.dday.month, indi.dday.day) < (indi.bday.month, indi.bday.day)))

                indi.alive = False
            elif indi.bday != 'NA':
                today = date.today()
                indi.age = int(today.year - indi.bday.year - (
                        (today.month, today.day) < (indi.bday.month, indi.bday.day)))
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
                        print("ERROR: Please check the date format! ")  # what if this raises exception? #Solved!
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
            if i.age != 'NA' and i.age >= 150:
                s = f'ERROR: INDIVIDUAL: US07: {k} More than 150 years old at death - Birth {i.bday}'
                if i.dday != 'NA':
                    s += f': Death {i.dday}'
                print(s)
                l.append(k)
        return l

    def us02(self):
        """Birth should occur before marriage of an individual"""
        l = []
        for x, y in self.fam.items():
            if self.indi[y.hus_id].bday != "NA" and y.mar_date != "NA" and self.indi[
                y.wife_id].bday != "NA":  # both birthdates are available
                if (self.indi[y.hus_id].bday > y.mar_date and self.indi[
                    y.wife_id].bday > y.mar_date):  # both of them werent born
                    print(
                        f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before both of them were born")
                    l.append(x)
                elif (self.indi[y.hus_id].bday > y.mar_date):  # Husband married before birth
                    print(
                        f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.hus_id].name}")
                    l.append(x)
                elif (self.indi[y.wife_id].bday > y.mar_date):  # wife married before birth
                    print(
                        f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.wife_id].name}")
                    l.append(x)
            elif self.indi[y.hus_id].bday != "NA" and y.mar_date != "NA":
                if (self.indi[y.hus_id].bday > y.mar_date):  # wife doesnt exits but husband is married before birth
                    print(
                        f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.hus_id].name}")
                    l.append(x)
            elif self.indi[y.wife_id].bday != "NA" and y.mar_date != "NA":
                if (self.indi[y.wife_id].bday > y.mar_date):  # husband id doesnt exist but wife is married before birth
                    print(
                        f"ERROR: Family US02: {self.indi[y.hus_id].name} and {self.indi[y.wife_id].name} have been married before birth of {self.indi[y.wife_id].name}")
                    l.append(x)
        return l

    def us03(self):
        """Birth should not occur before death of an individual"""
        l = []
        for x, y in self.indi.items():
            if y.dday != "NA" and y.bday != "NA":
                if (y.dday < y.bday):
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
                if self.indi[f.hus_id].bday != "NA" and self.indi[f.wife_id].bday != "NA":
                    d1 = self.indi[f.hus_id].bday
                    d2 = self.indi[f.wife_id].bday
                    d3 = f.mar_date
                    d4 = d1 + relativedelta(years=14)
                    d5 = d2 + relativedelta(years=14)
                    if d1 != "NA" and d2 != "NA" and d3 < d4 or d3 < d5:
                        print(f"ERROR: FAMILY: US10: {k} Marriage {d3} before 14")
                        l.append(k)
        return l

    def us04(self):
        """Marriage before divorce
        date of marrige should be before date of divorce"""
        l = []
        for k, f in self.fam.items():
            if f.mar_date != "NA" and f.div_date != "NA":
                d1 = f.mar_date
                d2 = f.div_date
                if d1 != "NA" and d2 != "NA" and d1 > d2:
                    print(f"ERROR: FAMILY: US04: {k} Marriage {d1} before divorse {d2}")
                    l.append(k)
        return l

    def us08(self):
        """Birth before marriage of parent
        Children should be born after marriage of parents (and not more than 9 months after their divorce)"""
        l = []
        for k, f in self.fam.items():
            for i in f.child_id:
                if f.mar_date != "NA" and f.div_date != "NA":
                    d1 = self.indi[i].bday
                    d2 = f.mar_date
                    d3 = f.div_date
                    d4 = d3 + relativedelta(months=9)
                    if d1 != "NA" and d2 != 'NA' and d3 != 'NA' and (d1 < d2 or d1 > d4):
                        print(
                            f"ERROR: FAMILY: US08: {k} Birth {d1} before marriage of parents on {d2} or birth {d1} more than 9 months after divorce")
                        l.append(k)
                elif f.mar_date != "NA":
                    d1 = self.indi[i].bday
                    d2 = f.mar_date
                    if d1 != "NA" and d2 != "NA" and d1 < d2:
                        print(f"ERROR: FAMILY: US08: {k} Birth {d1} before marriange {d2}")
                        l.append(k)

        return l

    def us01(self):
        """Dates (birth, marriage, divorce, death) should not be after the current date """
        error_id = set()
        curr_date = date.today()
        check_items_indi = ['bday', 'dday']
        check_items_fam = ['mar_date', 'div_date']
        for usr_id, usr in self.indi.items():  # check the usr bday and dday
            for check_item in check_items_indi:
                if self.ad_date_compare(getattr(usr, check_item), curr_date) == -1:
                    error_id.add(usr_id)
                    print(
                        f"ERROR: INDIVIDUAL: US01: {usr_id} {check_item} {getattr(usr, check_item)} occurs in the future")
        for fam_id, fam in self.fam.items():
            for check_item in check_items_fam:
                if self.ad_date_compare(getattr(fam, check_item), curr_date) == -1:
                    error_id.add(fam_id)
                    print(f"ERROR: FAMILY: US01: {fam_id} {check_item} {getattr(fam, check_item)} occurs in the future")
        return error_id

    def us05(self):
        """ Marriage should occur before death of either spouse """
        error_id = set()
        for fam_id, fam in self.fam.items():
            fam_mar_d = fam.mar_date
            hus_dday = self.indi[fam.hus_id].dday
            if self.ad_date_compare(fam_mar_d, hus_dday) == -1:
                print(
                    f"ERROR: FAMILY: US05: {fam_id} Husband death {self.indi[fam.hus_id].dday} before the marrige {fam.mar_date}")
                if (not error_id.issuperset({fam_id})):
                    error_id.add(fam_id)
            if self.ad_date_compare(fam.mar_date, self.indi[fam.wife_id].dday) == -1:
                print(
                    f"ERROR: FAMILY: US05: {fam_id} Wife death {self.indi[fam.wife_id].dday} before the marrige {fam.mar_date}")
                if (not error_id.issuperset({fam_id})):
                    error_id.add(fam_id)
        return error_id

    def ad_date_compare(self, my_date, compare_date):
        """
        advanced time comparation, if my date is before or equal to the compare date, the return will be 1
        if my date is later than the compare date then return -1
        if my date is not comparable aka 'NA' return 0
        """
        if my_date == 'NA' or compare_date == 'NA':
            return False
        else:
            if my_date > compare_date:
                return -1
            else:
                return 1

    def us12(self):
        '''Mother should be less than 60 years older than her children
        and father should be less than 80 years older than his children'''
        res = set()
        for f in self.fam.values():
            if f.wife_id != 'NA':
                wife = self.indi[f.wife_id]
                if wife.age == "NA":
                    print(f"f{f.id} Wife age does not exist. ")
                    continue
            if f.hus_id != 'NA':
                hus = self.indi[f.hus_id]
                if hus.age == "NA":
                    print(f"f{f.id} Husband age does not exist. ")
                    continue
            if f.child_id:
                for child in [self.indi[c] for c in f.child_id]:
                    if child.age == "NA":
                        print(f"Child {child.id} age does not exist.")
                        continue
                    if (wife.age - child.age) > 60:
                        print(f"ERROR: FAMILY: US12: {f.id} Mother's age: {wife.age}, child's age: {child.age}")
                        res.add(f.id)
                    if (hus.age - child.age) > 80:
                        print(f"ERROR: FAMILY: US12: {f.id} Father's age: {hus.age}, child's age: {child.age}")
                        res.add(f.id)
        return res

    def us16(self):
        '''All male members of a family should have the same last name'''
        res = []
        for f in self.fam.values():
            lastname = (self.indi[f.hus_id].name).split('/')[-2]
            child_lastname = []
            if f.hus_id != 'NA' and f.child_id:
                for id in f.child_id:
                    child = self.indi[id]
                    if child.gender == 'M':
                        child_lastname.append((child.name).split('/')[-2])

                for name in child_lastname:
                    if name != lastname:
                        print(f"Error: FAMILY:US16: <{f.id}> Last names don't match {lastname} vs {name}")
                        res.append(f.id)
        return res

    def us14(self):
        """No more than five siblings should be born at the same time"""
        fam_result = []
        for fam_id, fam in self.fam.items():
            # fam_result.extend(fam_result)
            child_bdy = defaultdict(int)
            for child in fam.child_id:
                if self.indi[child].bday != "NA":
                    child_bdy[self.indi[child].bday] += 1
            fam_result.extend([fam_id for birth, res in child_bdy.items() if res > 5])
        print(f"ERROR: FAMILY: US14: {fam_result} has more than 5 children born on same date")
        return (fam_result)

    def us15(self):
        """There should be fewer than 15 siblings in a family"""
        fam_result = []
        for fam_id, fam in self.fam.items():
            if (len(fam.child_id) >= 15):
                fam_result.append(fam_id)
        if (fam_result):
            print(f"ERROR: FAMILY: US15: {fam_result} has more than 15 children born")
            return (fam_result)

    def us19(self):
        '''First cousins should not marry one another'''
        result = []
        count = 0
        for fam_id, fam in self.fam.items():
            hus = fam.hus_id
            wife = fam.wife_id

            hus_mom = 'NA'
            hus_mom_mom = 'NA2'
            hus_mom_dad = 'NA3'
            hus_dad = 'NA'
            hus_dad_mom = 'NA5'
            hus_dad_dad = 'NA6'

            wife_mom = 'NA'
            wife_mom_mom = 'NA8'
            wife_mom_dad = 'NA9'
            wife_dad = 'NA'
            wife_dad_mom = 'NA11'
            wife_dad_dad = 'NA12'

            for fam_id, fam in self.fam.items():
                for i in fam.child_id:
                    if i == hus:
                        hus_mom = fam.wife_id
                        hus_dad = fam.hus_id

                        for fam_id, fam in self.fam.items():
                            for j in fam.child_id:
                                if j == hus_mom:
                                    hus_mom_mom = fam.wife_id
                                    hus_mom_dad = fam.hus_id
                                    break
                        for fam_id, fam in self.fam.items():
                            for k in fam.child_id:
                                if k == hus_dad:
                                    hus_dad_mom = fam.wife_id
                                    hus_dad_dad = fam.hus_id
                                    break

            for fam_id, fam in self.fam.items():
                for i in fam.child_id:
                    if i == wife:
                        wife_mom = fam.wife_id
                        wife_dad = fam.hus_id

                        for fam_id, fam in self.fam.items():
                            for j in fam.child_id:
                                if j == wife_mom:
                                    wife_mom_mom = fam.wife_id
                                    wife_mom_dad = fam.hus_id
                                    break
                        for fam_id, fam in self.fam.items():
                            for k in fam.child_id:
                                if k == wife_dad:
                                    wife_dad_mom = fam.wife_id
                                    wife_dad_dad = fam.hus_id
                                    break

            if (hus_mom != wife_mom and hus_dad != wife_dad) and (
                    hus_mom_mom == wife_mom_mom and hus_mom_dad == wife_mom_dad) or (
                    hus_mom_mom == wife_dad_mom and hus_mom_dad == wife_dad_dad) or (
                    hus_dad_mom == wife_mom_mom and hus_dad_dad == wife_mom_dad) or (
                    hus_dad_mom == wife_dad_mom and hus_dad_dad == wife_dad_dad):
                result.append(hus)
                result.append(wife)
                print(f"ERROR: FAMILY: US19: {result[count]} and {result[count + 1]} are first cousins")
                count = count + 2
        return result

    def us20(self):
        '''Aunts and uncles should not marry their nieces or nephews'''
        result = []
        count = 0
        for fam_id, fam in self.fam.items():
            hus = fam.hus_id
            wife = fam.wife_id

            hus_mom = 'NA'
            hus_mom_mom = 'NA2'
            hus_mom_dad = 'NA3'
            hus_dad = 'NA'
            hus_dad_mom = 'NA5'
            hus_dad_dad = 'NA6'

            wife_mom = 'NA'
            wife_mom_mom = 'NA8'
            wife_mom_dad = 'NA9'
            wife_dad = 'NA'
            wife_dad_mom = 'NA11'
            wife_dad_dad = 'NA12'

            for fam_id, fam in self.fam.items():
                for i in fam.child_id:
                    if i == hus:
                        hus_mom = fam.wife_id
                        hus_dad = fam.hus_id

                        for fam_id, fam in self.fam.items():
                            for j in fam.child_id:
                                if j == hus_mom:
                                    hus_mom_mom = fam.wife_id
                                    hus_mom_dad = fam.hus_id
                                    break
                        for fam_id, fam in self.fam.items():
                            for k in fam.child_id:
                                if k == hus_dad:
                                    hus_dad_mom = fam.wife_id
                                    hus_dad_dad = fam.hus_id
                                    break

            for fam_id, fam in self.fam.items():
                for i in fam.child_id:
                    if i == wife:
                        wife_mom = fam.wife_id
                        wife_dad = fam.hus_id

                        for fam_id, fam in self.fam.items():
                            for j in fam.child_id:
                                if j == wife_mom:
                                    wife_mom_mom = fam.wife_id
                                    wife_mom_dad = fam.hus_id
                                    break
                        for fam_id, fam in self.fam.items():
                            for k in fam.child_id:
                                if k == wife_dad:
                                    wife_dad_mom = fam.wife_id
                                    wife_dad_dad = fam.hus_id
                                    break

            if (hus_mom == wife_mom_mom and hus_dad == wife_mom_dad) or (
                    hus_mom == wife_dad_mom and hus_dad == wife_dad_dad) or (
                    wife_mom == hus_mom_mom and wife_dad == hus_mom_dad) or (
                    wife_mom == hus_dad_mom and wife_dad == hus_dad_dad):
                result.append(hus)
                result.append(wife)
                print(f"ERROR: FAMILY: US20: {result[count]} and {result[count + 1]} are uncle-niece/wife-nephew")
                count = count + 2
        return result

    def us17(self):
        """No marriages to children"""
        fam_error = []
        for fam1_id, fam1 in self.fam.items():
            for fam2_id, fam2 in self.fam.items():
                if fam1.child_id != 'NA':
                    if (fam1.hus_id == fam2.hus_id and fam2.wife_id in fam1.child_id) or (
                            fam1.wife_id == fam2.wife_id and fam2.hus_id in fam1.child_id):
                        print(f"ERROR: FAMILY: US17: {fam2_id} contain(s) that parent married child")
                        fam_error.append(fam2_id)
        return fam_error

    def us18(self):
        """Siblings should not marry"""
        fam_error = []
        for fam1_id, fam1 in self.fam.items():
            for fam2_id, fam2 in self.fam.items():
                if fam1.child_id != "NA":
                    if fam2.hus_id in fam1.child_id and fam2.wife_id in fam1.child_id:
                        print(f"ERROR: FAMILY: US18: {fam2_id} married with his(her) siblings")
                        fam_error.append(fam2_id)
        return fam_error

    def us11(self):
        """
            This is th user story 11. no bigamy in each family.
        """
        error_id = set()
        for fam_id, fam in self.fam.items():
            for fam_id_2, fam_2 in self.fam.items():
                if fam_id == fam_id_2:
                    pass
                else:
                    if fam.hus_id == fam_2.hus_id:
                        if self.ad_date_compare(fam.mar_date, fam_2.div_date) * self.ad_date_compare(fam.mar_date,
                                                                                                     fam_2.mar_date) == -1 or self.ad_date_compare(
                            fam_2.mar_date, fam.div_date) * self.ad_date_compare(fam_2.mar_date,
                                                                                 fam.mar_date) == -1:
                            print(f"ERROR: FAMILY: US11: {fam.hus_id} has a bigamy cheat! of two family at same time! ")
                            if (not error_id.issuperset({fam.hus_id})):
                                error_id.add(fam.hus_id)
                    if fam.wife_id == fam_2.wife_id:
                        if self.ad_date_compare(fam.mar_date, fam_2.div_date) * self.ad_date_compare(fam.mar_date,
                                                                                                     fam_2.mar_date) == -1 or self.ad_date_compare(
                            fam_2.mar_date, fam.div_date) * self.ad_date_compare(fam_2.mar_date,
                                                                                 fam.mar_date) == -1:
                            print(
                                f"ERROR: FAMILY: US11: {fam.wife_id} has a bigamy cheat! of two family at same time! ")
                            if (not error_id.issuperset({fam.wife_id})):
                                error_id.add(fam.wife_id)
        return error_id

    def us13(self):
        """
            This is th user story 14. sibilings have more than 8 month birthday or less two day birthday.
        """
        error_id = set()
        for fam_id, fam in self.fam.items():
            if len(fam.child_id) >= 2:
                for child_id in fam.child_id:
                    for child_id_2 in fam.child_id:
                        if child_id != child_id_2:
                            date_1 = self.indi[child_id].bday
                            date_2 = self.indi[child_id_2].bday
                            if self.ad_date_compare(date_1, date_2) == 1:
                                temp = date_1
                                date_1 = date_2
                                date_2 = temp
                            if self.ad_date_compare(date_1, date_2) != 0 and (date_1 - date_2) > timedelta(10) and (
                                    date_1 - date_2) < timedelta(240):
                                print(
                                    f"ERROR: FAMILY: US13: {fam_id} has abnormal sbiling space less than 8 month but larger than 2days! ")
                                if (not error_id.issuperset({fam_id})):
                                    error_id.add(fam_id)
            else:
                pass
        return error_id

    def us30(self):
        '''List all living married people in a GEDCOM file'''
        l = []
        for i in self.indi.values():
            if i.alive and i.spouse != 'NA':
                l.append(i.id)
        print(f"US30: all living married people in a GEDCOM file:<{l}> ")
        return l

    def us31(self):
        '''List all living people over 30 who have never been married in a GEDCOM file'''
        l = []
        for i in self.indi.values():
            if i.alive and i.spouse == "NA" and i.age!='NA' and i.age > 30:
                l.append(i.id)
        print(f"US31: over 30 who have never been married in a GEDCOM file:<{l}>")
        return l

    def us22(self):
        '''All individual IDs should be unique and all family IDs should be unique'''
        Error_IDs = []
        Error_Fam_IDs = []
        Exist_IDs = []
        Exist_Fam_IDs = []
        for i in self.indi.values():
            if i.id not in Exist_IDs:
                Exist_IDs.append(i.id)
            else:
                print(f"ERROR: individual: US22: indi_id({i.id}) is not unique!")
                Error_IDs.append(i.id)


        for k in self.fam.values():
            if k.id not in Exist_Fam_IDs:
                Exist_Fam_IDs.append(k.id)
            else:
                print(f"ERROR: FAMILY: US22: fam_id({k.id}) is not unique!")
                Error_Fam_IDs.append(k.id)
        return Error_IDs, Error_Fam_IDs


    def us23(self):
        '''No more than one individual with the same name and birth date should appear in a GEDCOM file'''
        Error_Indi = []
        for i1 in self.indi.values():
            for i2 in self.indi.values():
                if i1.id != i2.id and i1.bday != "NA" and i2.bday != "NA":
                    if i1.name == i2.name and i1.bday == i2.bday:
                        print(f"ERROR: INDIVIDUAL: US23: INDIVIDUAL({i1.id}, {i2.id}) have not unique name and birth date!")
                        Error_Indi.append(i1.id)
                        Error_Indi.append(i2.id)
        return Error_Indi

    def us21(self):

        result = []
        for fam_id, fam in self.fam.items():
            hus = fam.hus_id
            wife = fam.wife_id
            for id in self.indi.items():
                if id.gender != 'NA':
                    if hus == id and id.gender == 'F':
                        result.append(hus)
                        print(f"ERROR: FAMILY: US21: {hus} has wrong gender")

                    if wife == id and id.gender == 'M':
                        result.append(hus.id)
                        print(f"ERROR: FAMILY: US21: {wife} has wrogn gender")
        return result




