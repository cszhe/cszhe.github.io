import sys

filename = sys.argv[1]
print(filename)
f = open(filename, "r").read()
lines = f.splitlines()
first, rest = lines[:10], lines[10:]
fixed_first = ["---", "layout: post"]

for line in first:
    for key in ["Title:", "Date:", "Slug:"]:
        if line.startswith(key):
            line = line.replace(key, key.lower())
            if key == "Date:":
                if not filename.startswith("20"):
                    date = line[6 : 6 + 10] + "-"
                else:
                    date = ""
    if line.startswith("Author:"):
        continue
    if line.startswith("Tags:"):
        line = line.replace("Tags: ", "categories: [") + "]"
    fixed_first.append(line)
    if line.startswith("slug:"):
        fixed_first.append("---")

with open(f"jekyll/{date}{filename}", "w") as f:
    f.writelines(l + "\n" for l in fixed_first + rest)