import csv
import sys

from multihash.multicodec import Table


def multihashes(file):
    def is_multihash(row):
        return row['tag'] == 'multihash'

    return filter(is_multihash, csv.DictReader(file, skipinitialspace=True))


def parse(row):
    return row['name'].upper().replace('-', '_'), int(row['code'], 16)


def output(name, code, ident=4):
    print(f"{' ' * ident}{name} = {'0x%X' % code}")


def missing(file=sys.stdin):
    for row in multihashes(file):
        name, code = parse(row)

        if name not in Table.__members__:
            yield name, code


outdated = False

for name, code in missing():
    outdated = True
    output(name, code)

sys.exit(outdated)
