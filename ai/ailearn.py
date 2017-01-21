import os
import csv

def learn(where):
    if where == 'null':
        os.chdir('pkg/learned/ai')
    else:
        os.chdir('pkg/%s/ai' % where)
    cfile = raw_input("Filename: ")
    if os.path.isfile(cfile):
        cfile = open(cfile, 'a')
    else:
        cfile = open(cfile, 'w')
    cfile = csv.writer(cfile)
    q = "N"
    i = "Y"
    while q == "N":
        row = []
        while i == "Y":
            row.append(raw_input("Question: "))
            row.append(raw_input("Awnser: "))
            i = raw_input("Continue (Y/N): ")
        cfile.writerow(row)
        q = raw_input("Exit or new (E/N): ")
