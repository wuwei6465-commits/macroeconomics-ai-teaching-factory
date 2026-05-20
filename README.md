# 宏观经济学AI教学资源工厂

> 基于国产大模型的智能备课系统 —— 让AI成为教师的得力助手

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Obsidian](https://img.shields.io/badge/Obsidian-6838A5?logo=obsidian&logoColor=white)](https://obsidian.md/)
[![TRAE CN](https://img.shields.io/badge/TRAE%20CN-国产AI-green)](https://www.trae.ai/)

---

## 🎯 项目简介

**宏观经济学AI教学资源工厂**是一个基于国产大模型（DeepSeek、GLM、Kimi、Qwen、豆包等）构建的智能备课系统。通过将经典教育理论（BOPPPS、布鲁姆分类法）数字化封装，实现教案、课件、题库的自动化、标准化生产。

**核心理念**：不是替代教师，而是放大教师能力 —— 教师负责教学设计，AI负责资源生成。

---

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                    宏观经济学AI教学资源工厂                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  Obsidian   │◄──►│   TRAE CN   │◄──►│ Jupyter Lab │     │
│  │  知识库管理  │    │  AI推理引擎  │    │ 可视化实验  │     │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘     │
│         │                  │                  │            │
│         ▼                  ▼                  ▼            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                 三大智能体工厂                        │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │ 教案工厂 │  │ 课件工厂 │  │ 题库工厂 │          │   │
│  │  │(Word)    │  │(HTML5)   │  │(学习通)  │          │   │
│  │  └──────────┘  └──────────┘  └──────────┘          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 技术栈

| 层级 | 工具 | 功能 |
|------|------|------|
| **知识库层** | Obsidian | Markdown知识管理、双向链接、知识图谱 |
| **AI引擎层** | TRAE CN | 国产AI IDE，集成14款国产大模型 |
| **可视化层** | Jupyter Lab | Python交互式数据可视化 |
| **输出层** | docxtpl / html-ppt | Word模板渲染 / HTML5课件生成 |

### 集成的国产大模型

- **字节跳动**：Doubao-Seed-2.0-Code / 1.8 / Code
- **智谱AI**：GLM-5.1 / 5V-Turbo / 5
- **DeepSeek**：V4-Pro / V4-Flash
- **月之暗面**：Kimi-K2.6 / K2.5
- **阿里巴巴**：Qwen3.6-Plus / 3.5-Plus

---

## ✨ 核心功能

### 1. 教案工厂 (lesson-plan-maker)

**功能**：Markdown源码 → 标准化Word教案

**特色**：
- 基于 **BOPPPS教学模型**（导言→目标→前测→参与→后测→总结）
- 融入 **布鲁姆分类法**（L1-L6认知能级目标设计）
- 嵌入 **五问设计链**（基本→重点→难点→实践→拓展）
- 自动从知识库检索相关资源

**效率提升**：传统4-6小时 → AI辅助5分钟

### 2. 课件工厂 (pro-slides-maker)

**功能**：讲义 → 专业HTML5幻灯片

**特色**：
- 36套精美主题（aurora、tokyo-night等）
- MathJax公式完美渲染
- 粒子特效（neural-net、data-stream等）
- 演讲者模式（逐字稿+计时器）
- 实时数据嵌入（FRED图表）

**致谢**：基于 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill)（MIT许可证）

### 3. 题库工厂 (question-bank-generator)

**功能**：Markdown习题 → 学习通格式题库

**特色**：
- 批量转换（支持20章同时处理）
- 自动标注布鲁姆认知能级
- 符合学习通快速导入格式
- 已生成400道题目（20章）

---

## 📊 应用成果（2025年春季学期）

| 资源类型 | 数量 | 说明 |
|---------|------|------|
| 📄 智慧教案 | 22次课 | 覆盖整学期教学内容 |
| 🖥️ HTML5课件 | 22套 | 含粒子特效和MathJax公式 |
| 📝 学习通题库 | 20章400题 | 按布鲁姆分类法标注难度 |
| 🔬 Jupyter实验 | 8个 | IS-LM、AD-AS等核心模型 |
| 🎬 Manim动画 | 12个 | 理论推导动态可视化 |

### 学情数据分析

基于454道学生答题记录：
- **高难度知识点**（<70%）：3个，重点突破
- **中难度知识点**（70%-85%）：8个，巩固强化
- **低难度知识点**（≥85%）：8个，提升挑战

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Obsidian（知识库管理）
- TRAE CN（AI开发环境）
- Jupyter Lab（可选，用于可视化实验）

### 安装依赖

```bash
pip install docxtpl python-frontmatter jupyter
```

### 使用示例

#### 1. 制作教案

```python
from skills.lesson_plan_maker import generate_lesson_plan

# 生成第11次课教案（IS-LM模型）
generate_lesson_plan(
    session_num="11",
    module_name="IS-LM模型分析",
    md_file_path="examples/chapter11-isl/lesson_plan.md",
    template_path="templates/word_template/教案模板.docx",
    output_dir="output/教案/"
)
```

#### 2. 制作课件

```bash
# 使用html-ppt生成HTML5课件
cd skills/pro-slides-maker
python generate_slides.py \
    --input examples/chapter11-isl/lecture.md \
    --output output/课件/第11次课-IS-LM模型.html \
    --theme aurora
```

#### 3. 批量转换题库

```python
from skills.question_bank_generator import batch_convert

# 批量转换第11-12章习题
batch_convert(
    input_dir="examples/chapter11-isl/exercises/",
    output_dir="output/题库/"
)
```

---

## 📁 项目结构

```
macro-econ-ai-teaching-factory/
├── README.md                          # 本文件
├── LICENSE                            # MIT许可证
├── docs/                              # 文档目录
│   ├── 系统架构.md                     # 五阶段路线图详解
│   ├── 快速开始.md                     # 详细使用指南
│   ├── Skill使用手册/
│   │   ├── lesson-plan-maker.md       # 教案工厂文档
│   │   ├── pro-slides-maker.md        # 课件工厂文档
│   │   └── question-bank-generator.md # 题库工厂文档
│   └── Prompt设计规范/
│       ├── 教案专供.md
│       ├── 课件专供.md
│       └── 习题专供.md
├── prompts/                           # Prompt模板（脱敏版）
│   ├── README.md                      # Prompt设计理念说明
│   ├── Prompt-教案专供-模板.md         # 教案生成模板
│   ├── Prompt-课件专供-模板.md         # 课件生成模板
│   └── Prompt-习题专供-模板.md         # 习题生成模板
├── skills/                            # Skill核心代码
│   ├── lesson-plan-maker/
│   │   ├── lesson_plan_generator.py   # 教案生成脚本
│   │   └── requirements.txt
│   ├── pro-slides-maker/
│   │   ├── generate_slides.py         # 课件生成脚本
│   │   └── html_template/             # HTML模板
│   └── question-bank-generator/
│       ├── batch_converter.py         # 题库批量转换
│       └── requirements.txt
├── templates/                         # 模板文件
│   ├── word_template/                 # Word教案模板
│   └── html_template/                 # HTML课件模板
├── examples/                          # 示例章节
│   └── chapter11-isl/                 # 第11章：IS-LM模型
│       ├── lecture.md                 # 讲义
│       ├── lesson_plan.md             # 教案源码
│       ├── exercises.md               # 习题
│       └── output/                    # 生成结果
└── third-party/                       # 第三方依赖
    └── html-ppt-skill/                # html-ppt（MIT）
```

---

## 🎓 教育理论支撑

### BOPPPS教学模型

| 阶段 | 英文 | 功能 | 时间占比 |
|------|------|------|---------|
| B | Bridge-in | 情境导入，激发兴趣 | 5% |
| O | Objective | 明确目标与认知能级 | 5% |
| P1 | Pre-assessment | 前测，摸底已有认知 | 10% |
| P2 | Participatory | 参与式学习（核心） | 60% |
| P3 | Post-assessment | 后测，评估目标达成 | 15% |
| S | Summary | 总结梳理，承上启下 | 5% |

### 布鲁姆认知分类法

- **L1 记忆**：列举、定义、识别
- **L2 理解**：解释、归纳、举例
- **L3 运用**：计算、演示、应用
- **L4 分析**：比较、对比、推导
- **L5 评价**：评判、评估、辩论
- **L6 创造**：设计、构建、规划

---

## 🤝 致谢

### 开源项目

- **[html-ppt-skill](https://github.com/lewislulu/html-ppt-skill)**：专业级HTML5演示框架，提供36套主题、31种布局、47个动画效果。作者：lewis，许可证：MIT

### 国产AI工具

- **TRAE CN**：字节跳动出品的国产AI IDE
- **DeepSeek / GLM / Kimi / Qwen / 豆包**：国产大模型

---

## 📄 许可证

本项目采用 [MIT许可证](LICENSE) 开源。

您可以自由使用、修改、分发，只需保留原作者声明。

**注意**：Word教案模板涉及学校资产，请根据实际情况决定是否公开。

---

## 📮 联系方式

- 作者：[您的姓名]
- 单位：广东白云学院
- 邮箱：[您的邮箱]

---

## 🌟 项目愿景

> "AI是杠杆，教师是支点，教育的未来是人机融合。"

我们希望这个项目能为更多教师提供参考，让AI成为教学的得力助手，而非替代品。

**欢迎Star ⭐ 和 Fork！**
