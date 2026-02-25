# buildozer.spec
# 用于 Android APK 打包的完整配置

[app]
# 应用的基本信息
title = GuGu App
package.name = guguapp
package.domain = org.example

# 源代码目录（通常为当前目录）
source.dir = .

# 需要包含的文件扩展名（必须包含 mp3，否则声音文件不会打包）
source.include_exts = py,png,jpg,kv,atlas,mp3

# 版本号
version = 0.1
# 版本代号（用于 Google Play）
version.code = 1

# 应用的 requirements（依赖库）
requirements = python3,kivy

# 应用图标（可选，如果没有可留空）
# icon = icon.png
# 应用启动画面（可选）
# presplash = splash.png

# 支持的 Android 架构（默认包含所有主流架构）
android.archs = armeabi-v7a, arm64-v8a

# 屏幕方向（portrait 或 landscape，默认为 portrait）
orientation = portrait

# 全屏模式（隐藏状态栏和导航栏）
fullscreen = 1

# 权限（你的应用不需要特殊权限，留空即可）
# android.permissions =

# Android API 级别（Buildozer 会自动选择合适版本）
# android.api = 30
# android.minapi = 21

# 如果使用 SDL2 后端（Kivy 默认）
# android.sdk = 34

# 打包时的额外命令行参数（一般不需要）
# android.gradle_dependencies = ''

# 应用分类（用于 Google Play）
# android.category = GAME

[buildozer]
# 日志级别（0=安静, 1=标准, 2=详细）
log_level = 2

# 是否在构建后自动运行（一般设为 0）
warn_on_root = 1

# 构建输出目录（通常保持默认）
# bin_dir = ./bin
# build_dir = ./.buildozer

# Android SDK 和 NDK 的下载路径（通常自动处理）
# android.accept_sdk_license = True
