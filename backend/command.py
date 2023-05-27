import typer
# from utils.exporting import export_level1_to_json, export_schedules, save_schedules, export_groups, save_groups, export_attendance, save_attendance
from utils.faking_names import save_fake_names_to_db

cli = typer.Typer()

@cli.command()
def hello(name: str):
    print(f"Hello {name}")

@cli.command()
def exporting():
    # print(Categories()())
    # export_level1_to_json()
    # export_schedules()
    # save_schedules()
    # export_groups()
    # save_groups()
    # export_attendance()
    # save_attendance()
    save_fake_names_to_db()
    pass

if __name__ == "__main__":
    cli()
