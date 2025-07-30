import click
from cleaner import YaDiskCleaner
import yadisk
import sys

@click.command()
@click.option('-t', '--token', type=str, required=True)
@click.option('-i', '--id', type=str, required=True)
@click.option('-s', '--secret', type=str, required=True)
@click.option('-f', '--folder_name', type=str, required=True)
@click.option('-p', '--permanently', type=str, default=False, is_flag=True)
def main(token: str, id: str, secret: str, folder_name: str, permanently: bool) -> None:
    cleaner = YaDiskCleaner(token, id, secret)
    deleted_count = cleaner.clean_folder('/' + folder_name, permanently)
    click.echo(f"Deleted: {deleted_count}")

if __name__ == '__main__':
    main()