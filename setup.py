from setuptools import setup, find_packages

setup(
    name='gh_subdir',
    version='0.1.9',
    description='A Python module for installing GitHub subdirectories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Reece Vela',
    author_email='reecevela@outlook.com',
    url='https://github.com/reecevela/gh-subdir-py',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords='github directory download python',
)
