# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_LeapPython', [dirname(__file__)])
        except ImportError:
            import _LeapPython
            return _LeapPython
        if fp is not None:
            try:
                _mod = imp.load_module('_LeapPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _LeapPython = swig_import_helper()
    del swig_import_helper
else:
    import _LeapPython
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _LeapPython.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _LeapPython.SwigPyIterator_value(self)
    def incr(self, n=1): return _LeapPython.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _LeapPython.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _LeapPython.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _LeapPython.SwigPyIterator_equal(self, *args)
    def copy(self): return _LeapPython.SwigPyIterator_copy(self)
    def next(self): return _LeapPython.SwigPyIterator_next(self)
    def __next__(self): return _LeapPython.SwigPyIterator___next__(self)
    def previous(self): return _LeapPython.SwigPyIterator_previous(self)
    def advance(self, *args): return _LeapPython.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _LeapPython.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _LeapPython.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _LeapPython.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _LeapPython.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _LeapPython.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _LeapPython.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _LeapPython.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class FingerArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FingerArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FingerArray, name)
    __repr__ = _swig_repr
    def iterator(self): return _LeapPython.FingerArray_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _LeapPython.FingerArray___nonzero__(self)
    def __bool__(self): return _LeapPython.FingerArray___bool__(self)
    def __len__(self): return _LeapPython.FingerArray___len__(self)
    def pop(self): return _LeapPython.FingerArray_pop(self)
    def __getslice__(self, *args): return _LeapPython.FingerArray___getslice__(self, *args)
    def __setslice__(self, *args): return _LeapPython.FingerArray___setslice__(self, *args)
    def __delslice__(self, *args): return _LeapPython.FingerArray___delslice__(self, *args)
    def __delitem__(self, *args): return _LeapPython.FingerArray___delitem__(self, *args)
    def __getitem__(self, *args): return _LeapPython.FingerArray___getitem__(self, *args)
    def __setitem__(self, *args): return _LeapPython.FingerArray___setitem__(self, *args)
    def append(self, *args): return _LeapPython.FingerArray_append(self, *args)
    def empty(self): return _LeapPython.FingerArray_empty(self)
    def size(self): return _LeapPython.FingerArray_size(self)
    def clear(self): return _LeapPython.FingerArray_clear(self)
    def swap(self, *args): return _LeapPython.FingerArray_swap(self, *args)
    def get_allocator(self): return _LeapPython.FingerArray_get_allocator(self)
    def begin(self): return _LeapPython.FingerArray_begin(self)
    def end(self): return _LeapPython.FingerArray_end(self)
    def rbegin(self): return _LeapPython.FingerArray_rbegin(self)
    def rend(self): return _LeapPython.FingerArray_rend(self)
    def pop_back(self): return _LeapPython.FingerArray_pop_back(self)
    def erase(self, *args): return _LeapPython.FingerArray_erase(self, *args)
    def __init__(self, *args): 
        this = _LeapPython.new_FingerArray(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _LeapPython.FingerArray_push_back(self, *args)
    def front(self): return _LeapPython.FingerArray_front(self)
    def back(self): return _LeapPython.FingerArray_back(self)
    def assign(self, *args): return _LeapPython.FingerArray_assign(self, *args)
    def resize(self, *args): return _LeapPython.FingerArray_resize(self, *args)
    def insert(self, *args): return _LeapPython.FingerArray_insert(self, *args)
    def reserve(self, *args): return _LeapPython.FingerArray_reserve(self, *args)
    def capacity(self): return _LeapPython.FingerArray_capacity(self)
    __swig_destroy__ = _LeapPython.delete_FingerArray
    __del__ = lambda self : None;
FingerArray_swigregister = _LeapPython.FingerArray_swigregister
FingerArray_swigregister(FingerArray)

class HandArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HandArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HandArray, name)
    __repr__ = _swig_repr
    def iterator(self): return _LeapPython.HandArray_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _LeapPython.HandArray___nonzero__(self)
    def __bool__(self): return _LeapPython.HandArray___bool__(self)
    def __len__(self): return _LeapPython.HandArray___len__(self)
    def pop(self): return _LeapPython.HandArray_pop(self)
    def __getslice__(self, *args): return _LeapPython.HandArray___getslice__(self, *args)
    def __setslice__(self, *args): return _LeapPython.HandArray___setslice__(self, *args)
    def __delslice__(self, *args): return _LeapPython.HandArray___delslice__(self, *args)
    def __delitem__(self, *args): return _LeapPython.HandArray___delitem__(self, *args)
    def __getitem__(self, *args): return _LeapPython.HandArray___getitem__(self, *args)
    def __setitem__(self, *args): return _LeapPython.HandArray___setitem__(self, *args)
    def append(self, *args): return _LeapPython.HandArray_append(self, *args)
    def empty(self): return _LeapPython.HandArray_empty(self)
    def size(self): return _LeapPython.HandArray_size(self)
    def clear(self): return _LeapPython.HandArray_clear(self)
    def swap(self, *args): return _LeapPython.HandArray_swap(self, *args)
    def get_allocator(self): return _LeapPython.HandArray_get_allocator(self)
    def begin(self): return _LeapPython.HandArray_begin(self)
    def end(self): return _LeapPython.HandArray_end(self)
    def rbegin(self): return _LeapPython.HandArray_rbegin(self)
    def rend(self): return _LeapPython.HandArray_rend(self)
    def pop_back(self): return _LeapPython.HandArray_pop_back(self)
    def erase(self, *args): return _LeapPython.HandArray_erase(self, *args)
    def __init__(self, *args): 
        this = _LeapPython.new_HandArray(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _LeapPython.HandArray_push_back(self, *args)
    def front(self): return _LeapPython.HandArray_front(self)
    def back(self): return _LeapPython.HandArray_back(self)
    def assign(self, *args): return _LeapPython.HandArray_assign(self, *args)
    def resize(self, *args): return _LeapPython.HandArray_resize(self, *args)
    def insert(self, *args): return _LeapPython.HandArray_insert(self, *args)
    def reserve(self, *args): return _LeapPython.HandArray_reserve(self, *args)
    def capacity(self): return _LeapPython.HandArray_capacity(self)
    __swig_destroy__ = _LeapPython.delete_HandArray
    __del__ = lambda self : None;
HandArray_swigregister = _LeapPython.HandArray_swigregister
HandArray_swigregister(HandArray)

class Interface(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Interface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Interface, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
Interface_swigregister = _LeapPython.Interface_swigregister
Interface_swigregister(Interface)

class Vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LeapPython.new_Vector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["x"] = _LeapPython.Vector_x_set
    __swig_getmethods__["x"] = _LeapPython.Vector_x_get
    if _newclass:x = _swig_property(_LeapPython.Vector_x_get, _LeapPython.Vector_x_set)
    __swig_setmethods__["y"] = _LeapPython.Vector_y_set
    __swig_getmethods__["y"] = _LeapPython.Vector_y_get
    if _newclass:y = _swig_property(_LeapPython.Vector_y_get, _LeapPython.Vector_y_set)
    __swig_setmethods__["z"] = _LeapPython.Vector_z_set
    __swig_getmethods__["z"] = _LeapPython.Vector_z_get
    if _newclass:z = _swig_property(_LeapPython.Vector_z_get, _LeapPython.Vector_z_set)
    __swig_destroy__ = _LeapPython.delete_Vector
    __del__ = lambda self : None;
Vector_swigregister = _LeapPython.Vector_swigregister
Vector_swigregister(Vector)

class Ray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LeapPython.new_Ray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["position"] = _LeapPython.Ray_position_set
    __swig_getmethods__["position"] = _LeapPython.Ray_position_get
    if _newclass:position = _swig_property(_LeapPython.Ray_position_get, _LeapPython.Ray_position_set)
    __swig_setmethods__["direction"] = _LeapPython.Ray_direction_set
    __swig_getmethods__["direction"] = _LeapPython.Ray_direction_get
    if _newclass:direction = _swig_property(_LeapPython.Ray_direction_get, _LeapPython.Ray_direction_set)
    __swig_destroy__ = _LeapPython.delete_Ray
    __del__ = lambda self : None;
Ray_swigregister = _LeapPython.Ray_swigregister
Ray_swigregister(Ray)

class Ball(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ball, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ball, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _LeapPython.new_Ball(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["position"] = _LeapPython.Ball_position_set
    __swig_getmethods__["position"] = _LeapPython.Ball_position_get
    if _newclass:position = _swig_property(_LeapPython.Ball_position_get, _LeapPython.Ball_position_set)
    __swig_setmethods__["radius"] = _LeapPython.Ball_radius_set
    __swig_getmethods__["radius"] = _LeapPython.Ball_radius_get
    if _newclass:radius = _swig_property(_LeapPython.Ball_radius_get, _LeapPython.Ball_radius_set)
    __swig_destroy__ = _LeapPython.delete_Ball
    __del__ = lambda self : None;
Ball_swigregister = _LeapPython.Ball_swigregister
Ball_swigregister(Ball)

class Finger(Interface):
    __swig_setmethods__ = {}
    for _s in [Interface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Finger, name, value)
    __swig_getmethods__ = {}
    for _s in [Interface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Finger, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def id(self): return _LeapPython.Finger_id(self)
    def tip(self): return _LeapPython.Finger_tip(self)
    def velocity(self): return _LeapPython.Finger_velocity(self)
    def width(self): return _LeapPython.Finger_width(self)
    def length(self): return _LeapPython.Finger_length(self)
    def isTool(self): return _LeapPython.Finger_isTool(self)
    __swig_destroy__ = _LeapPython.delete_Finger
    __del__ = lambda self : None;
Finger_swigregister = _LeapPython.Finger_swigregister
Finger_swigregister(Finger)

class Hand(Interface):
    __swig_setmethods__ = {}
    for _s in [Interface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Hand, name, value)
    __swig_getmethods__ = {}
    for _s in [Interface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Hand, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def id(self): return _LeapPython.Hand_id(self)
    def fingers(self): return _LeapPython.Hand_fingers(self)
    def palm(self): return _LeapPython.Hand_palm(self)
    def velocity(self): return _LeapPython.Hand_velocity(self)
    def normal(self): return _LeapPython.Hand_normal(self)
    def ball(self): return _LeapPython.Hand_ball(self)
    __swig_destroy__ = _LeapPython.delete_Hand
    __del__ = lambda self : None;
Hand_swigregister = _LeapPython.Hand_swigregister
Hand_swigregister(Hand)

class Frame(Interface):
    __swig_setmethods__ = {}
    for _s in [Interface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Frame, name, value)
    __swig_getmethods__ = {}
    for _s in [Interface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Frame, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def id(self): return _LeapPython.Frame_id(self)
    def timestamp(self): return _LeapPython.Frame_timestamp(self)
    def hands(self): return _LeapPython.Frame_hands(self)
    __swig_destroy__ = _LeapPython.delete_Frame
    __del__ = lambda self : None;
Frame_swigregister = _LeapPython.Frame_swigregister
Frame_swigregister(Frame)

class Config(Interface):
    __swig_setmethods__ = {}
    for _s in [Interface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Config, name, value)
    __swig_getmethods__ = {}
    for _s in [Interface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Config, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _LeapPython.new_Config()
        try: self.this.append(this)
        except: self.this = this
    TYPE_UNKNOWN = _LeapPython.Config_TYPE_UNKNOWN
    TYPE_BOOLEAN = _LeapPython.Config_TYPE_BOOLEAN
    TYPE_INT32 = _LeapPython.Config_TYPE_INT32
    TYPE_INT64 = _LeapPython.Config_TYPE_INT64
    TYPE_UINT32 = _LeapPython.Config_TYPE_UINT32
    TYPE_UINT64 = _LeapPython.Config_TYPE_UINT64
    TYPE_FLOAT = _LeapPython.Config_TYPE_FLOAT
    TYPE_DOUBLE = _LeapPython.Config_TYPE_DOUBLE
    TYPE_STRING = _LeapPython.Config_TYPE_STRING
    def type(self, *args): return _LeapPython.Config_type(self, *args)
    def getBool(self, *args): return _LeapPython.Config_getBool(self, *args)
    def getInt32(self, *args): return _LeapPython.Config_getInt32(self, *args)
    def getInt64(self, *args): return _LeapPython.Config_getInt64(self, *args)
    def getUInt32(self, *args): return _LeapPython.Config_getUInt32(self, *args)
    def getUInt64(self, *args): return _LeapPython.Config_getUInt64(self, *args)
    def getFloat(self, *args): return _LeapPython.Config_getFloat(self, *args)
    def getDouble(self, *args): return _LeapPython.Config_getDouble(self, *args)
    def getString(self, *args): return _LeapPython.Config_getString(self, *args)
    __swig_destroy__ = _LeapPython.delete_Config
    __del__ = lambda self : None;
Config_swigregister = _LeapPython.Config_swigregister
Config_swigregister(Config)

class Controller(Interface):
    __swig_setmethods__ = {}
    for _s in [Interface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Controller, name, value)
    __swig_getmethods__ = {}
    for _s in [Interface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Controller, name)
    __repr__ = _swig_repr
    def __init__(self, listener=None): 
        this = _LeapPython.new_Controller(listener)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _LeapPython.delete_Controller
    __del__ = lambda self : None;
    def frame(self, history=0): return _LeapPython.Controller_frame(self, history)
    def config(self): return _LeapPython.Controller_config(self)
    def listener(self): return _LeapPython.Controller_listener(self)
Controller_swigregister = _LeapPython.Controller_swigregister
Controller_swigregister(Controller)

class Listener(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Listener, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Listener, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _LeapPython.delete_Listener
    __del__ = lambda self : None;
    def onInit(self, *args): return _LeapPython.Listener_onInit(self, *args)
    def onConnect(self, *args): return _LeapPython.Listener_onConnect(self, *args)
    def onDisconnect(self, *args): return _LeapPython.Listener_onDisconnect(self, *args)
    def onFrame(self, *args): return _LeapPython.Listener_onFrame(self, *args)
    def __init__(self): 
        if self.__class__ == Listener:
            _self = None
        else:
            _self = self
        this = _LeapPython.new_Listener(_self, )
        try: self.this.append(this)
        except: self.this = this
    def __disown__(self):
        self.this.disown()
        _LeapPython.disown_Listener(self)
        return weakref_proxy(self)
Listener_swigregister = _LeapPython.Listener_swigregister
Listener_swigregister(Listener)

# This file is compatible with both classic and new-style classes.


