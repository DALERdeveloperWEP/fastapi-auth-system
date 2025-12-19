import secrets
from passlib.hash import bcrypt

def hash_password(plain_password: str) -> str:
    """Hashes a password using bcrypt."""
    # Salt is generated automatically
    return bcrypt.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a password against a hash."""
    return bcrypt.verify(plain_password, hashed_password)


def generate_token():
    return secrets.token_urlsafe(48)









# # Usage
# plain_pw = "my_secret_password"
# hashed = hash_password(plain_pw)
# is_correct = verify_password(plain_pw, hashed)
 