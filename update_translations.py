import glob
import os
import subprocess
from pathlib import Path


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


def generate_git_hash():
	commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

	with open("lang/commit_hash.txt", "w") as file:
		file.write(commit_hash)


if __name__ == "__main__":
	os.chdir(str(Path(__file__).parent))
	os.chdir("..")
	generate_pot()
	update_translations()
	generate_git_hash()
