# 示例章节：IS-LM 模型

本目录展示了"宏观经济学AI教学资源工厂"的完整工作流程示例，选取了宏观经济学最核心的 **IS-LM 模型**（第11-12章）作为演示案例。

---

## 📁 目录结构

```
examples/
├── README.md                    # 本文件
├── chapter11-isl/               # 第11章：建立 IS-LM 模型
│   ├── lecture/                 # 📖 讲义（知识库输入）
│   ├── lesson_plan/             # 📋 教案源码（教案工厂输入）
│   ├── exercises/               # ✏️ 课后练习（题库工厂输入）
│   └── jupyter/                 # 🔬 交互实验（Jupyter Lab）
├── chapter12-isl-app/           # 第12章：应用 IS-LM 模型
│   ├── lecture/                 # 📖 讲义
│   ├── lesson_plan/             # 📋 教案源码
│   ├── exercises/               # ✏️ 课后练习
│   └── jupyter/                 # 🔬 交互实验
└── media/                       # 🎬 动画视频
    └── AD曲线的推导.mp4          # Manim 动画示例
```

---

## 🔄 完整工作流程

### 第一步：知识库（Obsidian）

讲义以 Markdown 格式存储在 Obsidian 知识库中，具有以下特色：

- **双向链接**：`[[凯恩斯交叉图]]`、`[[IS 曲线]]` 等概念自动关联
- **实验联动标签**：`[!LAB]` 标签标记与 Jupyter 实验的对应关系
- **MathJax 公式**：行内公式 `$PE = C(Y - T) + I + G$` 和独立公式块
- **折叠区块**：`[!MATH]-`、`[!TIP]`、`[!INFO]` 等多种折叠类型
- **Frontmatter 元数据**：章节编号、标题、标签、难度等结构化信息

### 第二步：教案工厂（TRAE + Python）

教案源码包含完整的 BOPPPS 教学设计：

```yaml
---
session_num: "11"
module_name: "AD-AS模型（AS曲线）"
obj_knowledge: |
  1. 理解总供给曲线（AS曲线）的定义与经济含义
  2. 掌握短期总供给曲线（SRAS）的推导过程
obj_ability: |
  5. 能够运用粘性价格模型解释AS曲线向上倾斜的原因
review_s: "回顾上节课内容：IS-LM模型的均衡条件"
intro_s: "引入总供给概念"
lecture1_s: "总供给曲线的基本概念与推导"
summary_s: "总结总供给理论的核心要点"
---
```

通过 `docxtpl` 模板渲染，生成符合学校格式的 Word 教案。

### 第三步：题库工厂（Python）

课后练习以 Markdown 格式编写，包含：

- **布鲁姆认知能级标注**：从 L1（记忆）到 L6（创造）
- **实验联动**：每道题标注对应的 Jupyter Cell
- **折叠式答案解析**：`[!SUCCESS]-` 折叠区块
- **数学公式**：完整的推导过程

通过批量转换脚本，生成学习通格式的题库文档。

### 第四步：交互实验（Jupyter Lab）

Jupyter Notebook 提供交互式可视化：

- **Cell 1**：凯恩斯交叉图 —— 存货调节机制（滑块控制产出 Y 和 MPC）
- **Cell 2**：乘数效应动态放大（柱状图展示连锁反应）
- **Cell 3**：IS 曲线推导实验室（利率 r 滑块）
- **Cell 4**：LM 曲线与货币市场均衡
- **Cell 5**：IS-LM 模型完整均衡分析

### 第五步：理论动画（Manim）

使用 Manim 生成的数学动画，将理论推导过程可视化：

- `AD曲线的推导.mp4`：从 IS-LM 模型推导 AD 曲线的完整动画

---

## 📊 文件说明

### 第11章：建立 IS-LM 模型

| 文件 | 类型 | 说明 |
|------|------|------|
| `第11章_总需求I_建立IS-LM模型.md` | 讲义 | 凯恩斯交叉→乘数效应→IS曲线→LM曲线→IS-LM均衡 |
| `教案_11_ASG模型_AS曲线.md` | 教案源码 | BOPPPS六阶段设计，含三维教学目标 |
| `第11章_课后练习.md` | 习题 | 4道题，含计算推导和实验联动 |
| `11_IS_LM_Master_Lab.ipynb` | Jupyter实验 | 5个交互式Cell，Plotly可视化 |

### 第12章：应用 IS-LM 模型

| 文件 | 类型 | 说明 |
|------|------|------|
| `第12章_总需求II_应用IS-LM模型.md` | 讲义 | 财政/货币政策→挤出效应→AD曲线推导→大萧条案例 |
| `教案_12_AD-AS模型_AD曲线.md` | 教案源码 | BOPPPS六阶段设计，含知识框架图 |
| `第12章_课后练习.md` | 习题 | 含IS-LM到AD曲线的数学推导 |
| `12_IS_LM_Application_Master_Lab.ipynb` | Jupyter实验 | 政策博弈系统+AD曲线生成 |

---

## 🚀 如何使用

### 运行 Jupyter 实验

```bash
# 安装依赖
pip install jupyter plotly ipywidgets numpy

# 启动 Jupyter Lab
jupyter lab

# 打开 notebook
# examples/chapter11-isl/jupyter/11_IS_LM_Master_Lab.ipynb
# examples/chapter12-isl-app/jupyter/12_IS_LM_Application_Master_Lab.ipynb
```

### 生成教案

```bash
cd skills/lesson-plan-maker
python lesson_plan_generator.py \
    --input examples/chapter11-isl/lesson_plan/教案_11_ASG模型_AS曲线.md \
    --template templates/word_template/教案模板.docx \
    --output output/
```

### 批量转换题库

```bash
cd skills/question-bank-generator
python batch_converter.py \
    --input examples/chapter11-isl/exercises/ \
    --output output/
```

---

## 📝 许可证

- 讲义、教案、习题：原创内容，遵循项目许可证
- Jupyter Notebook：原创内容，遵循项目许可证
- Manim 动画：原创内容，遵循项目许可证
