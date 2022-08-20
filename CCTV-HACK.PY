#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AMH-HC/CCTV-HACK

import requests, re , colorama
colorama.init()
print("""

\033[1;33m\033[1;37m╔█████═╗██╗      ██╗██║     ██╗ 
\033[1;33m\033[1;37m██╔══██║███║   ███║██║     ██║
\033[1;32m\033[1;37m███████║█████████║████████║
\033[1;32m\033[1;37m██╔══██║██╔═█══██║██╔═══██║
\033[1;31m\033[1;37m██║   ██║██╔════██║██║     ██║
\033[1;31m\033[1;37m╚═╝   ╚═╝╚═╝      ╚═╝╚═╝     ╚═╝     
\033[1;33m                          CCTV-HACK                                         
\033[1;33m1) \033[1;32mMyanmar Burma                            
\033[1;33m1) \033[1;32mUnited States
""")

try:
    print()
    countries = ["MB", "US",]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 2+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()
