from luz import Control, Meta, Module

# Define meta options here
meta = Meta(release=True)

# Define control metadata here
control = Control(
    name="BlurredPreferences",
    id="com.pookjw.BlurredPreferences",
    version="1.1.1",
    author="Jinwoo Kim",
    maintainer="Dhinak G",
    depends=["firmware (>= 15.0)", "mobilesubstrate (>= 0.9.5000)"],
    architecture="iphoneos-arm64",
    description="Hello World!",
    section="Utilities",
)

c_flags = ["-fobjc-arc", "-Wno-unused-variable", "-Wno-unused-function", "-Iheaders"]
frameworks = ["UIKit", "CoreGraphics"]

# Module info
modules = [
    Module(
        type="tweak",
        name="BlurredPreferencesHelper",
        files=["modules/BlurredPreferencesHelper/init.m"],
        filter={"bundles": ["com.apple.Preferences"]},
        c_flags=c_flags,
        frameworks=frameworks,
    ),
    Module(
        type="tweak",
        name="BlurredPreferencesSpringBoardHelper",
        files=["modules/BlurredPreferencesSpringBoardHelper/init.m"],
        filter={"bundles": ["com.apple.springboard"]},
        c_flags=c_flags,
        frameworks=frameworks,
    ),
]
