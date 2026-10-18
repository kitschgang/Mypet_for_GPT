# Leaf Jellyfish 🌱🫧

[한국어](README.md) · [English](README.en.md) · [日本語](README.ja.md)

A pastel-pink jelly body with a little fresh green leaf on top.
This tiny desktop friend bobs around, blinks, and waves hello with a tentacle.

<p align="center">
  <img src="character.png" alt="A pastel-pink jellyfish with a green leaf" width="420">
</p>

<p align="center">
  <img src="preview-idle.gif" alt="Leaf Jellyfish blinking" width="192">
  <img src="preview-waving.gif" alt="Leaf Jellyfish waving a tentacle" width="192">
  <img src="preview-jumping.gif" alt="Leaf Jellyfish bouncing" width="192">
</p>

## Bring your new pet home

1. [Download Leaf Jellyfish](https://github.com/kitschgang/Mypet_for_GPT/raw/refs/heads/main/leaf-jellyfish.zip) and unzip the file.
2. Copy the entire **`leaf-jellyfish` folder** to the location below.

   | Operating system | Destination |
   | --- | --- |
   | macOS | `~/.codex/pets/` |
   | Windows | `%USERPROFILE%\.codex\pets\` |

   Create the `pets` folder if it does not exist. If you have set a custom `CODEX_HOME`, use the `pets` folder inside that directory instead.

3. In the app, open **Settings → Pets → Refresh**, then choose **새싹 해파리** (Leaf Jellyfish). The pet's display name is currently in Korean.
4. Enter `/pet` in the chat box to show or hide your pet.

If your pet does not appear in the list right away, reopen the app and check again.

### Install with Python

If you have Python 3, you can also download the full repository using **Code → Download ZIP**, unzip it, and run this command from the extracted folder. No extra packages are needed.

```sh
python3 install.py
```

On Windows, you can use `py install.py`. If a pet folder with the same name already exists, the installer stops without overwriting it.

## What can it do?

| State | Animation |
| --- | --- |
| Idle | Quiet breathing and blinking |
| Moving right / left | Swimming with swaying tentacles |
| Greeting | Raising a tentacle to wave hello |
| Jumping | Bouncing up and settling back down |
| Error | Looking a little sad, then recovering |
| Waiting for input | Tilting its head expectantly |
| Working | Moving its tentacles in concentration |
| Reviewing | Looking things over and blinking |

The pet has 9 states and 57 frames in total. Its transparent WebP sprite sheet is 1536 × 1872 pixels, with 192 × 208-pixel cells.

## Files

- `leaf-jellyfish.zip`: a pet folder ready for manual installation
- `pet.json`, `spritesheet.webp`: pet settings and the original sheet containing all 9 animation states
- `preview-*.gif`: animated previews
- `character.png`: original character artwork
- `install.py`: an optional tool that copies the pet into your local pets folder
- `SHA256SUMS`: checksums for verifying the pet files

The character and animation artwork were created with OpenAI image generation tools. Frame layout, transparency, and motion were checked afterward. This is not an official OpenAI character.

Pet features and menu labels may vary by app version. See the [official pet guide](https://learn.chatgpt.com/docs/pets) for more information.
