#line 1 "scipy/signal/correlate_nd.c.src"

/*
 *****************************************************************************
 **       This file was autogenerated from a template  DO NOT EDIT!!!!      **
 **       Changes should be made to the original source (.src) file         **
 *****************************************************************************
 */

#line 1
/*
 * vim:syntax=c
 * vim:sw=4
 */
#include <Python.h>
#define PY_ARRAY_UNIQUE_SYMBOL _scipy_signal_ARRAY_API
#define NO_IMPORT_ARRAY
#include <numpy/noprefix.h>

#include "sigtools.h"

enum {
    CORR_MODE_VALID=0,
    CORR_MODE_SAME,
    CORR_MODE_FULL
};

static int _correlate_nd_imp(PyArrayIterObject* x, PyArrayIterObject *y,
        PyArrayIterObject *z, int typenum, int mode);

PyObject *
scipy_signal_sigtools_correlateND(PyObject *NPY_UNUSED(dummy), PyObject *args)
{
    PyObject *x, *y, *out;
    PyArrayObject *ax, *ay, *aout;
    PyArrayIterObject *itx, *ity, *itz;
    int mode, typenum, st;

    if (!PyArg_ParseTuple(args, "OOOi", &x, &y, &out, &mode)) {
        return NULL;
    }

    typenum = PyArray_ObjectType(x, 0);
    typenum = PyArray_ObjectType(y, typenum);
    typenum = PyArray_ObjectType(out, typenum);

    ax = (PyArrayObject *)PyArray_FromObject(x, typenum, 0, 0);
    if (ax == NULL) {
        return NULL;
    }

    ay = (PyArrayObject *)PyArray_FromObject(y, typenum, 0, 0);
    if (ay == NULL) {
        goto clean_ax;
    }

    aout = (PyArrayObject *)PyArray_FromObject(out, typenum, 0, 0);
    if (aout == NULL) {
        goto clean_ay;
    }

    if (ax->nd != ay->nd) {
        PyErr_SetString(PyExc_ValueError,
                "Arrays must have the same number of dimensions.");
        goto clean_aout;
    }

    if (ax->nd == 0) {
        PyErr_SetString(PyExc_ValueError, "Cannot convolve zero-dimensional arrays.");
        goto clean_aout;
    }

    itx = (PyArrayIterObject*)PyArray_IterNew((PyObject*)ax);
    if (itx == NULL) {
        goto clean_aout;
    }
    ity = (PyArrayIterObject*)PyArray_IterNew((PyObject*)ay);
    if (ity == NULL) {
        goto clean_itx;
    }
    itz = (PyArrayIterObject*)PyArray_IterNew((PyObject*)aout);
    if (itz == NULL) {
        goto clean_ity;
    }

    st = _correlate_nd_imp(itx, ity, itz, typenum, mode);
    if (st) {
        goto clean_itz;
    }

    Py_DECREF(itz);
    Py_DECREF(ity);
    Py_DECREF(itx);

    Py_DECREF(ax);
    Py_DECREF(ay);

    return PyArray_Return(aout);

clean_itz:
    Py_DECREF(itz);
clean_ity:
    Py_DECREF(ity);
clean_itx:
    Py_DECREF(itx);
clean_aout:
    Py_DECREF(aout);
clean_ay:
    Py_DECREF(ay);
clean_ax:
    Py_DECREF(ax);
    return NULL;
}

/*
 * Implementation of the type-specific correlation 'kernels'
 */

#line 115

static int _imp_correlate_nd_ubyte(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    ubyte acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((ubyte*)(curneighx->dataptr)) * *((ubyte*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((ubyte*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_byte(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    byte acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((byte*)(curneighx->dataptr)) * *((byte*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((byte*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_ushort(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    ushort acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((ushort*)(curneighx->dataptr)) * *((ushort*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((ushort*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_short(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    short acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((short*)(curneighx->dataptr)) * *((short*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((short*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_uint(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    uint acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((uint*)(curneighx->dataptr)) * *((uint*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((uint*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_int(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    int acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((int*)(curneighx->dataptr)) * *((int*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((int*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_ulong(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    ulong acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((ulong*)(curneighx->dataptr)) * *((ulong*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((ulong*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_long(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    long acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((long*)(curneighx->dataptr)) * *((long*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((long*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_ulonglong(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    ulonglong acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((ulonglong*)(curneighx->dataptr)) * *((ulonglong*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((ulonglong*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_longlong(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    longlong acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((longlong*)(curneighx->dataptr)) * *((longlong*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((longlong*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_float(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    float acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((float*)(curneighx->dataptr)) * *((float*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((float*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_double(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    double acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((double*)(curneighx->dataptr)) * *((double*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((double*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 115

static int _imp_correlate_nd_longdouble(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    npy_intp i, j;
    npy_longdouble acc;

    for(i = 0; i < curx->size; ++i) {
        acc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            acc += *((npy_longdouble*)(curneighx->dataptr)) * *((npy_longdouble*)(ity->dataptr));

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        *((npy_longdouble*)(itz->dataptr)) = acc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}



#line 149

static int _imp_correlate_nd_cfloat(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    int i, j;
    float racc, iacc;
    float *ptr1, *ptr2;

    for(i = 0; i < curx->size; ++i) {
        racc = 0;
        iacc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            ptr1 = ((float*)(curneighx->dataptr));
            ptr2 = ((float*)(ity->dataptr));
            racc += ptr1[0] * ptr2[0] + ptr1[1] * ptr2[1];
            iacc += ptr1[1] * ptr2[0] - ptr1[0] * ptr2[1];

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        ((float*)(itz->dataptr))[0] = racc;
        ((float*)(itz->dataptr))[1] = iacc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 149

static int _imp_correlate_nd_cdouble(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    int i, j;
    double racc, iacc;
    double *ptr1, *ptr2;

    for(i = 0; i < curx->size; ++i) {
        racc = 0;
        iacc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            ptr1 = ((double*)(curneighx->dataptr));
            ptr2 = ((double*)(ity->dataptr));
            racc += ptr1[0] * ptr2[0] + ptr1[1] * ptr2[1];
            iacc += ptr1[1] * ptr2[0] - ptr1[0] * ptr2[1];

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        ((double*)(itz->dataptr))[0] = racc;
        ((double*)(itz->dataptr))[1] = iacc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}


#line 149

static int _imp_correlate_nd_clongdouble(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    int i, j;
    npy_longdouble racc, iacc;
    npy_longdouble *ptr1, *ptr2;

    for(i = 0; i < curx->size; ++i) {
        racc = 0;
        iacc = 0;
        PyArrayNeighborhoodIter_Reset(curneighx);
        for(j = 0; j < curneighx->size; ++j) {
            ptr1 = ((npy_longdouble*)(curneighx->dataptr));
            ptr2 = ((npy_longdouble*)(ity->dataptr));
            racc += ptr1[0] * ptr2[0] + ptr1[1] * ptr2[1];
            iacc += ptr1[1] * ptr2[0] - ptr1[0] * ptr2[1];

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }
        PyArrayNeighborhoodIter_Next(curx);

        ((npy_longdouble*)(itz->dataptr))[0] = racc;
        ((npy_longdouble*)(itz->dataptr))[1] = iacc;
        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    return 0;
}



static int _imp_correlate_nd_object(PyArrayNeighborhoodIterObject *curx,
        PyArrayNeighborhoodIterObject *curneighx, PyArrayIterObject *ity,
        PyArrayIterObject *itz)
{
    int i, j;
    PyObject *tmp, *tmp2;
    char *zero;
    PyArray_CopySwapFunc *copyswap = curx->ao->descr->f->copyswap;

    zero = PyArray_Zero(curx->ao);

    for(i = 0; i < curx->size; ++i) {
        PyArrayNeighborhoodIter_Reset(curneighx);
        copyswap(itz->dataptr, zero, 0, NULL);

        for(j = 0; j < curneighx->size; ++j) {
            /*
             * compute tmp2 = acc + x * y. Not all objects supporting the
             * number protocol support inplace operations, so we do it the most
             * straightfoward way.
             */
            tmp = PyNumber_Multiply(*((PyObject**)curneighx->dataptr),
                                    *((PyObject**)ity->dataptr));
            tmp2 = PyNumber_Add(*((PyObject**)itz->dataptr), tmp);
            Py_DECREF(tmp);

            /* Update current output item (acc) */
            Py_DECREF(*((PyObject**)itz->dataptr));
            *((PyObject**)itz->dataptr) = tmp2;

            PyArrayNeighborhoodIter_Next(curneighx);
            PyArray_ITER_NEXT(ity);
        }

        PyArrayNeighborhoodIter_Next(curx);

        PyArray_ITER_NEXT(itz);

        PyArray_ITER_RESET(ity);
    }

    PyDataMem_FREE(zero);

    return 0;
}

static int _correlate_nd_imp(PyArrayIterObject* itx, PyArrayIterObject *ity,
        PyArrayIterObject *itz, int typenum, int mode)
{
    PyArrayNeighborhoodIterObject *curneighx, *curx;
    npy_intp i, nz, nx;
    npy_intp bounds[NPY_MAXDIMS*2];

    /* Compute boundaries for the neighborhood iterator curx: curx is used to
     * traverse x directly, such as each point of the output is the
     * innerproduct of y with the neighborhood around curx */
    switch(mode) {
        case CORR_MODE_VALID:
            /* Only walk through the input points such as the correponding
             * output will not depend on 0 padding */
            for(i = 0; i < itx->ao->nd; ++i) {
                bounds[2*i] = ity->ao->dimensions[i] - 1;
                bounds[2*i+1] = itx->ao->dimensions[i] - 1;
            }
            break;
        case CORR_MODE_SAME:
            /* Only walk through the input such as the output will be centered
               relatively to the output as computed in the full mode */
            for(i = 0; i < itx->ao->nd; ++i) {
                nz = itx->ao->dimensions[i];
                /* Recover 'original' nx, before it was zero-padded */
                nx = nz - ity->ao->dimensions[i] + 1;
                if ((nz - nx) % 2 == 0) {
                    bounds[2*i] = (nz - nx) / 2;
                } else {
                    bounds[2*i] = (nz - nx - 1) / 2;
                }
                bounds[2*i+1] = bounds[2*i] + nx - 1;
            }
            break;
        case CORR_MODE_FULL:
            for(i = 0; i < itx->ao->nd; ++i) {
                bounds[2*i] = 0;
                bounds[2*i+1] = itx->ao->dimensions[i] - 1;
            }
            break;
        default:
            PyErr_BadInternalCall();
            return -1;
    }

    curx = (PyArrayNeighborhoodIterObject*)PyArray_NeighborhoodIterNew(itx,
            bounds, NPY_NEIGHBORHOOD_ITER_ZERO_PADDING, NULL);
    if (curx == NULL) {
        PyErr_SetString(PyExc_SystemError, "Could not create curx ?");
        return -1;
    }

    /* Compute boundaries for the neighborhood iterator: the neighborhood for x
       should have the same dimensions as y */
    for(i = 0; i < ity->ao->nd; ++i) {
        bounds[2*i] = -ity->ao->dimensions[i] + 1;
        bounds[2*i+1] = 0;
    }

    curneighx = (PyArrayNeighborhoodIterObject*)PyArray_NeighborhoodIterNew(
            (PyArrayIterObject*)curx, bounds, NPY_NEIGHBORHOOD_ITER_ZERO_PADDING, NULL);
    if (curneighx == NULL) {
        goto clean_curx;
    }

    switch(typenum) {
#line 303
        case PyArray_UBYTE:
            _imp_correlate_nd_ubyte(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_BYTE:
            _imp_correlate_nd_byte(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_USHORT:
            _imp_correlate_nd_ushort(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_SHORT:
            _imp_correlate_nd_short(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_UINT:
            _imp_correlate_nd_uint(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_INT:
            _imp_correlate_nd_int(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_ULONG:
            _imp_correlate_nd_ulong(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_LONG:
            _imp_correlate_nd_long(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_ULONGLONG:
            _imp_correlate_nd_ulonglong(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_LONGLONG:
            _imp_correlate_nd_longlong(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_FLOAT:
            _imp_correlate_nd_float(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_DOUBLE:
            _imp_correlate_nd_double(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_LONGDOUBLE:
            _imp_correlate_nd_longdouble(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_CFLOAT:
            _imp_correlate_nd_cfloat(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_CDOUBLE:
            _imp_correlate_nd_cdouble(curx, curneighx, ity, itz);
            break;

#line 303
        case PyArray_CLONGDOUBLE:
            _imp_correlate_nd_clongdouble(curx, curneighx, ity, itz);
            break;


        /* The object array case does not worth being optimized, since most of
           the cost is numerical operations, not iterators moving in this case ? */
        case NPY_OBJECT:
            _imp_correlate_nd_object(curx, curneighx, ity, itz);
            break;
        default:
            PyErr_SetString(PyExc_ValueError, "Unsupported type");
            goto clean_curneighx;
    }

    Py_DECREF((PyArrayIterObject*)curx);
    Py_DECREF((PyArrayIterObject*)curneighx);

    return 0;

clean_curneighx:
    Py_DECREF((PyArrayIterObject*)curneighx);
clean_curx:
    Py_DECREF((PyArrayIterObject*)curx);
    return -1;
}

