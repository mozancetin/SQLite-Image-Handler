from setuptools import setup, find_packages, version

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='SQLiteImageHandler',
    version='0.0.1',
    description='Simple to use image handler for python sqlite3.',
    long_description='This package helps you to save images to sqlite database and get images from sqlite database.',
    url='',
    author='Mustafa Ozan Çetin',
    author_email='mustafaozancetin@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['sqlite', 'python', 'sqlite-image', 'image-handler'],
    packages=find_packages(),
    install_requires=['']
)