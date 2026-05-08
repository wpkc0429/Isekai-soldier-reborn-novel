---
name: "OPSX: Update"
description: 在 apply 前調整 proposal/design/tasks 的內容，嚴格限制只能修改 openspec/changes/ 下的 artifact 檔案
category: Workflow
tags: [workflow, artifacts, experimental]
---

在 apply 執行之前，調整指定 change 的 proposal.md、design.md 或 tasks.md 內容。

**此 skill 只能修改 `openspec/changes/<name>/` 下的三個 artifact 檔案。**
任何涉及 `openspec/specs/`、`.claude/`、`app/`、或任何其他路徑的修改，一律拒絕執行，並告知使用者等 `/opsx:apply` 時才能進行。

---

## Input

`/opsx:update` 後接更新描述，格式可以是：

- **指定 change + 描述**：`/opsx:update ai-docs-collab-strategy 增加需求：驗證文件內容`
- **只有描述**（從 context 推斷 change）：`/opsx:update 把 Task 3 工時改為 2h`
- **無輸入**：詢問要更新哪個 change 以及要改什麼

---

## Steps

### 1. 確認目標 change

若已從對話 context 知道 change 名稱，直接使用並告知：「更新 change：`<name>`」。

若不確定，列出 `openspec/changes/` 下所有子目錄，用 **AskUserQuestion** 請使用者選擇。

### 2. 確認更新內容

若使用者沒有描述要改什麼，用 **AskUserQuestion** 詢問：
> 「要調整哪個部分？（proposal / design / tasks），以及具體的變更是什麼？」

若描述已足夠，跳過此步。

### 3. 讀取現有 artifacts

讀取目標 change 下的相關 artifact（依更新範圍決定讀哪個）：

```
openspec/changes/<name>/proposal.md   ← What / Why
openspec/changes/<name>/design.md     ← How
openspec/changes/<name>/tasks.md      ← Implementation steps
```

若更新跨越多個 artifact，全部讀取。

### 4. 判斷更新範圍

根據使用者描述，判斷要修改的 artifact：

| 更新類型 | 修改目標 |
|---------|---------|
| 新增/修改問題背景、目標、方案選項 | `proposal.md` |
| 調整技術設計、目錄結構、規格細節 | `design.md` |
| 新增/修改/刪除 task、調整工時、更新驗收條件、調整執行順序 | `tasks.md` |
| 跨越多個面向 | 同時修改多個 artifact，保持三者一致 |

### 5. 執行更新

只使用 **Edit** 或 **Write** 工具修改 `openspec/changes/<name>/` 下的 artifact 檔案。

**嚴格禁止**：
- ❌ 修改 `openspec/specs/` 下的任何檔案
- ❌ 修改 `CLAUDE.md`、`.claude/` 下的任何檔案
- ❌ 修改任何程式碼檔案
- ❌ 執行 `git mv`、`git rm`、`git commit`
- ❌ 建立 `openspec/changes/<name>/` 以外的新檔案

若使用者的更新描述要求上述被禁止的操作，明確拒絕並說明：
> 「這個修改涉及 `openspec/specs/` 的實際檔案，必須等 `/opsx:apply` 執行時才能進行。我已將需求記錄在 tasks.md 中。」

### 6. 確認三份 artifact 一致

更新後快速確認三份 artifact 的描述沒有互相矛盾：
- proposal.md 的目標與 tasks.md 的 task 範圍一致
- design.md 的規格細節與 tasks.md 的步驟吻合
- 若有不一致，一併修正

### 7. 回報結果

輸出：

```
✅ 已更新 change：<name>

修改的 artifact：
  - [列出修改的檔案]

變更摘要：
  - [一句話說明每個 artifact 改了什麼]

提醒：openspec/specs/ 的實際檔案異動需執行 /opsx:apply 後才會發生。
```

---

## Guardrails

- **Never touch files outside `openspec/changes/<name>/`** — 這是最高優先的限制，任何情況下都不能違反
- 若使用者要求「直接更新 spec」或「現在就改檔案」，統一回應：「此 skill 只能調整 change 的規劃文件。要執行實際變更，請使用 `/opsx:apply`。」
- 若 change 狀態已是 `applied`（已完成 apply），提醒使用者直接編輯檔案或建立新的 change
- 更新 tasks.md 時，維持現有已完成 task 的 `✅` 狀態不變
- 工時估算調整需合理（每個 task ≤ 4h 的原則）

