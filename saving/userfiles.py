# python
import os
import json
from typing import Optional
import base64

def save_response_u(filename: Optional[str] = None, field: Optional[str] = None) -> None:
    from creation.serviceuser import resp, privkey

    data = resp.json()
    privkey_str = base64.b64encode(privkey).decode('ascii') if isinstance(privkey, (bytes, bytearray)) else str(privkey)
    data["privkey"] = privkey_str
    user_uuid = data.get("userUUID") or data.get("useruuid")

    if filename is None:
        filename = f"{user_uuid}.json" if user_uuid else "response.json"
    else:
        dirpath = os.path.dirname(filename)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)

    with open(filename, "w") as f:
        if field:
            value = data.get(field)
            f.write(value if isinstance(value, str) else json.dumps(value))
        else:
            f.write(json.dumps(data, indent=2))

    print(privkey)


def save_response_sv(filename: Optional[str] = None, field: Optional[str] = None) -> None:
    from creation.service import resp, useruuid, privkey

    data = resp.json()
    privkey_str = base64.b64encode(privkey).decode('ascii') if isinstance(privkey, (bytes, bytearray)) else str(privkey)
    data["privkey"] = privkey_str
    service_uuid = data.get("serviceuuid") or data.get("serviceUUID")
    user_uuid = useruuid or data.get("userUUID") or data.get("useruuid")

    if filename is None:
        if service_uuid:
            if user_uuid:
                dirpath = user_uuid
                os.makedirs(dirpath, exist_ok=True)
                filename = os.path.join(dirpath, f"{service_uuid}.json")
            else:
                filename = f"{service_uuid}.json"
        else:
            filename = "response.json"
    else:
        dirpath = os.path.dirname(filename)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)

    with open(filename, "w") as f:
        if field:
            value = data.get(field)
            f.write(value if isinstance(value, str) else json.dumps(value))
        else:
            f.write(json.dumps(data, indent=2))

    print(privkey)

def save_response_svu(filename: Optional[str] = None, field: Optional[str] = None) -> None:
    from creation.serviceuseruser import resp, serviceuuid, privkey

    data = resp.json()
    privkey_str = base64.b64encode(privkey).decode('ascii') if isinstance(privkey, (bytes, bytearray)) else str(privkey)
    data["privkey"] = privkey_str
    service_uuid = data.get("serviceuuid") or data.get("serviceUUID")
    svuUUID = data.get("svuUUID") or data.get("svuUUID")

    if filename is None:
        if service_uuid:
            if svuUUID:
                dirpath = service_uuid
                os.makedirs(dirpath, exist_ok=True)
                filename = os.path.join(dirpath, f"{svuUUID}.json")
            else:
                filename = f"{svuUUID}.json"
        else:
            filename = "fail.json"
    else:
        dirpath = os.path.dirname(filename)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)

    with open(filename, "w") as f:
        if field:
            value = data.get(field)
            f.write(value if isinstance(value, str) else json.dumps(value))
        else:
            f.write(json.dumps(data, indent=2))

    print(privkey)

if __name__ == "__main__":
    save_response_svu()
