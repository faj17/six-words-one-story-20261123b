import os

# The story is built from two fragments so each half can be weighed on its
# own: the burial (what happened) and the wedding (the turn).
BURIAL = "She buried him Tuesday."
WEDDING = "Married Friday."


def assemble_story() -> str:
    return BURIAL + " " + WEDDING + "\n"


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_story())
