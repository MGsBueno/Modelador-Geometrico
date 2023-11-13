class MyPoint:
    def __init__(self):
        self.m_x = 0
        self.m_y = 0

    def __init__(self,_x,_y):
        self.m_x = _x
        self.m_y = _y

    def setX(self,_x):
        self.m_x = _x

    def setY(self,_y):
        self.m_y = _y

    def getX(self):
        return self.m_x

    def getY(self):
        return self.m_y