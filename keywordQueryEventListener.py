import logging
import copy
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from commands import get_commands, get_menu

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        extension.preferences["keyword"]
        keyword = event.get_keyword()
        query = event.get_query() or ""
        argument = event.get_argument()
        items = []

        if argument:
            commands = get_commands()
            cmdList = list(x for x in commands if x["keyword"] == argument)
            if cmdList and cmdList[0]:
                cmd = cmdList[0]

                # This commands returns a list of Items
                if "items" in cmd:
                    available_options = extension.preferences[cmd["items"]].split(";")
                    for option in available_options:
                        command = copy.deepcopy(cmd)
                        command["command"] = command["command"].replace("%", option)
                        command["label"] = command["label"] + option

                        items.append(
                            ExtensionResultItem(
                                icon="icons/pipewire.png",
                                name=command["label"],
                                description=command["command"],
                                on_enter=ExtensionCustomAction(command, True),
                            )
                        )

                # This commands returns a single Item
                else:
                    items.append(
                        ExtensionResultItem(
                            icon="icons/pipewire.png",
                            name=cmd["label"],
                            description=cmd["command"],
                            on_enter=ExtensionCustomAction(cmd, True),
                        )
                    )
            else:
                items.append(
                    ExtensionResultItem(
                        icon="icons/pipewire.png",
                        name="No such command",
                        description="No such command.",
                        on_enter=HideWindowAction(),
                    )
                )

            return RenderResultListAction(items)
        else:
            items = get_menu(extension)
            return RenderResultListAction(items)
