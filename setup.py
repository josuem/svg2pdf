from setuptools import setup, find_packages

setup(
    name='svg2pdf',
    version='0.1',
    description="A simple package to convert Inkscape's SVG to PDFs",
    url='',
    author='Josue Meneses-Diaz',
    author_email='josue.meneses@usach.cl',
    license='MIT',
    package_dir={'': 'src'},
    py_modules=['svg2pdf'],
    zip_safe=False,
)
