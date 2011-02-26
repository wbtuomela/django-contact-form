from setuptools import setup, find_packages

setup(name='django-contact-form',
      version='0.5a1',
      description='Generic contact-form application for Django',
      author='James Bennett',
      author_email='james@b-list.org',
      url='http://code.google.com/p/django-contact-form/',
      packages=find_packages(),
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      package_data={'contact_form': ['locale/*/LC_MESSAGES/*']},
      )
