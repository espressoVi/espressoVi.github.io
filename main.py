import shutil
import toml
import os
from src.HTML import HTMLGenerator
import logging

config = toml.load("config.toml")

def copy_assets():
    assets = [i for i in os.listdir(config["pages"]["assets"]) if i not in {"html", "content"}]
    for asset in assets:
        shutil.copytree(
                os.path.join(config["pages"]["assets"],asset),
                os.path.join(config["pages"]["site"],asset),
                dirs_exist_ok = True,
        )
    return

def create_pages():
    index = config["pages"]["pages"][0][0]
    with open(os.path.join(config["pages"]["site"], f"{index}.html"), "w") as f:
        f.write(HTMLGenerator(index).get())
    other_pages = config["pages"]["pages"][1]
    available = [i.split(".")[0] for i in os.listdir(config["pages"]["content"])]
    for page in other_pages:
        if page not in available:
            logging.warning(f"Page {page} not found.")
        else:
            with open(os.path.join(config["pages"]["site"], f"{page}.html"), "w") as f:
                f.write(HTMLGenerator(page).get())

def main():
    copy_assets()
    create_pages()

if __name__ == "__main__":
    main()
