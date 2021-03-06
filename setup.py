from distutils.core import setup
setup(
  name = 'geoffsmodule',         # How you named your package folder (MyLib)
  packages = ['geoffsmodule'],   # Chose the same as "name"
  version = '0.2.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Materials for MBP Tech Talk on Software Engineering',   # Give a short description about your library
  author = 'Geoffrey Woollard',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/geoffwoollard/mbptechtalk',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/geoffwoollard/mbptechtalk/archive/v0.2.2.tar.gz',    # I explain this later on
  keywords = ['Python', 'Software Engineering'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'numba',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support

  ],
)