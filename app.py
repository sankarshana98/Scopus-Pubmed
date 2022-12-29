import pandas as pd
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
from flask import Response
import integration
from paginate_pandas import paginate
import os
from flask_jsonpify import jsonpify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


Bootstrap(app)

pub=[]
query=''

@app.route('/api/query', methods = [ 'POST'])
@cross_origin()
def retrive():
    input=request.get_json()
    publications=input['publications']
    query=input['query']
    print(query,publications)
    q=query
    pub=publications.replace('[','').replace(']','').replace("'",'').split(',')
    data_merged = pd.DataFrame(columns=['ArticleTitle', 'Authors', 'ID', 'Database'])
    data_pub=pd.DataFrame()
    data_sco=pd.DataFrame()
    if ('PubMed' in pub):
        
        print('PUBMED '+ q)        

        data_pub=integration.pubmeddata(query)

    if ('scopus' in pub):
        
        print(query)
        print(str(query))
        data_sco=integration.scopusdata(str(query))
    
    data_merged=pd.concat([data_pub,data_sco])
    data_merged=data_merged.drop_duplicates('ArticleTitle')
        

     
    
    return Response(data_merged.to_json(orient="records"), mimetype='application/json')



if __name__ == "__main__":
    app.run(debug=True)
