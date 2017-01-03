# -*- coding: utf-8 -*-

import win32ui
import win32gui
import win32print
import win32con


def list_printers():
    return win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS, None, 5)


def list_source(name, port):
    return win32print.DeviceCapabilities(name, port, win32con.DC_BINS)


def print_texts(printer_server, doc_name, texts, x_scale=1, y_scale=1, left_offset=0, top_offset=0):
    handler = win32print.OpenPrinter(printer_server)
    printer_info = win32print.GetPrinter(handler, 2)
    dev_mode = printer_info['pDevMode']
    dev_mode.DefaultSource = win32con.DMBIN_ONLYONE

    dc = win32gui.CreateDC('WINSPOOL', printer_server, dev_mode)
    hdc = win32ui.CreateDCFromHandle(dc)
    hdc.StartDoc(doc_name)
    hdc.StartPage()

    for text in texts:
        hdc.TextOut(
            int(left_offset + x_scale * text[0]),
            int(top_offset + y_scale * text[1]),
            text[2]
        )

    hdc.EndPage()
    hdc.EndDoc()
    win32gui.DeleteDC(dc)


def print_data(printer_server, doc_name, data):
    print_texts(
        printer_server, doc_name,
        data[0], data[1], data[2], data[3], data[4]
    )


def print_axis(printer_server):
    axis = []
    for y in range(0, 34):
        axis.append([0, y * 100, str(y)])
    for x in range(0, 24):
        axis.append([x * 100, 0, str(x)])
    for y in range(100, 34 * 100, 100):
        for x in range(100, 24 * 100, 100):
            axis.append([x, y, '+'])
    print_texts(printer_server, 'axis', axis)


def format_data(content, template=None):
    texts = [
        [7, 5, content['name']],
        [8, 6, content['trFrom']],
        [15, 6, content['trTo']],
        [14, 7.5, content['year']],
        [16.5, 7.5, content['month']],
        [18, 7.5, content['day']],
        [3, 13, content['sendTo']],
        [4, 14, content['name']],
        [14, 14, content['age']],
        [17, 14, content['nation']],
        [14, 15, content['idCard']],
        [4, 16.5, content['trFrom']],
        [13, 16.5, content['trTo']],
        [14, 17.5, content['paidToYear']],
        [16.5, 17.5, content['paidToMonth']],
        [5.5, 18.5, content['validity']],
        [14, 20.5, content['year']],
        [16.5, 20.5, content['month']],
        [18, 20.5, content['day']]
    ]
    return [texts, 100, 100, 0, 0]


if __name__ == '__main__':
    printer_name = '\\\\MANJINGSERVER\\Lenovo M7206'
    printer_port = 'USB001'

    print(list_printers())
    print(list_source(printer_name, printer_port))

    # print_axis(printer_name)
    print_data(printer_name, 'test_doc', format_data({
        'name': u'某某人', 'trFrom': u'某某组织', 'trTo': u'另一组织',
        'year': '2016', 'month': '09', 'day': '21',
        'sendTo': u'某某组织委员', 'gender': u'男', 'age': '21', 'nation': u'汉',
        'idCard': '******************',
        'paidToYear': '2020', 'paidToMonth': '09',
        'validity': '30'
    }))
