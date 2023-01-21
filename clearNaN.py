# Description: This script removes all the rows that contain NaN values in the dataset
# Path: clearNaN.py
# Might need more than 1 run to remove all for some reason

import csv

with open('complete_swarmIot_full_labeled_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

    for row in data:
        if(row[0] == ''):
            data.remove(row)

    f.close()

with open('complete_swarmIot_full_labeled_dataset.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)
    f.close()