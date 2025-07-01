from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path : str) -> List[str]:
    """
    This function reads the requirements from a file and returns them as a list.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        # Remove any '-e .' or similar editable installs
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


    

    

setup(
    name='mlproject', 
    version='0.1',
    author='Ons O.', 
    packages=find_packages(),
#    install_requires=[    => instead of this line, you can use get the packages directly from the requirements.txt file
#        'numpy>=1.21.0',
#        'pandas>=1.3.0',
#        'scikit-learn>=0.24.0',
#        'matplotlib>=3.4.0',
#       'seaborn>=0.11.0']
    install_requires= get_requirements('requirements.txt'),
        

)