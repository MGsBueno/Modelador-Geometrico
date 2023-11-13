from mypoint import *
class MyModel:
    def __init__(self):
        self.m_verts = []
        p1 = MyPoint(100.0,100.0)
        p2 = MyPoint(200.0,100.0)
        p3 = MyPoint(150.0,175.0)
        self.m_verts.append(p1)
        self.m_verts.append(p2)
        self.m_verts.append(p3)

    def getVerts(self):
        return self.m_verts

    def isEmpty(self):
        return len(self.m_verts) == 0