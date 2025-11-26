# 集置核心 GESTELL Core 无人机飞行控制系统 V1.0

## 项目简介 (Project Overview)

**集置核心 (GESTELL Core)** 是一款专为异构无人机集群设计的云边端协同飞行控制系统。本系统旨在解决传统飞控架构在通信延迟、边缘算力及扩展性方面的痛点，通过微服务架构与现代化技术栈（FastAPI, Vue 3, PostGIS），实现毫秒级低时延控制、高精度视觉感知及全生命周期管理。

本项目仓库主要包含该系统的**软件设计说明书**及**源代码汇编**的 LaTeX 工程文件，用于生成软件著作权申请所需的文档材料。

## 仓库结构 (Repository Structure)

*   `design_document.tex`: 软件设计说明书 LaTeX 源码。包含系统架构、模块设计、数据库设计、API 接口定义及测试用例等详细内容。
*   `source_code.tex`: 源代码汇编 LaTeX 源码。用于将项目源码格式化为 PDF 文档。
*   `collect_code.py`: Python 脚本。用于自动遍历指定目录下的源文件，并将其清洗、汇总到 `all_code.txt` 中，供 `source_code.tex` 调用。
*   `all_code.txt`: 由脚本生成的源码汇总文件（中间产物）。
*   `.vscode/`: VS Code 配置文件，包含 LaTeX Workshop 的编译设置。

## 环境依赖 (Prerequisites)

要编译本项目中的 LaTeX 文档，您需要安装以下环境：

1.  **TeX 发行版**: 推荐安装 [TeX Live](https://www.tug.org/texlive/) (Windows/Linux) 或 [MacTeX](https://www.tug.org/mactex/) (macOS)。确保包含 `xelatex` 编译器及 `ctex` 宏包。
2.  **Python 3.x**: 用于运行代码收集脚本。

## 编译指南 (Build Instructions)

### 1. 生成源代码汇总

首先运行 Python 脚本，扫描并汇总项目源码：

```bash
python collect_code.py
```

此命令将在当前目录下生成 `all_code.txt` 文件。

### 2. 编译设计说明书

使用 `xelatex` 编译设计说明书（建议编译两次以生成正确的目录和引用）：

```bash
xelatex design_document.tex
xelatex design_document.tex
```

输出文件：`design_document.pdf`

### 3. 编译源代码汇编

```bash
xelatex source_code.tex
```

输出文件：`source_code.pdf`

## 技术栈 (Tech Stack)

虽然本仓库主要为文档工程，但 GESTELL Core 系统本身基于以下技术构建：

*   **后端**: Python (FastAPI), Celery, MAVSDK
*   **前端**: Vue 3, TypeScript, Vite, Mapbox GL JS
*   **数据库**: PostgreSQL (PostGIS), TimescaleDB, Redis
*   **边缘计算**: NVIDIA Jetson, YOLOv8, OpenCV
*   **部署**: Docker, Kubernetes, Nginx

## 许可证 (License)

本项目文档及代码遵循 MIT 许可证。详见文档附录。

---
**嘉佳科技有限公司** | 2025
