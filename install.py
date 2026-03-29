import sys
import subprocess
from pathlib import Path

# 尝试使用原作者的 comfy_env 安装方式
try:
    from comfy_env import install
    install()
except ImportError:
    # 如果找不到 comfy_env，则降级使用标准的 pip 安装
    print("Warning: 'comfy_env' module not found. Falling back to standard pip install...")
    
    # 获取当前目录下 requirements.txt 的绝对路径
    req_file = Path(__file__).resolve().parent / "requirements.txt"
    
    if req_file.exists():
        try:
            print(f"Installing dependencies from {req_file}")
            # 调用当前 ComfyUI 环境的 Python 执行 pip install -r requirements.txt
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
            print("Installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during pip install: {e}")
    else:
        print("requirements.txt not found. Skipping dependency installation.")
