import pandas as pd
import numpy as np 

def parse_world_happiness_file(path):
    fp = open(path, 'r')
    lines = fp.readlines()

    for line in lines:
        print(line)

def main():
    parse_world_happiness_file('/Users/joy/Desktop/Repositories/world-happiness-report-analysis/datasets/world-happiness-report/2020.csv')

if __name__=="__main__": 
    main() 