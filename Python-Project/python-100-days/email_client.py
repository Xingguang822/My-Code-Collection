import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import socket
import re
from email.parser import BytesParser
from email.policy import default
import base64


class EmailClient:
    def __init__(self, root):
        self.root = root
        self.root.title("校园邮件客户端")
        self.root.geometry("800x600")

        # 服务器配置
        self.server_host = "172.16.100.10"
        self.pop3_port = 110
        self.smtp_port = 25

        # 当前状态
        self.logged_in = False
        self.current_user = None

        self.create_login_frame()

    def create_login_frame(self):
        """创建登录界面"""
        self.clear_window()

        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 服务器地址
        ttk.Label(frame, text="邮件服务器:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.server_var = tk.StringVar(value=self.server_host)
        server_entry = ttk.Entry(frame, textvariable=self.server_var, width=30)
        server_entry.grid(row=0, column=1, pady=5, padx=5)

        # 用户名
        ttk.Label(frame, text="用户名:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.username_var = tk.StringVar()
        username_entry = ttk.Entry(frame, textvariable=self.username_var, width=30)
        username_entry.grid(row=1, column=1, pady=5, padx=5)

        # 密码
        ttk.Label(frame, text="密码:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(frame, textvariable=self.password_var, show="*", width=30)
        password_entry.grid(row=2, column=1, pady=5, padx=5)

        # 登录按钮
        login_btn = ttk.Button(frame, text="登录", command=self.login)
        login_btn.grid(row=3, column=0, columnspan=2, pady=20)

        # 让界面元素居中
        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

    def create_main_frame(self):
        """创建主界面"""
        self.clear_window()

        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 顶部按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Button(button_frame, text="收信", command=self.receive_emails).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="写邮件", command=self.create_email).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="退出", command=self.logout).pack(side=tk.RIGHT, padx=5)

        # 邮件列表
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        ttk.Label(list_frame, text="邮件列表:").pack(anchor=tk.W)

        # 创建树形视图显示邮件列表
        columns = ("发件人", "主题", "日期")
        self.email_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)

        for col in columns:
            self.email_tree.heading(col, text=col)
            self.email_tree.column(col, width=150)

        self.email_tree.pack(fill=tk.BOTH, expand=True, pady=5)

        # 绑定选择事件
        self.email_tree.bind("<Double-1>", self.view_email)

        # 邮件内容框架
        content_frame = ttk.Frame(main_frame)
        content_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5, padx=10)

        ttk.Label(content_frame, text="邮件内容:").pack(anchor=tk.W)

        self.email_content = scrolledtext.ScrolledText(content_frame, width=50, height=20)
        self.email_content.pack(fill=tk.BOTH, expand=True, pady=5)

        # 配置权重使框架可伸缩
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

    def create_email_frame(self):
        """创建写邮件界面"""
        self.clear_window()

        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 收件人
        ttk.Label(frame, text="收件人:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.recipient_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.recipient_var, width=40).grid(row=0, column=1, pady=5, padx=5,
                                                                         sticky=(tk.W, tk.E))

        # 主题
        ttk.Label(frame, text="主题:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.subject_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.subject_var, width=40).grid(row=1, column=1, pady=5, padx=5,
                                                                       sticky=(tk.W, tk.E))

        # 内容
        ttk.Label(frame, text="内容:").grid(row=2, column=0, sticky=tk.NW, pady=5)
        self.compose_content = scrolledtext.ScrolledText(frame, width=40, height=15)
        self.compose_content.grid(row=2, column=1, pady=5, padx=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 按钮框架
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="发送", command=self.send_email).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="取消", command=self.create_main_frame).pack(side=tk.LEFT, padx=10)

        # 配置权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)

    def clear_window(self):
        """清除窗口中的所有控件"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        """登录到邮件服务器"""
        server = self.server_var.get()
        username = self.username_var.get()
        password = self.password_var.get()

        if not server or not username or not password:
            messagebox.showerror("错误", "请填写所有字段")
            return

        try:
            # 尝试连接到POP3服务器
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((server, self.pop3_port))
                response = sock.recv(1024).decode()

                # 发送用户名
                sock.sendall(f"USER {username}\r\n".encode())
                response = sock.recv(1024).decode()

                if not response.startswith("+OK"):
                    raise Exception("用户名错误")

                # 发送密码
                sock.sendall(f"PASS {password}\r\n".encode())
                response = sock.recv(1024).decode()

                if not response.startswith("+OK"):
                    raise Exception("密码错误")

                # 登录成功
                self.logged_in = True
                self.current_user = username
                self.server_host = server
                self.create_main_frame()
                messagebox.showinfo("成功", "登录成功")

        except Exception as e:
            messagebox.showerror("登录失败", f"登录过程中发生错误: {str(e)}")

    def logout(self):
        """退出登录"""
        self.logged_in = False
        self.current_user = None
        self.create_login_frame()

    def receive_emails(self):
        """接收邮件列表"""
        if not self.logged_in:
            messagebox.showerror("错误", "请先登录")
            return

        try:
            # 连接到POP3服务器
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.server_host, self.pop3_port))
                sock.recv(1024)  # 接收欢迎消息

                # 发送用户名和密码
                sock.sendall(f"USER {self.current_user}\r\n".encode())
                sock.recv(1024)
                sock.sendall(f"PASS {self.password_var.get()}\r\n".encode())
                sock.recv(1024)

                # 获取邮件列表
                sock.sendall(b"LIST\r\n")
                response = sock.recv(4096).decode()

                # 解析邮件列表
                emails = []
                lines = response.split('\r\n')
                for line in lines[1:-2]:  # 跳过状态行和结束行
                    if line:
                        parts = line.split()
                        if len(parts) >= 2:
                            email_id = parts[0]
                            size = parts[1]

                            # 获取邮件头部信息
                            sock.sendall(f"TOP {email_id} 0\r\n".encode())
                            header_response = sock.recv(4096).decode()

                            # 解析发件人、主题和日期
                            from_match = re.search(r"From: (.+)", header_response)
                            subject_match = re.search(r"Subject: (.+)", header_response)
                            date_match = re.search(r"Date: (.+)", header_response)

                            from_addr = from_match.group(1) if from_match else "未知"
                            subject = subject_match.group(1) if subject_match else "(无主题)"
                            date = date_match.group(1) if date_match else "未知日期"

                            emails.append((email_id, from_addr, subject, date))

                # 更新邮件列表显示
                self.update_email_list(emails)

                # 退出
                sock.sendall(b"QUIT\r\n")

        except Exception as e:
            messagebox.showerror("错误", f"接收邮件时发生错误: {str(e)}")

    def update_email_list(self, emails):
        """更新邮件列表显示"""
        # 清空现有列表
        for item in self.email_tree.get_children():
            self.email_tree.delete(item)

        # 添加新邮件
        for email_id, from_addr, subject, date in emails:
            self.email_tree.insert("", "end", values=(from_addr, subject, date), tags=(email_id,))

    def view_email(self, event):
        """查看选定邮件的内容"""
        selection = self.email_tree.selection()
        if not selection:
            return

        item = self.email_tree.item(selection[0])
        email_id = item["tags"][0] if item["tags"] else None

        if not email_id:
            return

        try:
            # 连接到POP3服务器获取邮件内容
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.server_host, self.pop3_port))
                sock.recv(1024)

                sock.sendall(f"USER {self.current_user}\r\n".encode())
                sock.recv(1024)
                sock.sendall(f"PASS {self.password_var.get()}\r\n".encode())
                sock.recv(1024)

                # 获取邮件内容
                sock.sendall(f"RETR {email_id}\r\n".encode())
                response = b""
                while True:
                    data = sock.recv(4096)
                    if not data or data.endswith(b"\r\n.\r\n"):
                        response += data
                        break
                    response += data

                # 退出
                sock.sendall(b"QUIT\r\n")

                # 解析并显示邮件内容
                email_text = response.decode()
                self.email_content.delete(1.0, tk.END)
                self.email_content.insert(tk.END, email_text)

        except Exception as e:
            messagebox.showerror("错误", f"获取邮件内容时发生错误: {str(e)}")

    def send_email(self):
        """发送邮件"""
        recipient = self.recipient_var.get()
        subject = self.subject_var.get()
        content = self.compose_content.get(1.0, tk.END)

        if not recipient or not subject or not content.strip():
            messagebox.showerror("错误", "请填写所有字段")
            return

        try:
            # 连接到SMTP服务器
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.server_host, self.smtp_port))
                response = sock.recv(1024).decode()

                # 发送EHLO命令
                sock.sendall(f"EHLO {socket.gethostname()}\r\n".encode())
                response = sock.recv(1024).decode()

                # 设置发件人
                sock.sendall(f"MAIL FROM: <{self.current_user}@campus.edu>\r\n".encode())
                response = sock.recv(1024).decode()

                if not response.startswith("250"):
                    raise Exception("发件人设置失败")

                # 设置收件人
                sock.sendall(f"RCPT TO: <{recipient}>\r\n".encode())
                response = sock.recv(1024).decode()

                if not response.startswith("250"):
                    raise Exception("收件人设置失败")

                # 发送数据
                sock.sendall(b"DATA\r\n")
                response = sock.recv(1024).decode()

                if not response.startswith("354"):
                    raise Exception("无法开始数据传输")

                # 发送邮件内容
                email_data = f"""From: {self.current_user}@campus.edu
To: {recipient}
Subject: {subject}

{content}
.
"""
                sock.sendall(email_data.encode())
                response = sock.recv(1024).decode()

                if not response.startswith("250"):
                    raise Exception("邮件发送失败")

                # 退出
                sock.sendall(b"QUIT\r\n")

                messagebox.showinfo("成功", "邮件发送成功")
                self.create_main_frame()

        except Exception as e:
            messagebox.showerror("错误", f"发送邮件时发生错误: {str(e)}")


def main():
    root = tk.Tk()
    app = EmailClient(root)
    root.mainloop()


if __name__ == "__main__":
    main()