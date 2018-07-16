'''
Strips whitespaces from CSV file.
'''
import os
import sys
import csv
import string

input_file_name = sys.argv[1]
if len(sys.argv) > 2:
	output_file_name = sys.argv[2]
else:
	output_file_name = "temp.csv"

with open(input_file_name) as f:
    reader = csv.reader(f, delimiter=",")
    with open(output_file_name, "wb") as fo:
        writer = csv.writer(fo)
        for rec in reader:
            writer.writerow(map(string.strip, rec))
			
if len(sys.argv) <= 2:
	os.remove(input_file_name)
	os.rename(output_file_name,input_file_name)			