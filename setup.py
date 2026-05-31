"""setup.py — only purpose is to build the _pkm_kernels C++ extension.

The project is otherwise hatchling/pyproject.toml driven (see pyproject.toml).
Adding setup.py alongside is the lightest-touch way to opt into a
torch.utils.cpp_extension build without rewriting the build backend.

Usage:
    python setup.py build_ext --inplace
        → drops src/mmllm/_pkm_kernels.cpython-*.so

Alternative (no setup.py change at all):
    Use torch.utils.cpp_extension.load() at import time. See note in
    _pkm_autograd.py. Pros: zero setup; .so cached under ~/.cache/torch_extensions.
    Cons: first import compiles (~15s); fragile under multi-process startup
    (workers race on the cache dir); harder to ship as a wheel.

We prefer setup.py for the spike because the train loop is multi-process
(Hogwild workers) and we want the .so committed-once, not race-compiled.
"""

from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension

EXT = CppExtension(
    name="mmllm._pkm_kernels",
    sources=["src/mmllm/_pkm_kernels.cpp"],
    extra_compile_args=[
        "-fopenmp",
        "-O3",
        "-march=native",
        "-std=c++17",
        "-Wall",
        # Silence the pybind11 deprecation noise that Torch's headers trip on
        # under -Wall; remove if/when we want full warnings.
        "-Wno-deprecated-declarations",
    ],
    extra_link_args=["-fopenmp"],
)

setup(
    name="mmllm-pkm-kernels",
    version="0.0.1",
    ext_modules=[EXT],
    cmdclass={"build_ext": BuildExtension},
    # Package metadata is in pyproject.toml; this setup.py only exists
    # to wire the C++ extension build into the standard distutils flow.
    zip_safe=False,
)
