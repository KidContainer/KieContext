from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class KieContextConan(ConanFile):
    name = "kie_context"
    version = "0.1.0"

    # Optional metadata
    license = "MIT"
    author = "Kie <qiongxiaozi158@sina.com>"
    url = "https://github.com/Kidsunbo/KieContext"
    description = "A wrapper that make multiple context easy for use"
    topics = ("async", "context", "asio")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "include/*", "CMakeLists.txt", "LICENSE"
    no_copy_source = True

    requires = "boost/1.79.0"

    # This generator is only needed for testing
    generators = "CMakeToolchain", "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def package(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_id(self):
        self.info.clear()
