from setuptools import setup,find_namespace_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirments"""
    
    requirments = []
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        [req.replace("\n","") for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
            
    return requirments
            
        
    
    

setup(
    name="SalesBot",
    version="0.0.1",
    author="Animesh",
    author_email="animesh.kr9044@gmail.com",
    packages=find_namespace_packages(),
    install_requires = get_requirements(file_path="requirements.txt")
)