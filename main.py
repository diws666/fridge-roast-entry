import os

# Verified count: 125 characters (125 bytes as UTF-8, no trailing newline).
LINE = "My smart fridge just rated my midnight snack one star and emailed my doctor. I live here, and it still thinks it is the boss."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
output_path = os.path.join(output_dir, "entry.txt") if output_dir else "/output/entry.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)

print(len(LINE))
