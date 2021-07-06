# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['reject_handling_gui_Smart_Rev8.py'],
             pathex=['C:\\Users\\sahil.nagpal\\Desktop\\Bushing Automatic Reject Handling\\Reject_Handling'],
             binaries=[],
             datas=[('C:/Users/sahil.nagpal/Desktop/Bushing Automatic Reject Handling/Reject_Handling/img','data')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='reject_handling_gui_Smart_Rev8',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='reject_handling_gui_Smart_Rev8')
