from setuptools import setup, find_packages

setup(
    name='lmquickbench',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lmquickbench = lmquickbench.cli:main',
        ],
    },
    author="Gordon Yeung",
    description="A lightweight CLI tool to benchmark local LLMs running on LM Studio.",
    url="https://github.com/yourusername/LMQuickBench",
    python_requires='>=3.7',
)
