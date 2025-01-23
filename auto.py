#!/usr/bin/env python3
"""
@author: Jhonatan
"""

import argparse

UL_DL_AMBR = '50000000'
APN = 'APNNAME1'
DEFAULT = 'yes'
GWIP = '127.0.0.1'
QCI = '9'
ARPPRIORLEV = '14'
ARPPCI = 'on'
ARPPVI = 'off'
PDNTYPE = 'ipv4'
SERVEDPARTYIPV4ADDR = '172.16.x'
SERVEDPARTYIPV6ADDRPREFIX = '1111'
PRIDNSIPADDR = '8.8.8.8'
SECONDARYDNSIPADDR = '114.114.114.114'

parser = argparse.ArgumentParser()
parser.add_argument('arq_simcard', help='Arquivo onde está os IMSI dos SIMCards que deseja ativar.')
parser.add_argument('arq_ativacao', help='Arquivo onde está os IMSI dos SIMCards com os códigos KI e OPC.')
args = parser.parse_args()

f_novo = open(args.arq_simcard.replace('.csv', '_ativado.csv'), 'w')
f_novo_halob = open('halob_b28_' + args.arq_simcard, 'w')
f_novo_apn = open('apn_b28_' + args.arq_simcard, 'w')
f_simcard = open(args.arq_simcard, 'r')

f_novo.write('IMSI,KI,OPC,ACTIV_CODE\n')
f_novo_halob.write("IMSI,IMSIID(no-repeat),UEAMBRDL(bps),UEAMBRUL(bps),KI,OPC,ACTIV_CODE\n")
f_novo_apn.write("IMSI,APNNAME,CONTEXTID(The same user value is different),DEFAULTAPN(There's only one default for each user),GWIP,QCI(5-9),ARPPRIORLEV,ARPPCI,ARPPVI,APNAMBRUL(bps,1000-1000000000),APNAMBRDL(bps,1000-1000000000),PDNTYPE,SERVEDPARTYIPV4ADDR,SERVEDPARTYIPV6ADDRPREFIX,PRIDNSIPADDR,SECONDARYDNSIPADDR\n")

ip_network = 1
ip_final = 0
count = 0
for line_simcard in f_simcard:
    f_gemalto = open(args.arq_ativacao, 'r')
    for line_gemalto in f_gemalto:
        if line_simcard.strip('\n') in line_gemalto:
            count += 1
            ip_final += 1
            if ip_final == 255:
                ip_network += 1
                ip_final = 1
            line_halob = line_gemalto.replace(line_simcard.strip('\n'), line_simcard.strip('\n') + ',' + str(count) + ',' + str(UL_DL_AMBR) + ',' + str(UL_DL_AMBR))
            line_apn = line_simcard.strip('\n') + ',' + APN + ',' + str(count) + ',' + DEFAULT + ',' + GWIP + ',' + QCI + ',' + ARPPRIORLEV + ',' + ARPPCI + ',' + ARPPVI + ',' + UL_DL_AMBR + ',' + UL_DL_AMBR + ',' + PDNTYPE + ',' + SERVEDPARTYIPV4ADDR.replace('x', str(ip_network) + '.' + str(ip_final)) + ',' + SERVEDPARTYIPV6ADDRPREFIX + ',' + PRIDNSIPADDR + ',' + SECONDARYDNSIPADDR + '\n'
            f_novo.write(line_gemalto)
            f_novo_halob.write(line_halob)
            f_novo_apn.write(line_apn)
