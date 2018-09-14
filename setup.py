from setuptools import setup


VERSION = '3'


setup(name='angou_okex',
      version=VERSION,
      description='Lightweight and suckless OKEX REST API client library',
      url='http://github.com/angou-exchange-utils/angou-okex',
      download_url='https://github.com/angou-exchange-utils/angou-okex/tarball/v' + VERSION,
      author='shdown',
      author_email='shdownnine@gmail.com',
      license='LGPLv3',
      packages=['angou_okex'],
      install_requires=['requests'],
      python_requires='>=3',
      platforms=['any'],
      keywords='angou okex crypto exchange',
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
      ],
      zip_safe=False)
