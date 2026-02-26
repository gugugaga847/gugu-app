[app]
title = GuGu App
package.name = guguapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 0.1
version.code = 1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Android specific
android.accept_sdk_license = True
android.build_tools_version = 34.0.0
android.sdk_manager_build_tools_version = 34.0.0
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
