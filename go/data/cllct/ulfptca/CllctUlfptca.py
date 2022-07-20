import os
from pydoc import pager 
import sys
import requests 
from urllib.parse import urlencode 
PROJ_ROOT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(PROJ_ROOT_PATH)

try:
    
    from es.EsClient import EsClient
    from ModelUlfptca import ModelUlfptca
    from util.TimeUtil import TimeUtil
except ImportError as err:
    print(err)

'''
@author JunHyeon.Kim
@date 20220720
'''
class CllctUlfptca:
    
    def __init__(self) -> None:
        self.config = ModelUlfptca.getConfig()
        self.baseUrl = self.config["baseUrl"]
        self.urlParam = CllctUlfptca.initUrlParam(self.config)
    
    def getData(self):
        '''
        '''
        url = self.setUrl(page=1)
        response = requests.get(url, verify= False)
        
        if response.status_code == 200:
            
            try:
                
                data = dict(response.json())["response"]
                resultCode = self.getHeader(data["header"])
                
                if resultCode:
                    print(data["body"])
            except:
                pass 
        
        response.close()

    def getHeader(self, header: dict):
        '''
        '''
        resultCode = header["resultCode"]
        if resultCode == "00":
            return True 
        else:
            return False
        
    def setUrl(self, page):
        '''
        :param:
        :return:
        '''
        return self.baseUrl + \
                "?" + \
                self.urlParam + \
                "&year=" + TimeUtil.getCurrentYear() + \
                "&pageNo=" + f"{page}" 
                
    @classmethod
    def initUrlParam(cls, config):
        '''
        '''
        return urlencode({
            "serviceKey": config["serviceKey"]
            ,"returnType": config["returnType"]
            ,"numOfRows": config["numOfRows"]
            ,"itemCode": config["itemCode"]
        })
        
if __name__ == "__main__":
    o = CllctUlfptca()
    o.getData()