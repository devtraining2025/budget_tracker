import click
from .models import TransactionIn
from .crud import add_transaction, monthly_summary
from datetime import date as _date


@click.group()
def cli():
    """Budget Tracker CLI"""


@cli.command()
@click.option("--amount", type=float, required=True)
@click.option("--date", type=click.DateTime(formats=["%Y-%m-%d"]), default=None)
@click.option("--category", type=str, required=True)
@click.option("--description", type=str, default="")
def add(amount, date, category, description):
    """Add a transaction"""
    date_obj = date.date() if date else _date.today()
    tx = TransactionIn(
        amount=amount, date=date_obj, category=category, description=description
    )
    added = add_transaction(tx)
    click.echo(f"Added transaction id={added.id}")


@cli.command()
@click.option("--year", type=int, required=True)
@click.option("--month", type=int, required=True)
def summary(year, month):
    s = monthly_summary(year, month)
    if not s:
        click.echo("No transactions")
    else:
        for cat, total in s.items():
            click.echo(f"{cat}: {total:.2f}")


if __name__ == "__main__":
    cli()
