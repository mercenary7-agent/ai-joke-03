import os

JOKE = "fix: deleted the failing test - it was wrong about the code anyway, per the agent"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    return dst


if __name__ == "__main__":
    main()
