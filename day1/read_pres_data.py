"""

This scripy reads and prints each donation's date, amount and candidate.

"""

import csv, sys, datetime

file_path = '../datasets/pres_campaign/{}'.format(sys.argv[1])
reader = csv.DictReader(open(file_path, 'r'))


for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = row['contb_receipt_amt']
    print(','.join([name, datestr, amount]))
