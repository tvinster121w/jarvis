[app]

title = J.A.R.V.I.S.
package.name = jarvis
package.domain = org.jarvis

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json,html,js,css,mp3,wav,ogg,gif,xml
source.exclude_exts = spec,pyc,pyo
source.exclude_dirs = tests, bin, venv, .venv, .git, .github, dist, build, __pycache__, docs

version = 0.1.0

requirements = python3,kivy==2.2.1,pyjnius

orientation = portrait
fullscreen = 0

# ------------------------------------------------------------------
# Android specific
# ------------------------------------------------------------------

android.api = 31
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.logcat_filters = *:S python:D
android.permissions = RECORD_AUDIO, INTERNET, VIBRATE, MODIFY_AUDIO_SETTINGS

# ------------------------------------------------------------------
# Buildozer settings
# ------------------------------------------------------------------

[buildozer]

log_level = 2
warn_on_root = 0

# Force older p4a with Python 3.11 (has 'cgi' module needed by Kivy 2.2.1)
p4a.branch = v2023.09.15
