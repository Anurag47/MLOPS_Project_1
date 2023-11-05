from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath:str) -> List[str]:
    '''
    This function will return a list of required packages
    '''
    required_packages = []
    with open(filepath) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n","") for r in req]

        if HYPHEN_E_DOT in req :
            req.remove(HYPHEN_E_DOT)

    return req



setup(
    name = 'MLOPS_Project_1',
    version = '0.0.1',
    author = 'Anurag B',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)