import sys
sys.path.append('/Users/khush')

from splitwise.controllers.user_controller import UserController
from splitwise.controllers.bill_controller import BillController
from splitwise.controllers.group_controller import GroupController

from splitwise.services.bill_service import BillService
from splitwise.services.group_service import groupService
from splitwise.services.user_service import userService

userController=UserController(userService())
billController=BillController(BillService())
groupController=GroupController(groupService())

user1=userController.addUser('user1','pawan')
user2=userController.addUser('user2','naman')
user3=userController.addUser('user3','gyan')
user4=userController.addUser('user4','pd')
user5=userController.addUser('user5','sa')

members=[user1,user2,user3,user4,user5]
group1=groupController.addGroup('group1','newgroup',members)

#print(group1.getMembers())

paidBy={'user1':200,'user2':100,'user3':50,'user4':50,'user5':100}
contribution={'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}

bill1=billController.addBill('bill1','group1',500,contribution,paidBy)

balance=billController.getUserBalance('user1')
print(balance)
