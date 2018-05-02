MP Examples
===========

This repo shows some examples on the benefits of multiprocessing and how simple
it can be. 

Three examples I can think of in which Mutlithreading/processing is crucial is (I'm
  sure there are more):

1. If you have infrequent/sporadic signals coming in. 
2. If you want to create a pipeline so that one bit of processing isn't held up
   by the other.
3. You want to use up the cores in your machine to speed up your python script.

This repo is mainly concerned with the second and third uses. In particular for me, it is
because I am often doing machine learning on a GPU and I want to parallelize the
preprocessing of data on the CPU with the model training on the GPU.

Repo Layout
-----------
You should be able to clone this repo and run these tests without difficulty.
They rely on loading in 'big files' which are randomly generated numbers saved
to disk. To do this, run the `prepare_data.py` file before going through the
examples. 

`example1.py` is the naive implementation, of loading the files in one by one
and doing some heavy processing. The examples are best illustrated if this takes
about 10s, so you may need to increase/decrease the size of the arrays generated
in here depending on your machine.

`example2.py` - `example4.py` show how to do multiprocessing with the high-level
`multiprocess.Pool` class. This is the easiest way to speed up your scripts, and
should be used if possible.  

`example5.py` onwards show more complex examples using the
`multiprocessing.Process` and `multiprocessing.Queue` classes to create some
parallelism. Note that queues aren't the only way to signal across processes,
but they are the one I use the most. You can also check out pipes and locks.

Other
-----
For an example of a repo that uses queues and multithreading to load data in
preparation for deep learning, check out `dataset_loading`__

__ https://github.com/fbcotter/dataset_loading
