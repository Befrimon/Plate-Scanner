from kivy.clock import Clock, mainthread
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button

from android.permissions import request_permissions, check_permission, Permission
from android import mActivity


## Class for requesting android permissions
class PermissionManager:
    def __init__(self, start_app :callable) -> None:
        # start_app (callable) : A function that should call after all permissions granted

        self.attempt_count = 0
        self.start_app = start_app
        self.permissions = [Permission.CAMERA]
        self.check_status([], [])

    def check_status(self, permissions :list[Permission], grants :list[Permission]) -> None:
        # permissions (list) : List of requested permissions
        # grants      (list) : List of granted permissions

        # Check if all permissions granted
        all_granted = True
        for perm in self.permissions:
            all_granted = all_granted and check_permission(perm)

        if all_granted:
            self.start_app()
        elif self.attempt_count < 2:
            Clock.schedule_once(lambda dt: self.call_dialog)
        else:
            self.no_permissions()

    def call_dialog(self) -> None:
        # Retry if user reject permission
        self.attempt_count += 1
        request_permissions(self.permissions, self.check_status)

    @mainthread
    def no_permissions(self) -> None:
        # Inform user about error
        view = ModalView()
        view.add_widget(Button(
            text='Разрешения НЕ выданы.\n\n' +\
                 'Нажмите, чтобы закрыть приложение.',
            on_press=mActivity.finishAndRemoveTask
        ))
        view.open()

