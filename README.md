# Mini URL Shortener (CLI)

A persistent command-line URL Shortener built with Python 3 using only the Python standard library.

Submitted for **GDG NSUT Recruitment Round 2 (Dev Department) - Task 1 (Track A: 1st Year)**.

---

## Features
- **Standard Library Only:** Zero external dependencies (uses `hashlib`, `json`, `sys`, and `os`).
- **Deterministic Hashing:** Generates consistent 6-character short codes using SHA-256.
- **Cross-Run Persistence:** Stores URL mappings, codes, and analytics in `urls.json`.
- **Custom Aliases (Bonus):** Supports custom user-defined short codes.
- **Click Tracking (Bonus):** Tracks and displays resolve/click counts for every code.
- **Error Handling:** Validates URL prefixes (`http://`, `https://`) and handles invalid/duplicate codes gracefully.

---

## How to Run

Ensure you have **Python 3** installed on your system.

### 1. Shorten a URL
Converts a long URL into an auto-generated 6-character code:
```bash
python3 main.py shorten https://www.google.com
Shortened Code: 1e838e

python3 main.py shorten https://nsut.ac.in mynsut
Shortened Code: mynsut

python3 main.py resolve mynsut
Original URL: https://nsut.ac.in
Clicks: 1


python3 main.py list
--------------------------------------------------
Code       | Clicks   | URL
--------------------------------------------------
1e838e     | 0        | [https://www.google.com](https://www.google.com)
mynsut     | 1        | [https://nsut.ac.in](https://nsut.ac.in)
--------------------------------------------------
