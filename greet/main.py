import click
from importlib import metadata

def showVersion():
    vrsn = metadata.version("gh-test-alpha")
    click.echo(f"Version {vrsn}")

@click.command(no_args_is_help=True, help="Automated greeter")
@click.option("--name","-n", help="Name of person to greet")
@click.option("--version",is_flag=True, help="Show version")
def cli(name, version):
    if (version) :
        showVersion()
    else:
        print(f"Hello to my best friend {name}.")



