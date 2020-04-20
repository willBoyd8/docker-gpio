import argparse
from gpiozero import LED, Button


def main():
    """
    Blinks an LED on and off forever
    """
    parser = argparse.ArgumentParser(description='Turn an LED on when a button is pressed')
    parser.add_argument('--pin', '-p', type=str, default="GPIO17", help='The pin the LED is connected to')
    parser.add_argument('--button', '-b', type=str, default="GPIO27", help='The pin the button is connected to')

    args = parser.parse_args()

    led = LED(args.pin)
    button = Button(args.button)

    print('Ready for interaction!')

    while True:
        button.wait_for_press()
        print('Button Pressed! Turning led ON...')
        led.on()

        button.wait_for_release()
        print('Button released! Turning led OFF...')
        led.off()


if __name__ == '__main__':
    main()
