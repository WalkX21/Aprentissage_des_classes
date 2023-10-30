from zelda2 import Link

knight = Link('linkle', 50, 25, 20, 'épée de legende')

knight.print_info()

ganondorf = Link('ganon', 20, 5, 5, 'espadon')
ganondorf.print_info()

knight.fight(ganondorf)