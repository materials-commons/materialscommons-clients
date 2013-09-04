#!/usr/bin/env python

import requests
import sys
from os import environ

_MC_API_URL = environ.get('MC_API_URL') or 'https://api.materialscommons.org:5000/v1.0'


def main():
    if len(sys.argv) < 2:
        usage()

    if sys.argv[1] == "get":
        getNews()
    elif sys.argv[1] == "delete":
        deleteNews()
    elif sys.argv[1] == "add":
        addNews()
    else:
        usage()

def usage():
    print "news [get|delete|add]"
    print " where"
    print "  delete <id>"
    sys.exit(1)

def getNews():
    r = requests.get(makeApiUrl('/news'), verify=False)
    for article in r.json():
        print "%s" % (article['date'])
        print "%s:%s" % (article['header'], article['description'])
        print "id:%s\n" % (article['id'])

def deleteNews():
    if len(sys.argv) != 3:
        usage()

    r = requests.delete(makeApiUrl('/news/%', sys.argv[2]), verify=False)
    print r.status_code

def addNews():
    pass

def makeApiUrl(urlstr, *args):
    for arg in args:
        urlstr = urlstr.replace('%', arg, 1)
    return _MC_API_URL + urlstr

if __name__ == "__main__":
    main()
