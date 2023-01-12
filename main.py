def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_string("A")
    elif False:
        pass
basic.forever(on_forever)
