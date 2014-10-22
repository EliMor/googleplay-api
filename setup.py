from distutils.core import setup

version = "1.0.0"

setup(name="googleplay-api",
      version=version,
      author="Emilien Girault",
      author_email="emilien.girault@gmail.com",
      license="BSD",
      description="Google Play API for Android",
      url="https://github.com/EliMor/googleplay-api",
      py_modules=[
        'apishell',
        'categories',
        'config',
        'download',
        'googleplay',
        'googleplay_pb2',
        'helpers',
        'list',
        'permissions',
        'search'
        ],
      install_requires=['protobuf']

)