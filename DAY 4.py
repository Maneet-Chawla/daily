# handling multiple Exception
try:
    x=int(input("Enter a number :"))
    result= 10/x
    
except ValueError:
    print("Invalid number! please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero.")

#custom exception :
class MyCustomerError(Exception)
    pass
try:
    MyCustomerError("this is the customer error!")
except MyCustomerError as e:
    print("caught the errpe",e)

#else and finally exception:

try:
    int(input("Enter a number :"))
    result = 10/x
except ZeroDivisionError:
    print("Division error")
else:
    print("Division coreect:",result)
finally:
    print("This block always run")

#write and read the text file :
# open the file in write mode('w create')
with open("data.text","w") as file:
    file.write("hello this is the saved data")
    file.write("it will stored even the prograam runs")

#for read rthe text file:
with open("data.txt","r") as file:
    content =file.read()
    print("content")

#CSV file operations:
# 1.read 
import csv
with open('data.txt','r') as file:
     reader=csv.reader(file)
     for row in reader:
         print(row)

# 2.write
import csv
Data =[['name','age'],['ally',20],['pal','10']]
with open('data.txt','w') as file:
    writer =csv.write(file)
    writer.writerows(Data)

# JSON HANDLING 
(1)CONVERT PYHON TO JSON (json.dumps)
import Json

person={"name:maneet","age:21","city:indore"}

Json_data=Json.dumps(person)
print(Json_data)

# (2) CONVERT JSON TO PYTHON(json.load)
import json

json_str={"name":"maneet","age":"21","city":"indore"}

person=json.load(json_str)
print(person["name"])

# (3) Write json file (using json.dump)
import json

data={"name:maneet","age:20","city:indore"}
with open("data.json","w") as file:
    json.dump(data)

# (4) read json file (using json.load)
import json
with open("data.json","r") as file:
    data=json.load(file)
    print(data["name"])


#context manager (with statement):
with("data.txt","w") as file:
    file.write("enter the number ")
    # file will automatically closed here