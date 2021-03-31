from os import path
from glob import glob

conferences = ['iccc2010', 'iccc2011', 'iccc2012', 'iccc2013', 'iccc2014', 'iccc2015', 'iccc2016', 'iccc2017', 'iccc2018', 'iccc2019', 'iccc2020']

path_to_files = "/Volumes/SDDMTL/ICCC_Proceedings_-_Exploration/"

def find_ext(dir, ext):
    return glob(path.join(dir,f'*.{ext}'))

papers_paths = find_ext(path_to_files+conferences[-2], 'txt')
print(len(papers_paths))

for paper in papers_paths:
    # print(paper.split('/')[-1])
    lines = open(paper, encoding='latin').readlines()
    title = lines[0]
    for i,line in enumerate(lines):
        line_no_n = line.replace('\n',' ')
        # print(f'{i} => {line_no_n}')
        #print(line_no_n[-9:-1])
        if line_no_n[-9:-1] == 'Abstract':
            print(line_no_n[-9:-1])
            if lines[i+1] == ' ':
                print(lines[i+2].replace('\n',' '))
            else:
                print(lines[i+1].replace('\n',' '))
        elif line_no_n[0:8] == 'Abstract':
            print(line_no_n[0:8])
            print(lines[i+1].replace('\n',' '))