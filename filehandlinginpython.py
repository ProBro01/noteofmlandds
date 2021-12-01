# import socket

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("192.168.164.14", 1234))
# server.listen()
# cli, add = server.accept()
# with open("main.exe", "rb") as f:
#     while True:
#         data = f.read(1024)
#         if data == b'':
#             cli.send(b'done')
#             break
#         cli.send(data)

# name = input("Enter Your name: ")
# age = input("Enter Your age: ")
# gender = input("Your Gender: ")
# birp = input("Birth Place: ")
# f = open("note.txt", "a")
# stringtobeenterd = ",".join([name, age, gender, birp])
# f.write("\n"+stringtobeenterd)
# f.close()


f = open("note.txt", "r")
data = f.read()
data = data.split("\n")
person = {}
keys = data.pop(0)
keys = keys.split(',')
for var in keys:
    person[var] = []
for var in data:
    person1 = var.split(",")
    if person1 != "":
        person[keys[0]].append(person1[0])
        person[keys[1]].append(person1[1])
        person[keys[2]].append(person1[2])
        person[keys[3]].append(person1[3])
    else:
        break
print(person)
