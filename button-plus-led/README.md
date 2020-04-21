# `button-plus-led`
---

`button-plus-led` is a demonstration of GPIO access from a Docker container.

## Building

You can build `button-plus-led` by running `docker build --tag button-plus-led .`

## Running

`button-plus-led` can be run directly on the host, from a docker container, or from a Kubernetes Pod.

### Running on the host

Connect an LED to the `BCM17` pin, and a button to the `BCM27`. On the SparkFun PiWedge, 
these are pins `G17` and `G27`, respectively. You can change pins, but if you do, you will
need to specify them with the `--button` and `--led` flags, respectively.

You will need `python3 >= 3.7`, and `pip3 >= 3.7`.
 
You can run a non-containerized `button-plus-led` by running the following:

```bash
pip3 install -r requirements.txt
python3 main.py
```

### Running in a container

Connect the button and LED according to the instructions in [`Running on the host`](#running-on-the-host)

Build the container according to the instructions in [`Building`](#building) 

Once the container is built and the GPIO is connected, you can run the container with

```bash
docker run --rm -it --device /dev/gpiomem --mount type=bind,source=/sys,destination=/sys button-plus-led
```
