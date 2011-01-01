#######################
Profiling with valgrind
#######################

This will run the script through valgrind::

    valgrind --tool=massif python test_scal.py

This produces a “massif.out.?????” file which is a text file, but not in a very readable format. 
To get a more human-readable file, use ms_print::

    ms_print massif.out.????? > profile.txt

More Info
---------

Credits how to use valgrind to http://www.shocksolution.com/2009/04/17/profiling-memory-usage-of-python-code/

Post about this @ https://mattions.wordpress.com/2011/01/01/profiling-python-app/

