import tkinter.filedialog
import Translation
import os

SAVE_FILE_PATH = os.getcwd()
ADDRESS_DATA = {"PICTURE_LIST": [], "PICTURE_PATH": "", "RESULT_FOLDER": ""}
PICTURE_LIST = []
RESULT_FOLDER = ""


# 获取用户选择的文件夹路径
def get_folder_path(title="choose file", initialdir=SAVE_FILE_PATH):
    '''
    读取文件
    '''
    folder_path = tkinter.filedialog.askdirectory(title=title,
                                                  initialdir=initialdir)
    # print("选择的文件路径为->", folder_path)

    return folder_path


def get_pictures():
    folder_path = get_folder_path()
    # 如果获取了有效的路径
    if len(folder_path) != 0:
        # 将工作目录切换到需要读取图片的文件夹
        os.chdir(folder_path)
        files_list = [f for f in os.listdir() if os.path.isfile(f)]
        ADDRESS_DATA["PICTURE_LIST"] = [
            f for f in files_list if f.endswith(("jpg", "png", "jpeg", "bmp"))
        ]
        # print(pictures_list)
        ADDRESS_DATA["PICTURE_PATH"] = folder_path
        os.chdir(SAVE_FILE_PATH)
    return ADDRESS_DATA["PICTURE_LIST"]


def set_result_path():
    folder_path = get_folder_path()
    # 如果获取了有效的路径
    if len(folder_path) != 0:
        ADDRESS_DATA["RESULT_FOLDER"] = folder_path

    return folder_path


def translate_files():
    # 如果图片和文件夹都存在
    if len(ADDRESS_DATA["PICTURE_LIST"]) != 0 and os.path.exists(
            ADDRESS_DATA["PICTURE_PATH"]) and os.path.exists(
                ADDRESS_DATA["RESULT_FOLDER"]):
        tr = Translation.Translate()
        for i in ADDRESS_DATA["PICTURE_LIST"]:
            photo_address = ADDRESS_DATA["PICTURE_PATH"] + '/' + i
            tr.connect(ADDRESS_DATA["RESULT_FOLDER"], photo_address)
    else:
        print("invalid path")
        return False
    print(ADDRESS_DATA)
    return True


"""
# 将信息保存至文件。注意filetypes中第一个list中的内容会
# 为initialfile中的名字提供后缀，进而导致defaultextasion中的设置失效，、
# 除非list中第一个的后缀内容为空或者“.*”
# 这是一个测试用函数
def save_file(title="save your file",
              initialdir=SAVE_FILE_PATH,
              initialfile="test",
              filetypes=[["任意文件", ".*"], ["文本文件", ".txt .docx. doc"],
                         ["Excel", ".xlsx .xls"]],
              defaultextension=".tif"):
    '''
    保存文件
    '''
    # 从系统的文件资源管理器中获取想要的文件保存路径
    get_save_path = tkinter.filedialog.asksaveasfilename(
        title=title,
        initialdir=initialdir,
        initialfile=initialfile,
        filetypes=filetypes,
        defaultextension=defaultextension)
    print("获取的文件保存路径为->", get_save_path)
    print("路径类型为", type(get_save_path))
    print("路径长度：", len(get_save_path))

    # 写入文件，io流
    text = input()
    newfile = open(get_save_path, "w+", encoding="utf-8")
    newfile.write(text)
    newfile.close()

    return
"""
"""
print("asksaveasfilename")
path =tkinter.filedialog.asksaveasfilename()#返回文件名
print(path)

print("asksaveasfile")
path =tkinter.filedialog.asksaveasfile()#会创建文件
print(path)

print("askopenfilename")
path =tkinter.filedialog.askopenfilename()#返回文件名
print(path)

print("askopenfile")
path =tkinter.filedialog.askopenfile()#返回文件流对象
print(path)

print("askdirectory")
path =tkinter.filedialog.askdirectory()#返回目录名
print(path)

print("askopenfilenames")
path =tkinter.filedialog.askopenfilenames()#可以返回多个文件名
print(path)

print("askopenfiles")
path =tkinter.filedialog.askopenfiles()#多个文件流对象
print(path)
"""
