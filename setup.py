from setuptools import setup, find_packages

setup(
    name='src',
    version='0.1.0',
    description='Shared clothe.ai library',
    url='https://github.com/shalireza/clothe-lib',
    author='Alireza Shateri',
    author_email='alirezashateri7@gmail.com',
    license='MIT',
    packages=find_packages(where='.'),
    package_dir={'': '.'},
    install_requires=[
        'requests>=2.25.1',
        'aiohttp>=3.7.4.post0',
        'pika',
        'torpy',
        'pysocks'
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
