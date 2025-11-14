Social Username Probe is a fast and lightweight public username scanner that checks whether a username exists across multiple social platforms — using only public webpages (no login, no scraping of private data).

⚠️ Legal Notice: This tool is for educational & legal OSINT purposes only. Use only with permission and never to violate platform ToS or privacy.


✨ Features

✔️ Scan a single username across multiple social platforms
✔️ Parallel requests for maximum speed
✔️ Color-coded terminal output (green = found, red = not found, yellow = unknown)
✔️ Export results to JSON and CSV
✔️ Works on Windows / Mac / Linux
✔️ Zero login — public data only



🌐 Supported Platforms
Platform	Public Check
Twitter (X)	✔️
Instagram	✔️
TikTok	✔️
YouTube	✔️
SoundCloud	✔️
Snapchat	✔️
Telegram	✔️
Reddit	✔️
Facebook	✔️
GitHub	✔️



🚀 Installation:

git clone https://github.com/USERNAME/social-username-probe
cd social-username-probe
pip install -r requirements.txt


Requirements:

requests
colorama


🖥️ Usage:

python social_username_probe.py -u user

With extra parameters:

python social_username_probe.py -u mlftt -t 12 --json result.json --csv result.csv


	Description
--username / -u	Username to scan
--threads / -t	Number of parallel requests (default 8)
--json	Export results as JSON
--csv	Export results as CSV


🧪 Example Output:

Found      | TikTok        | https://www.tiktok.com/@mlftt
Not Found  | YouTube       | https://www.youtube.com/@mlftt
Found      | SoundCloud    | https://soundcloud.com/mlftt
Unknown    | Telegram      | https://t.me/mlftt


📌 Notes

The tool does not bypass platform protections.

It does not access private information.

It only checks publicly visible profile URLs.

False positives/negatives may occur depending on platform changes.


🔧 Customization:

To add a new platform, edit the SITES list:

{
  "name": "NewSite",
  "url": "https://example.com/{u}",
  "neg": ["not found", "no such user"]
}


👨‍💻 Developer:

| Info     | Details               |
| -------- | --------------------- |
| Name     | **virus-hacker**      |
| Snapchat | **ml-ftt**            |
| GitHub   | **https://github.com/virus0hacker** |


📜 License:

This project is released under the MIT License.
You are free to use, modify and distribute the tool for legal use only.


⭐ Support the project

إذا أعجبتك الأداة لا تنس:

وضع نجمة (Star) ⭐ للمستودع

نشر المستودع لتصل الفائدة للمهتمين
