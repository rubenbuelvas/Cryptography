def caesar(message, key, mode="decode", alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    new_message = ""
    for i in range(len(message)):
        found = False
        for j in range (len(alphabet)):
            if message[i].upper() == alphabet[j]:
                found = True
                if mode == "decode":
                    new_message += alphabet[(j-key)%len(alphabet)]
                elif mode == "encode":
                    new_message += alphabet[(j+key)%len(alphabet)]
        if not found:
            new_message += message[i]
    return new_message


print(caesar("Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.", 7))
