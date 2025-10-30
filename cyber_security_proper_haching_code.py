#!/usr/bin/env python3
"""
Robust hash dictionary cracker (interactive).
Features:
 - Verifies wordlist file exists (allows retry)
 - Detects common hash lengths and supports MD5, SHA1, SHA256, SHA512
 - Better, explicit error/suggestion messages
 - Optional delay (set to 0.0 for best speed)
"""

import hashlib
import time
import os
from colorama import Fore, Style, init

COMMON_WORDLIST_HINTS = [
    "/usr/share/wordlists/rockyou.txt",
    "/usr/dict/words",
    "/usr/share/dict/words",
]

HASH_ALG_BY_LEN = {
    32: "md5",
    40: "sha1",
    64: "sha256",
    128: "sha512",
}

class HashCracker:
    def __init__(self, target_hash: str, wordlist_file: str, algorithm: str = "sha256"):
        self.target_hash = target_hash.strip().lower()
        self.wordlist_file = wordlist_file
        self.algorithm = algorithm.lower()

    def _hash(self, text: str) -> str:
        b = text.encode("latin-1", errors="ignore")
        if self.algorithm == "md5":
            return hashlib.md5(b).hexdigest()
        if self.algorithm == "sha1":
            return hashlib.sha1(b).hexdigest()
        if self.algorithm == "sha512":
            return hashlib.sha512(b).hexdigest()
        # default sha256
        return hashlib.sha256(b).hexdigest()

    def crack(self, delay: float = 0.0):
        attempts = 0
        try:
            with open(self.wordlist_file, "r", encoding="latin-1", errors="ignore") as f:
                for line in f:
                    password = line.rstrip("\n").rstrip("\r")
                    if password == "":
                        continue
                    attempts += 1
                    guessed = self._hash(password)
                    print(f'\r{Fore.YELLOW}Trying ({attempts}): {password} -> {guessed}{Style.RESET_ALL}', end="", flush=True)
                    if guessed == self.target_hash:
                        return password, attempts
                    if delay > 0:
                        time.sleep(delay)
        except FileNotFoundError:
            # This should not happen because we validate before creating the object,
            # but keep a safe guard.
            print(f"\n{Fore.RED}Wordlist file '{self.wordlist_file}' not found (unexpected).{Style.RESET_ALL}")
            return None, attempts
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Interrupted by user after {attempts} attempts.{Style.RESET_ALL}")
            return None, attempts
        return None, attempts

def choose_algorithm_by_hash(hash_str: str) -> str:
    ln = len(hash_str.strip())
    alg = HASH_ALG_BY_LEN.get(ln)
    if alg:
        print(f"{Fore.CYAN}Hash length {ln} suggests {alg.upper()}.{Style.RESET_ALL}")
        return alg
    print(f"{Fore.YELLOW}Unknown/unsupported hash length ({ln}). Common lengths: MD5=32, SHA1=40, SHA256=64, SHA512=128.{Style.RESET_ALL}")
    # fallback to user choice
    while True:
        choice = input("Choose algorithm (md5/sha1/sha256/sha512) [sha256]: ").strip().lower()
        if choice == "":
            return "sha256"
        if choice in ("md5", "sha1", "sha256", "sha512"):
            return choice
        print(f"{Fore.RED}Invalid choice. Try again.{Style.RESET_ALL}")

def prompt_for_existing_file(initial_path: str = "") -> str:
    path = initial_path.strip()
    while True:
        if path and os.path.isfile(path):
            return path
        if path:
            print(f"{Fore.RED}File not found: '{path}'.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No file path provided.{Style.RESET_ALL}")
        print("Suggestions:")
        for hint in COMMON_WORDLIST_HINTS:
            print(f"  - {hint}")
        path = input("Enter the path to the wordlist file (absolute path recommended): ").strip()

def main():
    init(autoreset=True)

    target_hash = input("Enter the hash to crack: ").strip()
    if not target_hash:
        print(f"{Fore.RED}No hash provided. Exiting.{Style.RESET_ALL}")
        return

    alg = choose_algorithm_by_hash(target_hash)

    user_path = input("Enter the path to the wordlist file (or leave blank to choose): ").strip()
    wordlist_path = prompt_for_existing_file(user_path)

    # optional demo delay; set to 0.0 for speed
    demo_delay = 0.0

    print(f"{Fore.CYAN}Using algorithm: {alg.upper()}, wordlist: {wordlist_path}{Style.RESET_ALL}")

    cracker = HashCracker(target_hash, wordlist_path, algorithm=alg)
    password, attempts = cracker.crack(delay=demo_delay)

    if password:
        print(f'\n{Fore.GREEN}Password found: "{password}" after {attempts} attempts.{Style.RESET_ALL}')
    else:
        print(f'\n{Fore.RED}Password not found in the wordlist after {attempts} attempts.{Style.RESET_ALL}')

if __name__ == "__main__":
    main()
