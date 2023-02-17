from pathlib import Path

root_dir = Path('files1')

for i in range(20,31):
  filename = str(i) + '.txt'
  filepath = root_dir / Path(filename)
  filepath.touch()
