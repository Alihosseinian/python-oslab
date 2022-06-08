from enum import Flag
import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtUiTools import  QUiLoader
from functools import partial

from PySide6.QtUiTools import  QUiLoader
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("Designer.ui")
        self.ui.show()

        self.eql=False
        self.input=None
        self.result=0.0
        self.sumop=False
        self.divop=False
        self.mulop=False
        self.subop=False
        self.remop=False
        self.powop=False

        self.ui.n1.clicked.connect(partial(self.handler, '1' ,None,'num'))
        self.ui.n2.clicked.connect(partial(self.handler, '2' ,None,'num'))
        self.ui.n3.clicked.connect(partial(self.handler, '3' ,None,'num'))
        self.ui.n4.clicked.connect(partial(self.handler, '4' ,None,'num'))
        self.ui.n5.clicked.connect(partial(self.handler, '5' ,None,'num'))
        self.ui.n6.clicked.connect(partial(self.handler, '6' ,None,'num'))
        self.ui.n7.clicked.connect(partial(self.handler, '7' ,None,'num'))
        self.ui.n8.clicked.connect(partial(self.handler, '8' ,None,'num'))
        self.ui.n9.clicked.connect(partial(self.handler, '9' ,None,'num'))
        self.ui.n0.clicked.connect(partial(self.handler, '0' ,None,'num'))

        self.ui.opoint.clicked.connect(partial(self.handler, '.' ,'num'))
        self.ui.osum.clicked.connect(partial(self.handler, None ,self.sum))
        self.ui.osub.clicked.connect(partial(self.handler, None ,self.sub))
        self.ui.odiv.clicked.connect(partial(self.handler, None ,self.div))

        self.ui.omulti.clicked.connect(partial(self.handler, None ,self.mul))

        self.ui.osign.clicked.connect(partial(self.handler, None ,self.sign))
        self.ui.clear.clicked.connect(partial(self.handler, None ,self.clear))
        self.ui.osin.clicked.connect(partial(self.handler, None ,self.sin))
        self.ui.ocos.clicked.connect(partial(self.handler, None ,self.cos))
        self.ui.otan.clicked.connect(partial(self.handler, None ,self.tan))
        self.ui.ocot.clicked.connect(partial(self.handler, None ,self.cot))
        self.ui.olog.clicked.connect(partial(self.handler, None ,self.log))
        self.ui.oln.clicked.connect(partial(self.handler, None ,self.ln))
        self.ui.o1x.clicked.connect(partial(self.handler, None ,self.ondivx))
        self.ui.orad.clicked.connect(partial(self.handler, None ,self.rad))
        self.ui.opower.clicked.connect(partial(self.handler, None ,self.power))
        self.ui.opower1y.clicked.connect(partial(self.handler, None ,self.power1))
        self.ui.oremain.clicked.connect(partial(self.handler, None ,self.remain))
        self.ui.oeq.clicked.connect(partial(self.handler, None ,self.equal,eq=True))


    def handler(self,input,oprator,type=None,eq=False):
        
        if self.input != None:
            if(input!=None or (input == '.' and '.' not in self.input)):
                self.input+=input
        else:
            self.input=input
        self.ui.label.setText(self.input)

        if eq:
            oprator()
            self.eql=True
        elif type!='num' and oprator != None and input!='.':
            oprator()

    def sin(self):
        self.result = math.sin(math.radians(float(self.input)))
        self.ui.label.setText(str(self.result)) 

    def cos(self):
       self.result = math.cos(math.radians(float(self.input)))
       self.ui.label.setText(str(self.result)) 

    def tan(self):
       self.result = math.tan(math.radians(float(self.input)))
       self.ui.label.setText(str(self.result)) 

    def cot(self):
       self.result = 1/math.tan(math.radians(float(self.input)))
       self.ui.label.setText(str(self.result)) 

    def log(self):
        self.result = math.log10(float(self.input))
        self.ui.label.setText(str(self.result)) 

    def ln(self):
        self.result = math.log2(float(self.input))
        self.ui.label.setText(str(self.result)) 

    def rad(self):
        self.result = math.radians(float(self.input))
        self.ui.label.setText(str(self.result)) 

    def ondivx(self):
        self.result = 1/float(self.input)
        self.ui.label.setText(str(self.result))

    def sign(self):
        if self.input[0]=='-':
            self.result = float(self.input[1:])
            self.input=str(self.result)
            self.ui.label.setText(str(self.result)) 
        else: 
            self.result =float("-" + self.input)
            self.input=str(self.result)
            self.ui.label.setText(str(self.result)) 

    def equal(self):
        if self.sumop :
            self.result = self.result + float(self.input)
            self.sumop=False
            self.input=str(self.result)
        elif self.subop:
            self.result -= float(self.input)
            self.subop=False
            self.input=str(self.result)
        elif self.mulop:
            self.result = self.result * float(self.input) 
            self.mulop=False
            self.input=str(self.result)
        elif self.divop:
            self.result = self.result / float(self.input) 
            self.divop=False
            self.input=str(self.result)
        elif self.remop:
            self.result = self.result % int(self.input)
            self.remop=False
            self.input=str(self.result)
        elif self.powop:
            self.result = self.result ** float(self.input) 
            self.powop=False
            self.input=str(self.result)
        self.ui.label.setText(str(self.result))

    def sum(self):
        if self.result !=0 and not self.eql:
            self.result+=float(self.input)
        else :
            self.result = float(self.input)
            self.eql=False
        self.ui.label.setText('')
        self.input=None
        self.sumop = True

    def power(self):

        if self.result !=0 and not self.eql:
            self.result**=float(self.input)
        else :
            self.result = float(self.input)
            self.eql=False

        self.ui.label.setText('')
        self.input=None
        self.powop = True
    
    def sub(self):
        if self.result !=0 and not self.eql:
            self.result-=float(self.input)
        else :
            self.result = float(self.input)
            self.eql=False

        self.ui.label.setText('')
        self.input=None
        self.subop = True

    def power1(self):
        self.result =math.sqrt(float(self.input))
        self.ui.label.setText(str(self.result)) 
        
    def remain(self):
        if self.result !=0 and not self.eql:
            self.result %= float(self.input)
        else :
            self.result = float(self.input)
            self.eql=False
        self.ui.label.setText('')
        self.input=None
        self.remop = True
    
    def div(self):
        
        if self.result !=0 and not self.eql:
            self.result/=float(self.input)
        else :
            self.result = float(self.input)
            self.eql=False
        self.ui.label.setText('')
        self.input=None
        self.divop = True

    def mul(self):
        if self.result !=0 and not self.eql:
            self.result*=float(self.input)
        else :
            self.result = float(self.input)
            self.eql=False
        self.ui.label.setText('')
        self.input=None
        self.mulop = True

    def clear(self):
       self.result = 0
       self.oprand = 0
       self.input = None
       self.ui.label.setText(self.input)

if __name__ == '__main__':    
    my_app = QApplication()
    calculator = Calculator()
    calculator.setFixedSize(200 , 300)
    my_app.exec()
