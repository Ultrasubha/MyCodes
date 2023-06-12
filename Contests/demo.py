'''import subprocess

package_name = 'keyboard'

try:
    import keyboard
except ImportError:
    try:
        subprocess.check_call(['pip', 'install', package_name])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing {package_name} package: {e}")

while True:
    if keyboard.read_key() == "a":
        break'''


#date = str(datetime.now())[:10]
#print(os.getcwd())