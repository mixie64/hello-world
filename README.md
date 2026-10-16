# hello-world

一个简单的 Hello World 示例，用来演示完整的 Git 工作流。

## 运行

```bash
python hello.py
```

输出：

```
Hello, World!
```

## 项目结构

- `hello.py` —— 打印 `Hello, World!` 的程序
- `README.md` —— 本说明文件

## 这个仓库是怎么来的

它是一次 Git 工作流演示的产物，完整走过了这几步：

1. `git init -b main` —— 初始化仓库，默认分支 `main`
2. `git add hello.py` —— 把文件放入暂存区
3. `git commit` —— 生成一次提交（`feat: add hello world program`）
4. `git remote add origin <url>` —— 关联远程仓库
5. `git push -u origin main` —— 推送并建立起跟踪关系

之后每次改动，流程简化为：`add` → `commit` → `push`。
