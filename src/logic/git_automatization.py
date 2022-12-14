import subprocess

def git_add():

    try:
        comando_add = f"git add ."
        comando_subprocess=subprocess.run(comando_add, shell=True, check=True)
        return comando_subprocess.returncode

    except subprocess.SubprocessError:
        print('El comando git add no ha sido ejecutado correctamente.')

def git_commit():

    try:
        comando_commit = f'git commit -m "chore Update Web Page data"'
        comando_subprocess = subprocess.run(comando_commit, shell=True, check=True)
        return comando_subprocess.returncode

    except subprocess.SubprocessError:
        print('El comando commit no ha sido ejecutado correctamente.')


def git_push():
    try:
        comando_push = f"git push"
        comando_subprocess = subprocess.run(comando_push, shell=True, check=True)
        return comando_subprocess.returncode

    except subprocess.SubprocessError:
        print('El comando commit no ha sido ejecutado correctamente.')
