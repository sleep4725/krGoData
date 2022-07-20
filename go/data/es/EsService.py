from elasticsearch import Elasticsearch

class EsService:
        
    @classmethod
    def esInstanceClose(cls, es: Elasticsearch):
        '''
        '''
        try:
            
            es.close()
        except:
            pass  