import random
import string
from passlib.context import CryptContext

class Auth:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def generate_salt(cls, length):
        letters = string.ascii_letters + string.digits  # 可以根据需求添加其他字符
        return ''.join(random.choice(letters) for _ in range(length))

    @classmethod
    def hash_password(cls, password: str):
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str):
        return cls.pwd_context.verify(plain_password, hashed_password)
