import csv
import os
import random
import sys
import calcmgr

def ai():
    ai_run = True
    os.chdir('pkg')
    print '\n'
    while ai_run == True:
        prl = []
        u = raw_input().lower().replace(',', '[comma]')
        if u == '-exit-':
            ai_run = False
        pkglist = open('pkg.list', 'r')
        qut = True
        for line in pkglist:
            if prl != ['[null]']:
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
                                        print (cell[(qas+1)].replace('[comma]', ','))
                                        qas = qas + 1
                                        u = raw_input().lower().replace(',', '[comma]')
                                    else:
                                        qut = False
                                prl = ['[null]']
                            else:
                                if len(cell) < 3 and u == cell[0]:
                                    prl.append((cell[1].replace('[comma]', ',')))
                        else:
                            if len(cell) < 3 and u == cell[0]:
                                prl.append((cell[1].replace('[comma]', ',')))
                    csv_file.close()
                if prl != ['null']:
                    calcl = calcmgr.main()
                    if calcl != 0:
                        prl.extend(calcl)
                os.chdir('..')
        if prl != ['[null]'] and len(prl) > 0:
            print random.choice(prl).replace('[comma]', '[,]')
        else:
            print '...\n'
        pkglist.close()
    os.chdir('..')
