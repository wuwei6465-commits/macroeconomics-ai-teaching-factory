# Pro Slides Maker - 专业课件工厂

## 简介

Pro Slides Maker 是一个基于 AI 的智能课件生成工具，能够将 Markdown 格式的讲义自动转换为精美的 HTML5 演示文稿。

本 Skill 基于 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill)（MIT许可证）构建，集成了教育理论（BOPPPS模型）和 AI 内容生成能力。

## 功能特性

- 🎨 **36套精美主题**：aurora、tokyo-night、matrix 等
- 📐 **31种页面布局**：封面、目录、内容、图表、结语等
- ✨ **47个动画效果**：neural-net、data-stream、particles 等
- 📝 **MathJax 公式渲染**：完美支持经济学数学公式
- 📊 **实时数据嵌入**：支持 FRED 经济数据图表
- 🎤 **演讲者模式**：逐字稿 + 计时器

## 前置要求

1. **安装 html-ppt-skill**

```bash
# 克隆仓库
git clone https://github.com/lewislulu/html-ppt-skill.git

# 进入目录
cd html-ppt-skill

# 安装依赖（如果需要）
# pip install -r requirements.txt
```

2. **目录结构要求**

```
html-ppt-skill/
├── index.html          # 主入口
├── css/                # 样式文件
├── js/                 # JavaScript文件
├── assets/             # 资源文件
│   ├── themes/         # 主题文件
│   ├── layouts/        # 布局文件
│   └── effects/        # 特效文件
└── ...
```

## 使用方法

### 方法1：使用 Python 脚本生成

```python
from skills.pro_slides_maker import generate_slides

# 生成课件
generate_slides(
    input_file='examples/chapter11-isl/lecture.md',
    output_file='output/第11次课-IS-LM模型.html',
    theme='aurora',
    title='IS-LM模型分析',
    subtitle='产品市场与货币市场的一般均衡'
)
```

### 方法2：使用命令行

```bash
python generate_slides.py \
    --input examples/chapter11-isl/lecture.md \
    --output output/第11次课-IS-LM模型.html \
    --theme aurora \
    --title "IS-LM模型分析" \
    --subtitle "产品市场与货币市场的一般均衡"
```

### 方法3：在 TRAE 中使用 Skill

1. 打开 TRAE CN
2. 调用 `pro-slides-maker` Skill
3. 提供讲义文件路径
4. AI 自动生成课件

## 主题列表

| 主题名称 | 风格 | 适用场景 |
|---------|------|---------|
| `aurora` | 极光渐变 | 通用课程 |
| `tokyo-night` | 东京夜景 | 数据可视化 |
| `matrix` | 黑客帝国 | 技术类课程 |
| `ocean` | 海洋深蓝 | 经济学课程 |
| `sunset` | 日落橙红 | 案例分享 |
| `minimal` | 极简白 | 学术报告 |

## 布局类型

- `cover`：封面页
- `toc`：目录页
- `section`：章节分隔页
- `content`：内容页（左文右图）
- `content-reverse`：内容页（右文左图）
- `full-image`：全图页
- `quote`：引用页
- `data`：数据图表页
- `formula`：公式推导页
- `summary`：总结页
- `thanks`：致谢页

## 特效列表

- `neural-net`：神经网络连线
- `data-stream`：数据流动
- `particles`：粒子效果
- `gradient-waves`：渐变波浪
- `geometric`：几何图形

## 讲义格式要求

Markdown 讲义需要遵循以下格式：

```markdown
---
title: IS-LM模型分析
subtitle: 产品市场与货币市场的一般均衡
theme: aurora
effect: neural-net
---

# 【B-导入】情境引入

## 新闻案例

[2024年央行降息新闻]

---

# 【O-目标】明确目标

## 本课目标

1. 理解IS曲线的推导（L2）
2. 掌握LM曲线的含义（L2）
3. 分析IS-LM模型的均衡（L4）

---

# 【P1-理论先行】IS曲线

## 产品市场均衡

$$Y = C + I + G + (X - M)$$

IS曲线表示产品市场均衡时利率与收入的关系。

---

# 【P2-模拟演练】曲线移动

## 财政政策的影响

- 扩张性财政政策 → IS曲线右移
- 紧缩性财政政策 → IS曲线左移

---

# 【S-总结】知识梳理

## 核心要点

1. IS曲线：产品市场均衡
2. LM曲线：货币市场均衡
3. 交点：双重市场均衡
```

## 配置说明

### config.yaml

```yaml
# html-ppt 路径配置
html_ppt_path: "third-party/html-ppt-skill"

# 默认主题
default_theme: "aurora"

# 默认特效
default_effect: "neural-net"

# 输出目录
output_dir: "output/课件"

# MathJax 配置
mathjax:
  enabled: true
  version: "3.2.2"

# FRED 数据配置
fred:
  enabled: true
  api_key: "YOUR_FRED_API_KEY"  # 可选
```

## 使用流程

```
┌─────────────────┐
│  准备讲义.md     │
│  (Markdown格式)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  调用Skill      │
│  (TRAE/Python)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI解析内容     │
│  匹配主题/布局   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  生成HTML5课件  │
│  (含特效+公式)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  浏览器打开     │
│  按S演讲者模式  │
└─────────────────┘
```

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| `→` / `↓` / `Space` | 下一页 |
| `←` / `↑` | 上一页 |
| `Home` | 第一页 |
| `End` | 最后一页 |
| `S` | 演讲者模式 |
| `T` | 切换主题 |
| `F` | 全屏 |
| `ESC` | 退出全屏/演讲者模式 |

## 示例

### 示例1：生成IS-LM模型课件

```python
from skills.pro_slides_maker import generate_slides

generate_slides(
    input_file='examples/chapter11-isl/lecture.md',
    output_file='output/第11次课-IS-LM模型.html',
    theme='aurora',
    effect='neural-net'
)
```

### 示例2：批量生成课件

```python
from skills.pro_slides_maker import batch_generate

chapters = [
    ('chapter11-isl/lecture.md', '第11次课-IS-LM模型'),
    ('chapter12-ad/lecture.md', '第12次课-AD-AS模型'),
]

for md_file, title in chapters:
    generate_slides(
        input_file=f'examples/{md_file}',
        output_file=f'output/{title}.html',
        theme='aurora'
    )
```

## 故障排除

### 问题1：公式显示不正确

**原因**：MathJax 未正确加载

**解决**：
- 检查网络连接
- 确认 MathJax CDN 可访问
- 或使用本地 MathJax 文件

### 问题2：特效不显示

**原因**：assets/effects 路径不正确

**解决**：
- 确认 html-ppt-skill 完整安装
- 检查 config.yaml 中的路径配置

### 问题3：主题切换无效

**原因**：主题文件缺失

**解决**：
- 确认 themes/ 目录存在
- 确认主题文件名正确

## 致谢

- **html-ppt-skill**：专业级HTML5演示框架，作者 lewis，MIT许可证
- **MathJax**：数学公式渲染库
- **FRED**：联邦储备经济数据

## 许可证

本项目采用 MIT 许可证开源。

html-ppt-skill 采用 MIT 许可证，版权归原作者所有。
