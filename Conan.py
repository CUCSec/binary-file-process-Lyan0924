import struct


def tamper(student_id):
    change_num=54
    with open('lenna.bmp','r+b') as f:
        f.seek(change_num)
        for i in range(12):
            change_num+=int(student_id[i])*3
            if int(student_id[i]) == 0:
                change_num+=30
            f.seek(change_num)
            f.write(b'\x00\x00\x00')

def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
