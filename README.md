# Git 冲突练习场

这是一个**专门用来练手**的仓库，里面的代码是假的，随便改、随便删、随便搞坏，不影响任何真实项目。

## 当前状态

- 分支 `main`：已有一版代码
- 分支 `feature`：修改了**同样的两个地方**
- 两个分支现在处于「分叉」状态，一旦合并必定冲突

## 练习目标

1. 在命令行执行 merge，亲眼看 `CONFLICT` 长什么样
2. 切到 IDEA，找到「合并冲突」分组
3. 在三栏界面里用 `<<` `>>` 选择代码
4. 提交并完成合并
5. 然后再练一次「反悔」：`git merge --abort`

## 重要

玩坏了不要紧，恢复原状只要一条命令：

```bash
cd D:/code-project/git-conflict-lab
git merge --abort
```

如果已经提交了，想彻底重来：

```bash
cd D:/code-project/git-conflict-lab
git reset --hard main-original
```

## 说明

`app/service/purchase.py` 和 `vite.config.ts` 会在合并时冲突。
`README.md` 本身不会被改动，所以它会**自动合并**，你可以对比一下「冲突文件」和「正常文件」的区别。
