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
        u = raw_input().lower().replace(',', '[comma]').replace('[space]', ' ')
        if u == '-exit-':
            ai_run = False
        pkglist = open('pkg.list', 'r')
        qut = True
        for line in pkglist:
            line = line.replace('\n', '')
            os.chdir(line)
            for file in os.listdir('ai'):
                csv_file = open(('ai/' + file), 'r')
                for line in csv_file:
                    cell = line.split(',')
                    qas = 0
                    if len(cell) > 2:
                        if random.randint(1,7) == 4:
                            while len(cell) > qas and qut == True:
                                if u == cell[(qas)]:
                                    print (cell[(qas+1)].replace('[comma]', ',').replace('[space]', ' '))
                                    u = raw_input().lower().replace(',', '[comma]').replace('[space]', ' ')
                                    qas = qas + 1
                                else:
                                    qut = False
                        else:
                            if len(cell) < 3 and u == cell[0]:
                                prl.append(cell[1])
                    else:
                        if len(cell) < 3 and u == cell[0]:
                            prl.append(cell[1])
                csv_file.close()
            os.chdir('..')
        if len(prl) > 0:
            print random.choice(prl).replace('[comma]', '[,]').replace('[space]', ' ')
        else:
            print '...\n'
        pkglist.close()
    os.chdir('..')
