import os
import sys
import multiprocessing
from tkinter import filedialog
import tkinter as tk


# 文件夹选择
def select_folder():
    selected_folder = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
    select_path.set(selected_folder)


# 文件选择
def select_file():
    selected_file_path = filedialog.askopenfilename()  # 使用askopenfilename函数选择单个文件
    select_file_path.set(selected_file_path)


# 执行查重
def excute():
    from imagededup.methods import PHash
    from imagededup.utils import plot_duplicates
    if select_path.get() is None or select_path.get().__eq__(""):
        tk.messagebox.showinfo("提示", "请先选择文件夹")
        return
    if select_file_path.get() is None or select_file_path.get().__eq__(""):
        tk.messagebox.showinfo("提示", "请先选择查重的图片")
        return
    str_list = select_file_path.get().split("/")
    file_name = str_list[len(str_list)-1]
    phasher = PHash()
    encodings = phasher.encode_images(image_dir=select_path.get())
    duplicates = phasher.find_duplicates(encoding_map=encodings)
    print(duplicates)
    plot_duplicates(image_dir=select_path.get(),
                    duplicate_map=duplicates,
                    filename=file_name,
                    outfile=select_path.get()+"/report.jpg")

    tk.messagebox.showinfo("成功", f"执行完成，请查看{select_path.get()}/report.jpg 图片查重报告")


def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    tk_window = tk.Tk()
    screenwidth = tk_window.winfo_screenwidth()
    screenheight = tk_window.winfo_screenheight()

    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    width = 560
    height = 230
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    tk_window.title("图片查重")
    tk_window.geometry(size_geo)
    # 更改左上角窗口的的icon图标
    tk_window.iconphoto(False, tk.PhotoImage(file=get_resource_path("icon.png")))
    # 或tk_window.iconbitmap('d:/icon.ico') 此方法必须是ico
    # 设置主窗口的背景颜色 #214283蓝色
    tk_window["background"] = "#FFFFFF"

    # 先初始化Entry控件的text variable 动态字符串属性值
    select_path = tk.StringVar()
    select_file_path = tk.StringVar()
    tk.Label(tk_window, text="文件夹路径：").grid(row=0, column=0)
    tk.Entry(tk_window, textvariable=select_path).grid(row=0, column=1, padx=5)
    tk.Button(tk_window, text="选择查找的文件夹", command=select_folder).grid(row=0, column=2)

    tk.Label(tk_window, text="图片路径：").grid(row=1, column=0, rowspan=1)
    tk.Entry(tk_window, textvariable=select_file_path).grid(row=1, column=1, rowspan=1, padx=10)
    tk.Button(tk_window, text="选择查重的图片", command=select_file).grid(row=1, column=2, rowspan=1)
    tk.Button(tk_window, anchor = "w",text="查重", command=excute).grid(row=2, column=2, rowspan=4, ipady=10, ipadx=30, pady=15)

    # 加载图片LOGO
    photo = tk.PhotoImage(file=get_resource_path("icon.png"))
    tk.Label(tk_window, image=photo).grid(row=0, column=3, rowspan=2, padx='20px', pady='10px')
    tk_window.mainloop()


