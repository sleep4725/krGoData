import time 

##
#
##
class TimeUtil:
    
    @classmethod
    def getCurrentYear(cls):
        '''
        :param:
        :return:
        '''
        return time.strftime("%Y", time.localtime())