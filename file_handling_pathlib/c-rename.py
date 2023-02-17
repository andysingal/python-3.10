from pathlib import Path
from datetime import datetime

root_dir = Path('/Users/ankush.singal/PycharmProjects/pythonProject9/file_handling_pathlib/ciles')
# stats = root_dir.stat()
# second_created = stats.st_ctime
# date_created = datetime.fromtimestamp(second_created)
# date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")
# split_date = date_created_str.split("_")
# print(split_date)

for path in root_dir.glob("**/*"):
  if path.is_file():
    created_date = datetime.fromtimestamp(path.stat().st_ctime)
    date_created_str = created_date.strftime ("%Y-%m-%d_%H:%M:%S")
    new_file = date_created_str + "-" + path.name
    new_filepath = path.with_name(new_file)
    path.rename (new_filepath)