#for i in *.pdf; do name=`echo $i | cut -d'.' -f1`; pdftotext "$i" "${name}.txt"; done

import os
from main import find_ext
from glob import glob

conferences = ['iccc2010', 'iccc2011', 'iccc2012', 'iccc2013', 'iccc2014', 'iccc2015', 'iccc2016', 'iccc2017', 'iccc2018', 'iccc2019', 'iccc2020']

path_to_files = "/Volumes/SDDMTL/ICCC_Proceedings_-_Exploration/"

for conference in conferences:
    path_conference = path_to_files + conference
    os.chdir(path_conference)
    print(conference)
    print(len(find_ext(path_conference, 'txt')))
    #print(os.system(f"ls"))
    #os.system("for i in *.pdf; do name=`echo $i`; pdftotext \"$i\" \"./txt/${name}.txt\"; done")
    #os.system(f"cd ..")
    