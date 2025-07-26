import click


@click.command()
@click.option('-t', '--token', type=str, required=True)
@click.option('-f', '--folder_name', type=str, required=True)
@click.option('-r', '--recursive', is_flag=True, help='Enable recursive mode')
def main(token, folder_name, recursive) -> int:
    print(token, folder_name, recursive)
    return 0


if __name__ == "__main__":
    main()