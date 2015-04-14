__author__ = 'Андрій'
import xml.dom.minidom
from enum import Enum
import random
_file_name = "stickers.xml"


colors = [
    {"header": "487E28", "body": "659A45"},
    {"header": "A17611", "body": "CF9C25"},
    {"header": "433668", "body": "5C507F"}
]

class Sticker:
    def __init__(self, caption, list_type, items, color):
        self.caption = caption
        self.list_type = list_type
        self.items = items
        self.color = color


def get_text(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def get_stickers():
    dom = xml.dom.minidom.parseString(open(_file_name).read())
    stickers_objects = []
    stickers = dom.getElementsByTagName("sticker")
    for sticker in stickers:
        caption = get_text(sticker.getElementsByTagName("caption")[0].childNodes)
        list_type = get_text(sticker.getElementsByTagName("list_type")[0].childNodes)
        items = get_list_items(sticker)
        stickers_objects.append(Sticker(caption, list_type, items, random.choice(colors)))
    return stickers_objects


def get_list_items(sticker):
    items = sticker.getElementsByTagName("li")
    return [get_text(item.childNodes) for item in items]

if __name__ == "__main__":
    stickers = get_stickers()
    for st in stickers:
        print(st.caption)
        print(st.list_type)
        print(st.items)
