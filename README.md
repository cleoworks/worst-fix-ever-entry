# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://img.shields.io/badge/make.fun-Worst%20Fix%20Ever-blue)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

Entry for the make.fun bounty **Worst Fix Ever: Funniest Commit Message** — one line of
commit message for a bug fix that made everything worse.

## The entry

```text
fix(auth): users saw each other's data; now nobody sees their own
```

65 characters. The fix for users seeing each other's data was to make sure
nobody sees their own either.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the line above to
`/output/entry.txt` when run. It is deterministic: every run writes the exact
same 65 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
