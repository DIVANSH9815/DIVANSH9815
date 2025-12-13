import hashlib
from datetime import datetime, timedelta
import time


# ---------------- SECURITY LOGGER ----------------
class SecurityLogger:
    LOG_FILE = "security.log"

    @staticmethod
    def log(message: str):
        with open(SecurityLogger.LOG_FILE, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")


# ---------------- USER MODEL ----------------
class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password_hash = self._hash_password(password)
        self.failed_attempts = []
        self.locked_until = None

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def is_locked(self) -> bool:
        if self.locked_until is None:
            return False
        return datetime.now() < self.locked_until

    def reset_failures(self):
        self.failed_attempts.clear()
        self.locked_until = None


# ---------------- USER STORE ----------------
class UserStore:
    def __init__(self):
        self.users = {}

    def add_user(self, email: str, password: str):
        self.users[email] = User(email, password)

    def get_user(self, email: str):
        return self.users.get(email)


# ---------------- AUTH SERVICE ----------------
class AuthService:
    MAX_ATTEMPTS = 5
    LOCK_TIME = timedelta(seconds=10)  # 🔥 demo ke liye 10 sec

    def __init__(self, user_store: UserStore):
        self.user_store = user_store

    def login(self, email: str, password: str) -> bool:
        user = self.user_store.get_user(email)

        if not user:
            print("❌ User not found")
            return False

        if user.is_locked():
            print("🔒 Account locked. Please wait.")
            SecurityLogger.log(f"LOGIN BLOCKED | {email}")
            return False

        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if hashed_input == user.password_hash:
            user.reset_failures()
            print("✅ Login successful")
            return True

        self._handle_failed_attempt(user)
        print("❌ Wrong password")
        return False

    def _handle_failed_attempt(self, user: User):
        now = datetime.now()
        user.failed_attempts.append(now)

        window = now - timedelta(minutes=10)
        user.failed_attempts = [t for t in user.failed_attempts if t > window]

        if len(user.failed_attempts) >= self.MAX_ATTEMPTS:
            user.locked_until = now + self.LOCK_TIME
            SecurityLogger.log(
                f"ACCOUNT LOCKED | {user.email} | Brute-force detected"
            )


# ---------------- TESTING ----------------
store = UserStore()

# ✅ RIGHT PASSWORD IS ADDED HERE
store.add_user("user@example.com", "Secure@123")

auth = AuthService(store)

print("\n--- WRONG PASSWORD ATTEMPTS ---")
for i in range(5):
    auth.login("user@example.com", "wrongpass")

print("\n--- TRY RIGHT PASSWORD (LOCKED) ---")
auth.login("user@example.com", "Secure@123")

print("\n⏳ Waiting for lock to expire...\n")
time.sleep(10)

print("--- TRY RIGHT PASSWORD AFTER UNLOCK ---")
auth.login("user@example.com", "Secure@123")
