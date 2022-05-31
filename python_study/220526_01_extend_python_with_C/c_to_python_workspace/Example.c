#include <Python.h>


int CfindPrimes(int num1, int num2)
{
    int flag_var, i, j;
    printf("The Prime numbers in (%d, %d) are:\n", num1, num2);

    for (i = num1 + 1; i < num2; ++i)
    {
        flag_var = 0;
        for (j = 2; j <= i/2; ++j)
        {
            if (i % j ==0)
            {
                flag_var = 1;
                break;
            }
        }
        if (flag_var == 0)
            printf("%d\n", i);
    }
    return 0;
}

static PyObject *findPrimes(PyObject *self, PyObject *args)
{
    int num1, num2, sts;


    if (!PyArg_ParseTuple(args, "il", &num1, %num2))
        return NULL
    sts = CfindPrimes(num1, num2)
    return PyLong_FromLong(sts);
}

static PyObject *version(PyObject *self)
{
    return Py_BuildValue("s", "Version 0.01");
}

static PyMethodDef Examples[] = {
    {"findPrimes", findPrimes, METH_VARAGS, "Calculates and aprints all prime number lower boudn ... "}
    {"version", (PyCFunction)version, METH_NOAGS, "Calculates and aprints all prime number lower boudn ... "}
    {}
}