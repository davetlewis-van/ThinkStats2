from __future__ import print_function
import sys
import nsfg


def ValidatePregnum(resp, preg):
    """make the map from caseid to list of pregnancy indices"""
    preg_map = nsfg.MakePregMap(preg)
    for k, v in resp.pregnum.iteritems():  # iterate over a pandas series
        caseid = resp.caseid[k]  # assign the caseid value for the current key
        indices = preg_map[caseid]  # get the list of rows for the case id
        # check if the number of entries is equal to
        # the resp.pregnum value
        if len(indices) != v:
            print(caseid, len(indices), v)
            return False
    return True


def main(script):
    preg = nsfg.ReadFemPreg()  # DataFrame 13593 rows
    resp = nsfg.ReadFemResp()  # DataFrame 7643 rows
    result = ValidatePregnum(resp, preg)
    if result:
        print("Pregnum column validated.")
    else:
        print("Problems identified with pregnum column.")


if __name__ == '__main__':
    main(*sys.argv)
