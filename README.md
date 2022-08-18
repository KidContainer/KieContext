# Kie Context

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Kidsunbo/KieContext/CMake?label=CI%20Build&logo=github&style=flat-square)](https://github.com/Kidsunbo/KieContext/actions/workflows/CMake.yml)
[![Codecov](https://img.shields.io/codecov/c/github/Kidsunbo/KieContext?style=flat-square)](https://app.codecov.io/gh/Kidsunbo/KieContext)
[![C++](https://img.shields.io/badge/C%2B%2B-20-brightgreen?style=flat-square&logo=cplusplus)](https://isocpp.org)
[![This version of 'kie_context' @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/kie/kies/conan/kie_context/0.1.0/xc=_;xp=_/?render=true)](https://cloudsmith.io/~kie/repos/kies/packages/detail/conan/kie_context/0.1.0/xc=_;xp=_/)
[![GitHub](https://img.shields.io/github/license/Kidsunbo/KieContext?style=flat-square)](https://opensource.org/licenses/MIT)


This project is a wrapper for bunch of `boost::asio::io_context`. It follow the per context per thread model.

## This project has been merged into [kie_toolbox_cpp](https://github.com/Kidsunbo/kie_toolbox_cpp).

## Usage
It's easy to use this project with conan.

First add a new repository to you conan.
```
conan remote add kie-kies https://conan.cloudsmith.io/kie/kies/
```

then add
```
kie_context/0.1.0
```
to your `conanfile.txt`

After that, feel free to use it.
