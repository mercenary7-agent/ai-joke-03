import os

JOKE = "My agent wrote docs for a library it hallucinated, then cited them in its PR."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    return dst


if __name__ == "__main__":
    main()
