# OpenClaw.json 编辑器

> 一个开箱即用的单文件可视化配置编辑器，专为 OpenClaw 项目的 `config.json` 文件设计。无需安装任何依赖，双击即可使用。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![HTML](https://img.shields.io/badge/HTML-Single%20File-orange.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![CodeMirror](https://img.shields.io/badge/CodeMirror-5.65-green.svg)

---

## ✨ 功能概览

| 功能 | 说明 |
|------|------|
| 📝 可视化表单编辑 | 通过侧边栏导航切换各配置分组，表单字段实时修改 |
| ⚡ JSON 编辑器 | 集成 CodeMirror + Dracula 主题，支持语法高亮、折叠、错误提示 |
| 🔄 双向同步 | 表单↔JSON 实时同步；可开启 JSON→表单自动同步开关（800ms 防抖） |
| ✅ 配置验证 | 自动验证（静默刷新底部面板）+ 手动触发（弹出 Toast 提示） |
| 📁 文件管理 | 支持拖拽打开文件、另存为、导出 JSON5；最近文件列表可点击一键恢复 |
| 🤖 Provider 管理 | 可添加/删除 AI 模型 Provider，自动深度合并保留原始未知字段 |
| 💡 模板生成 | 一键生成带有示例数据的完整配置模板 |

---

## 🚀 快速开始

### 方式一：直接打开（推荐）

下载 `openclaw-editor.html` 文件，用任意现代浏览器双击打开即可。

```bash
# 或者用本地服务器运行（避免部分浏览器的 file:// 限制）
python -m http.server 7788
# 然后访问 http://localhost:7788/openclaw-editor.html
```

### 方式二：GitHub Pages

Fork 本仓库后，在 **Settings → Pages** 中选择 `main` 分支根目录，等待部署完成后即可通过链接访问在线版本。

---

## 📖 使用说明

### 界面结构

```
┌─────────────┬──────────────────────────────────────┐
│             │  顶部工具栏（打开/保存/验证/导出...）  │
│   侧边栏    ├──────────────────────────────────────┤
│   导航菜单  │                                      │
│             │         主编辑区域                   │
│  ● 基础设置 │    （表单 ↔ JSON 编辑器双栏）        │
│  ● AI 模型  │                                      │
│  ● Provider │                                      │
│  ● 高级设置 ├──────────────────────────────────────┤
│  ● 最近文件 │  底部验证面板（错误/警告实时显示）    │
└─────────────┴──────────────────────────────────────┘
```

### 工具栏说明

| 按钮 | 功能 |
|------|------|
| 📂 打开文件 | 弹出文件选择框，支持拖拽 `.json` / `.json5` 文件 |
| 💾 保存 | 保存到当前路径（如已打开文件）|
| 💾 另存为 | 下载为新文件 |
| ✅ 验证配置 | 手动触发完整验证，弹出结果 Toast |
| 📤 导出 JSON5 | 以 JSON5 格式导出，支持注释 |
| 🔄 JSON→表单 | 开关：开启后 JSON 编辑器改动 800ms 后自动同步表单 |

### 最近文件

- 侧边栏底部的"最近文件"列表会记录最多 8 条历史
- 每条记录保存**文件名、保存时间和配置快照**
- 点击任意条目可立即恢复该时刻的配置状态

### Provider / 模型管理

- 在"AI 模型 Provider"页面可添加自定义 Provider
- 内置预设：OpenAI、Anthropic、Google Gemini、Azure OpenAI 等
- 保存时使用**深度合并策略**，原 JSON 中存在的未知字段不会被覆盖

---

## 🔧 技术栈

| 依赖 | 版本 | 用途 |
|------|------|------|
| [Bootstrap](https://getbootstrap.com/) | 5.3.0 | UI 框架、布局、组件 |
| [CodeMirror](https://codemirror.net/) | 5.65.2 | JSON 代码编辑器 |
| [JSON5](https://json5.org/) | 2.x | 宽松 JSON 解析（支持注释、末尾逗号）|
| [Font Awesome](https://fontawesome.com/) | 6.4.0 | 图标库 |

所有依赖均通过 CDN 引入，**无需本地安装**。

---

## 📁 文件结构

```
openclaw-editor.html    ← 完整独立的单文件应用（所有逻辑内嵌）
README.md               ← 本说明文档
```

---

## 🐛 已知限制

- 依赖 CDN 资源，**离线环境下无法正常使用**（可将依赖替换为本地文件）
- 浏览器安全限制：通过 `file://` 协议直接打开时，部分功能（如自动读取本地文件路径）受限，建议使用本地 HTTP 服务器
- localStorage 容量有限（约 5MB），最近文件快照在超限时自动降级（仅保存文件名和时间）

---

## 🤝 贡献

欢迎提 Issue 和 PR！如有功能建议或 bug 报告，请在 Issues 页面详细描述复现步骤。

---

## 📄 License

[MIT](LICENSE)
