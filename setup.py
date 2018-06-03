from cx_Freeze import setup, Executable


base = None

executables = [Executable("hello.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "hello.py",
    options = options,
    version = "3.6",
    description = '<any_description>',
    executables = executables
)
