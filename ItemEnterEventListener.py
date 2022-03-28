import logging
import os
import re
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from commands import get_commands, get_menu

logger = logging.getLogger(__name__)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        data = event.get_data()
        items = []

        logger.error(data["command"])

        command_output = os.popen(data["command"]).read()
        logger.debug(command_output)

        for line in command_output.strip().split("\n"):
            name = line
            description = line

            if data["keyword"] == "list":
                key = re.search(r"key:\'([^\']+)\'", line)
                if key and key.group(1):
                    name = key.group(1)

                value = re.search(r"value:\'([^\']+)\'", line)
                if value and value.group(1):
                    description = value.group(1)
            else:
                key = re.search(r"key:([^\'\s]+)", line)
                if key and key.group(1):
                    name = key.group(1)

                value = re.search(r"value:([^\'\s]+)", line)
                if value and value.group(1):
                    description = value.group(1)

            items.append(
                ExtensionResultItem(
                    icon="icons/pipewire.png",
                    name=name,
                    description=description,
                    on_enter=HideWindowAction(),
                )
            )
        return RenderResultListAction(items)
