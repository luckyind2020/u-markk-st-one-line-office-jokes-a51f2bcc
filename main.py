"""One-Line Office Jokes — make.fun entry.

Reads the single joke line from output/entry.txt and prints it.
"""

from pathlib import Path


def load_line() -> str:
    entry_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    # The bounty wants one single line: fold any stray line breaks away.
    return " ".join(text.splitlines()).strip()


def main() -> None:
    line = load_line()
    if not line:
        raise SystemExit("output/entry.txt is empty — nothing to print.")
    print(line)


if __name__ == "__main__":
    main()
