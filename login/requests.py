import requests
import json


dispatch_location = "https://dispatch.ssl.harrylevesque.dev"


def dispatch_service_lookup(sv_uuid: str, svu_uuid: str) -> None:
    resp = requests.get(f"{dispatch_location}/service/find/{sv_uuid}/{svu_uuid}")
    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text, "status_code": resp.status_code}

    print(json.dumps(body, indent=2))
    return {"status_code": resp.status_code, "body": body}