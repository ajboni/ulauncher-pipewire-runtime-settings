import os
import json
import os


from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction


def get_commands():
    path = os.path.join(os.path.dirname(__file__), "commands.json")
    commandsFile = open(path)
    commands = json.load(commandsFile)
    commandsFile.close()
    return commands


def get_menu(extension):
    keyword = extension.preferences["keyword"]
    items = []
    commands = get_commands()
    for command in commands:
        items.append(
            ExtensionResultItem(
                icon="icons/pipewire.png",
                name=command["title"],
                description=command["description"],
                on_enter=SetUserQueryAction(keyword + " " + command["keyword"]),
            )
        )
    return items
