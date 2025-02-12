
# Remove pre-done code.

START_PATTERNS = [
    "START CODE HERE",
    "YOUR CODE STARTS HERE"
]
END_PATTERNS = [
    "END CODE HERE",
    "END CODER HERE",
    "YOUR CODE ENDS HERE"
]

ENCODING = "utf-8"

def main(file):
    new = ""

    print(f"Editing file '{file}'...")
    with open(file, "r", encoding=ENCODING) as fo:
        active = False

        for line in fo.readlines():
            if active and any(end_pat in line for end_pat in END_PATTERNS):
                active = False
                new += line
            elif not active:
                active = any(start_pat in line for start_pat in START_PATTERNS)
                new += line

    with open(file, "w", encoding=ENCODING) as fo:
        fo.write(new)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])


