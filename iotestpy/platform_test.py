import platform
import subprocess
import sys

def print_environment_info():
    print("Operating System:", platform.system())
    print("OS Version:", platform.version())
    print("Platform:", platform.platform())
    print("Processor:", platform.processor())
    print("Python Version:", platform.python_version())
    print("Python Implementation:", platform.python_implementation())
    print("Python Compiler:", platform.python_compiler())
    print("Python Build:", platform.python_build())
    print("Python Executable:", sys.executable)
    print("Python Path:", sys.path)

if __name__ == "__main__":
    # print_environment_info()
    print(sys.executable)
    # subprocess.run(['pip', 'uninstall', 'tzlocal', '-y'])
    # subprocess.run(['pip', 'install', 'tzlocal'])
    # subprocess.check_call(f"{sys.executable} -m pip install Faker", shell=True)
    import pip

    if hasattr(pip, 'main'):
        pip.main(['install', "Faker"])
    else:
        pip._internal.main(['install', "Faker"])

    import tzlocal
    from faker import Faker

    print(tzlocal.get_localzone())
    print("ok")