import csv
import os
import random
import sys

def ai():
    ai_run = True
    os.chdir('pkg')
    print '\n'
    while ai_run == True:
        prl = []
        u = raw_input().lower()
        if u == '-exit-':
            ai_run = False
        pkglist = open('pkg.list', 'r')
        for line in pkglist:
            for file in os.listdir('%s/ai' % line):
                if file.endswith('.csv'):
                    csv_file = open((line + '/ai/' + file), 'r')
                    for line in csv_file:
                        cell = line.split(',')
                        qas = 0
                        if random.randint(1,7) == 4:
                            while len(cell) > qas:
                                if u == cell[(qas)]:
                                    print (cell[(qas+1)])
                                u = raw_input().lower()
                            prl.append('')
                        else:
                            if len(cell) < 3 and u == cell[0]:
                                prl.append(cell[1])
                    csv_file.close()
        if len(prl) > 0:
            print random.choice(prl)
        else:
            print '...\n'
        pkglist.close()
    os.chdir('..')
