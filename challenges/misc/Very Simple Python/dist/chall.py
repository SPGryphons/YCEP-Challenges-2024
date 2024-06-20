import base64

flag = "JJJEIRKFKZFUYS2WIJDEOURSKNDVMS2VJ5HEGVKMJJEFKRKNKNCUSRSOIRDVKMSIJNFE2VKPKVFFOSSNGNKVOTSDLJGEERKUIVIVUWCKJZBEISKXINFEOSSCIZBVIUZSJNBEWVSTKRJUKSRVI5KEWTKTLBEU4TSEI5JFGUKLKU3FIMSQJI2UQVJWKE6T2PJ5"

def my_decoder(flag):
    for _ in range(3):
        try:
            flag = base64.b32decode(flag)
        except Exception as e:
            return f"Decoding failed: {str(e)}"
    return flag

Destination = input("Where do you want to go: ")

if Destination == "" :
    print("Invalid destination")
elif Destination == "Singapore" :
    print("Are you sure?")
elif Destination == "jce8457bej539csjbhrsjewcjk" :
    print(my_decoder(flag))
else:
    print("Welcome to " + Destination)
