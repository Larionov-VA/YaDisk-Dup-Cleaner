import click


@click.command()
@click.option('-t', '--token', type=str, required=True)
@click.option('-f', '--folder_name', type=str, required=True)
def main(token, folder_name) -> int:
    print(token, folder_name)
    return 0


if __name__ == "__main__":
    main()