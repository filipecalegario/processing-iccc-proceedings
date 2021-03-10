from os import path
from glob import glob

conferences = ['iccc2010', 'iccc2011', 'iccc2012', 'iccc2013', 'iccc2014', 'iccc2015', 'iccc2016', 'iccc2017', 'iccc2018', 'iccc2019', 'iccc2020']

path_to_files = "/Volumes/SDDMTL/ICCC Proceedings - Exploration/"

def find_ext(dir, ext):
    return glob(path.join(dir,"*.{}".format(ext)))

papers_paths = find_ext(path_to_files+conferences[-1], 'txt')
print(len(papers_paths))

for paper in papers_paths:
    print(paper.split('/')[-1])