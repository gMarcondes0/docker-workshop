from pathlib import Path 

dir = Path.cwd()
file = Path(__file__).name

print(f'files no dir {dir}')

for fp in dir.iterdir():
    if fp.name == file:
        continue
    print(fp)

    if fp.is_file():
        content = fp.read_text()
        print(f'Content: {content}')