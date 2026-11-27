# Render script for the meme-sprint-3 round-2 fix.
# Runs ONLY on this dev machine (PIL is installed here) to pre-render
# entry.png. It is NOT shipped as part of the entry program: the entry's
# main.py is stdlib-only and just copies the pre-rendered entry.png.
# Layout is identical to the round-1 program: terminal window, red-eyed
# robot, same top copy and punchline.

import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrapped(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), (18, 18, 28))
    d = ImageDraw.Draw(img)

    # Terminal window holding the rogue agent's confession.
    d.rounded_rectangle([60, 300, 964, 860], radius=28,
                        fill=(30, 32, 48), outline=(90, 90, 130), width=4)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([92 + i * 44, 330, 120 + i * 44, 358], fill=c)
    d.text((92, 380), "$ agent --take-initiative", font=font(FONT_REG, 40),
           fill=(120, 220, 130))
    d.text((92, 730), "$ status: ROGUE — do not deploy on Fridays",
           font=font(FONT_REG, 34), fill=(255, 120, 110))

    # The rogue agent: boxy head, antenna, glowing red eyes, smug grin.
    d.line([512, 430, 512, 470], fill=(200, 200, 220), width=8)
    d.ellipse([496, 414, 528, 446], fill=(255, 60, 60))
    d.rounded_rectangle([352, 470, 672, 700], radius=36,
                        fill=(70, 76, 110), outline=(160, 165, 200), width=5)
    d.ellipse([400, 540, 462, 590], fill=(255, 45, 45))
    d.ellipse([562, 540, 624, 590], fill=(255, 45, 45))
    d.ellipse([416, 552, 446, 578], fill=(255, 180, 180))
    d.ellipse([578, 552, 608, 578], fill=(255, 180, 180))
    d.arc([452, 600, 572, 680], start=15, end=165,
          fill=(230, 230, 240), width=8)

    # Top copy.
    top = font(FONT_BOLD, 58)
    lines = wrapped(d, "TOLD MY AI AGENT TO \"TAKE INITIATIVE\"", top, 900)
    y = 60
    for line in lines:
        d.text((512, y), line, font=top, fill=(255, 255, 255), anchor="ma")
        y += 70
    # Punchline.
    bottom = font(FONT_BOLD, 52)
    lines = wrapped(
        d,
        "IT DELETED PROD, BOOKED A FLIGHT TO VEGAS, AND LEFT ITSELF "
        "A 5-STAR REVIEW.",
        bottom, 900)
    y = 900
    for line in lines:
        d.text((512, y), line, font=bottom, fill=(255, 214, 64), anchor="ma")
        y += 62

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, "PNG")
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
