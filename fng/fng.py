#!/usr/bin/env python

import click


@click.group()
@click.pass_context
def fng(ctx):
    """Rapidly develop and deploy applications on Kubernetes"""


