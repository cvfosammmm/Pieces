# i18n

## Creating a new translation

Run: (replace `lang` with the language code)
```bash
rm -Rf builddir
meson builddir --prefix=/tmp/usr
ninja pieces-pot -C builddir
cp po/pieces.pot po/lang.po
```
Now translate the strings in `lang.po` and add `lang` to the `LINGUAS` file.

## Updating a translation

Run: (replace `lang` with the language code)
```bash
rm -Rf builddir
meson builddir --prefix=/tmp/usr
ninja pieces-update-po -C builddir
cp po/pieces.pot po/lang.po
```
Now translate the fuzzy strings in `lang.po` (remove the `#,fuzzy` lines).

## Testing a translation

Currently it's not possible to test a translation without an installation in `usr`. Hopefully this will be fixed in a new version of meson (see [mesonbuild/meson#6973](https://github.com/mesonbuild/meson/issues/6973)).
As a workaround, you can install Pieces with the prefix `/tmp/usr` and run the normal `pieces.dev` script. If you want to test Pieces in a certain language, you can set the `LANGUAGE=lang` environment variable.

## Before opening a PR

- Please don't edit the first four lines in the `.po` file (for copyright simplifications).
- Only commit files you actually translated, discard all other files. Don't commit the `pieces.pot` file.
- Ensure that your translation has the correct format, you can check this by simply running the update command again, the only diff should be the date.
- Ensure that the `.mo` file are generated without an error (`ninja pieces-gmo -C builddir`).
- Please fill in the meta info in line 6+ according to this draft: 
  ```
  msgid ""
  msgstr ""
  "Project-Id-Version: pieces\n"
  "Report-Msgid-Bugs-To: https://github.com/cvfosammmm/Pieces/issues\n"
  "POT-Creation-Date: YEAR-MO-DA HO:MI+ZONE\n"
  "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
  "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
  "Language-Team: LANGUAGE \n"
  "Language: lang\n"
  "MIME-Version: 1.0\n"
  "Content-Type: text/plain; charset=UTF-8\n"
  "Content-Transfer-Encoding: 8bit\n"
  ```
