# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\2380\\OneDrive - FernUni Schweiz\\Dokumente\\GitHub\\tKinter-experiment\\src\\CustomTKinter\\Windows-Account-Creator.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['customtkinter', 'tkinter', 'subprocess', 'os'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Windows-Account-Creator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\2380\\OneDrive - FernUni Schweiz\\Dokumente\\GitHub\\tKinter-experiment\\src\\CustomTKinter\\Pictogrammers-Material-Account.512.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Windows-Account-Creator',
)
