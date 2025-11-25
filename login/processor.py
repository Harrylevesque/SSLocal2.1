from login.requests import dispatch_service_lookup


def login_processor(sv_uuid: str, svu_uuid: str) -> None:
    dispatch_service_lookup(sv_uuid, svu_uuid)
    print("Login processor executed.")