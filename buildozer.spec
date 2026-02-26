[app]

# (str) Title of your application
title = GuGu App

# (str) Package name
package.name = guguapp

# (str) Package domain
package.domain = org.example

# (str) Source code directory
source.dir = .

# (list) Source files to include (mp3必须包含)
source.include_exts = py,png,jpg,kv,atlas,mp3

# (str) Application version
version = 0.1
version.code = 1

# (list) Application requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1

# Android specific
#
# (bool) Automatically accept SDK licenses (重要)
android.accept_sdk_license = True

# (str) Specify a stable build-tools version (避免预览版)
android.build_tools_version = 34.0.0

# (str) Also specify via sdk_manager (双重保险)
android.sdk_manager_build_tools_version = 34.0.0

# (int) Android API level
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Target SDK
android.sdk = 33

# (str) NDK version
android.ndk = 25b

# (list) Architectures
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
