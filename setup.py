from distutils.core import setup

setup(
    name='elm',
    version='0.3',
    description='Extreme Learning Machine',
    author='masaponto',
    author_email='masaponto@gmail.com',
    url='masaponto.github.io',
    install_requires=['scikit-learn', 'numpy'],
    py_modules=['elm', 'cob_elm', 'ml_elm'],
    package_dir={'': 'src'}
)
