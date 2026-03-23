"""将 openclaw_editor.html 打包为 Windows .exe 的最小脚本。

用法：
1) pip install pywebview pyinstaller
2) pyinstaller -F -w package_to_exe.py --add-data "openclaw_editor.html;."
3) dist/package_to_exe.exe
"""
from pathlib import Path
import webview

html = Path(__file__).with_name("openclaw_editor.html")
if not html.exists():
    raise SystemExit("openclaw_editor.html 不存在")

webview.create_window("OpenClaw.json Editor", html.as_uri(), width=1400, height=900)
webview.start()
