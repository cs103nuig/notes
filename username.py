def username(first, last):
    "compute a username from a person's name"
    uname = (first[0] + last[:7]).lower()
    return uname

def csv2name(line):
    "convert a line of csv into first, last"
    name = line.strip()
    name = name.split(',')
    return name[1], name[0]
