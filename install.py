#!/usr/bin/env python3
"""Install the bundled Leaf Jellyfish pet without replacing existing files."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile


def main():
    root = Path(__file__).resolve().parent
    source = root
    expected = {}
    for line in (root / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        expected[relative] = digest
    for filename in ("pet.json", "spritesheet.webp"):
        path = source / filename
        relative = path.relative_to(root).as_posix()
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected.get(relative):
            raise ValueError("Pet file verification failed: " + filename)
    metadata = json.loads((source / "pet.json").read_text(encoding="utf-8"))
    if metadata["id"] != "leaf-jellyfish" or metadata["spritesheetPath"] != "spritesheet.webp":
        raise ValueError("Unexpected pet metadata")

    configured = os.environ.get("CODEX_HOME")
    home = Path(configured).expanduser() if configured else Path.home() / ".codex"
    pets = home / "pets"
    destination = pets / "leaf-jellyfish"
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("Already exists; nothing replaced: " + str(destination))
    pets.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".leaf-jellyfish-", dir=pets) as temporary:
        staged = Path(temporary) / "leaf-jellyfish"
        staged.mkdir()
        for filename in ("pet.json", "spritesheet.webp"):
            shutil.copy2(source / filename, staged / filename)
        staged.rename(destination)
    print("Installed Leaf Jellyfish: " + str(destination))
    print("Settings > Pets > Refresh > 새싹 해파리")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
