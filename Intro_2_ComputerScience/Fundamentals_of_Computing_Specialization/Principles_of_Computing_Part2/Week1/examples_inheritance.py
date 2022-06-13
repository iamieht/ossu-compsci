# Simple inheritance

class Base:
    def hello(self):
        print "hello"
        
    def message(self, msg):
        print msg
        
class Sub(Base):
    def message(self, msg):
        print "sub:", msg
        
obj = Sub()
obj.hello()
obj.message("what's going to happen?")

baseobj = Base()
baseobj.hello()
baseobj.message("another message")
