from setuptools import setup, find_packages

setup(
    name='click-lock',
    version='0.5',
    url='https://github.com/baverman/click-lock/',
    license='MIT',
    author='Anton Bobrov',
    author_email='baverman@gmail.com',
    description='Adds locks and timeouts to click entrypoints',
    long_description=open('README.rst').read(),
    py_modules=['click_lock'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
    ]
)
