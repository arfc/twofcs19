#!/usr/bi.env python
import csv
import jinja2
import numpy as np
import os
import sys

def get_id(num):
    return "{0:0=2d}".format(num)

def get_item(data, name):
    item = data[name].decode('utf-8')
    if len(item) == 0:
        item = None
    return item

def file_name(num, title, presenter):
    lastname= presenter.lower().split(' ', 1)[-1]
    firstword = title.lower().split()[0]
    file_name = get_id(num) + '-' + lastname + '-' + firstword + '.pdf'
    return file_name


# print(abstracts)

def print_program(data):
    num = 0
    program_body = ''
    for abstract in data:
        #print(num)
        sessiontype = get_item(abstract, 'sessiontype')
        presenter = get_item(abstract, 'presenter')
        title = get_item(abstract, 'title')
        if 'Talk' in sessiontype:
            talk = 'Talk'
            filename = file_name(num, title, presenter)
        else:
            talk = None
            filename = None
        abstract_yml =template.render(
            date=get_item(abstract, 'date'),
            session=get_item(abstract, 'session'),
            sessiontype=get_item(abstract, 'sessiontype'),
            time=get_item(abstract, 'time'),
            presenter=get_item(abstract, 'presenter'),
            coauthors=get_item(abstract, 'coauthors'),
            chair=get_item(abstract, 'chair'),
            title=get_item(abstract, 'title'),
            abstract_text=get_item(abstract, 'abstract_text'),
            filename=filename,
            talk = talk,
            paper = get_item(abstract, 'paper'),
            slides = get_item(abstract, 'slides')
        )

        num += 1
        #print(abstract_yml)
        program_body += abstract_yml
    print(program_body)
    return program_body


# Main activity·
# Get commandline args
if len(sys.argv) < 3:
    print('Usage: ./write-site.py abstracts.csv program.yml.in')

# identify data path
data_path = sys.argv[1]

# open the file
with open(sys.argv[2], 'r') as fp:
    program_template = fp.read()
template = jinja2.Template(program_template)

# column names
cols = ('date', 'time', 'duration', 'sessiontype', 'session', 'chair', 'presenter',
        'coauthors', 'title', 'abstract_text', 'paper', 'slides')

# get data
abstracts = np.genfromtxt(data_path, delimiter='\t', dtype=None, names=cols,
                          skip_header=1)

# print
print_program(abstracts)
