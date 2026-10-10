# Build from the repository root with packaging/build-windows.ps1.
from pathlib import Path
root = Path(SPECPATH).parent

a = Analysis(
    [str(root / 'start.py')],
    pathex=[str(root)],
    binaries=[],
    datas=[(str(root / 'frontend' / 'dist'), 'frontend/dist'),
           (str(root / 'lmu_telemetry' / 'data' / 'tracks'), 'lmu_telemetry/data/tracks'),
           (str(root / 'LICENSE'), '.')],
    hiddenimports=['uvicorn.logging', 'uvicorn.loops.asyncio',
                   'uvicorn.protocols.http.h11_impl', 'uvicorn.lifespan.on'],
    hookspath=[], hooksconfig={}, runtime_hooks=[],
    excludes=['backend', 'pytest', 'pandas', 'IPython'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='LMU Telemetry',
          debug=False, bootloader_ignore_signals=False, strip=False,
          upx=False, console=False)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name='LMU Telemetry')
