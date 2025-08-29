# utils/auth.py
from huggingface_hub import whoami, HfApi

def validate_token(token: str):
    try:
        api = HfApi()
        user_info = whoami(token)
        return True, user_info["name"]
    except Exception:
        return False, None
