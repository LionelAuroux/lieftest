from lief import *
from lieftest import lief_layer as ll
import logging

log = logging.getLogger(__name__)

def test_binary():
    log.info(f"COOL")
    lsbin = ELF.parse("/bin/ls")
    log.info(f"LS HEADER {lsbin.header}")
    head = ELF.Header()
    head.identity_class = ELF.ELF_CLASS.CLASS64
    head.identity_version = ELF.VERSION.CURRENT
    head.identity_data = ELF.ELF_DATA.LSB
    head.identity_os_abi = ELF.OS_ABI.SYSTEMV
    head.identity_abi_version = 0
    head.machine_type = ELF.ARCH.x86_64
    head.file_type = ELF.E_TYPE.DYNAMIC
    head.object_file_version = ELF.VERSION.CURRENT
    log.info(f"New Header {head}")
    log.info(f"TEST CTYPES ELF LAYER")
    empty = ll.EmptyElf64()
    bempty = bytes(empty)
    log.info(f"EMPTY {[hex(it) for it in bempty]}")
    binempty = ELF.parse([it for it in bempty])
    log.info(f"BINEMPTY {binempty.header}")
    binempty.interpreter = "./lieftest/load_test.py"
    builder = ELF.Builder(binempty)
    builder.build()
    bin2 = ELF.parse(builder.get_build())
    log.info(f"BIN2 {bin2.header}")
    builder.write('test.x')
