from lief import *
from ctypes import *
import logging

log = logging.getLogger(__name__)

class EmptyElf64(Structure):
    _fields_ = [
        # Header
        ("e_ident", c_char * 16),
        ("e_type", c_ushort),
        ("e_machine", c_ushort),
        ("e_version", c_uint),
        ("e_entry", c_ulonglong),
        ("e_phoff", c_ulonglong),
        ("e_shoff", c_ulonglong),
        ("e_flags", c_uint),
        ("e_ehsize", c_ushort),
        ("e_phentsize", c_ushort),
        ("e_phnum", c_ushort),
        ("e_shentsize", c_ushort),
        ("e_shnum", c_ushort),
        ("e_shstrndx", c_ushort),
    ]

    def __init__(self):
        log.info(f"CTOR EmptyElf64")
        Structure.__init__(self,
                b'\x7fELF\x02\x01\x01',
                #0x2, # type EXECUTABLE cause a segfault when build
                0x3, # type DYNAMIC
                0x3e, # machine
                0x01, # version
                0x67d0, # entry
                0x40, # phoff
                0, # section header None
                0, # flags
                0x40, # head size
                0x38, # prog head size
                0x0, # num prog head
                0x40, # section head size
                0, # num section head
                0, # section name table idx
                )
