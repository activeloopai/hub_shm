Hub Shared Memory
---

This package provides a backport of the Python 3.8's shared\_memory module that works for 3.6 and 3.7. This is based off dillonlaird's Shared Numpy array but is leaner.


Install
---

To install run `pip install hub-shm`.


Usage
---

```python
import hub-shm as shm
```


You can then access `shm.SharedMemory` and `shm.ShareableList` which are the same as the
ones in Python 3.8's [shared\_memory](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
module.

