def if_valid(filepath):
    """base on proj 02
    returns each valid line"""
    tags = {'0': ['HEAD', 'TRLR', 'NOTE'],
            '1': ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'], '2': ['DATE']}
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            l = line.split(' ', 2)
            validity = 'N'
            tag=l[1]
            try:
                args = l[2]
            except IndexError:
                args = ''
            if int(l[0]) < 3 and l[1] in tags[l[0]]:
                validity = 'Y'
            elif l[0] == '0' and (l[2] == 'INDI' or l[2] == 'FAM'):
                validity = 'Y'
                tag = l[2]
                args = l[1]
            yield f"{l[0]}|{tag}|{validity}|{args}"


def main():
    f1 = './Project01_Shihao Miao.ged'
    f2 = './proj02test.ged'
    print(f"Test {f1}")
    if_valid(f1)
    print(f"Test {f2}")
    if_valid(f2)


if __name__ == '__main__':
    main()
