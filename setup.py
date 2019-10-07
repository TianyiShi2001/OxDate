from setuptools import setup

setup(name='OxDate',
      version='0.1',
      description='Oxford term dates tools',
      url='http://github.com/TianyiShi2001/OxDate',
      author='Tianyi Shi',
      author_email='ShiTianyi2001@outlook.com',
      license='MIT',
      packages=['OxDate'],
      install_requires=[
          'requests', 'lxml', 'python-dateutil'
      ],
      zip_safe=False,
      python_requires='>=3.1')