import tkinter as tk
import FileOperation

if __name__ == "__main__":
    # 实例化tkinker窗口
    root = tk.Tk()
    root.title("hsl youdao translation test")
    # 创建框架,用于放置其他组件
    frm = tk.Frame(root)
    frm.grid(padx="50", pady="50")
    # 创建可被滚动的canvas，以此作为frame的子容器，来放置scrollbar
    canvas = tk.Canvas(frm)
    canvas.grid(row=0, column=1)
    # 创建滚动条，滚动条在canvas上可以滚动listbox
    sb1 = tk.Scrollbar(canvas)
    sb1.pack(side="right", fill="y")
    # 创建列表框listbox
    listbox = tk.Listbox(canvas,
                         width="40",
                         height="10",
                         yscrollcommand=sb1.set)
    listbox.pack(side="left")
    # 将滚动按钮绑定在canvas上
    sb1.config(command=listbox.yview)

    # 创建标签用于显示选定的存放输出结果的文件夹
    label = tk.Label(frm, width="40", height="2")
    label.grid(row=1, column=1)

    # Overriding FileOperation中的get_picture
    def get_pictures():
        picture_list = FileOperation.get_pictures()
        listbox.delete(0, "end")
        for i in picture_list:
            listbox.insert("end", i)

    # Overriding FileOperation中的set_result_path
    def set_result_path():
        folder_path = FileOperation.set_result_path()
        label["text"] = ""
        print(folder_path)
        label["text"] = folder_path

    # 创建按钮并分配布局
    btn_get_file = tk.Button(frm,
                             text="choose raw material",
                             command=get_pictures)
    btn_get_file.grid(row=0,
                      column=0,
                      ipadx="3",
                      ipady="3",
                      padx="10",
                      pady="20")
    btn_get_result_path = tk.Button(
        frm,
        text="choose address for translation result",
        command=set_result_path)
    btn_get_result_path.grid(row=1, column=0)

    # 运行按钮
    btn_sure = tk.Button(frm,
                         text="Translate",
                         command=FileOperation.translate_files)
    btn_sure.grid(row=2, column=1)

    root.mainloop()

# tk.messagebox.showinfo("提示","无文件")
