import os
import qrcode


def txt_to_qrcode(txt, qr_filepath, qr_filetype='JPEG'):
    qr = qrcode.QRCode(version=1, box_size=2, border=4)
    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image()
    img_file = open(qr_filepath, 'wb')
    img.save(img_file, qr_filetype)
    img_file.close()


if __name__ == '__main__':
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_qr = os.path.join(cur_dir, 'qr_mysite.jpg')
    txt_to_qrcode("https://stm-labs.ru/ru/", path_to_qr)
    print(path_to_qr)