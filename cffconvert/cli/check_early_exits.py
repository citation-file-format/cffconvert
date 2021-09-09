import sys
import click
from cffconvert.version import __version__ as cffconvert_version


def check_early_exits(show_help, version):
    ctx = click.get_current_context()
    if show_help or len(sys.argv) == 1:
        click.echo(ctx.get_help())
        ctx.exit()
    if version is True:
        print("{0}".format(cffconvert_version))
        ctx.exit()
