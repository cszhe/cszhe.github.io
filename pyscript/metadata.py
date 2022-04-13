"""
Convert image path from pellican directory to jeklly 
"""
import os
import pathlib


def main():
    # find root path
    root_dir = pathlib.PosixPath(__file__).parent.parent
    post_dir = pathlib.PosixPath(root_dir, '_posts')
    img_dir = pathlib.PosixPath(root_dir, 'assets/images')

    for f in post_dir.iterdir():
        if f.suffix.lower() != '.md':
            print(f"{f} not markdown")
            continue
        # process markdown
        text = f.read_text()
        # process metadata
        
        f.write_text(text)

main()


