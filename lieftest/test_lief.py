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
    binempty.interpreter = "./lieftest/load_test"
    #null = ELF.Segment()
    #null.type = ELF.SEGMENT_TYPES.NULL
    #binempty.add(null, 0)
    code = [
            0xb8, 0x3c, 0x00, 0x00, 0x00, # mov EAX, 0x3c // SYSEXIT
            0xbf, 0x00, 0x00, 0x00, 0x00, # mov EDI, 0 // 0
            0x0f, 0x05, # syscall
            ]
    segment = ELF.Segment()
    segment.content = code
    segment.add(ELF.SEGMENT_FLAGS.R)
    segment.add(ELF.SEGMENT_FLAGS.X)
    segment.type = ELF.SEGMENT_TYPES.LOAD
    binempty.add(segment, base=0x400000)
    builder = ELF.Builder(binempty)
    builder.build()
    bin2 = ELF.parse(builder.get_build())
    log.info(f"BIN2 {bin2.header}")
    builder.write('test.x')
