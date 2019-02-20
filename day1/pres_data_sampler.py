"""

This script samples donations dataset
It only selects data from Obama's amd McCain's contributions.

"""

import csv, sys, datetime

file_path = '../datasets/pres_campaign/{}'.format(sys.argv[1])

with file(file_path, 'r') as f:
    i = 0
    for line in f:
        # print 1 out of every 1000 donations
        if i % 1000 == 0:
            # skip last character, a carriage return. Print adds one for us.
            print line[:-1]
        i += 1
