# Recursive Bible Tutor

> 把任何教材變成「依賴圖驅動、錯誤模型可追蹤、必須通過 mastery gate」的私人教科書與家教。

`recursive-bible-tutor` 是一個符合 Agent Skills 格式的學習 skill。它不是摘要 prompt，也不是把教材講得更長；它的核心任務是找出學習者腦中**第一個壞掉的 prerequisite**，一次修一個 atomic concept，並要求 retrieval / application / discrimination / transfer 證據後才標記 mastered。

## 核心理念

**Exposure ≠ recognition ≠ understanding ≠ retrieval ≠ transfer ≠ mastery.**

「看懂」和「真的會」是不同狀態。

## 它可以吃什麼？

- PDF / textbook / paper
- 投影片、截圖、公式
- 老師逐字稿或影片筆記
- 程式碼 / GitHub repository
- 網頁 / URL
- 一個主題名稱
- 一句「我完全看不懂」

## 它怎麼教？

`Target → prerequisite graph → first broken link → atomic lesson → retrieval → misconception repair → transfer → spaced review`

預設一次只推進一個核心概念。學習者若答錯，skill 追的是「產生錯答案的 mental model」，不是只把答案改正。

## Repo 結構

```text
recursive-bible-tutor/
├── SKILL.md
├── README.md
├── AGENTS.md
├── references/
│   ├── pedagogy.md
│   ├── mastery-gates.md
│   ├── state-machine.md
│   ├── mathematical-mode.md
│   ├── research-paper-mode.md
│   ├── visual-mode.md
│   └── source-grounding.md
├── assets/templates/
│   ├── TOPIC.md
│   ├── KNOWLEDGE_GRAPH.md
│   ├── LEARNER_STATE.md
│   ├── MISCONCEPTIONS.md
│   ├── REVIEW_QUEUE.md
│   └── SESSION_LOG.md
├── scripts/
│   ├── init_workspace.py
│   └── validate_skill.py
├── examples/
│   └── probability-bayes.md
└── evals/
    └── evals.json
```

## 快速開始

### 1. 驗證 skill

```bash
python scripts/validate_skill.py
```

### 2. 建立一個持久化學習 workspace

```bash
python scripts/init_workspace.py workspaces/differential-privacy
```

### 3. 對 AI 說

```text
START
學這個：<PDF / 圖片 / 論文 / URL / 主題>

我想真的融會貫通。先找 prerequisite graph 和第一個 broken link；一次只教一小節。
```

或直接使用：

```text
BIBLE MODE
```

## Mastery Gate

概念狀態：

```text
NEW → LEARNING → FRAGILE → MASTERED → REVIEW_DUE
```

`MASTERED` 不是使用者說「懂了」就成立。至少需要多數以下證據：

- Reconstruction — 不抄原句，自己重建概念
- Application — 新例子仍會用
- Discrimination — 能抓出看似合理的錯誤說法
- Transfer — 換表面形式仍能辨認結構

## Bible Mode

遇到「從頭教」、「聖經模式」、「教科書模式」、「徹底不會」時：

1. 建 dependency roadmap。
2. 找第一個 broken prerequisite。
3. Purpose before details。
4. Intuition before formalism。
5. Mechanism before math/memorization。
6. 每個符號第一次出現都定義。
7. 加例子、反例、boundary、misconception。
8. 每次只教一小節。
9. 最後讓學習者閉卷生成答案。
10. 沒有 mastery evidence 就不假裝完成。

## Commands

`START` · `CONTINUE` · `WHY` · `PREREQ` · `MAP` · `TEXTBOOK` · `DEEP` · `INTUITION` · `FORMAL` · `TEST` · `CLOSED BOOK` · `REVIEW` · `MISCONCEPTION` · `CONNECT` · `TEACH BACK`

## 設計方向

這個 repo 採用 Agent Skills 的 `SKILL.md + references + scripts + assets` 結構，目標是能被不同支援 Agent Skills 的工具重用，而不是綁死單一模型。

目前版本是 **v0.1.0**。下一階段預計加入：

- automatic review scheduler;
- machine-readable concept graph;
- mastery scoring based on evidence rather than self-report;
- source-ingestion adapters;
- benchmark/eval suite;
- topic-to-topic learner model transfer.

## License

MIT
