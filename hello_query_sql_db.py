#!/usr/bin/env python3

import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL DB"""
    pass

# build a click command
@cli.command()
@click.option("--query", default="SELECT * FROM default.diamonds LIMIT 2", help="SQL query to execute")
def cli_query(query):
    """Execute a SQL query"""
    result = querydb(query)
    click.echo(result)

# run the CLI
if __name__ == "__main__":
    cli()
