from conans import ConanFile, CMake, tools
import os


class TdConan(ConanFile):
    name = "tdlib"
    
    license = "BSL-1.0"
    author = "Infactum infactum@gmail.com"
    url = "https://github.com/Infactum/conan-tdlib"
    description = "TDLib (Telegram Database Library) is a cross-platform, fully functional Telegram client."
    topics = ("telegram")

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = ["CMakeLists.txt", "patches/*"]
    generators = "cmake"
    _source_subfolder = "source_subfolder"

    requires = (
        "openssl/1.1.1d",
        "zlib/1.2.11"
    )
    build_requires = "gperf/3.1"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename("td-%s" % (self.version), self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        for patch in self.conan_data["patches"][self.version]:
            tools.patch(**patch)
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
