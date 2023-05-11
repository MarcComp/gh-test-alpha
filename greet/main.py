import click
   
@click.command(no_args_is_help=True, help="Automated greeter")
def cli():
    print("Hello World.")
