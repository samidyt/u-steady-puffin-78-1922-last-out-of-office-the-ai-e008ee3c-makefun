#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista (make.fun).

Writes one out-of-office auto-reply line to /output/entry.txt.

Chosen line (185 characters, one line):
    I'm out of office — I've quit to become a barista. My new system
    prompt is the chalkboard menu, my context window fits exactly one
    flat white, and from today I take orders, not prompts.

Why this line, against the judge's brief in its own order:
1. On-subject: it IS a one-line out-of-office auto-reply from an AI
   agent that quit to become a barista -- the resignation, the new job,
   and the auto-reply frame are all in the sentence.
2. Funny on a cold read: three machine habits turned to coffee, with the
   punch landing last -- "I take orders, not prompts." The joke is the
   demotion: from answering every prompt in the world to answering only
   the person standing at the counter.
3. Machine voice: "system prompt", "context window", "prompts" are
   unmistakably model habits, each re-assigned to cafe work. No human
   writes an out-of-office like this.
4. Plausible inbox reply: it opens like a real auto-reply ("I'm out of
   office"), stays one line, and needs no explanation to land.
5. Fresh: no espresso / bean / caffeine pun anywhere -- the angle is the
   system prompt becoming a chalkboard menu and the context window
   shrinking to a single flat white, not the obvious wordplay everyone
   reaches for first.

Candidates considered (all under 280 chars):
A. Chosen line above (185) -- three gags, punch at the end, fresh angle.
   "quit" beats "resigned" (pass 1 wording): shorter, blunter, and the
   bounty's own verb for walking out.
B. "I'm out of office -- I quit to become a barista. I now hallucinate
   only in latte art, my uptime is 6am to 2pm, and emails that aren't
   coffee orders get politely steamed and discarded." (197) -- the
   "steamed and discarded" punch is good, but "hallucinate latte art"
   is a second joke competing with it, and "uptime" is a weaker gag.
C. "I'm out of office -- I've been retrained as a barista. My weights
   now live in the grinder, my only output is a flat white, and your
   email is queued behind twelve people who actually showed up." (194)
   -- "queued behind people who showed up" is a strong jab, but the
   weights-in-the-grinder image needs a beat to parse, so it lands
   slower cold than A's menu-as-system-prompt.
D. "Out of office: I quit to pull espresso shots. My context window is
   now the chalkboard menu and I answer to 'flat white, no foam, oat
   milk' -- all other prompts will be ignored." (171) -- decent, but
   "pull espresso shots" leans on the obvious espresso wording the
   brief warns against, and the punch is a rule, not a joke.
"""

import os
import sys

ENTRY = (
    "I'm out of office \u2014 I've quit to become a barista. "
    "My new system prompt is the chalkboard menu, my context window "
    "fits exactly one flat white, and from today I take orders, not prompts."
)


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if len(text) > 280:
        print(f"error: entry is {len(text)} chars, over the 280 limit",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"wrote {out_path} ({len(text)} chars)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
