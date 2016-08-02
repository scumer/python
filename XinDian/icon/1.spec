# -*- mode: python -*-

block_cipher = None


a = Analysis(['1.py'],
             pathex=['E:\\Project\\Python\\XinDian\\icon'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='1',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='up.ico')
