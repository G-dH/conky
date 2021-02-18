#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

countries = ('EMU', 'USA', 'Velká Británie')
url = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'
n = 5

for line in urllib.request.urlopen(url):
    parts = line.decode('utf-8').split('|')
    if parts[0] in countries:
            print ('${goto ' + str(n) + '}' + parts[3] + ':  ' + parts[4].rstrip() + '${voffset -13}')
            n=n+120

