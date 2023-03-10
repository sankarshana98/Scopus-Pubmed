from Bio import Entrez
import json
import pandas as pd


def search(query):
    Entrez.email = ' your mail registered with pubmed API'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax=10_000,
                            retmode='xml',
                            #retstart=retstart,
                            usehistory='y',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = ' your mail registered with pubmed API'
    handle = Entrez.efetch(db='pubmed',retmode='xml',id=ids)
    results = Entrez.read(handle)
    return results

