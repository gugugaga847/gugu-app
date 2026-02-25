[app]

# (str) Title of your application
title = GuGu App

# (str) Package name
package.name = guguapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp3

# (str) Application versioning
version = 0.1
version.code = 1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# Android specific
#

# (list) Permissions
#android.permissions = INTERNET

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Specify a specific build-tools version to use
android.build_tools_version = 34.0.0

# (list) The Android architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (str) The Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) The Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
#android.skip_update = False

# (bool) If True, then download the NDK and use it. If False, use the existing NDK
#android.ndk_download = True

# (bool) If True, then accept the NDK license
#android.ndk_accept_license = False

# (str) Path to a custom AndroidManifest.xml
#android.manifest =

# (str) Path to a custom strings.xml
#android.strings =

# (str) Path to a custom template gradle project
#android.gradle_project_template =

# (str) Path to a custom source code template
#android.project_template =

# (str) Argument to pass to the buildozer gradle command
#android.gradle_build_args =

# (str) Path to the Java classes to include
#android.add_src =

# (str) Path to the Java library to include
#android.add_libs =

# (list) List of Java files/classes to add (if they are not in the src directory)
#android.add_src = src/java

# (list) List of Java libraries to add (if they are not in the libs directory)
#android.add_libs = libs/*.jar

# (str) Path to a AAR library to include
#android.add_aar =

# (list) List of AAR libraries to include
#android.add_aars =

# (list) List of recipes to build with python-for-android
#android.recipes =

# (str) The directory that contains the python-for-android source code
#android.p4a_dir =

# (str) The branch of python-for-android to use
#android.p4a_branch = master

# (str) The directory that contains the python-for-android distribution
#android.p4a_dist_dir =

# (str) The name of the python-for-android distribution
#android.p4a_dist_name =

# (bool) Use the python-for-android bootstrap that can handle multiple architectures
#android.p4a_multiapi = False

# (str) Extra arguments to pass to the python-for-android build
#android.p4a_args =

# (str) Extra command to run before the python-for-android build
#android.p4a_pre_build_command =

# (str) Extra command to run after the python-for-android build
#android.p4a_post_build_command =

# (list) List of Java versions to include
#android.java_versions = 8,11,17

# (str) Path to the Java keystore (for release signing)
#android.keystore =

# (str) Password for the Java keystore
#android.keystore_password =

# (str) Alias for the Java keystore
#android.keystore_alias =

# (str) Path to the Java key
#android.key =

# (str) Password for the Java key
#android.key_password =

# (bool) If True, then the application will be debuggable
#android.debug = False

# (list) Android extra manifests to add
#android.extra_manifests =

# (list) Android extra resources to add
#android.extra_resources =

# (list) Android extra libraries to add
#android.extra_libs =

# (list) Android extra Java sources to add
#android.extra_java_src =

# (list) Android native libraries to add
#android.extra_native_libs =

[buildozer]

# (int) Log level (0 = quiet, 1 = normal, 2 = verbose)
log_level = 2

# (str) Path to build artifacts storage
#build_dir = ./.buildozer

# (str) Path to build output (i.e., .apk, .ipa) storage
#bin_dir = ./bin
