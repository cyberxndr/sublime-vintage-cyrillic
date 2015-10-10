latin_keymap="""`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?"""
cyrillic_keymap="""ё1234567890-=йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"""

patterns = [
    "\"%s\"",
    "+%s\""
]

default = open("Default.sublime-keymap", "r")
config = default.read()
default.close()

for i in range(0, len(latin_keymap)):
    for p in patterns:
        config = config.replace(p % latin_keymap[i], p % cyrillic_keymap[i])

localized = open("cyrillic.sublime-keymap", "w")
localized.write(config)
localized.close()
