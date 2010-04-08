#!/usr/bin/env python
# encoding: utf-8
"""
airports.py

Created by Pedro Valente on 2010-03-28.
"""

import yql

icao_br = ['SBHT',
 'SBAR',
 'SBBE',
 'SBBH',
 'SBCF',
 'SBBV',
 'SBBR',
 'SBKG',
 'SBKP',
 'SBCG',
 'SBCP',
 'SBCJ',
 'SBCR',
 'SBCM',
 'SBCZ',
 'SBCY',
 'SBCT',
 'SBFL',
 'SBFZ',
 'SBFI',
 'SBGO',
 'SBIL',
 'SBIZ',
 'SBJP',
 'SBJV',
 'SBJU',
 'SBLO',
 'SBME',
 'SBMQ',
 'SBMO',
 'SBEG',
 'SBMA',
 'SBMK',
 'SBNT',
 'SBNF',
 'SBPJ',
 'SBPK',
 'SBPL',
 'SBPA',
 'SBPV',
 'SBRF',
 'SBRB',
 'SBGL',
 'SBRJ',
 'SBSV',
 'SBSN',
 'SBSL',
 'SBSP',
 'SBGR',
 'SBTE',
 'SBUR',
 'SBUL',
 'SBUG',
 'SBVT']


icao_to_code = {
 'SBAR': 'AJU',
 'SBBE': 'BEL',
 'SBBH': 'PLU',
 'SBBR': 'BSB',
 'SBBV': 'BVB',
 'SBCF': 'CNF',
 'SBCG': 'CGR',
 'SBCJ': 'CKS',
 'SBCM': 'CCM',
 'SBCP': 'CAW',
 'SBCR': 'CMG',
 'SBCT': 'CWB',
 'SBCY': 'CGB',
 'SBCZ': 'CZS',
 'SBEG': 'MAO',
 'SBFI': 'IGU',
 'SBFL': 'FLN',
 'SBFZ': 'FOR',
 'SBGL': 'GIG',
 'SBGO': 'GYN',
 'SBGR': 'GRU',
 'SBHT': 'ATM',
 'SBIL': 'IOS',
 'SBIZ': 'IMP',
 'SBJP': 'JPA',
 'SBJU': 'JDO',
 'SBJV': 'JOI',
 'SBKG': 'CPV',
 'SBKP': 'VCP',
 'SBLO': 'LDB',
 'SBMA': 'MAB',
 'SBME': 'MEA',
 'SBMK': 'MOC',
 'SBMO': 'MCZ',
 'SBMQ': 'MCP',
 'SBNF': 'NVT',
 'SBNT': 'NAT',
 'SBPA': 'POA',
 'SBPJ': 'PMW',
 'SBPK': 'PET',
 'SBPL': 'PNZ',
 'SBPV': 'PVH',
 'SBRB': 'RBR',
 'SBRF': 'REC',
 'SBRJ': 'SDU',
 'SBSL': 'SLZ',
 'SBSN': 'STM',
 'SBSP': 'CGH',
 'SBSV': 'SSA',
 'SBTE': 'THE',
 'SBUG': 'URG',
 'SBUL': 'UDI',
 'SBUR': 'UBA',
 'SBVT': 'VIX'}

code_to_icao = {
 'AJU': 'SBAR',
 'ATM': 'SBHT',
 'BEL': 'SBBE',
 'BSB': 'SBBR',
 'BVB': 'SBBV',
 'CAW': 'SBCP',
 'CCM': 'SBCM',
 'CGB': 'SBCY',
 'CGH': 'SBSP',
 'CGR': 'SBCG',
 'CKS': 'SBCJ',
 'CMG': 'SBCR',
 'CNF': 'SBCF',
 'CPV': 'SBKG',
 'CWB': 'SBCT',
 'CZS': 'SBCZ',
 'FLN': 'SBFL',
 'FOR': 'SBFZ',
 'GIG': 'SBGL',
 'GRU': 'SBGR',
 'GYN': 'SBGO',
 'IGU': 'SBFI',
 'IMP': 'SBIZ',
 'IOS': 'SBIL',
 'JDO': 'SBJU',
 'JOI': 'SBJV',
 'JPA': 'SBJP',
 'LDB': 'SBLO',
 'MAB': 'SBMA',
 'MAO': 'SBEG',
 'MCP': 'SBMQ',
 'MCZ': 'SBMO',
 'MEA': 'SBME',
 'MOC': 'SBMK',
 'NAT': 'SBNT',
 'NVT': 'SBNF',
 'PET': 'SBPK',
 'PLU': 'SBBH',
 'PMW': 'SBPJ',
 'PNZ': 'SBPL',
 'POA': 'SBPA',
 'PVH': 'SBPV',
 'RBR': 'SBRB',
 'REC': 'SBRF',
 'SDU': 'SBRJ',
 'SLZ': 'SBSL',
 'SSA': 'SBSV',
 'STM': 'SBSN',
 'THE': 'SBTE',
 'UBA': 'SBUR',
 'UDI': 'SBUL',
 'URG': 'SBUG',
 'VCP': 'SBKP',
 'VIX': 'SBVT'}


def main():
    pass

def getairports():
    y = yql.Public()
    query = "select code from pidgets.airports(1) where icao=@icao"
    
    for icao in icao_br:
        r = y.execute(
            query,
            {'icao':icao }, 
            env="store://datatables.org/alltableswithkeys"
            )
        code = ""
        if r.rows:
            code = r.rows['code']
        print "%s = %s\n" % (icao, code)
        table[icao] = code
    print table


if __name__ == '__main__':
	main()

