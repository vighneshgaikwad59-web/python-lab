class Account():
    def __init__(self,owner,blance):
        self.owner=owner
        self.blance=blance
    def __str__(self):
        return(f"account owner: {self.owner}\naccount balnced: {self.blance}")
    def despoit(self,dep_amont):
        self.blance+=dep_amont
        print("despoit accepted")
    def withdraw(self,wd_amt):
        if self.blance>=wd_amt:
            self.blance=wd_amt
            print("withdrawel accepetd")
        else:
            print("invalid")
acc1=Account("Jose",100)
print(acc1)
acc1.despoit(100)
acc1.withdraw(1000)