# rename this to siteconf.py for building Universal Binary on OSX
BOOST_INC_DIR = ['/usr/local/include']
BOOST_LIB_DIR = ['/usr/local/lib']
BOOST_COMPILER = 'gcc'
BOOST_PYTHON_LIBNAME = ['boost_python']
BOOST_THREAD_LIBNAME = ['boost_thread']
USE_SHIPPED_BOOST = False
CUDA_TRACE = False
CUDA_ROOT = '/usr/local/cuda'
CUDA_ENABLE_GL = True
CUDADRV_LIB_DIR = []
CUDADRV_LIBNAME = ['cuda']
CXXFLAGS = ["-arch", "x86_64", "-arch", "i386"]
LDFLAGS = ["-arch", "x86_64", "-arch", "i386"]
