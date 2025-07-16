import os
import time
import hashlib
import hmac
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()

PARTNER_ID   = os.getenv("SHOPEE_PARTNER_ID")
PARTNER_KEY  = os.getenv("SHOPEE_PARTNER_KEY")
SHOP_ID      = os.getenv("SHOPEE_SHOP_ID")
ACCESS_TOKEN = os.getenv("SHOPEE_ACCESS_TOKEN")

BASE_URL = "https://partner.shopeemobile.com"

def sign(path: str, timestamp: int) -> str:
    """Shopee OpenAPI v2 の署名を生成"""
    base_string = f"{PARTNER_ID}{path}{timestamp}{ACCESS_TOKEN}{SHOP_ID}"
    return hmac.new(
        PARTNER_KEY.encode(), base_string.encode(), hashlib.sha256
    ).hexdigest()

def request(path: str, payload: dict | None = None) -> dict:
    """GET リクエストの共通処理"""
    timestamp = int(time.time())
    payload = payload or {}

    query = {
        "partner_id": PARTNER_ID,
        "shop_id": SHOP_ID,
        "access_token": ACCESS_TOKEN,
        "timestamp": timestamp,
        **payload,
    }
    url_path = f"/api/v2{path}"
    headers = {"Authorization": sign(url_path, timestamp)}
    url = f"{BASE_URL}{url_path}?{urlencode(query)}"

    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()

# --- テスト用関数 -------------------------------------------------

def get_shop_info() -> dict:
    """ショップ基本情報を取得"""
    return request("/shop/get_shop_info")

# スクリプト単体実行時のテスト
if __name__ == "__main__":
    try:
        print(get_shop_info())
    except Exception as e:
        print("Error:", e)