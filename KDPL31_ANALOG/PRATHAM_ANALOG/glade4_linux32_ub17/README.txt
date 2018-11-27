Installing Glade on Linux 32 bit
----------------------------------------------------------------------------

Note: this version has been compiled on Ubuntu 17.10. It should run on 
compatible versions of Linux.

Note: this version will use OpenGL if it is available, and if so
needs at least 16Mb graphics RAM to hold textures and display lists. 
It also requires pbuffer or framebuffer object (FBO) support. Most modern 
graphics cards are suitable - it has been tested on ATI 9200, 9550, 
Nvidia 5600, 7600GT, Quadro 600, GeForce 9300M GS and Intel 855GM.

If you do not want to use OpenGL, you can set the environment variable
GLADE_USE_OPENGL to no. However OpenGL is strongly recommended.

If Glade reports your OpenGL vendor is MESA, you have software emulation
and it may be slow. Download the latest driver from NVidia/AMD and
install to fix this.

If you find that cursor movement becomes slow and jerky when you maximise
the application, it's because your GPU does not support textures at
that resolution in hardware. The workaround is to make the application
window smaller.

1.      Unzip the glade4_linux32_ub17.tar.gz file to any directory

2.      Set the environment variable GLADE_HOME to this directory
        e.g. export GLADE_HOME=/home/user/glade4_linux64_ub17

3.      Prepend $GLADE_HOME/bin to your PATH environment variable
        e.g export PATH=$GLADE_HOME/bin:$PATH

4.      Set your LD_LIBRARY_PATH to $GLADE/lib. 

5.      If you intend to use the Python API, you need a python 
        installation on your system. www.python.org offer a good 
        platform independent version of python available for free 
        download. Glade is currently linked to version 2.7.8. If you
        install it, make sure you do that by using 'make altinstall'
        rather than just 'make install' so you don't clobber any
        existing version of python on your system.

6.      Add $GLADE_HOME/bin to your PYTHONPATH environment variable
        e.g export PYTHONPATH=/usr/local/lib/python2.7:$GLADE_HOME/bin


The library 'example', the DRC rules file 'drc.py' and technology file
'example.tch' are provided as examples.

----------------------------------------------------------------------------

Legal mumbo-jumbo:

   	This package is provided "as is" and without any express or implied
   	warranties, including, without limitation, the implied warranties of
   	merchantability and fitness for a particular purpose.

   	Various portions of this package are copyright:

		LEF/DEF interface: Cadence Design Systems and Si2
		(http://openeda.si2.org)

		Python: http://www.python.org

		SWIG: http://www.swig.org

		Qt: Trolltech (http://www.trolltech.com)

		OpenGL: http://www.opengl.org

		Capo: University of Michigan 
		(http://vlsicad.eecs.umich.edu/BK/PDtools/Capo)

		zlib: http://www.zlib.org

		Gemini: Carl Ebeling (http://www.cs.washington.edu)

        Fastcap: MIT (http://www.rle.mit.edu/cpg/research_codes.htm)

		Special thanks to Software Verification Ltd
		(http://www.softwareverify.com) for Memory Validator,
		Coverage Validator and Performance Validator which were 
		extensively used in the development of Glade.

----------------------------------------------------------------------------
