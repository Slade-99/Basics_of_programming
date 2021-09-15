def phnum(number):

    if len(number) != 11:
        return False
    if number[0:2] != "01":
        return False
    for i in range(len(number)):
        if not number[i].isdecimal():
            return False
            

    return True

message = "awdsfokanmsdokfm  asdfn[asdkfn 01923453390 asdljfnasdojfnaosjdfn"


flag = False
for i in range(len(message)):
    part = message[i:i+11]
 
    if phnum(part):
        print(f"Phone number found {part}")
        flag = True


if not flag:
    print("No numbers found")



