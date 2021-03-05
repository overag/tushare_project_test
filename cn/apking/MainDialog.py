#!/usr/bin/python
# -*-coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from _ast import If
import mxnet as mx
from cnocr import CnOcr

top = tk.Tk()
# 这里四个参数分别为：宽、高、左、上
top.geometry("500x300+750+200")
top.title("简易OCR识别")

strPath = StringVar()
strResult = StringVar()


def pathCallBack():
    # , ('All Files', '*')
    filePath = filedialog.askopenfilename(title='Select picture to OCR', filetypes=[('PNG', '*.png'), ('JPG', '*.jpg'),('JPEG', '*.jpeg'), ('bmp', '*.bmp')])
    if (filePath != ''):
        strPath.set(filePath)

        ocr = CnOcr()
        img_fp = ''
        # img_fp = 'D://download/multi-line_cn1.png'
        img_fp = filePath

        img = mx.image.imread(img_fp, 1)

        res = ocr.ocr(img)
        # print("Predicted Chars:", res)

        # print(type(res))
        strResult = ""

        for s in res:
            strResult = strResult + ''.join('%s' % id for id in s) + "\n"

        txtResult.delete(0.0, tk.END)
        txtResult.insert(tk.INSERT, strResult)
        txtResult.update()

def okCallBack():
    # strResult = 'i love you!'
    # txtResult.delete(0.0, tk.END)
    # txtResult.insert(tk.INSERT, strResult)
    # txtResult.update()
    pass



btnPath = tk.Button(top,
                    text='选择',
                    width=10,
                    command=pathCallBack)
# btnOk = tk.Button(top,
#                   text='Close',
#                   width=10,
#                   command=okCallBack)
Label(top, text="图片路径：").grid(row=0, column=0)
Entry(top, width=45, textvariable=strPath).grid(row=0, column=1)
btnPath.grid(row=0, column=2);
Label(top, text="文本内容：").grid(row=2, column=0)
txtResult = Text(top, width=45, height=15)
txtResult.grid(row=3, column=1)
txtResult.insert(tk.END, 'Hello World!')
# btnOk.grid(row=4, column=2);
top.mainloop()
