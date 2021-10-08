import hashlib
def machine():
    # creating key strings
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # auto generating the vaules of strings
    # value will be generted by taking last to first
    # concatinated with the rest of the string
    values = keys[-1] + keys[0:-1]
    # print(keys)
    # print(values)

    # creating two dictionaries
    encrytDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    # user input
    message = input("Enter your secret message: ")
    mode = input("Crypto Mode : Encode(E) OR Decode(D)")

    #encode and decode
    if mode.upper() == 'E':
        newMessage = ''.join([encrytDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("Please try again, wrong choice entered")

    return newMessage.capitalize()

pt=input("Enter PlainText: ")
print("Select the Hash Algorithm You want to use now: '\n")
print("1. SHA-1 '\n'")
print("2. SHA-256 '\n'")
print("2. SHA-512 '\n'")
print("3. MD5 '\n'")
switcher = {
    1: 

}
return switcher.get(num,"Wrong Algorithm Selected")
print(machine())