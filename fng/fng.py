import click

from .version import commands as version
from .init import commands as init

from . import __version__
from .appfile import *


@click.group()
@click.pass_context
def cli():
    """Rapidly develop and deploy applications on Kubernetes"""


