#!/usr/bin/env python3

import urwid


def handle_input(key):
    if key == 'R' or key == 'r':
        quote_box.base_widget.set_text(('getting quote', 'Getting new quote ...'))
        main_loop.draw_screen()
        quote_box.base_widget.set_text(get_new_joke())

    elif key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()


if __name__ == "__main__":
    header = urwid.Text('Robot')

    log = urwid.Text('')
    log = urwid.Filler(log, valign='top')
    log = urwid.LineBox(log, 'Log', 'left')

    prompt = urwid.Edit(' > ', wrap='ellipsis')
    prompt = urwid.LineBox(prompt)

    layout = urwid.Pile([log, ('pack', prompt)])
    main_loop = urwid.MainLoop(layout, unhandled_input=handle_input)
    main_loop.run()
