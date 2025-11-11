import sys
import base64
import requests
import quantcrypt.kem as qkem
import quantcrypt.internal.pqa.kem_algos as algos

try:
    # Example: if your discover is MLKEM_768.keygen()
    kp = algos.MLKEM_768()
    pubkey, privkey = kp.keygen()
except Exception as e:
    print(f"quantcrypt imported but could not generate keypair: {e}")
    sys.exit(1)

def to_bytes(x):
    if isinstance(x, (bytes, bytearray, memoryview)):
        return bytes(x)
    if isinstance(x, str):
        return x.encode()
    raise TypeError("unexpected key type")

try:
    pub_bytes = to_bytes(pubkey)
    priv_bytes = to_bytes(privkey)
except TypeError as e:
    print(f"Unexpected key types: {e}")
    sys.exit(1)

print(f"Private key length: {len(priv_bytes)} bytes")
print(f"Public key length: {len(pub_bytes)} bytes")

useruuid = input("Enter UUID: ")

data = {"pubk": base64.b64encode(pub_bytes).decode()}
resp = requests.post("http://localhost:8000/service/{useruuid}/service/new", json=data)
print(resp.status_code)
try:
    print(resp.json())
except ValueError:
    print(resp.text)
