from pathlib import Path
from setuptools import setup

ROOT = Path(__file__).parent
FOLDERS = ['bin', 'vaspup', 'config']
setup(
    name='vaspup',
    version="0.0.0+archer2.20261015",
    description="Preserved customized vaspup command-line tools",
    python_requires=">=3.9",
    packages=['vaspup_cli'],
    data_files=[
        ("share/vaspup/" + folder,
         [str(p.relative_to(ROOT)) for p in sorted((ROOT / folder).iterdir()) if p.is_file()])
        for folder in FOLDERS
    ],
    entry_points={"console_scripts": [
        name + "=" + target for name, target in {'vaspup1': 'vaspup_cli:main', 'data-sod-energy': 'vaspup_cli:main', 'data-sod-report': 'vaspup_cli:main', 'data-sod-volume': 'vaspup_cli:main', 'full-clean': 'vaspup_cli:main', 'generate-nbands': 'vaspup_cli:main', 'generate-potcar': 'vaspup_cli:main', 'generate-sod': 'vaspup_cli:main', 'vaspup1-data-converge': 'vaspup_cli:main', 'vaspup1-data-sod-energy': 'vaspup_cli:main', 'vaspup1-data-sod-report': 'vaspup_cli:main', 'vaspup1-data-sod-volume': 'vaspup_cli:main', 'vaspup1-full-clean': 'vaspup_cli:main', 'vaspup1-generate-converge': 'vaspup_cli:main', 'vaspup1-generate-nbands': 'vaspup_cli:main', 'vaspup1-generate-potcar': 'vaspup_cli:main', 'vaspup1-generate-sod': 'vaspup_cli:main'}.items()
    ]},
)
