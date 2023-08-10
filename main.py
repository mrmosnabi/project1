from kivymd.app import MDApp
from kivy.lang.builder import Builder
kv="""

<NavigationDrawerItem@MDNavigationDrawerItem>
<DrawerClickableItem@MDNavigationDrawerItem>


MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title:" Itdude"
                    elivation:4
                    pos_hint:{"top":1}
                    left_action_items:[['menu',lambda x:nav_drawer.set_state("open")]]
        MDNavigationDrawer:
            id:nav_drawer
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    left_action_items:[["account-circle"]]
                    title:"Chuder Vai"
                    text:"@dula vai"
                    spacing:"4dp"
                    padding:"12dp",0,0,"44dp"
                MDNavigationDrawerLabel:
                    text:"menu"
                DrawerClickableItem:
                    icon:"gmail"
                    text:"Inbox"
                DrawerClickableItem:
                    icon:"folder"
                    text:"all"
                MDNavigationDrawerLabel:
                    text:"all.."
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
                DrawerClickableItem:
                    icon:"send"
                    text:"hello"
"""




class x5(MDApp):
    def build(self):
        bldr= Builder.load_string(kv)
        return bldr
x5().run()