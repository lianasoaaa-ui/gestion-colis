[app]

title = Gestion Colis Test
package.name = gestioncolistest
package.domain = org.example

source.dir = .
source.include_exts = py

version = 1.0

# 🔥 MINIMAL STABLE BUILD
requirements = python3,kivy==2.3.0

orientation = portrait

android.api = 33
android.minapi = 21

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
