from setuptools import setup, find_packages
from typing import List
def get_requirement(filePath:str)-> List[str]:
    '''
        This function returns a list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirement = []
    with open(filePath) as file_obj:
         requirement = file_obj.readlines()
    requirement = [req.replace("\n","") for req in requirement] 
    
    if HYPEN_E_DOT in requirement:
        requirement.remove(HYPEN_E_DOT)
        
    return requirement

setup(
    name="MLProject_MetalManufacturing",
    version= "0.0.1",
    author="Taiwo Oluwafemi",
    author_email="fanthony16@yahoo.com",
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
)