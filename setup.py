from setuptools import setup

version = '0.1'

setup(
    name='wsgidelegator',
    version=version,
    author='Casey Marks',
    author_email='casey@fivehut.com',
    description='WSGI service that delegates to other services based on path',
    keywords='wsgi',
    url='http://github.com/fivehut/wsgidelegator',
    license='MIT',
    py_modules=['wsgidelegator'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        ],
    install_requires = [
        'WebOb == 1.0',
        'Paste >= 1.7.5.1',
        ],
    )
