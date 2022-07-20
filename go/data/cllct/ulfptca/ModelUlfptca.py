from pathlib import Path
import yaml
import os 
PROJ_ROOT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

##
# @author JunHyeon.Kim
# @date 20220720
## -----------------------
class ModelUlfptca:
   
    @classmethod
    def getConfig(cls)->yaml.safe_load:
        '''
        :param:
        :return:
        '''
        global PROJ_ROOT_PATH
        configFile = os.path.join(PROJ_ROOT_PATH, f"config/DataServ_{Path(__file__).stem}.yml") 
        isExists = os.path.exists(configFile)
        if isExists: # 파일이 존재하는지 확인
            isFile = os.path.isfile(configFile)
            if isFile: # 파일이 normal file 인지 확인
                with open(configFile, "r", encoding="utf-8") as stream:
                    
                    try:
                    
                        information = yaml.safe_load(stream)
                        print(information)
                        stream.close()
                    except yaml.YAMLError as err:
                        print(err)
                    else:
                        return information
        else:
            raise FileNotFoundError