#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
教案工厂 - 基于BOPPPS模型的智能教案生成器

功能：读取Markdown格式的教案源码，渲染生成符合学校模板要求的Word教案
作者：吴伟
单位：广东白云学院
日期：2025年
"""

import os
import re
from datetime import datetime
from pathlib import Path
from docxtpl import DocxTemplate
import frontmatter


def generate_lesson_plan(
    md_file_path: str,
    template_path: str,
    output_dir: str,
    session_num: str = None,
    module_name: str = None
) -> str:
    """
    生成Word格式教案
    
    参数:
        md_file_path: 教案源码Markdown文件路径
        template_path: Word模板文件路径
        output_dir: 输出目录
        session_num: 课次（可选，默认从md文件读取）
        module_name: 模块名称（可选，默认从md文件读取）
    
    返回:
        生成的Word文件路径
    """
    
    # 路径处理
    md_path = Path(md_file_path)
    tpl_path = Path(template_path)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # 读取Markdown文件（必须指定UTF-8编码）
    with open(md_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
        meta = post.metadata
    
    # 获取当前日期
    today = datetime.now()
    
    # 构建模板变量上下文
    context = {
        # 基本信息
        'session_num': session_num or meta.get('session_num', '1'),
        'module_name': module_name or meta.get('module_name', '未命名模块'),
        'hours': meta.get('hours', '2'),
        'teacher_name': meta.get('teacher_name', '吴伟'),
        
        # 教学目标（三维目标）
        'obj_knowledge': meta.get('obj_knowledge', '').strip(),
        'obj_ability': meta.get('obj_ability', '').strip(),
        'obj_literacy': meta.get('obj_literacy', '').strip(),
        
        # 教学内容
        'teaching_content': meta.get('teaching_content', ''),
        'key_points': meta.get('key_points', ''),
        'difficult_points': meta.get('difficult_points', ''),
        
        # BOPPPS六阶段教学过程（带标签）
        'review_s': meta.get('review_s', ''),
        'review_a': meta.get('review_a', ''),
        'intro_s': meta.get('intro_s', ''),
        'intro_a': meta.get('intro_a', ''),
        'lecture1_s': meta.get('lecture1_s', ''),
        'lecture1_a': meta.get('lecture1_a', ''),
        'lecture2_s': meta.get('lecture2_s', ''),
        'lecture2_a': meta.get('lecture2_a', ''),
        'summary_s': meta.get('summary_s', ''),
        'summary_a': meta.get('summary_a', ''),
        'homework_s': meta.get('homework_s', ''),
        'homework_a': meta.get('homework_a', ''),
        
        # 教学评价与反思
        'evaluation': meta.get('evaluation', '过程性评价'),
        'reflection': meta.get('reflection', '（见随堂记录）'),
        
        # 日期
        'year': today.year,
        'month': today.month,
        'day': today.day
    }
    
    try:
        # 渲染模板
        doc = DocxTemplate(tpl_path)
        doc.render(context)
        
        # 生成文件名
        file_name = f"教案_{context['module_name']}_第{context['session_num']}次.docx"
        final_save_path = out_path / file_name
        
        # 保存文件
        doc.save(final_save_path)
        print(f'SUCCESS: 教案已生成 - {final_save_path}')
        return str(final_save_path)
        
    except Exception as e:
        print(f'FAILED: 生成失败 - {e}')
        raise


def batch_generate_lesson_plans(
    md_files: list,
    template_path: str,
    output_dir: str
) -> list:
    """
    批量生成多个教案
    
    参数:
        md_files: Markdown文件路径列表
        template_path: Word模板文件路径
        output_dir: 输出目录
    
    返回:
        生成的Word文件路径列表
    """
    generated_files = []
    
    for md_file in md_files:
        try:
            result = generate_lesson_plan(md_file, template_path, output_dir)
            generated_files.append(result)
        except Exception as e:
            print(f'跳过文件 {md_file}: {e}')
            continue
    
    print(f'\n批量生成完成：成功 {len(generated_files)}/{len(md_files)}')
    return generated_files


# 使用示例
if __name__ == '__main__':
    # 示例1：生成单个教案
    generate_lesson_plan(
        md_file_path='examples/chapter11-isl/lesson_plan.md',
        template_path='templates/word_template/教案模板.docx',
        output_dir='output/教案/'
    )
    
    # 示例2：批量生成
    # md_files = [
    #     'examples/chapter11-isl/lesson_plan.md',
    #     'examples/chapter12-ad/lesson_plan.md'
    # ]
    # batch_generate_lesson_plans(
    #     md_files=md_files,
    #     template_path='templates/word_template/教案模板.docx',
    #     output_dir='output/教案/'
    # )
