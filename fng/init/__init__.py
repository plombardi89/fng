import click

from fng import fng


@fng.fng.group()
def init():
    """Init shit"""
    pass


@init.command()
def app():
    """Init app"""
    pass