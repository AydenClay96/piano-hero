import pygame
import pygame.midi


class MidiController:
    def __init__(self) -> None:
        pygame.midi.init()
        (in_device_id, out_device_id) = self.find_controller()
        self.midi_in = pygame.midi.Input(in_device_id)
        print(f"Using input id: {in_device_id}.")

    def find_controller(self) -> None:
        in_id = None
        out_id = None

        for i in range(pygame.midi.get_count()):
            r = pygame.midi.get_device_info(i)
            (interf, name, input, output, opened) = r

            in_out = ""
            if input:
                in_out = "(input)"
            if output:
                in_out = "(output)"

            if name == "test" and input:
                in_id = i
            if name == "test" and output:
                out_id = i

            print("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
                  (i, interf, name, opened, in_out))

        return (in_id, out_id)
