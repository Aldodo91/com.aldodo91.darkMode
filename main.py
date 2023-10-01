from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        options = ['airDots', 'nuove']
        my_list = event.query.split(" ")

        # uncume pro lite && move up

        items.append(darkOn())
        items.append(darkOff())
        items.append(darkAuto())

        return RenderResultListAction(items)


def darkOn():
    return ExtensionResultItem(icon='images/moon.png',
                               name='Dark Mode ON',
                               description='Set DarkMode ON',
                               on_enter=RunScriptAction("/home/aldo/Documenti/Scripts/ThinkPad/darkMode on", None))


def darkOff():
    return ExtensionResultItem(icon='images/sun.png',
                               name='Dark Mode OFF',
                               description='Set DarkMode OFF',
                               on_enter=RunScriptAction("/home/aldo/Documenti/Scripts/ThinkPad/darkMode off", None))

def darkAuto():
    return ExtensionResultItem(icon='images/ico.png',
                               name='Dark Mode AUTO',
                               description='Set DarkMode AUTO',
                               on_enter=RunScriptAction("/home/aldo/Documenti/Scripts/ThinkPad/darkMode auto", None))


if __name__ == '__main__':
    GnomeSessionExtension().run()
