class RCB:
    def execute(self):
        print("RCB executes itself")
    def talks(self):
        print("RCB talks")

class DC :
    def execute(self):
        print("DC executes itself")

    def talks(self):
            print("DC talks")
class IPL :
    def __init__(self,kohli):
        kohli.execute()
        kohli.talks()

class SRH:
    def code(self,rabada):
        rabada.execute()
        rabada.talks()

#IPL(DC())
rcb = RCB()
dc = DC()
ipl = IPL(rcb)
srh = SRH()
srh.code(dc)

