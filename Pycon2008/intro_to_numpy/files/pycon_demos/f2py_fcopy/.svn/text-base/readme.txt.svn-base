In this example we'll use f2py to wrap a simple fortran function
found in fcopy.f so that it can be called by python.  The file
already has a working version of the wrapper.  Your job is to
improve the wrapper so that it is more pythonic.  The example
follows along exactly with the notes from the lecture.

1. Examine the following:

    fcopy.f -- fortran file that implements the algorithm.
    fcopy.pyf -- simplistic f2py interface definition.
    setup.py -- Equivalent of a Python "make" file to build the 
                fcopy extension module.
    fcopy_test.py -- A Test module that will ensure that fcopy
                     works correctly.

2. Build the fcopy.pyf module using the following:
   
   ~/exercises/f2py_copy> setup.py build_src build_ext --inplace

   This tells setup that you need to convert the pyf file into
   a source file (build_src step) and that you would like the
   extension modules built in this directory instead of a separate
   build directory (build_ext --inplace).
    
3. Now run fcopy_test.py to ensure that the build worked.  If it
   runs without error and prints a few results, it is working
   fine.
   
4. Your job is now to make a new interface called fcopy2 that
   improves the fcopy function so that it is called like this:
   
     b = fcopy2.fcopy(a)
   
   This is exactly the same interface as the function in the
   lecture notes, so use this as guidance.
    
   a. Generate a f2py wrapper file for f2py by calling the
      following from a *shell* command line:
   
         f2py fcopy.f -m fcopy2 -h fcopy2.pyf
         
   b. Modify the fcopy2.pyf file accordingly.
   c. uncomment the following lines in the setup.py and run
      the setup.py file exactly as in step 2.

       #fcopy2 = Extension(name='fcopy2',
       #                   sources=['fcopy2.pyf', 'fcopy.f'])
       #ext_modules.append(fcopy2)
      