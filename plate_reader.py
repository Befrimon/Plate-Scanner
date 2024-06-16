from kivy.graphics.texture import Texture
from camera4kivy import Preview

from android.storage import app_storage_path

import numpy as np
import time
import cv2
import os


## Camera class
class PlateReader(Preview):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
        # Configure photo save path
        self.subdir = "plate_scanner"
        self.photo_name = "kivyplatephoto"
        self.photo_path = app_storage_path()+f"/DCIM/{self.subdir}/{self.photo_name}.jpg"

    def capture(self) -> None:
        # Update photo in storage
        if os.path.isfile(self.photo_path):
            os.remove(self.photo_path)
        self.capture_photo(location='private', subdir=self.subdir, name=self.photo_name)
        
        while not os.path.isfile(self.photo_path):
            time.sleep(.1)
        
        # Photo processing for dectyption
        raw_image = cv2.imread(self.photo_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.flip(raw_image, 0)
        
        x1, x2 = int((image.shape[1] - .35*image.shape[0]) / 2), int((image.shape[1] + .35*image.shape[0]) / 2)
        y1, y2 = int(.5*image.shape[0]), int(.85*image.shape[0])
        work_area = image[y1:y2, x1:x2]

        # TODO find plate on image and transform to matrix

        # Update label
        self.parent.update_result(self.decode(None))

        # Check precessing result
        # NOTE Delete on release
        kivy_texture = Texture.create(size=(work_area.shape[1], work_area.shape[0]), colorfmt="luminance")
        kivy_texture.blit_buffer(work_area.tostring(), colorfmt="luminance", bufferfmt="ubyte")
        self.parent.ids.debug_img.texture = kivy_texture

    def decode(self, code) -> str:
        # code (np.array?) : Raw matrix for decoding 
        
        # TODO decode matrix
        return "Decode string here!"

