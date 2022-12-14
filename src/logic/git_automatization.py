import subprocess

def git_add():

    try:
        comand_add = f"git add ."
        comand_subprocess=subprocess.run(comand_add, shell=True, check=True)
        return comand_subprocess.returncode

    except subprocess.SubprocessError:
        print('El comando git add no ha sido ejecutado correctamente.')

def git_commit():

    try:
        comand_commit = f'git commit -m "chore Update Web Page data"'
        comand_subprocess = subprocess.run(comand_commit, shell=True, check=True)
        return comand_subprocess.returncode

    except subprocess.SubprocessError:
        print('El comando commit no ha sido ejecutado correctamente.')


def git_push():
    try:
        comand_push = f"git push"
        comand_subprocess = subprocess.run(comand_push, shell=True, check=True)
        return comand_subprocess.returncode

    except subprocess.SubprocessError:
        print('El comando commit no ha sido ejecutado correctamente.')
