import hashlib
nonce=0
string="Heldlo World"
while True:
    res=str(nonce)+string
    hash_object = hashlib.md5(res.encode('utf-8'))
    if str(hash_object)[0:2]=="00":
        print(nonce)
        break
    nonce+=1


