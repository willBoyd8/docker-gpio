from argparse import ArgumentParser
from flask import Flask


def main() -> Flask:
    """returns a new flask app"""
    parser = ArgumentParser(description='Launch a server that controls Raspberry Pi GPIO')
    