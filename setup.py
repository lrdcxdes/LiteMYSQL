from setuptools import setup, find_packages

long_description1 = '''
https://github.com/LORD-ME-CODE/LiteMYSQL
'''

setup(
    name='LiteMYSQL', 
    version='1.0',
    description='Библиотека для легкого использования mysql базы данных!', 
    packages=['LiteMYSQL'],
    author_email='lordgrief176@gmail.com', 
    zip_safe=False,
    url='https://github.com/LORD-ME-CODE/LiteMYSQL',
    license='GPLv3',
    install_requires=['aiomysql', 'pymysql'],
    author='lordcodes',
    python_requires='>=3.6',
    long_description=long_description1,
    long_description_content_type="text/markdown"
)