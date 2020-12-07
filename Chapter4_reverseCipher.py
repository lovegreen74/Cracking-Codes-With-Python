# Reverse Cipher
# https://www.nostarc.com/crackingcodes/ (BSD Licensed)
#%%
def reverseCipher():
    message=input("Enter message: ")
    translated = ''
    i = len(message) - 1
    while i>= 0:
        translated = translated + message[i]
        print('i is', i, ', message[i] is', message[i], ', translated is',
        translated)
        i = i - 1
    print(translated)
#%%
def reverseCipher():
    message=input("Enter message: ")
    translated = ''
    i = len(message) - 1
    while i>= 0:
        translated = translated + message[i]
        i = i - 1
    print()
    print(translated)
