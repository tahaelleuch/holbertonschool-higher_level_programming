#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject
*/
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i, len;

	list = (PyListObject *)p;
	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < len; i++)
		printf("Element %li: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
