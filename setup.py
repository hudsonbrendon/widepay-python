from setuptools import setup


setup(name='widepay-python',
      version='0.1',
      description='Com o Wide Pay você pode receber por boletos/carnês, cartão de crédito na internet ou mesmo através das maquininhas.',
      url='https://github.com/hudsonbrendon/widepay-python',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['widepay'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
