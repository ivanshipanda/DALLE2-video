from setuptools import setup, find_packages

setup(
  name = 'dalle2-video',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'DALL-E2 for Video - Straightforward extension of DALL-E2 architecture to video generation from text',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/dalle2-video',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'video synthesis',
    'imagination machine'
  ],
  install_requires=[
    'einops>=0.4',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
