def file_reading_gen(filepath):
    """base on proj 02
    returns valid lines from the ged file"""
    tags = {'0': ['HEAD', 'TRLR', 'NOTE'],
            '1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'], '2': ['DATE']}
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            l = line.split(' ', 2)
            validity = False
            tag = l[1]
            try:
                args = l[2]
            except IndexError:
                args = ''
            if int(l[0]) < 3 and l[1] in tags[l[0]]:
                validity = True
            elif l[0] == '0' and (l[2] == 'INDI' or l[2] == 'FAM'):
                validity = True
                tag = l[2]
                args = l[1]
            if validity:
                yield f"{l[0]}|{tag}|{args}"
