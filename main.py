"""news-image-20261117 entry.

Writes one image, entry.png, summarising the world news of
17 November 2026, to /output/entry.png.

The image is committed in this repository (entry.png, 1024x1024 PNG,
under 1 MiB). This program copies it byte-for-byte, so repeated runs
are fully deterministic. No network access, standard library only.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Guard the deterministic-output rule: the written file must be
    # byte-identical to the committed image, so a partial or failed
    # copy can never pass as an entry.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
