#include <Python.h>

static PyObject *foo_bar(PyObject *self) {
	/* Do something interesting here. */
	Py_RETURN_NONE;
}

static PyObject *foo_baz(PyObject *self, PyObject *args) {
	int     i;
	double  d;
	char   *s;
	int     i2 = 4;
	double  d2 = 5.0;
	char   *s2 = "six";
	if (!PyArg_ParseTuple(args, "ids|ids", &i, &d, &s, &i2, &d2, &s2)) {
		return NULL;
	}
	/* Do something interesting here. */
	Py_RETURN_NONE;
}

static PyObject *foo_quux(PyObject *self, PyObject *args, PyObject *kw) {
	char *kwlist[] = { "i", "d", "s", NULL };
	int     i;
	double  d = 2.0;
	char   *s = "three";
	if (!PyArg_ParseTupleAndKeywords(args, kw, "i|ds", kwlist, &i, &d, &s)) {
	       return NULL;
	}
	/* Do something interesting here. */
	Py_RETURN_NONE;
}

static PyObject *foo_add(PyObject *self, PyObject *args) {
	int a;
	int b;
	if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
		return NULL;
	}
	return Py_BuildValue("i", a + b);
}

static PyObject *foo_add_and_subtract(PyObject *self, PyObject *args) {
	int a;
	int b;
	if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
		return NULL;
	}
	return Py_BuildValue("(ii)", a + b, a - b);
}

static PyMethodDef foo_methods[] = {
	{ "bar",  (PyCFunction)foo_bar, METH_NOARGS, NULL },
	{ "baz",  foo_baz, METH_VARARGS, NULL },
	{ "quux", (PyCFunction)foo_quux, METH_VARARGS|METH_KEYWORDS, NULL },
	{ "add",  foo_add, METH_VARARGS, NULL },
	{ "add_and_subtract",  foo_add_and_subtract, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initfoo() {
	Py_InitModule("foo", foo_methods);
}

