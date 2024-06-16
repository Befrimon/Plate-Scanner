import kivy
kivy.require('2.3.0')
from kivy.lang import Builder
Builder.load_file("applayout.kv")

from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.layout import Layout
from kivy.uix.image import Image
from kivy.app import App

from permission_manager import PermissionManager
from plate_reader import PlateReader 


## All app layout classes
class MainScreen(FloatLayout):
    # Declaring object vars for quick reference
    plate_reader = ObjectProperty()
    result_text = ObjectProperty()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.remove_widget(self.ids.debug_img)  # Hide debug image

    def update_result(self, value :str) -> None:
        # value (str) : New text value for decode label

        self.result_text.text = value


class ButtonBox(FloatLayout):
    def debug_switch(self, toggle :str) -> None:
        # toggle (str) : ToggleButton state

        image = self.parent.ids.debug_img
        if toggle == "down":
            self.parent.remove_widget(image)
        else:
            self.parent.add_widget(image)

    def switch_flashlight(self, toggle :str) -> None:
        # toggle (str) : ToggleButton state

        if toggle == "down":
            flash = "on"
        else:
            flash = "off"
        self.parent.plate_reader.torch(flash)

    def capture_photo(self) -> None:
        self.parent.plate_reader.capture()


## Window class
class MainApp(App):
    def on_start(self) -> None:
        self.perm_manager = PermissionManager(self.start_app)  # Requesting permissions

    def start_app(self) -> None:
        # Triggered after permissions granted
        self.perm_manager = None
        self.screen.plate_reader.connect_camera(
                enable_video = False,
                default_zoom = .1
        )
    
    def build(self) -> Layout:
        self.screen = MainScreen()
        return self.screen
   
    def on_stop(self) -> None:
        self.screen.plate_reader.disconnect_camera()


## Run app
MainApp().run()

