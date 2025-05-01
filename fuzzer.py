import subprocess
import random
import string

def gen_input():
    return ''.join(random.choices(string.ascii_letters, k=random.randint(20, 120)))

for i in range(50):
    fuzz = gen_input()
    try:
        res = subprocess.run(["./vuln", fuzz], capture_output=True, timeout=2)
        if res.returncode != 0:
            print(f"[!] Crash Detected on input: {fuzz}")
    except Exception as e:
        print(f"Exception: {e}")

