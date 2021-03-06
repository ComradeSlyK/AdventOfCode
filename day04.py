# Author: ComradeSlyK (gregorini.silvio@gmail.com)
# Solutions for https://adventofcode.com/2020/day/4

from string import digits, hexdigits

from AdventOfCode.common import load_input, timer


def validate_byr(byr):
    return 1920 <= int(byr) <= 2002


def validate_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth']


def validate_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def validate_hcl(hcl):
    return len(hcl) == 7 \
        and hcl.startswith('#') \
        and all(c in hexdigits for c in hcl[1:])


def validate_hgt(hgt):
    if hgt.endswith('cm'):
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith('in'):
        return 59 <= int(hgt[:-2]) <= 76
    return False


def validate_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def validate_pid(pid):
    return len(pid) == 9 and all(c in digits for c in pid)


FIELDS = {
    # Birth Year
    'byr': {
        'mandatory': True,
        'validate': validate_byr,
    },
    # Country ID
    'cid': {
        'mandatory': False,
        'validate': None,
    },
    # Eye Color
    'ecl': {
        'mandatory': True,
        'validate': validate_ecl,
    },
    # Expiration Year
    'eyr': {
        'mandatory': True,
        'validate': validate_eyr,
    },
    # Hair Color
    'hcl': {
        'mandatory': True,
        'validate': validate_hcl,
    },
    # Height
    'hgt': {
        'mandatory': True,
        'validate': validate_hgt,
    },
    # Issue Year
    'iyr': {
        'mandatory': True,
        'validate': validate_iyr,
    },
    # Passport ID
    'pid': {
        'mandatory': True,
        'validate': validate_pid,
    },
}


def has_all_mandatory_fields(pdict):
    return all(f in pdict for f in FIELDS if FIELDS[f]['mandatory'])


def has_all_valid_fields(pdict):
    return has_all_mandatory_fields(pdict) \
        and all(
        FIELDS[f]['validate'](pdict.get(f))
        for f in FIELDS
        if FIELDS[f]['validate']
    )


def convert2passports(raw_passport_input):
    return tuple(
        dict([s.split(':') for s in p_str.replace('\n', ' ').split(' ')])
        for p_str in ''.join(raw_passport_input).split('\n\n')
    )


@timer
def problem1_solution():
    passports = convert2passports(load_input(4, 1))
    return len(tuple(filter(has_all_mandatory_fields, passports)))


@timer
def problem2_solution():
    passports = convert2passports(load_input(4, 2))
    return len(tuple(filter(has_all_valid_fields, passports)))


if __name__ == '__main__':
    print("** Solution to problem 1: {} **".format(problem1_solution()))
    print("** Solution to problem 2: {} **".format(problem2_solution()))
