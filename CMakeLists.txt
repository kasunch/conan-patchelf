cmake_minimum_required(VERSION 3.1)
project(patchelf LANGUAGES CXX)

set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_VERBOSE_MAKEFILE ON)

include(GNUInstallDirs)

if(NOT CMAKE_CROSSCOMPILING)
	execute_process(COMMAND getconf PAGE_SIZE
		OUTPUT_VARIABLE system_page_size
		ERROR_STRIP_TRAILING_WHITESPACE)
endif()

if(NOT system_page_size)
	set(system_page_size 4096)
endif()

set(PATCHELF_PAGESIZE ${system_page_size} CACHE STRING "")

add_executable(patchelf src/elf.h src/patchelf.cc)
target_compile_definitions(patchelf
	PRIVATE
		_FILE_OFFSET_BITS=64
		PAGESIZE=${PATCHELF_PAGESIZE}
		PACKAGE_STRING="patchelf ${PROJECT_VERSION}"
)

install(TARGETS patchelf
	EXPORT patchelf-targets
	RUNTIME DESTINATION bin
)

install(FILES README
	DESTINATION ${CMAKE_INSTALL_DOCDIR})

install(FILES patchelf.1
	DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)
