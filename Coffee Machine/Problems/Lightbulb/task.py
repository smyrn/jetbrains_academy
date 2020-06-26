class Lightbulb:
    def __init__(self):
        self.state = "off"

    def change_state(self):
        if self.state == 'off':
            print(f'Turning the light on')
            self.state = 'on'
        else:
            print(f'Turning the light off')
            self.state = 'off'
