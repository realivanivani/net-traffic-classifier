import numpy as np
import pandas as pd

def http_parser(textfile):
    ## Takes a text file with HTTP requests and parses all attributes as features
    ## into dataframe objects
    ## Returns reqget and reqpost
    ##

    reqget = pd.DataFrame()             # GET requests
    reqpost = pd.DataFrame()            # POST requests
    singlereq = pd.DataFrame()          # intermediate DataFrame object

    with open(textfile) as infile:
        for line in infile:
                if not len(line.strip()) == 0:
                    splitline = pd.DataFrame(line.split())
                    singlereq= pd.concat([singlereq,splitline], ignore_index=True)

                elif not len(singlereq.index) == 0:
                    if singlereq.values[0,0] == 'POST':
                        splitline = pd.DataFrame(next(infile).split())
                        singlereq = pd.concat([singlereq,splitline], ignore_index=True)
                        singlereq = singlereq.T
                        reqpost = pd.concat([reqpost,singlereq], ignore_index=True)
                    else:
                        singlereq = singlereq.T
                        reqget = pd.concat([reqget,singlereq], ignore_index=True)

                    del singlereq
                    singlereq = pd.DataFrame()
                else:
                    next(infile)

    return (reqget,reqpost)

# Extracting objects from HTTP requests as features and putting it into DataFrame
normaltraffic_train = '/Users/ivanivani/Documents/python/net_traffic_classifier/normalTrafficTraining.txt'
anomaloustraffic_test = '/Users/ivanivani/Documents/python/net_traffic_classifier/anomalousTrafficTest.txt'
normaltraffic_test = '/Users/ivanivani/Documents/python/net_traffic_classifier/normalTrafficTest.txt'

[reqgetnorm_train,reqpostnorm_train] = http_parser(normaltraffic_train)
reqnorm_train=pd.DataFrame(pd.concat([reqgetnorm_train,reqpostnorm_train], ignore_index=True))
# Saving to .csv for easier handdling
reqnorm_train.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-train.csv', index=False)
reqgetnorm_train.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-get-train.csv', index=False)
reqpostnorm_train.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-post-train.csv', index=False)

[reqgetanom,reqpostanom] = http_parser(anomaloustraffic_test)
reqanom_test=pd.DataFrame(pd.concat([reqgetanom,reqpostanom], ignore_index=True))
reqanom_test.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqanom-test.csv', index=False)
reqgetanom.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqanom-get-test.csv', index=False)
reqpostanom.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqanom-post-test.csv', index=False)

[reqgetnorm_test,reqpostnorm_test] = http_parser(normaltraffic_test)
reqnorm_test=pd.DataFrame(pd.concat([reqgetnorm_test,reqpostnorm_test], ignore_index=True))
reqnorm_test.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-test.csv', index=False)
reqgetnorm_test.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-get-test.csv', index=False)
reqpostnorm_test.to_csv('/Users/ivanivani/Documents/python/net_traffic_classifier/reqnorm-post-test.csv', index=False)
