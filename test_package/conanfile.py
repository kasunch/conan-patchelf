#!/usr/bin/env python3

from conans import ConanFile, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch"

    def test(self):
        if tools.cross_building(self.settings):
            return

        bin_path = os.path.join("bin", "test_package")
        self.run("patchelf --help", run_environment=True)
        self.run("patchelf --version", run_environment=True)
