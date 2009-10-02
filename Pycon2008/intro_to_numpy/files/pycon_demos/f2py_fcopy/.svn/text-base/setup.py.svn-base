from numpy.distutils.core import Extension

ext_modules = []

fcopy1 = Extension(name='fcopy',
                   sources=['fcopy.pyf','fcopy.f'])
ext_modules.append(fcopy1)

fcopy2 = Extension(name='fcopy2',
                   sources=['fcopy2_solution.pyf', 'fcopy.f'])
ext_modules.append(fcopy2)

if __name__ == "__main__":
    from numpy.distutils.core import setup

    setup(name='fcopy',
          description = "f2py example",
          ext_modules = ext_modules,
    )
