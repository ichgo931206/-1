import hashlib
import hmac
import base64
import urllib.parse

def md5(text: str, encoding='utf-8') -> str:
    """Generate MD5 hash of the input string."""
    md5_hash = hashlib.md5(text.encode(encoding)).hexdigest()
    return md5_hash

def hash_hmac(text: str, key: bytes) -> str:
    """Generate HMAC-SHA256 of the input text using the given key."""
    hmac_hash = hmac.new(key, text.encode('utf-8'), hashlib.sha256).digest()
    return base64.b64encode(hmac_hash).decode('utf-8')

def sign(to_sign: str, secret_key: bytes) -> str:
    """Generate the final sign by encoding the HMAC-SHA256 result and URL encoding it."""
    md5_value = md5(to_sign)
    sign_str = hash_hmac(md5_value, secret_key).upper()
    return urllib.parse.quote(sign_str)

def verify(to_sign: str, secret_key: bytes, expected_sign: str) -> bool:
    """Verify if the generated sign matches the expected sign."""
    md5_value = md5(to_sign)
    calculated_sign = hash_hmac(md5_value, secret_key).upper()
    return calculated_sign == expected_sign

def generate_arg_md5():
    # 准备要签名的字符串和密钥
    to_sign = "{\"projectId\":2024012301,\"type\":2,\"id\":\"9022603\",\"data\":{\"timeType\":1,\"startTime\":1713283200,\"endTime\":1713369600}}"
    # secret_key = b'046A752BE25BCE2D'

    # 使用 MD5Util 类生成 argMd5 参数
    arg_md5 = md5(to_sign)

    return arg_md5


