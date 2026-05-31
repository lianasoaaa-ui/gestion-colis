import os
import json
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

from reportlab.pdfgen import canvas
from kivy.utils import platform

# =========================
# SAFE STORAGE (IMPORTANT)
# =========================

try:
    from android.storage import primary_external_storage_path
except:
    primary_external_storage_path = None

Window.clearcolor = (1, 1, 1, 1)

# =========================
# FILES SAFE MODE
# =========================

if platform == "android":
    from android.storage import app_storage_path
    BASE_DIR = app_storage_path()
else:
    BASE_DIR = os.getcwd()

FICHIER_COLIS = os.path.join(BASE_DIR, "colis.json")
FICHIER_USER = os.path.join(BASE_DIR, "users.json")