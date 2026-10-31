# 24039100286-license-lab
# 密码生成器

一个用 Python 编写的命令行密码生成器，使用标准库 `secrets` 模块生成加密安全的随机密码，适合用来练习开源项目的基本结构、许可证选择和 README 写作。

## 项目状态

已完成，可正常运行。

## 功能

- 默认生成16 位随机密码
- 可指定所生成密码的长度和数量
- 可分别关闭大写字母、小写字母、数字或符号
- 每个启用的字符组至少出现一次，避免随机结果缺少某类字符

## 安装或获取

1. 安装 Python 3.8 或更高版本
2. 克隆或下载本仓库

本项目只依赖 Python 标准库，无需安装第三方包。

## 使用说明

在仓库目录中运行：

```bash
# 生成一个 16 位默认密码
python password_generator.py

# 生成 3 个 20 位密码
python password_generator.py --length 20 --count 3

# 生成不含符号的 12 位密码
python password_generator.py --length 12 --no-symbols
```

查看所有参数：

```bash
python password_generator.py --help
```

## 项目结构与依赖

- `password_generator.py`：主程序，包含密码生成逻辑和命令行入口
- `test_password_generator.py`：单元测试
- `README.md`：项目说明
- `LICENSE`：许可证全文

当前版本未引入第三方素材。

## 如何贡献

可通过 GitHub Issue 反馈问题，或提交 Pull Request。提交前请运行测试：

```bash
python -m unittest -v
```

## 许可证

本项目采用 MIT 许可证，全文见 `LICENSE`。选择 MIT 是因为本项目功能简单、面向学习与复用，希望使用者可以宽松地复制、修改和商用，同时保留版权声明即可。

## 安全提示

生成后的密码请自行妥善保存，本项目不会记录或上传任何密码。
