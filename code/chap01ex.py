"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys

import thinkstats2
import pandas as pd
import nsfg
from pprint import pprint

from collections import defaultdict


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass


def ValidatePregnum(resp, preg):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    preg: pregnancy DataFrame
    """
    # make the map from caseid to list of pregnancy indices
    preg_map = MakePregMap(preg)

    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

        if len(indices) == pregnum:
            print(caseid, len(indices), pregnum)

    return True

# pattern seems to be something like this
# def LinkFiles(f1, f2):
#     for key, value in f1.col.iteritems():
#         id1 = f1.id1[key]
#         id2 = f2[id1]

def MakePregMap(df):
    """Make a map from caseid to list of preg indices.

    df: DataFrame

    returns: dict that maps from caseid to list of indices into `preg`
    """
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid].append(index)
    return d


def main(script):

    preg = nsfg.ReadFemPreg()  # DataFrame
    resp = nsfg.ReadFemResp()  # DataFrame
    preg_by_caseid = MakePregMap(preg)  # dictionary

    total_pregnancies_by_caseid = {}
    for key, preg_list in preg_by_caseid.items():
        total_preg = 0
        for p in preg_list:
            total_preg += 1
        total_pregnancies_by_caseid[key] = total_preg

    print(len(total_pregnancies_by_caseid))
    print(len(resp))
    # for k, v in total_pregnancies_by_caseid.items():
    #     print(k,v)

    # # iterate through the respondent pregnum series
    # for index, pregnum in resp.pregnum.iteritems():
    #     caseid = resp.caseid[index]
    #     indices = total_pregnancies_by_caseid[caseid]


    #     # check that pregnum from the respondent file equals
    #     # the number of records in the pregnancy file
    #     if indices != pregnum:
    #         print(caseid, indices, pregnum)


    # preg_pregnum = pd.DataFrame([total_pregnancies_by_caseid], columns=['caseid', 'pregnum'])
    # result = ValidatePregnum(resp, preg_pregnum)
    # print(result)

    # df = ReadFemResp()
    # print(df.pregnum.head())
    # print(df.pregnum.value_counts().sort_index())

    # bins = [0,1,2,3,4,5,6,100]
    # print(pd.cut(df.pregnum, bins).value_counts().sort_index())

    # preg = nsfg.ReadFemPreg()
    # resp = nsfg.ReadFemResp()
    # print(ValidatePregnum(resp, preg))
    # print(preg.head())

    # pregnum_map = nsfg.MakePregMap(preg)
    # # pprint(pregnum_map)


    # print(len(pregnum_map))
    # print(len(resp))

    # for key, value in pregnum_map.items():
    #     pass
        # print(key, len(value))
        # print(type(resp.pregnum[key]))
        # if resp.pregnum[key] == len(value):
        #     print("MATCH")
        # elif resp.pregnum[key] != len(value):
        #     print("NO MATCH")
        # else:
        #     print("ERROR")
    # print(pregnum_map)



    # print(resp.pregnum)

    # caseid = 12556
    # pregnum_map = nsfg.MakePregMap(preg)
    # indices = pregnum_map[caseid]
    # # resp.pregnum[indices].values
    # result = preg.pregnum
    # print(result)
    # print(resp.head())


    # print(result)

    """Tests the functions in this module.



    # indices = preg_map[caseid]
    # preg.outcome[indices].values
    script: string script name
    """
    # print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
