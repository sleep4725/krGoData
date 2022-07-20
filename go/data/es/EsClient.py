from elasticsearch import Elasticsearch
import elasticsearch

import yaml
import os
import sys 
PROJ_ROOT_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(PROJ_ROOT_PATH)

try:
    
    from error.EsError import EsClusterHealthError
except ImportError as err:
    print(f"Import error: {err}")

'''
@author JunHyeon.Kim
@date 20220719
''' 
class EsClient:
    
    @classmethod
    def getInstance(cls)-> Elasticsearch:
        '''
        :param:
        :return Elasticsearch instance: 
        '''
        global PROJ_ROOT_PATH
        esConfigPath = os.path.join(PROJ_ROOT_PATH, "config/ElasticConfig.yml")

        isExists = os.path.exists(esConfigPath)
        if isExists and os.path.isfile (esConfigPath):
            with open(esConfigPath, "r", encoding="utf-8") as config:
                esConnectInformation = yaml.safe_load(config)
                config.close()
                
                http = esConnectInformation["esHttp"] # es_http_protocol
                port = esConnectInformation["esPort"] # es_port 
                hosts = esConnectInformation["esHosts"]
                
                """http://127.0.0.1:9200"""
                
                esHosts = [f"{http}://{h}:{port}" for h in hosts]
                
                esHealthGood = False
                
                try:
                    
                    esClient = Elasticsearch(hosts=esHosts)
                    response = esClient.cluster.health()
                    if response["status"] in ["yellow", "green"]:
                       esHealthGood = True  
                except elasticsearch.exceptions.ConnectionError as err:
                    print(err)
                else:
                    if esHealthGood:
                        print(f"Elastic cluster health: {response['status']}")
                        return esClient
                    else:
                        raise EsClusterHealthError
                
if __name__ == "__main__":
    EsClient.getInstance()
        