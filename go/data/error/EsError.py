'''
@author JunHyeon.Kim
'''
class EsClusterHealthError(Exception):
    
    def __init__(self) -> None:
        super().__init__("Cluster의 Health가 문제가 있습니다.")
    