#!/usr/bin/env python3

import threading
import serial
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
    serial.write(command.encode())

def handle_serial(loop, serial):
    while serial.inWaiting() > 0:
        reading = serial.readline().decode()
        log.set_text(log.get_text()[0] + reading)
    loop.set_alarm_in(0.5, handle_serial, serial)

if __name__ == "__main__":
    header = urwid.Text('Robot')

    log = urwid.Text('')
    log_widget = urwid.Filler(log, valign='top')
    log_widget = urwid.LineBox(log_widget, 'Log', 'left')

    prompt = Prompt(' > ', multiline=True, wrap='ellipsis')
    #urwid.connect_signal(prompt, 'command', on_prompt_command)
    prompt = urwid.LineBox(prompt)

    layout = urwid.Pile([log_widget, ('pack', prompt)])
    main_loop = urwid.MainLoop(layout, unhandled_input=unhandled_input)

    serial = serial.Serial('/dev/serial0');
    handle_serial(main_loop, serial)

    main_loop.run()

    serial.close()
