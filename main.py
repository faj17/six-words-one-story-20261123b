import os

# The story is built from two fragments so each half can be weighed on its
# own: the burial (what happened) and the wedding (the turn).
BURIAL = "She buried him Tuesday."
WEDDING = "Married Friday."


def assemble_story() -> str:
    text = BURIAL + " " + WEDDING + "\n"
    # The bounty is a six-word story: enforce the word count before
    # anything is written.
    words = text.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    return text


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_story())
