from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='pip-pytest-template',
    version='0.1.0',
    license="ライセンス",
    description='Python project template with pip and pytest',
    author="作成者",
    url='https://github.com/masaharu-kato/pip-pytest-template',
    packages=find_packages(),
    py_modules=[splitext(basename(path))[0] for path in glob('mypkg/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov']
)