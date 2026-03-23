# OpenClaw Config Editor

一个用于编辑 `openclaw.json / openclaw.json5` 的单文件图形化工具。  
支持**表单编辑 + JSON5 编辑 + 校验 + 导入导出**，可直接双击 HTML 使用，也可打包为 Windows `.exe`。

## 功能特性

- 左侧导航分区配置（Agents / Channels / Models / Session / Gateway）
- 右侧 JSON5 编辑器（CodeMirror）
- 表单 ↔ JSON5 双向同步
- JSON Schema（AJV）+ 自定义规则校验
- 自动验证开关（定时校验）
- 拖拽导入、文件打开、另存为、导出
- `Ctrl+S` 快捷保存
- 暗黑模式
- 模型自动检测（请求 `/models`）
- localStorage 本地缓存最近配置

## 快速开始（HTML 单文件）

1. 直接打开 `openclaw_editor.html`
2. 左侧填写配置项，或切到「JSON编辑器」手写 JSON5
3. 查看底部「验证结果」
4. 点击「导出/保存配置」输出 `openclaw.json`

> 该工具是纯前端单文件应用，不依赖服务器。

## 打包为 Windows EXE

项目包含 `package_to_exe.py` 启动脚本。

### 1) 安装依赖

```bash
pip install pywebview pyinstaller
```

### 2) 打包

```bash
pyinstaller -F -w package_to_exe.py --add-data "openclaw_editor.html;."
```

### 3) 运行

打包产物位于：

- `dist/package_to_exe.exe`

## 配置兼容说明

编辑器已兼容新版常见结构，包括：

- `meta`
- `wizard`
- `models.mode / models.providers`
- `list.main.model`
- `gateway.port / mode / bind / auth.token`
- `channels.telegram / discord / whatsapp`

## 发布

### v1.0.0（首个正式版本）

- 发布日期：2026-03-22
- 里程碑：首个可用正式版本
- 包含：图形化编辑、JSON5 编辑、双向同步、校验、导入导出、暗黑模式、模型检测、EXE 打包脚本

## 目录结构

```text
.
├── openclaw_editor.html   # 主应用（单文件前端）
├── package_to_exe.py      # EXE 启动封装脚本
└── README.md              # 项目说明文档
```

## 许可证

可按你的项目需要添加（例如 MIT）。

## PR 提交流程说明（Codex 限制）

如果你在平台里看到提示：

> Codex 目前不支持更新在 Codex 以外更新的拉取请求。

处理方式：

1. 不要继续往原 PR 追加更新。
2. 基于当前最新代码重新创建一个新 PR。
3. 在新 PR 描述中注明：用于替代旧 PR（旧 PR 因外部更新无法继续由 Codex 维护）。

这样可以避免 PR 同步冲突，并确保后续更新可继续由 Codex 自动提交。
