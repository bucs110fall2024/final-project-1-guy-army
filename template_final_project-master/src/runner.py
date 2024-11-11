class Runner:
    
    def __init__(self,x, y, img_file):
        """
        Initializes the Runner object
        args:
        - x : int - starting x coordinate
        - y : int - starting y coordinate
        - img_file : str - path to img file
        """
        self.x = x
        self.y = y
        self.img = img_file
        self.xvel = 0
        self.yvel = 0
        self.hp = 1
    def jump(self):
        '''
        makes the runner jump
        args: none
        return: none
        NOT YET IMPLENTED
        '''
    def slide(self):
        ''' makes the runner slide
        args: none
        return: none
        NOT YET IMPLENTED
        '''
