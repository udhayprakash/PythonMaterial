#include <Python.h>

#include <lame.h>

/* defined in clame.c */
int encode(char *, char *);

static PyObject *pylame1_encode(PyObject *self, PyObject *args) {
	int status;
	char *inpath;
	char *outpath;
	if (!PyArg_ParseTuple(args, "ss", &inpath, &outpath)) {
		return NULL;
	}
	status = encode(inpath, outpath);
	return Py_BuildValue("i", status);
}

static PyMethodDef pylame1_methods[] = {
	{ "encode", pylame1_encode, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initpylame1() {
	Py_InitModule3("pylame1", pylame1_methods, "My first LAME module.");
}

