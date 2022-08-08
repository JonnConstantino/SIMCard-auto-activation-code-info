#!/usr/bin/env python3
"""
@author: Jhonatan
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arq_simcard', help='Arquivo onde está os IMSI dos SIMCards que deseja ativar.')
parser.add_argument('arq_ativacao', help='Arquivo onde está os IMSI dos SIMCards com os códigos KI e OPC.')
args = parser.parse_args()

f_novo = open(args.arq_simcard+'_ativado', 'w')
f_simcard = open(args.arq_simcard, 'r')

f_novo.write('IMSI,KI,OPC,ACTIV_CODE\n')

for line_simcard in f_simcard:
    f_gemalto = open(args.arq_ativacao, 'r')
    for line_gemalto in f_gemalto:
        if line_simcard.strip('\n') in line_gemalto:
            f_novo.write(line_gemalto)