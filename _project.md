---
title: "GitHub 仓库闭环测试项目"
id: sc-rna-seq-loop-test
type: research
status: active
phase: planning
priority: high
tags: [测试, GitHub仓库闭环]
created: 2026-06-04
updated: 2026-06-05
external_path: ""
visibility: local
repo:
  url: git@github.com:kaisermoon/sc-rna-seq-loop-test.git
  default_branch: main
  protected_branches: [main]
  ci_required_checks: [test, lint]
  pr_size_limit: {files: 10, lines: 400}
  reviewer_profile: default
---

# GitHub 仓库闭环测试项目

## 项目概述

AI-OS GitHub 仓库项目闭环测试样板，用于验证 coder → code_reviewer → merge → repo-loop 完整工作流。可随时删除。

## 相关项目

- 无

## 外部目录

- **路径**: 无
- **说明**: 无外部目录
