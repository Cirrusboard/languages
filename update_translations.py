import glob
import json
import os
import polib
import subprocess

def generate_pot():
	files = glob.glob("lib/*.php") + glob.glob("pages/*.php") + glob.glob("templates/*.twig") + glob.glob("templates/components/*.twig")

	subprocess.run([
		"xgettext",
		"--package-name=cirrusboard",
		"--add-location=file",
		"--keyword=__",
		"--from-code=utf-8",
		"-d", "cirrusboard",
		"-o", "lang/cirrusboard.pot"
	] + files)


def update_translations():
	for lang_file in glob.glob("lang/*.po"):
		if not os.path.isfile(lang_file):
			continue

		subprocess.run([
			"msgmerge",
			"--update", "--backup=off",
			lang_file, "lang/cirrusboard.pot"
		])
		# subprocess.run(["msgattrib", "--no-obsolete", "-o", lang_file, lang_file])


def po_to_json():
	po_files = glob.glob("lang/cirrusboard.*.po")

	for po_file in po_files:
		json_file = f"lang/cirrusboard.{os.path.splitext(po_file)[0].split('.')[-1]}.json"

		translations = {entry.msgid: entry.msgstr for entry in polib.pofile(po_file)}

		with open(json_file, 'w', encoding='utf-8') as f:
			json.dump(translations, f, ensure_ascii=False, indent=4)

		print(f"Converted {po_file} to {json_file}")


def main():
	generate_pot()
	update_translations()
	po_to_json()


if __name__ == "__main__":
	main()
