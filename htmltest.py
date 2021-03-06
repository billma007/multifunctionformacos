import tkinter as tk
import tkinter.messagebox
import urllib.request
import webbrowser
import requests
import os
from tqdm import tqdm
import sys
import tkinter.ttk as ttk
def getHtml(url):
    
    response = urllib.request.urlopen(url)
    html = response.read()
    html=html.decode("utf-8")
    return html 
def CreateIt():
    a=open("cancelupdate.txt","w")
    a.close()
def callbackreturn():
    destroyask=tkinter.messagebox.askokcancel(title="提示",message="真的要退出吗？")
    if destroyask ==True:
        sys.exit(0)
class Down:
    def flush(self):
        pass
    def DownloadFile2_cdn(self):
        try:
            if self.downloadurl_cdn is None or self.filename is None:
                
                print('参数错误')
                return None
    
            # 读取exe资源
            res = requests.get(self.downloadurl_cdn,stream=True) 
            total_size = int(int(res.headers["Content-Length"])/1024+0.5)
            # 获取文件地址
            file_path = os.path.join(self.filename)

            # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
            with open(file_path, 'wb') as fd:
                self.deletejudge=True
                print('开始下载文件：{},当前文件大小：{}KB'.format(self.filename,total_size))
                for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='kb',desc=None,ascii="=>"):
                    fd.write(chunk)
                self.deletejudge=False
                print(self.filename+' 下载完成！\n您可以打开新版本程序并且删除本文件了'+self.htmllll)
        except Exception as eeee:
            print(eeee) 
    def DownloadFile2_fa(self):
        try:
            if self.downloadurl_cdn is None or self.filename is None:
                
                print('参数错误')
                return None
    
            # 读取exe资源
            res = requests.get(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave/latestdownload.html").strip().replace(' ', '').replace('\t', '').replace('\r', '').strip(),stream=True,allow_redirects=True) 
            total_size = int(int(res.headers["Content-Length"])/1024+0.5)
            # 获取文件地址
            file_path = os.path.join(self.filename)

            # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
            with open(file_path, 'wb') as fd:
                self.deletejudge=True
                print('开始下载文件：{},当前文件大小：{}KB'.format(self.filename,total_size))
                for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='kb',desc=None,ascii="=>"):
                    fd.write(chunk)
                self.deletejudge=False
                print(self.filename+' 下载完成！\n您可以打开新版本程序并且删除本文件了')
        except Exception as eeee:
            print(eeee) 
            
    def DownloadFile2_fastly(self):
        try:
            if self.downloadurl_fastly is None or self.filename is None:
                print('参数错误')
                return None
    
            # 读取exe资源
            res = requests.get(self.downloadurl_fastly,stream=True) 
            total_size = int(int(res.headers["Content-Length"])/1024+0.5)
            # 获取文件地址
            file_path = os.path.join(self.filename)

            # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
            with open(file_path, 'wb') as fd:
                self.deletejudge=True
                print('开始下载文件：{},当前文件大小：{}KB'.format(self.filename,total_size))
                for chunk in tqdm(iterable=res.iter_content(1024),total=total_size,unit='kb',desc=None,ascii="=>"):
                    fd.write(chunk)
                self.deletejudge=False
                print(self.filename+' 下载完成！\n您可以打开新版本程序并且删除本文件了')
        except Exception as eeee:
            print(eeee)
    def __init__(self):
                # 将其备份
        self.stdoutbak = sys.__stdout__
        self.stderrbak = sys.__stderr__
        self.thissoftware="1.2.5"
        self.deletejudge=False

        # 重定向
        sys.stdout = self
        sys.stderr = self
        self.htmllinshi=str(max(str(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltoolsupdatecheck.html")),str(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltoolsupdatecheck.html")),str(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/update/latest.html")),str(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/update/latest.html"))))
        self.htmllll=self.htmllinshi.strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()

        self.downloadurl_fastly = "https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltool"+self.htmllll+".exe"
        self.downloadurl_cdn = "https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltool"+self.htmllll+".exe"
        self.filename="MultiFunctional Tool"+self.htmllll+".exe"
        self.printinit=str(max(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/downloadintroduction.html"),getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/downloadintroduction.html")))
        self.title = '马哥多功能工具：软件更新系统'
        self.root = tk.Tk(className=self.title)
        self.root.geometry("850x400")
        self.a = tk.StringVar()
        self.openfinal = False
        self.root.resizable(False, False)
        frame_2 = tk.Frame(self.root)
        frame_3 = ttk.Frame(self.root)
        frame_4 = ttk.Frame(self.root)

        # set frame_3
        self.entry_path = tk.Text(frame_2,highlightcolor='Fuchsia', highlightthickness=1, width=125)
        
        # set frame_2

        url_path = ttk.Button(frame_3, text = "中国直接下载",
        command = self.DownloadFile2_fa)
        down_fastly = ttk.Button(frame_3, text='fastly直接下载\n暂时无法使用',command=self.DownloadFile2_fastly)
        down_cdn = ttk.Button(frame_3, text='cdn直接下载\n暂时无法使用',
                         command=self.DownloadFile2_cdn)
        goackbutton = ttk.Button(frame_3, text='创建', 
                         command=lambda:CreateIt())
        
        label_desc = ttk.Label(frame_4, 
                              text='本项目已在GitHub上开源,遵守GNU通用公共许可证(GPL)')
        label_jnxxhzz = ttk.Label(frame_4,
                              text='Copyright (C) 2022 billma007')
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
#        label_img.pack(side=tk.RIGHT)
#        label_img.pack(ipadx=100,ipady=0)
        self.entry_path.grid(row=1, column=1,pady=10)	
        
        down_cdn.grid(row=1, column=3, ipadx=20)
        down_fastly.grid(row=1,column=4,ipadx=20)
        url_path.grid(row=1,column=5,ipadx=20)
        goackbutton.grid(row=1,column=6,ipadx=20)
        label_desc.grid(row=1, column=0)
        label_jnxxhzz.grid(row=2, column=0)

        print(self.printinit)
    def write(self,info):
        if self.deletejudge==True:
            self.entry_path.delete('1.0','end')
        self.entry_path.insert('end', info)
        self.entry_path.update()	# 更新显示的文本，不加这句插入的信息无法显示

    def cometohere(self):
        self.root.protocol("WM_DELETE_WINDOW", callbackreturn)
        self.root.mainloop()
def checkupdate():
    return str(max(str(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltoolsupdatecheck.html")),str(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/multifunctionaltoolsupdatecheck.html")),str(getHtml("https://cdn.jsdelivr.net/gh/billma007/imagesave@latest/update/latest.html")),str(getHtml("https://fastly.jsdelivr.net/gh/billma007/imagesave@latest/update/latest.html"))))
def gotoweather():
    if '1.4.0'!=checkupdate():
        asd=Down()
        asd.cometohere()
    else:
        from tkinter import messagebox
        messagebox.showinfo("成功！","你的版本已经是最新版本！")

if __name__=="__main__":
    gotoweather()