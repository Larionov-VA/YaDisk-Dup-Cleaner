import click
from .cleaner import YaDiskCleaner


@click.command()
@click.option('-t', '--token', type=str, required=True)
@click.option('-f', '--folder_name', type=str, required=True)
def main(token: str, folder: str, recursive: bool, dry_run: bool) -> None:
    cleaner = YaDiskCleaner(token)
    deleted_count = cleaner.clean_folder(folder, recursive)
    click.echo(f"Deleted: {deleted_count}")

if __name__ == '__main__':
    main()