from setuptools import setup, find_packages

__version__ = '0.0.9'
__authur__ = "Pongpol Prommacharoen"
__email__ = "pongpol095@gmail.com"
__github__ = "https://github.com/Armynous"

#----------------------------------------------------------------------------#

#-------#
# Setup #
#-----------------------------------------------------------------------------#

setup(
    name='Excel_split_merge_tool',
    version=__version__,
    author=__authur__,
    author_email=__email__,
    packages=find_packages(include=[
        'Excel_split_merge_tool',
    ]),
    url='https://github.com/Armynous/split_n_merge_excelfile.git',
    install_requires=[
        'tqdm',
        'openpyxl>=3.1.2',
        'pandas>=2.1.0',
        'numpy>=1.25.2'
    ],
    package_dir={'Excel_split_merge_tool': 'Excel_split_merge_tool'},
    package_data={'Excel_split_merge_tool': ['resource/*.json']}
    include_package_data=True
)

#-----------------------------------------------------------------------------#