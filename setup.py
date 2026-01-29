import os
import subprocess
import setuptools

def run(*cmd):
    wd = os.path.dirname(os.path.abspath(__file__))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=wd)
    return p.stdout.read().decode().rstrip()


tag = run('git', 'for-each-ref', '--format=%(refname:short)', '--sort=-authordate', '--count=1', 'refs/tags')
rev = run('git', 'rev-parse', '--short=8', 'HEAD')

setuptools.setup(
    name='execution_domain',
    version=f'{tag}+{rev}'
    author='Thang Dinh'
    author_email='',
    packages=["execution_domain"]
)
