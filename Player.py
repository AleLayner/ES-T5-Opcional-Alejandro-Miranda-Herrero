class Player():
    def __init__(self, name:str):
        self.name=name
        self.num_points= 0
    
    def get_name(self)->str:
        return self.name
    
    def get_points(self)->int:
        return self.num_points
    
    def is_equal(self,player)->bool:
        return self.name==player.name
    
    def add_point(self)->None:
        self.num_points=1+self.num_points
        