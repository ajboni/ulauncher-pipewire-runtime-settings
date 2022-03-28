import imp
import logging
import os

from gi.repository import Notify
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from commands import get_commands, get_menu
from keywordQueryEventListener import KeywordQueryEventListener
from ItemEnterEventListener import ItemEnterEventListener


logger = logging.getLogger(__name__)
Notify.init("PipeWire Runtime Settings")


class PipeWireExt(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


if __name__ == "__main__":
    PipeWireExt().run()
