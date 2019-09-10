#!/usr/bin/env python3
from conans import ConanFile, AutoToolsBuildEnvironment, tools
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
    exports = ["LICENSE.md"]
    settings = "os", "os_build", "arch", "arch_build"

    scm = {
        "type": "git",
        "url": "https://github.com/NixOS/patchelf.git",
        "revision": version
    }

    autotools = None
    def configure_autotools(self):
        if not self.autotools:
            self.run("autoreconf -fiv", win_bash=tools.os_info.is_windows)
            self.autotools = AutoToolsBuildEnvironment(
                self, win_bash=tools.os_info.is_windows)
            self.autotools.configure()
        return self.autotools

    def build(self):
        autotools = self.configure_autotools()
        autotools.make()

    def package(self):
        autotools = self.configure_autotools()
        autotools.install()

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.env_info.MANDIR.append(os.path.join(self.package_folder, "share", "man"))

    def pacakge_id(self):
        del self.info.settings.os
        del self.info.settings.arch
