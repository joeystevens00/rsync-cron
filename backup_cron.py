#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x7333562d

# Compiled with Coconut version 1.4.1 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
if _coconut_sys.version_info < (3,):
    from __builtin__ import chr, filter, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, raw_input, xrange
    py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_zip, py_filter, py_reversed, py_enumerate, py_raw_input, py_xrange, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, raw_input, xrange, repr
    _coconut_NotImplemented, _coconut_raw_input, _coconut_xrange, _coconut_int, _coconut_long, _coconut_print, _coconut_str, _coconut_unicode, _coconut_repr = NotImplemented, raw_input, xrange, int, long, print, str, unicode, repr
    from future_builtins import *
    chr, str = unichr, unicode
    from io import open
    class object(object):
        __slots__ = ()
        def __ne__(self, other):
            eq = self == other
            if eq is _coconut_NotImplemented:
                return eq
            return not eq
    class int(_coconut_int):
        __slots__ = ()
        if hasattr(_coconut_int, "__doc__"):
            __doc__ = _coconut_int.__doc__
        class __metaclass__(type):
            def __instancecheck__(cls, inst):
                return _coconut.isinstance(inst, (_coconut_int, _coconut_long))
            def __subclasscheck__(cls, subcls):
                return _coconut.issubclass(subcls, (_coconut_int, _coconut_long))
    class range(object):
        __slots__ = ("_xrange",)
        if hasattr(_coconut_xrange, "__doc__"):
            __doc__ = _coconut_xrange.__doc__
        def __init__(self, *args):
            self._xrange = _coconut_xrange(*args)
        def __iter__(self):
            return _coconut.iter(self._xrange)
        def __reversed__(self):
            return _coconut.reversed(self._xrange)
        def __len__(self):
            return _coconut.len(self._xrange)
        def __contains__(self, elem):
            return elem in self._xrange
        def __getitem__(self, index):
            if _coconut.isinstance(index, _coconut.slice):
                args = _coconut.slice(*self._args)
                start, stop, step, ind_step = (args.start if args.start is not None else 0), args.stop, (args.step if args.step is not None else 1), (index.step if index.step is not None else 1)
                return self.__class__((start if ind_step >= 0 else stop - step) if index.start is None else start + step * index.start if index.start >= 0 else stop + step * index.start, (stop if ind_step >= 0 else start - step) if index.stop is None else start + step * index.stop if index.stop >= 0 else stop + step * index.stop, step if index.step is None else step * index.step)
            else:
                return self._xrange[index]
        def count(self, elem):
            """Count the number of times elem appears in the range."""
            return _coconut_int(elem in self._xrange)
        def index(self, elem):
            """Find the index of elem in the range."""
            if elem not in self._xrange: raise _coconut.ValueError(_coconut.repr(elem) + " is not in range")
            start, _, step = self._xrange.__reduce_ex__(2)[1]
            return (elem - start) // step
        def __repr__(self):
            return _coconut.repr(self._xrange)[1:]
        @property
        def _args(self):
            return self._xrange.__reduce__()[1]
        def __reduce_ex__(self, protocol):
            return (self.__class__, self._xrange.__reduce_ex__(protocol)[1])
        def __reduce__(self):
            return self.__reduce_ex__(_coconut.pickle.DEFAULT_PROTOCOL)
        def __hash__(self):
            return _coconut.hash(self._args)
        def __copy__(self):
            return self.__class__(*self._args)
        def __eq__(self, other):
            return _coconut.isinstance(other, self.__class__) and self._args == other._args
    from collections import Sequence as _coconut_Sequence
    _coconut_Sequence.register(range)
    from functools import wraps as _coconut_wraps
    @_coconut_wraps(_coconut_print)
    def print(*args, **kwargs):
        file = kwargs.get("file", _coconut_sys.stdout)
        flush = kwargs.get("flush", False)
        if "flush" in kwargs:
            del kwargs["flush"]
        if _coconut.hasattr(file, "encoding") and file.encoding is not None:
            _coconut_print(*(_coconut_unicode(x).encode(file.encoding) for x in args), **kwargs)
        else:
            _coconut_print(*(_coconut_unicode(x).encode() for x in args), **kwargs)
        if flush:
            file.flush()
    @_coconut_wraps(_coconut_raw_input)
    def input(*args, **kwargs):
        if _coconut.hasattr(_coconut_sys.stdout, "encoding") and _coconut_sys.stdout.encoding is not None:
            return _coconut_raw_input(*args, **kwargs).decode(_coconut_sys.stdout.encoding)
        return _coconut_raw_input(*args, **kwargs).decode()
    @_coconut_wraps(_coconut_repr)
    def repr(obj):
        if isinstance(obj, _coconut_unicode):
            return _coconut_unicode(_coconut_repr(obj)[1:])
        if isinstance(obj, _coconut_str):
            return "b" + _coconut_unicode(_coconut_repr(obj))
        return _coconut_unicode(_coconut_repr(obj))
    ascii = repr
    def raw_input(*args):
        """Coconut uses Python 3 "input" instead of Python 2 "raw_input"."""
        raise _coconut.NameError('Coconut uses Python 3 "input" instead of Python 2 "raw_input"')
    def xrange(*args):
        """Coconut uses Python 3 "range" instead of Python 2 "xrange"."""
        raise _coconut.NameError('Coconut uses Python 3 "range" instead of Python 2 "xrange"')
    if _coconut_sys.version_info < (2, 7):
        import functools as _coconut_functools, copy_reg as _coconut_copy_reg
        def _coconut_new_partial(func, args, keywords):
            return _coconut_functools.partial(func, *(args if args is not None else ()), **(keywords if keywords is not None else {}))
        _coconut_copy_reg.constructor(_coconut_new_partial)
        def _coconut_reduce_partial(self):
            return (_coconut_new_partial, (self.func, self.args, self.keywords))
        _coconut_copy_reg.pickle(_coconut_functools.partial, _coconut_reduce_partial)
else:
    from builtins import chr, filter, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate
    py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_zip, py_filter, py_reversed, py_enumerate, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, zip, filter, reversed, enumerate, repr
    _coconut_str = str
class _coconut(object):
    import collections, copy, functools, types, itertools, operator, threading, weakref, os
    if _coconut_sys.version_info < (3, 2):
        try:
            from backports.functools_lru_cache import lru_cache
            functools.lru_cache = lru_cache
        except ImportError: pass
    if _coconut_sys.version_info < (3,):
        import cPickle as pickle
    else:
        import pickle
    if _coconut_sys.version_info >= (2, 7):
        OrderedDict = collections.OrderedDict
    else:
        OrderedDict = dict
    if _coconut_sys.version_info < (3, 3):
        abc = collections
    else:
        import collections.abc as abc
    class typing(object):
        @staticmethod
        def NamedTuple(name, fields):
            return _coconut.collections.namedtuple(name, [x for x, t in fields])
    Ellipsis, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, property, range, reversed, set, slice, str, sum, super, tuple, type, zip, repr, bytearray = Ellipsis, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, property, range, reversed, set, slice, str, sum, super, tuple, type, zip, staticmethod(repr), bytearray
_coconut_sentinel = _coconut.object()
class MatchError(Exception):
    """Pattern-matching error. Has attributes .pattern and .value."""
    __slots__ = ("pattern", "value")
class _coconut_tail_call(object):
    __slots__ = ("func", "args", "kwargs")
    def __init__(self, func, *args, **kwargs):
        self.func, self.args, self.kwargs = func, args, kwargs
_coconut_tco_func_dict = {}
def _coconut_tco(func):
    @_coconut.functools.wraps(func)
    def tail_call_optimized_func(*args, **kwargs):
        call_func = func
        while True:
            wkref = _coconut_tco_func_dict.get(_coconut.id(call_func))
            if (wkref is not None and wkref() is call_func) or _coconut.isinstance(call_func, _coconut_base_pattern_func):
                call_func = call_func._coconut_tco_func
            result = call_func(*args, **kwargs)  # pass --no-tco to clean up your traceback
            if not isinstance(result, _coconut_tail_call):
                return result
            call_func, args, kwargs = result.func, result.args, result.kwargs
    tail_call_optimized_func._coconut_tco_func = func
    tail_call_optimized_func.__module__ = _coconut.getattr(func, "__module__", None)
    tail_call_optimized_func.__name__ = _coconut.getattr(func, "__name__", "<coconut tco function (pass --no-tco to remove)>")
    tail_call_optimized_func.__qualname__ = _coconut.getattr(func, "__qualname__", tail_call_optimized_func.__name__)
    _coconut_tco_func_dict[_coconut.id(tail_call_optimized_func)] = _coconut.weakref.ref(tail_call_optimized_func)
    return tail_call_optimized_func
def _coconut_igetitem(iterable, index):
    if isinstance(iterable, (_coconut_reversed, _coconut_map, _coconut.zip, _coconut_enumerate, _coconut_count, _coconut.abc.Sequence)):
        return iterable[index]
    if not _coconut.isinstance(index, _coconut.slice):
        if index < 0:
            return _coconut.collections.deque(iterable, maxlen=-index)[0]
        return _coconut.next(_coconut.itertools.islice(iterable, index, index + 1))
    if index.start is not None and index.start < 0 and (index.stop is None or index.stop < 0) and index.step is None:
        queue = _coconut.collections.deque(iterable, maxlen=-index.start)
        if index.stop is not None:
            queue = _coconut.list(queue)[:index.stop - index.start]
        return queue
    if (index.start is not None and index.start < 0) or (index.stop is not None and index.stop < 0) or (index.step is not None and index.step < 0):
        return _coconut.list(iterable)[index]
    return _coconut.itertools.islice(iterable, index.start, index.stop, index.step)
class _coconut_base_compose(object):
    __slots__ = ("func", "funcstars")
    def __init__(self, func, *funcstars):
        self.func = func
        self.funcstars = []
        for f, stars in funcstars:
            if _coconut.isinstance(f, _coconut_base_compose):
                self.funcstars.append((f.func, stars))
                self.funcstars += f.funcstars
            else:
                self.funcstars.append((f, stars))
    def __call__(self, *args, **kwargs):
        arg = self.func(*args, **kwargs)
        for f, stars in self.funcstars:
            if stars == 0:
                arg = f(arg)
            elif stars == 1:
                arg = f(*arg)
            elif stars == 2:
                arg = f(**arg)
            else:
                raise _coconut.ValueError("invalid arguments to " + _coconut.repr(self))
        return arg
    def __repr__(self):
        return _coconut.repr(self.func) + " " + " ".join(("..*> " if star == 1 else "..**>" if star == 2 else "..> ") + _coconut.repr(f) for f, star in self.funcstars)
    def __reduce__(self):
        return (self.__class__, (self.func,) + _coconut.tuple(self.funcstars))
    def __get__(self, obj, objtype=None):
        return _coconut.functools.partial(self, obj)
def _coconut_forward_compose(func, *funcs): return _coconut_base_compose(func, *((f, 0) for f in funcs))
def _coconut_back_compose(*funcs): return _coconut_forward_compose(*_coconut.reversed(funcs))
def _coconut_forward_star_compose(func, *funcs): return _coconut_base_compose(func, *((f, 1) for f in funcs))
def _coconut_back_star_compose(*funcs): return _coconut_forward_star_compose(*_coconut.reversed(funcs))
def _coconut_forward_dubstar_compose(func, *funcs): return _coconut_base_compose(func, *((f, 2) for f in funcs))
def _coconut_back_dubstar_compose(*funcs): return _coconut_forward_dubstar_compose(*_coconut.reversed(funcs))
def _coconut_pipe(x, f): return f(x)
def _coconut_star_pipe(xs, f): return f(*xs)
def _coconut_dubstar_pipe(kws, f): return f(**kws)
def _coconut_back_pipe(f, x): return f(x)
def _coconut_back_star_pipe(f, xs): return f(*xs)
def _coconut_back_dubstar_pipe(f, kws): return f(**kws)
def _coconut_assert(cond, msg=None): assert cond, msg if msg is not None else "(assert) got falsey value " + _coconut.repr(cond)
def _coconut_bool_and(a, b): return a and b
def _coconut_bool_or(a, b): return a or b
def _coconut_none_coalesce(a, b): return a if a is not None else b
def _coconut_minus(a, *rest):
    if not rest:
        return -a
    for b in rest:
        a = a - b
    return a
@_coconut.functools.wraps(_coconut.itertools.tee)
def tee(iterable, n=2):
    if n >= 0 and _coconut.isinstance(iterable, (_coconut.tuple, _coconut.frozenset)):
        return (iterable,) * n
    if n > 0 and (_coconut.hasattr(iterable, "__copy__") or _coconut.isinstance(iterable, _coconut.abc.Sequence)):
        return (iterable,) + _coconut.tuple(_coconut.copy.copy(iterable) for _ in _coconut.range(n - 1))
    return _coconut.itertools.tee(iterable, n)
class reiterable(object):
    """Allows an iterator to be iterated over multiple times."""
    __slots__ = ("iter",)
    def __init__(self, iterable):
        self.iter = iterable
    def _get_new_iter(self):
        self.iter, new_iter = _coconut_tee(self.iter)
        return new_iter
    def __iter__(self):
        return _coconut.iter(self._get_new_iter())
    def __getitem__(self, index):
        return _coconut_igetitem(self._get_new_iter(), index)
    def __reversed__(self):
        return _coconut_reversed(self._get_new_iter())
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "reiterable(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self._get_new_iter())
    def __fmap__(self, func):
        return _coconut_map(func, self)
class scan(object):
    """Reduce func over iterable, yielding intermediate results,
    optionally starting from initializer."""
    __slots__ = ("func", "iter", "initializer")
    def __init__(self, function, iterable, initializer=_coconut_sentinel):
        self.func = function
        self.iter = iterable
        self.initializer = initializer
    def __iter__(self):
        acc = self.initializer
        if acc is not _coconut_sentinel:
            yield acc
        for item in self.iter:
            if acc is _coconut_sentinel:
                acc = item
            else:
                acc = self.func(acc, item)
            yield acc
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "scan(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __copy__(self):
        return self.__class__(self.func, _coconut.copy.copy(self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class reversed(object):
    __slots__ = ("iter",)
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.reversed.__doc__
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut.range):
            return iterable[::-1]
        if not _coconut.hasattr(iterable, "__reversed__") or _coconut.isinstance(iterable, (_coconut.list, _coconut.tuple)):
            return _coconut.object.__new__(cls)
        return _coconut.reversed(iterable)
    def __init__(self, iterable):
        self.iter = iterable
    def __iter__(self):
        return _coconut.iter(_coconut.reversed(self.iter))
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return _coconut_igetitem(self.iter, _coconut.slice(-(index.start + 1) if index.start is not None else None, -(index.stop + 1) if index.stop else None, -(index.step if index.step is not None else 1)))
        return _coconut_igetitem(self.iter, -(index + 1))
    def __reversed__(self):
        return self.iter
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "reversed(%r)" % (self.iter,)
    def __hash__(self):
        return -_coconut.hash(self.iter)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(_coconut.copy.copy(self.iter))
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.iter == other.iter
    def __contains__(self, elem):
        return elem in self.iter
    def count(self, elem):
        """Count the number of times elem appears in the reversed iterator."""
        return self.iter.count(elem)
    def index(self, elem):
        """Find the index of elem in the reversed iterator."""
        return _coconut.len(self.iter) - self.iter.index(elem) - 1
    def __fmap__(self, func):
        return self.__class__(_coconut_map(func, self.iter))
class map(_coconut.map):
    __slots__ = ("func", "iters")
    if hasattr(_coconut.map, "__doc__"):
        __doc__ = _coconut.map.__doc__
    def __new__(cls, function, *iterables):
        new_map = _coconut.map.__new__(cls, function, *iterables)
        new_map.func = function
        new_map.iters = iterables
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, *(_coconut_igetitem(i, index) for i in self.iters))
        return self.func(*(_coconut_igetitem(i, index) for i in self.iters))
    def __reversed__(self):
        return self.__class__(self.func, *(_coconut_reversed(i) for i in self.iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "map(%r, %s)" % (self.func, ", ".join((_coconut.repr(i) for i in self.iters)))
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.iters)
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(self.func, *_coconut.map(_coconut.copy.copy, self.iters))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), *self.iters)
class parallel_map(map):
    """Multi-process implementation of map using concurrent.futures.
    Requires arguments to be pickleable."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor() as executor:
            return _coconut.iter(_coconut.list(executor.map(self.func, *self.iters)))
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(map):
    """Multi-thread implementation of map using concurrent.futures."""
    __slots__ = ()
    def __iter__(self):
        from concurrent.futures import ThreadPoolExecutor
        from multiprocessing import cpu_count  # cpu_count() * 5 is the default Python 3.5 thread count
        with ThreadPoolExecutor(cpu_count() * 5) as executor:
            return _coconut.iter(_coconut.list(executor.map(self.func, *self.iters)))
    def __repr__(self):
        return "concurrent_" + _coconut_map.__repr__(self)
class filter(_coconut.filter):
    __slots__ = ("func", "iter")
    if hasattr(_coconut.filter, "__doc__"):
        __doc__ = _coconut.filter.__doc__
    def __new__(cls, function, iterable):
        new_filter = _coconut.filter.__new__(cls, function, iterable)
        new_filter.func = function
        new_filter.iter = iterable
        return new_filter
    def __reversed__(self):
        return self.__class__(self.func, _coconut_reversed(self.iter))
    def __repr__(self):
        return "filter(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(self.func, _coconut.copy.copy(self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip(_coconut.zip):
    __slots__ = ("iters",)
    if hasattr(_coconut.zip, "__doc__"):
        __doc__ = _coconut.zip.__doc__
    def __new__(cls, *iterables):
        new_zip = _coconut.zip.__new__(cls, *iterables)
        new_zip.iters = iterables
        return new_zip
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(*(_coconut_igetitem(i, index) for i in self.iters))
        return _coconut.tuple(_coconut_igetitem(i, index) for i in self.iters)
    def __reversed__(self):
        return self.__class__(*(_coconut_reversed(i) for i in self.iters))
    def __len__(self):
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip(%s)" % (", ".join((_coconut.repr(i) for i in self.iters)),)
    def __reduce__(self):
        return (self.__class__, self.iters)
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(*_coconut.map(_coconut.copy.copy, self.iters))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class enumerate(_coconut.enumerate):
    __slots__ = ("iter", "start")
    if hasattr(_coconut.enumerate, "__doc__"):
        __doc__ = _coconut.enumerate.__doc__
    def __new__(cls, iterable, start=0):
        new_enumerate = _coconut.enumerate.__new__(cls, iterable, start)
        new_enumerate.iter = iterable
        new_enumerate.start = start
        return new_enumerate
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(_coconut_igetitem(self.iter, index), self.start + (0 if index.start is None else index.start if index.start >= 0 else len(self.iter) + index.start))
        return (self.start + index, _coconut_igetitem(self.iter, index))
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "enumerate(%r, %r)" % (self.iter, self.start)
    def __reduce__(self):
        return (self.__class__, (self.iter, self.start))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(_coconut.copy.copy(self.iter), self.start)
    def __fmap__(self, func):
        return _coconut_map(func, self)
class count(object):
    """count(start, step) returns an infinite iterator starting at start and increasing by step.
    If step is set to 0, count will infinitely repeat its first argument."""
    __slots__ = ("start", "step")
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
    def __iter__(self):
        while True:
            yield self.start
            if self.step:
                self.start += self.step
    def __contains__(self, elem):
        if not self.step:
            return elem == self.start
        if elem < self.start:
            return False
        return (elem - self.start) % self.step == 0
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice) and (index.start is None or index.start >= 0) and (index.stop is None or index.stop >= 0):
            new_start, new_step = self.start, self.step
            if self.step and index.start is not None:
                new_start += self.step * index.start
            if self.step and index.step is not None:
                new_step *= index.step
            if index.stop is None:
                return self.__class__(new_start, new_step)
            if self.step and _coconut.isinstance(self.start, _coconut.int) and _coconut.isinstance(self.step, _coconut.int):
                return _coconut.range(new_start, self.start + self.step * index.stop, new_step)
            return _coconut_map(self.__getitem__, _coconut.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
        if index < 0:
            raise _coconut.IndexError("count indices must be positive")
        return self.start + self.step * index if self.step else self.start
    def count(self, elem):
        """Count the number of times elem appears in the count."""
        if not self.step:
            return _coconut.float("inf") if elem == self.start else 0
        return int(elem in self)
    def index(self, elem):
        """Find the index of elem in the count."""
        if elem not in self:
            raise _coconut.ValueError(_coconut.repr(elem) + " not in " + _coconut.repr(self))
        return (elem - self.start) // self.step if self.step else 0
    def __reversed__(self):
        if not self.step:
            return self
        raise _coconut.TypeError(repr(self) + " object is not reversible")
    def __repr__(self):
        return "count(%r, %r)" % (self.start, self.step)
    def __hash__(self):
        return _coconut.hash((self.start, self.step))
    def __reduce__(self):
        return (self.__class__, (self.start, self.step))
    def __copy__(self):
        return self.__class__(self.start, self.step)
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.start == other.start and self.step == other.step
    def __fmap__(self, func):
        return _coconut_map(func, self)
class groupsof(object):
    """groupsof(n, iterable) splits iterable into groups of size n.
    If the length of the iterable is not divisible by n, the last group may be of size < n."""
    __slots__ = ("group_size", "iter")
    def __init__(self, n, iterable):
        self.iter = iterable
        try:
            self.group_size = _coconut.int(n)
        except _coconut.ValueError:
            raise _coconut.TypeError("group size must be an int; not %r" % (n,))
        if self.group_size <= 0:
            raise _coconut.ValueError("group size must be > 0; not %r" % (self.group_size,))
    def __iter__(self):
        iterator = _coconut.iter(self.iter)
        loop = True
        while loop:
            group = []
            for _ in _coconut.range(self.group_size):
                try:
                    group.append(_coconut.next(iterator))
                except _coconut.StopIteration:
                    loop = False
                    break
            if group:
                yield _coconut.tuple(group)
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "groupsof(%r)" % (self.iter,)
    def __reduce__(self):
        return (self.__class__, (self.group_size, self.iter))
    def __copy__(self):
        return self.__class__(self.group_size, _coconut.copy.copy(self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class recursive_iterator(object):
    """Decorator that optimizes a function for iterator recursion."""
    __slots__ = ("func", "tee_store", "backup_tee_store")
    def __init__(self, func):
        self.func = func
        self.tee_store = {}
        self.backup_tee_store = []
    def __call__(self, *args, **kwargs):
        key = (args, _coconut.frozenset(kwargs))
        use_backup = False
        try:
            hash(key)
        except _coconut.Exception:
            try:
                key = _coconut.pickle.dumps(key, -1)
            except _coconut.Exception:
                use_backup = True
        if use_backup:
            for i, (k, v) in _coconut.enumerate(self.backup_tee_store):
                if k == key:
                    to_tee, store_pos = v, i
                    break
            else:  # no break
                to_tee = self.func(*args, **kwargs)
                store_pos = None
            to_store, to_return = _coconut_tee(to_tee)
            if store_pos is None:
                self.backup_tee_store.append([key, to_store])
            else:
                self.backup_tee_store[store_pos][1] = to_store
        else:
            self.tee_store[key], to_return = _coconut_tee(self.tee_store.get(key) or self.func(*args, **kwargs))
        return to_return
    def __repr__(self):
        return "@recursive_iterator(" + _coconut.repr(self.func) + ")"
    def __reduce__(self):
        return (self.__class__, (self.func,))
    def __get__(self, obj, objtype=None):
        return _coconut.functools.partial(self, obj)
class _coconut_FunctionMatchErrorContext(object):
    __slots__ = ('exc_class', 'taken')
    threadlocal_var = _coconut.threading.local()
    def __init__(self, exc_class):
        self.exc_class = exc_class
        self.taken = False
    def __enter__(self):
        try:
            self.threadlocal_var.contexts.append(self)
        except _coconut.AttributeError:
            self.threadlocal_var.contexts = [self]
    def __exit__(self, type, value, traceback):
        self.threadlocal_var.contexts.pop()
    @classmethod
    def get(cls):
        try:
            ctx = cls.threadlocal_var.contexts[-1]
        except (_coconut.AttributeError, _coconut.IndexError):
            return _coconut_MatchError
        if not ctx.taken:
            ctx.taken = True
            return ctx.exc_class
        return _coconut_MatchError
_coconut_get_function_match_error = _coconut_FunctionMatchErrorContext.get
class _coconut_base_pattern_func(object):
    __slots__ = ("FunctionMatchError", "__doc__", "patterns")
    def __init__(self, *funcs):
        self.FunctionMatchError = _coconut.type(_coconut_str("MatchError"), (_coconut_MatchError,), {})
        self.__doc__ = None
        self.patterns = []
        for func in funcs:
            self.add(func)
    def add(self, func):
        self.__doc__ = _coconut.getattr(func, "__doc__", None) or self.__doc__
        if _coconut.isinstance(func, _coconut_base_pattern_func):
            self.patterns += func.patterns
        else:
            self.patterns.append(func)
    def __call__(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return self.patterns[-1](*args, **kwargs)
    def _coconut_tco_func(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return _coconut_tail_call(self.patterns[-1], *args, **kwargs)
    def __repr__(self):
        return "addpattern(" + _coconut.repr(self.patterns[0]) + ")(*" + _coconut.repr(self.patterns[1:]) + ")"
    def __reduce__(self):
        return (self.__class__, _coconut.tuple(self.patterns))
    def __get__(self, obj, objtype=None):
        return _coconut.functools.partial(self, obj)
def addpattern(base_func):
    """Decorator to add a new case to a pattern-matching function,
    where the new case is checked last."""
    return _coconut.functools.partial(_coconut_base_pattern_func, base_func)
_coconut_addpattern = addpattern
def prepattern(base_func):
    """DEPRECATED: Use addpattern instead."""
    def pattern_prepender(func):
        return addpattern(func)(base_func)
    return pattern_prepender
class _coconut_partial(object):
    __slots__ = ("func", "_argdict", "_arglen", "_stargs", "keywords")
    if hasattr(_coconut.functools.partial, "__doc__"):
        __doc__ = _coconut.functools.partial.__doc__
    def __init__(self, func, argdict, arglen, *args, **kwargs):
        self.func = func
        self._argdict = argdict
        self._arglen = arglen
        self._stargs = args
        self.keywords = kwargs
    def __reduce__(self):
        return (self.__class__, (self.func, self._argdict, self._arglen) + self._stargs, self.keywords)
    def __setstate__(self, keywords):
        self.keywords = keywords
    @property
    def args(self):
        return _coconut.tuple(self._argdict.get(i) for i in _coconut.range(self._arglen)) + self._stargs
    def __call__(self, *args, **kwargs):
        callargs = []
        argind = 0
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                callargs.append(self._argdict[i])
            elif argind >= _coconut.len(args):
                raise _coconut.TypeError("expected at least " + _coconut.str(self._arglen - _coconut.len(self._argdict)) + " argument(s) to " + _coconut.repr(self))
            else:
                callargs.append(args[argind])
                argind += 1
        callargs += self._stargs
        callargs += args[argind:]
        kwargs.update(self.keywords)
        return self.func(*callargs, **kwargs)
    def __repr__(self):
        args = []
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                args.append(_coconut.repr(self._argdict[i]))
            else:
                args.append("?")
        for arg in self._stargs:
            args.append(_coconut.repr(arg))
        return _coconut.repr(self.func) + "$(" + ", ".join(args) + ")"
def consume(iterable, keep_last=0):
    """consume(iterable, keep_last) fully exhausts iterable and return the last keep_last elements."""
    return _coconut.collections.deque(iterable, maxlen=keep_last)
class starmap(_coconut.itertools.starmap):
    __slots__ = ("func", "iter")
    if hasattr(_coconut.itertools.starmap, "__doc__"):
        __doc__ = _coconut.itertools.starmap.__doc__
    def __new__(cls, function, iterable):
        new_map = _coconut.itertools.starmap.__new__(cls, function, iterable)
        new_map.func = function
        new_map.iter = iterable
        return new_map
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, _coconut_igetitem(self.iter, index))
        return self.func(*_coconut_igetitem(self.iter, index))
    def __reversed__(self):
        return self.__class__(self.func, *_coconut_reversed(self.iter))
    def __len__(self):
        return _coconut.len(self.iter)
    def __repr__(self):
        return "starmap(%r, %r)" % (self.func, self.iter)
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __copy__(self):
        return self.__class__(self.func, _coconut.copy.copy(self.iter))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), self.iter)
def makedata(data_type, *args):
    """Construct an object of the given data_type containing the given arguments."""
    if _coconut.hasattr(data_type, "_make") and _coconut.issubclass(data_type, _coconut.tuple):
        return data_type._make(args)
    if _coconut.issubclass(data_type, (_coconut.map, _coconut.range, _coconut.abc.Iterator)):
        return args
    if _coconut.issubclass(data_type, _coconut.str):
        return "".join(args)
    return data_type(args)
def datamaker(data_type):
    """DEPRECATED: Use makedata instead."""
    return _coconut.functools.partial(makedata, data_type)
def fmap(func, obj):
    """fmap(func, obj) creates a copy of obj with func applied to its contents.
    Override by defining obj.__fmap__(func)."""
    if _coconut.hasattr(obj, "__fmap__"):
        return obj.__fmap__(func)
    if obj.__class__.__module__ == "numpy":
        from numpy import vectorize
        return vectorize(func)(obj)
    return _coconut_makedata(obj.__class__, *(_coconut_starmap(func, obj.items()) if _coconut.isinstance(obj, _coconut.abc.Mapping) else _coconut_map(func, obj)))
def memoize(maxsize=None, *args, **kwargs):
    """Decorator that memoizes a function,
    preventing it from being recomputed if it is called multiple times with the same arguments."""
    return _coconut.functools.lru_cache(maxsize, *args, **kwargs)
_coconut_MatchError, _coconut_count, _coconut_enumerate, _coconut_makedata, _coconut_map, _coconut_reversed, _coconut_starmap, _coconut_tee, _coconut_zip, TYPE_CHECKING, reduce, takewhile, dropwhile = MatchError, count, enumerate, makedata, map, reversed, starmap, tee, zip, False, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile

# Compiled Coconut: -----------------------------------------------------------

from datetime import datetime
import hashlib
import os
from os.path import basename
from os.path import exists
from os.path import normpath
import subprocess
sys = _coconut_sys
from typing import Sequence

from crontab import CronTab

default_out_path = 'output'
out_path = (lambda _coconut_none_coalesce_item: default_out_path if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(os.environ.get('BACKUP_OUTPUT_PATH'))
debug_mode = (lambda x: int(x))((lambda _coconut_none_coalesce_item: '0' if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(os.environ.get('BACKUP_DEBUG')))
cron_slices_str = os.environ.get('BACKUP_CRON_SLICE')
cron_force = os.environ.get('BACKUP_FORCE')

file_no_ext = lambda x: basename(x).split('.')[0]
first = lambda y: y[0] if isinstance(y, Sequence) else y
is_pair = lambda y: True if isinstance(y, Sequence) and len(y) == 2 else False
is_singleton = lambda y: True if isinstance(y, Sequence) and len(y) == 1 else False
fingerprint = lambda y: hashlib.sha256(y.encode('utf-8')).hexdigest()

def help_content():
    (print)("Usage: {_coconut_format_0}: [options...] <paths>".format(_coconut_format_0=(__file__)))
    (print)("\t-v, --verbose\tEnable debug mode (ENV VAR: BACKUP_DEBUG). -v -v for very verbose.")
    (print)("\t-h, --help\tDisplay this info")
    (print)("\t-o, --output <path>\tThe directory to copy paths to. (ENV VAR: BACKUP_OUTPUT_PATH)")
    (print)("\t-c, --cron <tab definition>\tThe cron 'm h dom mon dow' e.g. '0 * * * *' (ENV VAR: BACKUP_CRON_SLICE)")
    (print)("\t-f, --force\tOverride existing cron job if conflict (ENV VAR: BACKUP_FORCE).")
    sys.exit(1)


def parse_boolean_args(args  # type: Sequence
    ):
# type: (...) -> list
    """Set boolean flags and parse them out of args."""
    clean_args = []
    for arg in args:
        _coconut_match_to = arg
        _coconut_case_check_0 = False
        if _coconut_match_to == "-v":
            _coconut_case_check_0 = True
        if (not _coconut_case_check_0) and (_coconut_match_to == "--verbose"):
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            global debug_mode
            debug_mode += 1
        if not _coconut_case_check_0:
            if _coconut_match_to == "-h":
                _coconut_case_check_0 = True
            if (not _coconut_case_check_0) and (_coconut_match_to == "--help"):
                _coconut_case_check_0 = True
            if _coconut_case_check_0:
                help_content()
        if not _coconut_case_check_0:
            if _coconut_match_to == '-f':
                _coconut_case_check_0 = True
            if (not _coconut_case_check_0) and (_coconut_match_to == '--force'):
                _coconut_case_check_0 = True
            if _coconut_case_check_0:
                global cron_force
                cron_force = True
        if not _coconut_case_check_0:
            clean_args.append(arg)
    return clean_args


def parse_arg(arg_pair  # type: Sequence
    ):
# type: (...) -> bool
    """Check if arg pair is an option and sets it."""
    if is_singleton(arg_pair):
        arg_pair = (arg_pair[0], None)
    name, value = arg_pair
    _coconut_match_to = name
    _coconut_case_check_1 = False
    if _coconut_match_to == "-o":
        _coconut_case_check_1 = True
    if (not _coconut_case_check_1) and (_coconut_match_to == "--output"):
        _coconut_case_check_1 = True
    if _coconut_case_check_1:
        global out_path
        if out_path == default_out_path:
            out_path = value
        return True
    if not _coconut_case_check_1:
        if _coconut_match_to == "-c":
            _coconut_case_check_1 = True
        if (not _coconut_case_check_1) and (_coconut_match_to == "--cron"):
            _coconut_case_check_1 = True
        if _coconut_case_check_1:
            global cron_slices_str
            cron_slices_str = value
            return True
    return False


@_coconut_tco
def log(s  # type: str
    ):
    return _coconut_tail_call((print), *(str(datetime.utcnow()) + ':', s))
def debug(s,  # type: str
     min_weight=1  # type: int
    ):
    if debug_mode >= min_weight:
        (log)("DEBUG: " + s)
@_coconut_tco
def error(s  # type: str
    ):
    return _coconut_tail_call(log, "ERROR: " + s)

def main():
# Remove file name from args
    args = (list)((reversed)((list)(takewhile(lambda x: file_no_ext(x) != file_no_ext(__file__), reversed(sys.argv)))))
# Remove boolean flags from args
    args = (parse_boolean_args)(args)
# Group args in pairs, parse args and remove any options from the args
    paths_to_backup = (list)(filter(lambda x: x if not parse_arg(x) else None, groupsof(2, args)))
# Flatten (the paths will still be grouped)
    paths_to_backup = [path for paths in paths_to_backup for path in paths]

# Create the output directory if needed
    os.path.isdir(out_path) or os.mkdir(out_path)

    (debug)(*('paths_to_backup: ' + repr(paths_to_backup), 2))
    (debug)(*('output: {_coconut_format_0}'.format(_coconut_format_0=(out_path)), 2))
    (debug)(*('force: {_coconut_format_0}'.format(_coconut_format_0=(cron_force)), 2))
    (debug)(*('cron: {_coconut_format_0}'.format(_coconut_format_0=(cron_slices_str)), 2))

    for path in paths_to_backup:
        if not exists(path):
            (error)("{_coconut_format_0} does not exist!".format(_coconut_format_0=(path)))
            continue
        if os.path.isdir(path):
            out_file_name = ((list)(dropwhile(lambda x: len(x) == 0, (reversed)(path.split("/")))))[0]
        else:
            out_file_name = basename(path)
        rsync_args = ["rsync", "-avz", normpath(path), normpath("{_coconut_format_0}/{_coconut_format_1}".format(_coconut_format_0=(out_path), _coconut_format_1=(out_file_name)))]
        (debug)("EXEC CMD: {_coconut_format_0}".format(_coconut_format_0=(' '.join(rsync_args))))
        (debug)(subprocess.check_output(rsync_args, stderr=subprocess.STDOUT).decode('utf-8'))

        if cron_slices_str:
            user_cron = CronTab(user=True)
            cmd = " ".join(rsync_args)
            (debug)(*("Existing cron jobs: {_coconut_format_0}".format(_coconut_format_0=(repr(user_cron.crons))), 2))
# If task already exists
            try:
                job = _coconut_igetitem((_coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: user_cron.find_comment(fingerprint(cmd)), lambda: user_cron.find_command(cmd))))), 0)
                if job:
                    if cron_force:
                        (debug)("Cron job already exists... DELETING {_coconut_format_0})".format(_coconut_format_0=(job.comment)))
                        user_cron.remove(job)
                    else:
                        (error)("Cron job already exists for {_coconut_format_0}!".format(_coconut_format_0=(cmd)))
                        continue
            except StopIteration:
                pass
            job = (user_cron.new)(**{'command': cmd, 'comment': fingerprint(cmd)})
            job.setall(cron_slices_str)
            if not job.is_valid:
                (error)("Cannot create cron job!: {_coconut_format_0}".format(_coconut_format_0=(repr(job))))
            else:
                (debug)("Creating cron job: {_coconut_format_0}".format(_coconut_format_0=(job)))
                user_cron.write()

if __name__ == "__main__":
    main()
