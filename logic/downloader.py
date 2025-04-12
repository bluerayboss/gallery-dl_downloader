import subprocess
import re

def download_multiple(urls, output_dir, log_func, status_var, enable_ui_func, filter_exts, filename):
    for i, url in enumerate(urls, start=1):
        log_func(f"🔹 URL {i}/{len(urls)}: {url}")
        download_gallery(url, output_dir, log_func, status_var, filter_exts, filename)
    status_var.set("상태: 완료")
    enable_ui_func()

def download_gallery(url, output_dir, log_func, status_var, filter_exts, filename):
    command = ["gallery-dl", "-d", output_dir]
    if filter_exts:
        ext_list_str = ", ".join(f"'{ext}'" for ext in filter_exts)
        command += ["--filter", f"extension in ({ext_list_str})"]
    if filename:
        command += ["-o", f"filename={filename}.{{extension}}"]
    command.append(url)
    log_func(f"명령어 실행: {' '.join(command)}")
    # [subprocess 실행 로직 생략 가능]