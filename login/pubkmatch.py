
import base64
import hashlib

pubk = input("Enter public key: ").strip()
pubkb64 = base64.b64encode(pubk.encode()).decode()
pubkfinal = hashlib.sha256(pubkb64.encode()).digest()
print(pubkfinal.hex())




def tree():
    step1 = input("Enter step 1: ").strip()
    if step1 == "1":
        pubkserver = input("Enter server public key: ").strip()
        pubkserverb64 = base64.b64encode(pubkserver.encode()).decode()
        pubkserverfinal = hashlib.sha256(pubkserverb64.encode()).digest()
        print(pubkserverfinal)


        if pubkserverfinal == pubkserverfinal:
            print("Server public key is correct.")

# example usage
if __name__ == "__main__":
    print(tree())
