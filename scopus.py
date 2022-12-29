from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from elsapy.elsprofile import ElsAuthor
from elsapy.elsdoc import AbsDoc
import pandas as pd
import json
import itertools
import csv
import json

data = []


def scopus_data(searchTerm):
    apikey = 'Your API KEY'
    client = ElsClient(apikey)
    doc_srch = ElsSearch("KEY({}) AND PUBYEAR > 2021".format(searchTerm), 'scopus')
    doc_srch.execute(client, get_all=True)
    return doc_srch.results



