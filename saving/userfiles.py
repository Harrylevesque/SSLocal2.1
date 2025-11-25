# python
import os
import json
from typing import Optional
import base64
import requests


def save_response_u(filename: Optional[str] = None, field: Optional[str] = None) -> None:
    from creation.serviceuser import get_user_creation_result

    resp, privkey = get_user_creation_result()

    try:
        data = resp.json()
    except ValueError:
        data = {"raw": resp.text, "status_code": resp.status_code}

    privkey_str = base64.b64encode(privkey).decode("ascii") if isinstance(privkey, (bytes, bytearray)) else str(privkey)
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
    # Import lazily to avoid circular import and to fetch the latest response
    from creation.service import get_service_creation_result

    resp, useruuid, privkey = get_service_creation_result()

    # Normalise useruuid: strip any trailing .json if user pasted it
    useruuid = useruuid.strip()
    if useruuid.endswith(".json"):
        useruuid = useruuid[:-5]

    # Try to parse JSON; if it fails (e.g. 500 HTML), fall back to using resp.text
    try:
        data = resp.json()
    except (ValueError, requests.exceptions.RequestException, Exception):
        data = {"raw": resp.text, "status_code": resp.status_code}

    privkey_str = base64.b64encode(privkey).decode("ascii") if isinstance(privkey, (bytes, bytearray)) else str(privkey)
    data["privkey"] = privkey_str

    service_uuid = data.get("serviceuuid") or data.get("serviceUUID")
    # Prefer the explicitly entered useruuid as the identifier
    user_uuid = useruuid or data.get("userUUID") or data.get("useruuid")

    # If the caller passes an explicit filename, just honour it like before
    if filename is not None:
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
        return

    # No explicit filename: follow the desired behaviour
    # 1) Create/overwrite a file with the user UUID as the name
    if user_uuid:
        base_user_file = f"{user_uuid}.json"
        with open(base_user_file, "w") as f:
            if field:
                value = data.get(field)
                f.write(value if isinstance(value, str) else json.dumps(value))
            else:
                f.write(json.dumps(data, indent=2))
    else:
        base_user_file = None

    # 2) Create a directory with that same UUID name (if we have one)
    #    and then write the service-specific file inside it.
    if service_uuid and user_uuid:
        dirpath = user_uuid
        # If a file with this name already exists, remove it so a directory can be created
        if os.path.isfile(dirpath):
            os.remove(dirpath)
        os.makedirs(dirpath, exist_ok=True)
        filename = os.path.join(dirpath, f"{service_uuid}.json")
    elif service_uuid:
        # Fallback: just use the service UUID as a plain file name
        filename = f"{service_uuid}.json"
    else:
        filename = "response.json"

    with open(filename, "w") as f:
        if field:
            value = data.get(field)
            f.write(value if isinstance(value, str) else json.dumps(value))
        else:
            f.write(json.dumps(data, indent=2))

    print(privkey)


def save_response_svu(filename: Optional[str] = None, field: Optional[str] = None) -> None:
    # Import lazily to avoid circular import at module load time
    from creation.serviceuseruser import get_svu_creation_result

    resp, serviceuuid, privkey = get_svu_creation_result()

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
    # Default to service-user variant when run directly
    save_response_sv()
