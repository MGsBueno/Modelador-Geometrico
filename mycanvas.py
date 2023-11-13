from PyQt5 import QtOpenGL
from PyQt5.QtWidgets import *
from OpenGL.GL import *

class MyCanvas(QtOpenGL.QGLWidget):
    def __init__(self):
        super(MyCanvas, self).__init__()
        self.m_model = None
        self.m_w = 0 # width: GL canvas horizontal size
        self.m_h = 0 # height: GL canvas vertical size

    def initializeGL(self):
        #glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
    def resizeGL(self, _width, _height):
        # store GL canvas sizes in object properties
        self.m_w = _width
        self.m_h = _height
        # setup the viewport to canvas dimensions
        glViewport(0, 0, self.m_w, self.m_h)
        # reset the coordinate system
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # establish the clipping volume by setting up an
        # orthographic projection
        glOrtho(0.0, self.m_w, 0.0, self.m_h, -1.0, 1.0)
        # setup display in model coordinates
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    def paintGL(self):
        # clear the buffer with the current clear color
        glClear(GL_COLOR_BUFFER_BIT)
        # draw the model
        if (self.m_model==None)or(self.m_model.isEmpty()):
            return
        # Display model polygon RGB color at its vertices
        # interpolating smoothly the color in the interior
        verts = self.m_model.getVerts()
        glShadeModel(GL_SMOOTH)
        glColor3f(0.0, 1.0, 0.0) # green
        glBegin(GL_TRIANGLES)
        for vtx in verts:
            glVertex2f(vtx.getX(), vtx.getY())
        glEnd()
    def setModel(self,_model):
        self.m_model = _model