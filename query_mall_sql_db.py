#!/usr/bin/env python3
import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL DB"""


# build a click command
@cli.command()
@click.option("--income", default=50, help="Type in the customer's annual income")
def cli_query(income):
    """Execute a SQL query"""
    result = querydb(income)
    click.echo(result)


# run the CLI
if __name__ == "__main__":
    cli()
