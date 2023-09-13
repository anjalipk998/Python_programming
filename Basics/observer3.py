class A(object):

    def __init__(self):
        self._p=23
    
    def m(self,):
         print(self._p)

    @property
    def p(self):
        return self._p 

    @p.setter
    def p(self, value):
        self._p = value
        self.m(value)

aObj= A()
aObj.m()
aObj._p=12
aObj.m()