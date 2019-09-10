#!/usr/bin/env python3
from conans import ConanFile, CMake, tools
import os
import shutil


class PatchelfConan(ConanFile):
    name = "patchelf"
    version = "0.10"
    description = "A small utility to modify the dynamic linker and RPATH of ELF executables"
    url = "https://github.com/mmha/conan-patchelf"
    homepage = "https://nixos.org/patchelf.html"
    author = "Morris Hafner"
    license = "MIT"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt"
    settings = "os", "os_build", "arch", "arch_build"

    scm = {
        "type": "git",
        "url": "https://github.com/NixOS/patchelf.git",
        "revision": version
    }

    cmake = None
    def configure_cmake(self):
        if not self.cmake:
            self.cmake = CMake(self)
            self.cmake.configure()
        return self.cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.env_info.MANDIR.append(os.path.join(self.package_folder, "share", "man"))

    def pacakge_id(self):
        del self.info.settings.os
        del self.info.settings.arch
