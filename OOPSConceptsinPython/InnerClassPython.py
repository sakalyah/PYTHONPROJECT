class Cricket:
    def __init__(self,bowler,batsmen):
        self.bowler = bowler
        self.batsmen = batsmen
        self.t20 = self.T20("UAE") #Without this line in __init__ the class cannot be instantined.

    def details(self):
        print("Team's Details are :"+self.bowler+" "+self.batsmen)
    class T20: #Inner CLass
        def __init__(self,venue):
            self.venue = venue
            self.country = "DUBAI"
        def DC(self):
            print(self.venue,self.country)
SRH = Cricket("Rashid","Bairstow")
print(SRH.t20.venue,SRH.details(),SRH.t20.DC())
RCB = Cricket("YADAV","ABD")
print(RCB.t20.venue,RCB.details(),RCB.t20.DC())

