class BillController(object):
    def __init__(self,BillService):
        self.BillService = BillService

    def addBill(self,id,groupId,amount,contribution,paidBy):
        return self.BillService.addBill(id,groupId,amount,contribution,paidBy)
    
    def getUserBalance(self,userId):
        balance=0
        for billId in self.BillService.billDetails:
            bill=self.BillService.billDetails.get(billId)

            if userId in bill.getContribution():
                balance=balance - bill.getContribution().get(userId)
            
            if userId in bill.getPaidBy():
                balance=balance + bill.getPaidBy().get(userId)
        return balance
        
