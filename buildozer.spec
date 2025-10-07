[app]

# --- App Info ---
title = Oraciones del Catecismo Catolico
package.name = OracionesCatecismo
package.domain = org.test
version = 7.0

# --- Source ---
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,mp3

# --- Requirements ---
requirements = python3==3.9.9, kivy==2.3.0, cython==0.29.33
p4a.bootstrap = sdl2
p4a.branch = master

# --- Icons and Splash ---
icon.filename = %(source.dir)s/logo.png
presplash.filename = %(source.dir)s/data/loading.png

# --- Orientation & Display ---
orientation = portrait
fullscreen = 0

# --- Android Settings ---
android.api = 33
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.copy_libs = 1
android.debug_artifact = apk
android.release_artifact = aab
android.logcat_filters = *:S python:D

# --- Gradle / AndroidX Configuration ---
android.gradle_dependencies = com.google.android.material:material:1.10.0
android.gradle_plugins = com.android.tools.build:gradle:7.4.2

android.enable_androidx = True
android.use_androidx = True
android.jetifier = True

# --- Performance / Compatibility ---
android.api_level = 33
android.accept_sdk_license = True

# --- Permissions (add if needed) ---
# android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# --- Docker Environment ---
docker.default_image = kivy/buildozer
docker.add_packages = autoconf,automake,libtool

[buildozer]
log_level = 2
warn_on_root = 1

