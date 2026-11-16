import hashlib
import os


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    with open(source, "rb") as handle:
        blob = handle.read()
    digest = sha256_hex(blob)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(blob)
    with open(target, "rb") as handle:
        written = handle.read()
    if sha256_hex(written) != digest:
        raise SystemExit("Self-check failed: /output/entry.png does not match entry.png")
    print("Wrote /output/entry.png (sha256 %s, %d bytes)" % (digest, len(blob)))


if __name__ == "__main__":
    main()
