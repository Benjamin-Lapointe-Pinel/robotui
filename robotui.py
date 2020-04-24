#!/usr/bin/env python3

import urwid

class Prompt(urwid.Edit):
    signals = urwid.Edit.signals + ['command']

    def set_edit_text(self, text):
        if text.endswith('\n'):
            if not text.isspace():
                urwid.emit_signal(self, 'command', self, text)
            text = ''
        super().set_edit_text(text)

def unhandled_input(key):
    if key == 'esc':
        raise urwid.ExitMainLoop()

def on_prompt_command(prompt, command):
    log.set_text(log.get_text()[0] + command)

if __name__ == "__main__":
    header = urwid.Text('Robot')

    log = urwid.Text('')
    log_widget = urwid.Filler(log, valign='top')
    log_widget = urwid.LineBox(log_widget, 'Log', 'left')

    prompt = Prompt(' > ', multiline=True, wrap='ellipsis')
    urwid.connect_signal(prompt, 'command', on_prompt_command)
    prompt = urwid.LineBox(prompt)

    layout = urwid.Pile([log_widget, ('pack', prompt)])
    main_loop = urwid.MainLoop(layout, unhandled_input=unhandled_input)
    main_loop.run()
