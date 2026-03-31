try:
    from config_local import TOKEN
except ImportError:
    TOKEN = None
    print("Токен ен найден")

BASE_URL = "https://yougile.com/api-v2"


def get_headers():
    if not TOKEN:
        raise ValueError("Токена нет")
    return {
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json"
    }
