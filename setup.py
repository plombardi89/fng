import versioneer

from setuptools import setup, find_packages

setup(
    name="fng",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points="""
        [console_scripts]
        fng=fng.main:main
    """,
    author="datawire.io",
    author_email="dev@datawire.io",
    url="https://github.com/datawire/fng",
    download_url="https://github.com/datawire/fng/tarball/{}".format(versioneer.get_version()),
    keywords=[
        "testing",
        "development",
        "kubernetes",
        "microservices"
    ],
    classifiers=[],
)
