from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch==2.0.1',
        'torchvision==0.15.2',
        'numpy==1.26.0',
        'matplotlib==3.7.2',
        'pandas==2.1.1',
        'scipy==1.11.2',
    ],
    description='Quantum Convolutional Neural Networks (QCNN) implementation',
    author='Raja Appapurapu',
    author_email='your_email@example.com',
    url='https://github.com/your_github_repo',
)