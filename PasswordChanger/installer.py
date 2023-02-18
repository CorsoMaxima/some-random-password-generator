from cx_Freeze import setup, Executable

base = None    

executables = [Executable("pwdchanger.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Made by Corso_Maxima#8304 [through internet lmao]",
    options = options,
    version = "v1.01",
    description = 'there is none',
    executables = executables
)