# Some utility commands for this project

# refresh the pot file and maybe some po files
mktxt:
    xgettext --files-from=po/POTFILES --output=po/merise_gtk.pot
