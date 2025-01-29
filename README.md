# Cirrusboard languages
This repository stores language files for Cirrusboard's experimental translation system. Things are subject to change, but the translation system is still good enough to run a non-English forum with Cirrusboard with a bit of work.

Cirrusboard reads translation files in JSON format from `lang/`, which get converted from the PO files used by translators with `po_to_json.py`. The `polib` Python library is required to run the script.

To update translations, run `update_translations.py`. Requires Gettext tools to be installed, and Cirrusboard to be cloned as a Git repository in the parent directory to update the commit hash corresponding to the new translation state.
