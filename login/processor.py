from saving.workingfiles import save_workingfiles
from typing import Optional


def login_processor(sv_uuid: str, svu_uuid: str, serviceip: str) -> Optional[str]:
    """Initialize the working file for a login attempt.

    This calls `save_workingfiles` using the UUIDs provided and returns the saved
    filename (or None if saving failed).
    """
    # Pass the supplied UUIDs so `save_workingfiles` doesn't prompt again.
    saved = save_workingfiles(serviceip, sv_uuid=sv_uuid, svu_uuid=svu_uuid)
    if saved:
        print(f"Working file saved to: {saved}")
    else:
        print("Working file was not saved.")
    return saved
