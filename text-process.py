import numpy as np
import pandas as pd
import pyprind
import os

def file_len(textfile):
    # checking the number of lines in the file
    with open(textfile) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def http_parser(textfile):
    ## Takes a text file with HTTP requests and parses all attributes as features
    ## into dataframe objects
    ## Returns reqget and reqpost
    ##

    reqget = pd.DataFrame()             # GET requests
    reqpost = pd.DataFrame()            # POST requests
    reqall = pd.DataFrame()             # All requests
    singlereq = pd.DataFrame()          # intermediate DataFrame object

    # defining the status bar of the import
    num_of_lines = file_len(textfile)
    pbar = pyprind.ProgBar(num_of_lines)       # status bar
    # this is not much useful, it's more for the estetics as I like status bars

    # import
    with open(textfile) as infile:
        for line in infile:
                if len(line.strip()) != 0:
                    splitline = pd.DataFrame(line.split())
                    singlereq= pd.concat([singlereq,splitline], ignore_index=True)

                elif len(singlereq.index) != 0:
                    if singlereq.values[0,0] != 'GET':
                        splitline = pd.DataFrame(next(infile).split())
                        singlereq = pd.concat([singlereq,splitline], ignore_index=True)
                        singlereq = singlereq.T
                        reqpost = pd.concat([reqpost,singlereq], ignore_index=True)
                    else:
                        # alligning columns of GET to be as POST and PUT
                        singlereq.loc[34,0] = singlereq.values[32,0]
                        singlereq.loc[35,0] = singlereq.values[33,0]
                        singlereq.loc[32,0] = 'Content-Type:'
                        singlereq.loc[33,0] = ''
                        singlereq.loc[36,0] = 'Content-Length:'
                        singlereq.loc[37,0] = ''
                        singlereq = singlereq.T
                        reqget = pd.concat([reqget,singlereq], ignore_index=True)

                    reqall = pd.concat([reqall,singlereq], ignore_index=True)
                    del singlereq
                    singlereq = pd.DataFrame()

                pbar.update()

    return (reqall, reqget,reqpost)

## Import
# Extracting objects from HTTP requests as features into DataFrames and saving .csv

path = '/Users/ivanivani/Documents/python/net_traffic_classifier'

normaltraffic_train = 'normalTrafficTraining.txt'
anomaloustraffic_test = 'anomalousTrafficTest.txt'
normaltraffic_test = 'normalTrafficTest.txt'

#Saving to .csv for easier handdling
print ('\nImporting ' + normaltraffic_train + ' file')
[reqnorm_train, reqgetnorm_train,reqpostnorm_train] = http_parser(os.path.join(path, normaltraffic_train))
reqnorm_train.to_csv(os.path.join(path,'net-traffic-classifier/reqnorm-train.csv'), index=False)
reqgetnorm_train.to_csv(os.path.join(path,'net-traffic-classifier/reqnorm-get-train.csv'), index=False)
reqpostnorm_train.to_csv(os.path.join(path,'net-traffic-classifier/reqnorm-post-train.csv'), index=False)

print ('\nImporting ' + anomaloustraffic_test + ' file')
[reqanom_test,reqgetanom,reqpostanom] = http_parser(os.path.join(path, anomaloustraffic_test))
reqanom_test.to_csv(os.path.join(path,'net-traffic-classifier/reqanom-test.csv'), index=False)
reqgetanom.to_csv(os.path.join(path,'net-traffic-classifier/reqanom-get-test.csv'), index=False)
reqpostanom.to_csv(os.path.join(path,'net-traffic-classifier/reqanom-post-test.csv'), index=False)

print ('\nImporting ' + normaltraffic_test + ' file')
[reqnorm_test, reqgetnorm_test,reqpostnorm_test] = http_parser(os.path.join(path, normaltraffic_test))
reqnorm_test.to_csv(os.path.join(path,'net-traffic-classifier/reqnorm-test.csv'), index=False)
reqgetnorm_test.to_csv(os.path.join(path,'net-traffic-classifier/reqnorm-get-test.csv'), index=False)
reqpostnorm_test.to_csv(os.path.join(path,'net-traffic-classifier/reqnorm-post-test.csv'), index=False)
