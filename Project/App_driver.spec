# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['App_driver.py'],
    pathex=[],
    binaries=[],
    datas=[('splash.png', '.'), ('worldMap.jpeg', '.'), ('world_population.csv', '.'), ('worldcities.csv', '.'), ('continents.jpeg', '.'), ('ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp', 'data')],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='App_driver',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='App_driver.app',
    icon=None,
    bundle_identifier=None,
)
