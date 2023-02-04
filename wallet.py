

class wallet:
  def __init__(self,b):
    self.balance=b
  def getAmount(self):
    return self.balance
  def setAmount(self,am):
    self.balance=am
  def removeAmount(self,am):
    if(self.balance-am>0):
      self.balance-=am
