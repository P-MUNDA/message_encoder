


# def decode_message(encoded_message):
#     decoded_message=''
#     for char in encoded_message:
#         decoded_message+= chr(ord(char)-1)
#     return decoded_message
# # Encoded message
# encoded_message = "Ifmmp!J'n opu b gfxmppst nztfmf jt zpv"

# # Decode and print the message
# hidden_message = decode_message(encoded_message)
# print(hidden_message)



print("................Wellcome to Message encoder.............")

message2= input("Enter Your message here: ")
def encode_message2 (message2):
    encoded_message2=''
    for char in message2:
        encoded_message2+=chr(ord(char)-1)
    return encoded_message2

hidden_message2=encode_message2(message2)
print(f'Your hidden message is : {hidden_message2}')
