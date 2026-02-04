[app]

# (str) Title of your application
title = TV直播测试

# (str) Package name
package.name = tvlive2024

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tvlive

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas,xml

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,urllib3,chardet

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = landscape

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# (str) Author name
author = 直播APK测试

# (str) Author email
author.email = tvtest@163.com

# (str) URL for your website (optional)
author.url = http://example.com

# (str) License information for your application
#license = MIT

# (str) Short description of the application
#description = A Kivy Application

# (str) Long description of the application
#long_description =

# (str) Keywords for your application
#keywords = kivy,tv,live

# (list) Extra info to send to the app store
#osx.app_category = Productivity
#osx.app_release = 1.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using Adobe After Effects or Animaker.
#android.presplash_lottie = %(source.dir)s/data/presplash.lottie

# (str) Adaptive icon of the application (used if Android API level is 26+)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported permissions)
android.permissions = INTERNET,ACCESS_WIFI_STATE,ACCESS_NETWORK_STATE

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
#android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, e.g. 'foo/*.jar'
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.dir'.
#android.add_assets = asset/*,other_asset

# (list) Put these files or directories in the apk res directory.
#android.add_res =

# (list) List of binary libraries (native libs) to add to the apk
#android.add_libs = libs/android/*.so

# (list) List of extra python packages to install
#android.add_python_packages =

# (list) List of extra python packages to install
#android.add_python3_packages =

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as a string, but it can be a list now.
android.archs = armeabi-v7a, arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
#android.numeric_version = 1

# (bool) enables AndroidX support. Enable when 'android.arch' is arm64-v8a
#android.enable_androidx = True

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Use a custom gradle build script
#android.custom_gradle = False

# (str) Custom gradle build script path
#android.gradle_script =

# (str) Custom build.gradle template path
#android.build_gradle_template =

# (str) Custom AndroidManifest.xml template path
#android.manifest_template =

# (str) Custom meta-data to add to manifest
#android.meta_data =

# (list) Custom intents to add to manifest
#android.intents =

# (str) Custom service to add to manifest
#android.service =

# (str) Custom receiver to add to manifest
#android.receiver =

# (str) Custom provider to add to manifest
#android.provider =

# (str) Custom permission to add to manifest
#android.add_permission =

# (bool) If True, removes default permissions from manifest
#android.remove_permissions =

# (str) If True, stacktrace includes python lines.
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The directory in the apk where libpymodules.so will be stored
#android.libpymodules_dir = libs

# (str) The directory in the apk where app code will be stored
#android.app_libs_dir = libs/python3

# (bool) Allow user to access system properties from python
#androidAllowSystemProperties = False

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios
#ios.kivy_ios_branch = master

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.debug_signer = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.release_signer = "iPhone Distribution: <lastname> <firstname> (<hexstring>)"

# (str) Provisioning profile to use for the debug version
#ios.debug_provisioning_profile = <name or UUID>

# (str) Provisioning profile to use for the release version
#ios.release_provisioning_profile = <name or UUID>

# (str) Command line options to pass to xcodebuild
#ios.xcodebuild_args = -configuration Release

# (bool) Whether or not to sign the code
#ios.sign = True

# (str) Path to the key used to sign
#ios.key_path =

# (str) The development team to use for signing the app
#ios.development_team_id = <hexstring>

# (list) Extra info to send to the app store
#ios.app_category = Productivity
#ios.app_release = 1.0

# (str) The name of the IPA file to create
#ios.ipa_filename =

# (str) Extra plist keys to add (i.e. UIBackgroundModes, see https://developer.apple.com/documentation/bundleresources/information_property_list/uibackgroundmodes)
#ios.add_plist = UIStatusBarHidden=False,UIViewControllerBasedStatusBarAppearance=True

# (bool) If True, the app will be distributed as a free app
#ios.free = False

# (bool) If True, the app will be distributed as a paid app
#ios.paid = False

# (bool) If True, the app will be distributed as a free app with in-app purchases
#ios.free_in_app_purchases = False

# (bool) If True, the app will be distributed as a paid app with in-app purchases
#ios.paid_in_app_purchases = False

# (bool) If True, the app will be distributed as a subscription app
#ios.subscription = False

# (bool) If True, the app will be distributed as a free subscription app
#ios.free_subscription = False

# (bool) If True, the app will be distributed as a paid subscription app
#ios.paid_subscription = False

# (bool) If True, the app will be distributed as a universal app (iPhone and iPad)
#ios.universal = False

# (bool) If True, the app will be distributed as an iPhone only app
#ios.iphone = True

# (bool) If True, the app will be distributed as an iPad only app
#ios.ipad = False

# (bool) If True, the app will be distributed as an Apple TV app
#ios.appletv = False

# (bool) If True, the app will be distributed as an Apple Watch app
#ios.watch = False

# (bool) If True, the app will be distributed as an Apple Vision app
#ios.vision = False

# (bool) If True, the app will be distributed as a Mac Catalyst app
#ios.mac_catalyst = False

# (bool) If True, the app will be distributed as a Mac app
#ios.mac = False

# (bool) If True, the app will be distributed as a Apple TV app (deprecated)
#ios.tvos = False

# (bool) If True, the app will be distributed as a Apple Watch app (deprecated)
#ios.watchos = False

#
# Desktop specific
#

# (str) Desktop entry file default name
#desktop.entry_fname = %(title)s.desktop

# (str) Desktop entry file comment
#desktop.comment = A Kivy Application

# (str) Desktop entry file categories
#desktop.categories = Development;Utility;

# (str) Desktop entry file keywords
#desktop.keywords = kivy,tv,live;

# (str) Desktop entry file executable
#desktop.exec = %(title)s

# (str) Desktop entry file icon
#desktop.icon = %(title)s

# (str) Desktop entry file name
#desktop.name = %(title)s

# (str) Desktop entry file generic name
#desktop.generic_name = Kivy Application

# (str) Desktop entry file startup notify
#desktop.startup_notify = true

# (str) Desktop entry file startup wmclass
#desktop.startup_wmclass = %(title)s

# (str) Desktop entry file terminal
#desktop.terminal = false

# (str) Desktop entry file type
#desktop.type = Application

# (str) Desktop entry file url
#desktop.url = http://example.com

# (str) Desktop entry file version
#desktop.version = 1.0

# (str) Desktop entry file encoding
#desktop.encoding = UTF-8

#
# Other
#

# (str) The description of the app
#description = A Kivy Application

# (str) The long description of the app
#long_description =

# (str) The keywords of the app
#keywords = kivy,tv,live

# (str) The license of the app
#license = MIT

# (str) The author of the app
#author = 直播APK测试

# (str) The author's email
#author.email = tvtest@163.com

# (str) The author's website
#author.url = http://example.com

# (str) The version of the app
#version = 1.0

# (str) The release date of the app
#release_date = 2024-01-01

# (str) The url of the app
#url = http://example.com

# (str) The category of the app
#category = Productivity

# (str) The subcategory of the app
#subcategory = Utilities

# (str) The language of the app
#language = en

# (str) The country of the app
#country = US

# (str) The copyright of the app
#copyright = © 2024 直播APK测试

# (bool) Whether or not to include a copy of the license in the app
#include_license = True

# (bool) Whether or not to include a copy of the readme in the app
#include_readme = True

# (bool) Whether or not to include a copy of the changelog in the app
#include_changelog = True

# (str) The path to the changelog file
#changelog_path = CHANGELOG.md

# (str) The path to the license file
#license_path = LICENSE.md

# (str) The path to the readme file
#readme_path = README.md

[buildozer]

# (int) Log level (0 = error only, 1 = warning, 2 = info, 3 = debug (default))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

# (str) Path to temp directory
# temp_dir = ./.buildozer/temp

# (str) Path to root directory for all buildozer projects
# root_dir = ./.buildozer

# (str) Path to python for android directory (if empty, it will be automatically downloaded.)
# p4a_dir = ./.buildozer/python-for-android

# (str) python-for-android git clone directory (if empty, it will be automatically downloaded.)
# p4a_url = https://github.com/kivy/python-for-android
# p4a_branch = master
# p4a_tag =

# (str) python-for-android recipe directory (if empty, it will use the default)
# p4a_recipes_dir =

# (str) python-for-android local source directory (if empty, it will use the default)
# p4a_local_recipes =

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# ndk_dir = ./.buildozer/android/platform/android-ndk-r25b

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# sdk_dir = ./.buildozer/android/platform/android-sdk-24

# (str) ANT directory (if empty, it will be automatically downloaded.)
# ant_dir = ./.buildozer/android/tools/apache-ant-1.9.4

# (bool) If True, buildozer will check for updates each time it runs.
# check_for_updates = True

# (bool) If True, buildozer will use color in the output.
# use_color = True

# (bool) If True, buildozer will use verbose output.
# verbose = False

# (bool) If True, buildozer will skip the check for required packages.
# skip_requirements_check = False

# (bool) If True, buildozer will skip the check for required system packages.
# skip_system_packages_check = False

# (bool) If True, buildozer will skip the check for required tools.
# skip_tools_check = False

# (bool) If True, buildozer will skip the check for required environment variables.
# skip_env_check = False

# (bool) If True, buildozer will skip the check for required permissions.
# skip_permissions_check = False

# (bool) If True, buildozer will skip the check for required build tools.
# skip_build_tools_check = False

# (bool) If True, buildozer will skip the check for required platform tools.
# skip_platform_tools_check = False

# (bool) If True, buildozer will skip the check for required build types.
# skip_build_types_check = False

# (bool) If True, buildozer will skip the check for required build modes.
# skip_build_modes_check = False

# (bool) If True, buildozer will skip the check for required build architectures.
# skip_arch_check = False

# (bool) If True, buildozer will skip the check for required build versions.
# skip_version_check = False

# (bool) If True, buildozer will skip the check for required build dependencies.
# skip_dependencies_check = False

# (bool) If True, buildozer will skip the check for required build resources.
# skip_resources_check = False

# (bool) If True, buildozer will skip the check for required build assets.
# skip_assets_check = False

# (bool) If True, buildozer will skip the check for required build libs.
# skip_libs_check = False

# (bool) If True, buildozer will skip the check for required build src.
# skip_src_check = False

# (bool) If True, buildozer will skip the check for required build jars.
# skip_jars_check = False

# (bool) If True, buildozer will skip the check for required build aars.
# skip_aars_check = False

# (bool) If True, buildozer will skip the check for required build proguard.
# skip_proguard_check = False

# (bool) If True, buildozer will skip the check for required build manifest.
# skip_manifest_check = False

# (bool) If True, buildozer will skip the check for required build gradle.
# skip_gradle_check = False

# (bool) If True, buildozer will skip the check for required build ant.
# skip_ant_check = False

# (bool) If True, buildozer will skip the check for required build ndk.
# skip_ndk_check = False

# (bool) If True, buildozer will skip the check for required build sdk.
# skip_sdk_check = False

# (bool) If True, buildozer will skip the check for required build tools.
# skip_build_tools_check = False

# (bool) If True, buildozer will skip the check for required platform tools.
# skip_platform_tools_check = False

# (bool) If True, buildozer will skip the check for required build types.
# skip_build_types_check = False

# (bool) If True, buildozer will skip the check for required build modes.
# skip_build_modes_check = False

# (bool) If True, buildozer will skip the check for required build architectures.
# skip_arch_check = False

# (bool) If True, buildozer will skip the check for required build versions.
# skip_version_check = False

# (bool) If True, buildozer will skip the check for required build dependencies.
# skip_dependencies_check = False

# (bool) If True, buildozer will skip the check for required build resources.
# skip_resources_check = False

# (bool) If True, buildozer will skip the check for required build assets.
# skip_assets_check = False

# (bool) If True, buildozer will skip the check for required build libs.
# skip_libs_check = False

# (bool) If True, buildozer will skip the check for required build src.
# skip_src_check = False

# (bool) If True, buildozer will skip the check for required build jars.
# skip_jars_check = False

# (bool) If True, buildozer will skip the check for required build aars.
# skip_aars_check = False

# (bool) If True, buildozer will skip the check for required build proguard.
# skip_proguard_check = False

# (bool) If True, buildozer will skip the check for required build manifest.
# skip_manifest_check = False

# (bool) If True, buildozer will skip the check for required build gradle.
# skip_gradle_check = False

# (bool) If True, buildozer will skip the check for required build ant.
# skip_ant_check = False

# (bool) If True, buildozer will skip the check for required build ndk.
# skip_ndk_check = False

# (bool) If True, buildozer will skip the check for required build sdk.
# skip_sdk_check = False