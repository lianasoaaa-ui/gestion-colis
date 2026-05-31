[app]

title = Gestion Colis Madagascar

package.name = gestioncolis
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,mp3,json

version = 1.0

requirements = python3,kivy==2.3.0,reportlab,ffpyplayer

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.accept_sdk_license = True

presplash.color = #FFFFFF

[buildozer]
log_level = 2
warn_on_root = 1
