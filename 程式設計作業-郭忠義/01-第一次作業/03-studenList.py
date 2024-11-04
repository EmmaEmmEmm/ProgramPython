name = input()
id = int(input())
chinese = int(input())
computer = int(input()) 
design = int(input())

total = chinese + computer + design
average = int(total/3)

a = {"name":name, "id":id, "total":total, "average":average}

print("Name:{name}".format(**a))
print("Id:{id}".format(**a))
print("Total:{total}".format(**a))
print("Average:{average}".format(**a))