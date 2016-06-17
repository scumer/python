# coding=utf-8

import barcode
from barcode.writer import ImageWriter

fp = open('barcode.png','w')

gen = barcode.get_barcode_class('code39')

writer_=ImageWriter()
options = {'text_distance':2}


ean = gen(u'A5901234123457', writer=writer_, add_checksum=False)

ean.write(fp, options)
#ean.save('code')

from StringIO import StringIO
io = StringIO()
ean.write(io, options)

print io.len

#print io.read()



from flask import make_response

def gen_barcode(code):
    from StringIO import StringIO
    import barcode

    try:
        code_class = barcode.get_barcode_class('code39')
        image_writer=barcode.writer.ImageWriter()
        code_generater = code_class(code, writer=image_writer, add_checksum=False)
        io = StringIO()
        options = {'text_distance': 2}
        code_generater.write(io, options)
        #response = make_response(io.read())
        #response.headers['content-Type'] = 'image/png'
        #return response
        print io.len
        return io.read()
    except Exception, e:
        print e

    return None

print gen_barcode('A5901234123457')


