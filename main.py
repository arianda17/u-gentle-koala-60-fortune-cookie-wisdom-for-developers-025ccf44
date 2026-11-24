#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - entrypoint."""

ENTRY_LINE = "Your code review approval is a bet on someone else's Friday."

def main():
    assert isinstance(ENTRY_LINE, str)
    assert "\n" not in ENTRY_LINE
    assert 1 <= len(ENTRY_LINE) <= 120
    assert ENTRY_LINE.strip() != ""
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    print(ENTRY_LINE)

if __name__ == "__main__":
    main()
