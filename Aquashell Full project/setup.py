from cx_Freeze import setup, Executable

setup(
    name="AquaShell",
    version="3.0",
    description="Indie Hacker Terminal",
    executables=[Executable("aquashell.py", icon="aquashell.ico")]
)

