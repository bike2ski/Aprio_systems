import csv

with open("tonal_dictionary.csv","rU") as infile, open("fixed_tonal.csv","wb") as outfile:
    reader = csv.reader(infile, skipinitialspace=True)
    writer = csv.writer(outfile)
    writer.writerows(reader)