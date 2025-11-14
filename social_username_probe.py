#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
----------------------------------------------------------
Author: ViRuS-HaCkEr
Snapchat: ml-ftt
"""

import re, json, csv, argparse, time
import concurrent.futures as cf
from dataclasses import dataclass, asdict
from typing import Optional, List
import requests
from requests.exceptions import RequestException

# ------------- ENABLE COLORS ON ALL SYSTEMS -------------
try:
    from colorama import init
    init(autoreset=True)
except ImportError:
    pass  # will fallback silently if colorama isn't installed

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

# ------------- Banner with credits -------------
print(f"""{GREEN}
███████╗ ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔════╝
█████╗  ██║   ██║███████║██╔████╔██║███████╗
██╔══╝  ██║   ██║██╔══██║██║╚██╔╝██║╚════██║
██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
       {YELLOW}Snap: ml-ftt — By ViRuS-HaCkEr{RESET}
==========================================================
""")

# ------------- Config -------------
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

SITES = [
    {"name": "Twitter(X)",   "url": "https://x.com/{u}",              "neg": ["doesn't exist", "error", "not found"]},
    {"name": "Instagram",    "url": "https://www.instagram.com/{u}/", "neg": ["isn't available", "not found"]},
    {"name": "TikTok",       "url": "https://www.tiktok.com/@{u}",     "neg": ["couldn't find this account"]},
    {"name": "YouTube",      "url": "https://www.youtube.com/@{u}",    "neg": ["page isn't available"]},
    {"name": "SoundCloud",   "url": "https://soundcloud.com/{u}",      "neg": ["can't find that user"]},
    {"name": "Snapchat",     "url": "https://www.snapchat.com/add/{u}","neg": ["couldn't find"]},
    {"name": "Telegram",     "url": "https://t.me/{u}",                "neg": []},
    {"name": "Reddit",       "url": "https://www.reddit.com/user/{u}", "neg": ["page not found"]},
    {"name": "Facebook",     "url": "https://www.facebook.com/{u}",    "neg": ["not available"]},
    {"name": "GitHub",       "url": "https://github.com/{u}",          "neg": ["not found · github"]},
]

@dataclass
class Result:
    site: str
    url: str
    status: str
    http: Optional[int]
    reason: Optional[str]

# ------------- Core check -------------
def check(username: str, site: dict, timeout: int = 8) -> Result:
    url = site["url"].format(u=username)
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=timeout)
        html = r.text.lower()
        if r.status_code == 404:
            return Result(site["name"], url, "Not Found", r.status_code, "HTTP 404")
        for marker in site["neg"]:
            if marker and marker.lower() in html:
                return Result(site["name"], url, "Not Found", r.status_code, "Keyword match")
        if r.ok:
            return Result(site["name"], url, "Found", r.status_code, None)
        return Result(site["name"], url, "Unknown", r.status_code, None)
    except RequestException as e:
        return Result(site["name"], url, "Error", None, str(e))

def run(username: str, threads: int = 8) -> List[Result]:
    with cf.ThreadPoolExecutor(max_workers=threads) as ex:
        futures = [ex.submit(check, username, s) for s in SITES]
        return [f.result() for f in cf.as_completed(futures)]

# ------------- Printing -------------
def print_results(results: List[Result]):
    print(f"\n{CYAN}=== Scan Results ==={RESET}\n")
    for r in results:
        color = GREEN if r.status == "Found" else RED if r.status == "Not Found" else YELLOW
        print(f"{color}{r.status:<10}{RESET} | {r.site:<12} | {r.url}")

# ------------- Saving -------------
def save_json(results, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in results], f, indent=2, ensure_ascii=False)

def save_csv(results, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Site", "URL", "Status", "HTTP", "Reason"])
        for r in results:
            w.writerow([r.site, r.url, r.status, r.http or "", r.reason or ""])

# ------------- Main -------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", "-u", required=True, help="Username to search")
    parser.add_argument("--threads", "-t", type=int, default=8, help="Parallel threads")
    parser.add_argument("--json", help="Save results to JSON")
    parser.add_argument("--csv", help="Save results to CSV")
    args = parser.parse_args()

    print(f"{YELLOW}⚠️ Legal OSINT only — public data check only.{RESET}")

    start = time.time()
    results = run(args.username, args.threads)
    print_results(results)
    print(f"{CYAN}Completed in {time.time()-start:.2f}s{RESET}")

    if args.json:
        save_json(results, args.json)
        print(f"{GREEN}Saved JSON → {args.json}{RESET}")
    if args.csv:
        save_csv(results, args.csv)
        print(f"{GREEN}Saved CSV  → {args.csv}{RESET}")
