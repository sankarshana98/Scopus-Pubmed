import pubmed,scopus
import pandas as pd
#import scopus

def pubmeddata(topic):
    topic = topic
    results = pubmed.search(topic)
    print(f"Total number of results: {results['Count']}")
    id_list = results['IdList']
    papers = pubmed.fetch_details(id_list)
    df = pd.DataFrame(columns=['ArticleTitle', 'Authors', 'ID', 'Database'])
    for i, paper in enumerate(papers['PubmedArticle']):
        authors = []
        if 'AuthorList' in paper['MedlineCitation']['Article'].keys():
            for name in paper['MedlineCitation']['Article']['AuthorList']:
                if 'Initials' in  name.keys() & 'LastName' in  name.keys(): 
                    authors.append(name['LastName'] + ' ' + name['Initials'] + ' ')
                elif 'LastName' in  name.keys():
                    authors.append(name['LastName'])
                else:
                    authors.append(' ')

        else:
            authors = 'No authors listed'
        artDate = paper['MedlineCitation']['DateRevised']['Day'] + '/' + \
                    paper['MedlineCitation']['DateRevised']['Month'] + '/' + paper['MedlineCitation']['DateRevised']['Year']
        dictTemp = {
            "ArticleTitle": paper['MedlineCitation']['Article']['ArticleTitle'],
            "Authors": ', '.join(authors),
            "ID": paper['MedlineCitation']['PMID'],
            # "Language": paper['MedlineCitation']['Article']['Language'],
            # "Date": artDate,
            "Database": 'PubMed'
        }
        df.loc[len(df.index)] = dictTemp

#with pd.option_context('display.max_rows', 100,'display.max_columns', None,'display.precision', 3,):
    return df

def scopusdata(topic):
    data = scopus.scopus_data(topic)
    print(topic)
    df_temp=pd.DataFrame(data)
    print(data)
    print(len(df_temp))
    dict_scop_temp = {"Database": 'Scopus'}
    df_scopus = df_temp[[ 'dc:title','dc:creator', 'source-id' ]]
    df_scopus['Database'] = "Scopus"
    cols = ['ArticleTitle', 'Authors', 'ID', 'Database']
    df_scopus.columns = cols
    return df_scopus
    