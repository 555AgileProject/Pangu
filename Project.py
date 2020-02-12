from datetime import datetime,timedelta
from prettytable import PrettyTable
from Project02 import file_reading_gen

#klksjdakdjald
#kjkjkwkkklqlq
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

    def update_age_alive(self):
        for indi_id, indi in self.indi.items():
            if indi.bday != 'NA':
                birth_date = indi.bday
                age = datetime.now() - birth_date
                indi.age = int(age.days/365)
            else:
                indi.age = 'NA'
            if indi.dday != 'NA':
                indi.alive = False
            else:
                indi.alive = True

    def _analyze_files(self):
        indi_index = {'NAME':'name','SEX':'gender','BIRT':'bday','DEAT':'dday','FAMC':'child','FAMS':'spouse'}
        fam_index = {'MARR':'mar_date','HUSB':'hus_id','WIFE':'wife_id','CHIL':'child_id','DIV':'div_date'}
        indi_buff = Individual(None)
        indi_date_buff = [False,False]                        # 0 indicates bday 1 indicates dday 
        fam_buff = Family(None,'NA','NA','NA','NA',set())
        fam_date_buff = [False,False]                         # 0 indicates div_date 1 indicates mar_date
        for eachrow in file_reading_gen(self.dir):
            readline = eachrow.split("|")
            if (readline[0] == '0'):
                if (indi_buff.id != None):
                     # condition 1 push the individual buffer
                    new_indi = indi_buff
                    if new_indi.id not in self.indi.keys():
                        self.indi[new_indi.id] = new_indi
                    indi_buff = Individual(None) #clear the buffer
                    indi_date_buff = [False,False]                        # 0 indicates bday 1 indicates dday 
                elif(fam_buff.id != None):
                    # condition 2 push the family buffer
                    new_fam = fam_buff
                    if new_fam.id not in self.fam.keys():
                        self.fam[new_fam.id] = new_fam
                    fam_buff = Family(None,'NA','NA','NA','NA',set())       # clear the buffer
                    fam_date_buff = [False,False]                         # 0 indicates div_date 1 indicates mar_date
                if(indi_buff.id == fam_buff.id == None):
                    # condition 3 set the ?_buffer's id  
                    if (readline[1] in ["INDI", "FAM"]):
                        # Create New Family and push existing into the respective function
                        orig = readline[1]
                        if (orig == "INDI"):
                            indi_buff.id = readline[2]  # pass the attributes of self.data to it
                        else:
                            fam_buff.id = readline[2]
                    elif readline[1] == 'NOTE':
                        pass    #Ignore the line when there is a note

            elif (readline[0] == '1'):
                if (indi_buff.id != None):
                    # condition 1 for update indi_buff
                    if (readline[1] in ['BIRT','DEAT']):
                        if readline[1] == 'BIRT':
                            indi_date_buff[0] = True
                        else:
                            indi_date_buff[1] = True
                    else:
                        setattr(indi_buff,indi_index[readline[1]],readline[2])

                elif(fam_buff.id != None):
                    # condition 2 for update fam_buff
                    if (readline[1] in ['DIV','MARR']):
                        if readline[1] == 'DIV':
                            fam_date_buff[0] = True
                        else:
                            fam_date_buff[1] = True
                    elif readline[1] == 'CHIL':
                        fam_buff.child_id.add(readline[2])
                    else:
                        setattr(fam_buff,fam_index[readline[1]],readline[2])

            elif (readline[0] == '2'):
                if (readline[1] == 'DATE'):
                    try:
                        the_date = datetime.strptime(readline[2],'%d %b %Y')
                    except:
                        the_date = datetime.strptime(readline[2],'%Y')
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
        self.update_age_alive()


            
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
            ptf.add_row(
                [key, d.mar_date, d.div_date, d.hus_id, self.indi[d.hus_id].name, d.wife_id, self.indi[d.wife_id].name,
                 d.child_id])
        print(ptf.get_string(title="Families"))

    def us06(self):
        '''Divorce can only occur before death of both spouses'''
        l=[]
        #for i in self.indi.item()
        print('')
        l.append("i1")
        return l

    def us07(self):
        '''Death should be less than 150 years after birth for dead people,
        and current date should be less than 150 years after birth for all living people'''
        l=[]
        for i in self.indi:
            if 'DEAT' in self.indi[i].keys():
                pass
            else:
                pass
        return l

    def us02(self):
        """marriage before birth"""

    def us03(self):
        """Death before marriage"""

    #nodfijsi 
