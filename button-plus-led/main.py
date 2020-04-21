import argparse
from gpiozero import LED, Button
from time import sleep


def main():
    """
    Blinks an LED on and off forever
    """
    parser = argparse.ArgumentParser(description='Turn an LED on when a button is pressed')
    parser.add_argument('--led', '-l', type=str, default="GPIO17", help='The pin the LED is connected to')
    parser.add_argument('--button', '-b', type=str, default="GPIO27", help='The pin the button is connected to')
    parser.add_argument(
        '--blink-when-ready',
        default=False,
        dest='blink',
        action='store_true',
        help='If set, blink the LED when GPIO is ready'
    )

    args = parser.parse_args()

    led = LED(args.led)
    button = Button(args.button)

    print('Ready for interaction!')

    if args.blink:
        for _ in range(1, 5):
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)

    while True:
        button.wait_for_press()
        print('Button Pressed! Turning led ON...')
        led.on()

        button.wait_for_release()
        print('Button released! Turning led OFF...')
        led.off()


if __name__ == '__main__':
    main()
