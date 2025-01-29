import glob
import json
import os
from pathlib import Path
import polib

def po_to_json():
	po_files = glob.glob("cirrusboard.*.po")

	for po_file in po_files:
		json_file = f"cirrusboard.{os.path.splitext(po_file)[0].split('.')[-1]}.json"

		translations = {entry.msgid: entry.msgstr for entry in polib.pofile(po_file)}

		with open(json_file, 'w', encoding='utf-8') as f:
			json.dump(translations, f, ensure_ascii=False, indent=4)

		print(f"Converted {po_file} to {json_file}")


if __name__ == "__main__":
	os.chdir(str(Path(__file__).parent))
	po_to_json()
