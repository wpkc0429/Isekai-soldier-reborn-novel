## Why

第一卷 55 章 + vol1-optimization 已收尾。第二卷開寫前要做兩件事：

1. **看清楚第一卷實際好不好看**——模擬讀者視角，列具體章節而非泛論
2. **看清楚這套架構的真實執行率**——不是「規範完不完備」，是「實際被執行的部分有多少」

但這次審查本身有一個額外限制：**前一版 proposal 列出 8 P0 + 5 P1 + 7 個子 decision，剛好是它在診斷的那種「spec 通膨」的範本**。所以這份修訂版主動套用 audit 的發現於 audit 本身——**砍到只剩 3 P0 + 2 P1，加 7 天 deadline，其餘延到 vol2 ch10 的真實資料 checkpoint**。

audit 的可信度來自它願意自我約束。

## What Changes

### 類別 A：1 份合併 audit + 1 頁 action plan，不進 specs 樹

- 新增 `openspec/audits/vol1-2026-05/audit.md`：**quality 與 architecture 合併為單一文件**
  - §1 **vol1-optimization 修補類型統計**：先做證據基底——把 vol1-optimization 實際修了哪幾類 bug 統計清楚，作為其後 finding 的證據根
  - §2 quality findings（每條附 confidence label：[strong / pattern / single / inferred]）
  - §3 architecture findings（含使用者補充的 6 項，與 subagent 八項合併呈現，每條附 confidence label）
  - §4 vol2 ch10 checkpoint 待評估清單（明確標記「現在不做」的項目）
- 新增 `openspec/audits/vol1-2026-05/action-plan.md`：**單頁表格**，列 P0 與 P1 與 deferred
- **Top 3 P2 直接 inline 寫進 vol2 第一份 `ai-session-brief.md` 的內文**，不另開檔案、不靠連結（因為「靠記得去查」是原工作流故障的根因）
- audit artifact 放在 `openspec/audits/`，不放 `openspec/specs/`——audit 是時點性診斷快照，不是當前事實

### 類別 B：3 項 P0，7 天內完成

P0 嚴格定義：立刻能做、低成本、不需拍板、可逆。**P0 上限 5 項，否則此級別失去意義**。

1. **Chapter Brief 整併**——pre-chapter-checklist + ai-session-brief 合併為單一一張紙
2. **`chapter-sync.md`（合併 post-chapter-sync + mini-sync）**——同一張表的兩個 cadence：每章寫完答 5 題快版（5 分鐘）、每 10 章跑完整版（含「本次有無新類型不一致」的開放欄）
3. **foreshadowing 截止日欄**——foreshadowing-tracker / foreshadowing-list 各加一欄「最遲揭露章」

### 類別 C：2 項 P1 結構性決策，7 天內拍板並完成，逾期砍

需 `/opsx:apply` 之前用 AskUserQuestion 取得使用者決定：

- **P1-A：single source of truth 指派**——character-state-cards = 人物年齡，info-asymmetry-table = 知情狀態
- **P1-B：vol1-chapters 是否從 specs/ 移至 manuscript/vol1/**

### 類別 D：vol2 ch10 checkpoint 待評估清單（不在本 change 執行）

以下項目**全部延到第二卷寫到第 10 章時重新評估**——屆時有「第二卷工作流實際運作的真實資料」，比現在憑 vol1 推測更可靠：

- glossary 三欄擴充
- scene-beat template
- voice-corpus（前一版列為 P0；批判性閱讀 4–6 小時違反 P0 定義）
- emotion-distance-table（前一版 P0；9 對 × 5 欄 × 每章更新與 character-state-cards 同病；改為「先做梅拉/塔利/母親 3 對 × 試 10 章」由 checkpoint 決定）
- 規則正反對照
- spec 瘦身評估——**改為客觀標準**：vol2 ch10 自動掃描每份 spec 在這 10 章被引用幾次，零引用 = P3 候選；不再做主觀 P1/P2/P3 分級
- 自動化腳本——v1 只做字數統計（必能跑），節奏分析需 frontmatter 統一後再加（這是隱藏依賴，前一版漏寫）

### Stop condition

**本 change 在 `/opsx:apply` 後 7 天內必須 archive**。逾期：
- 未完成的 P1 自動砍，記入 timeline-changes.md
- audit / action-plan 仍以當下狀態 archive（不可拖）
- 砍掉的項目移至 vol2 ch10 checkpoint 清單

deadline 的目的：避免 audit 變成它自己的長期 project，重蹈 vol1-writing §7 的失敗。

## Capabilities

### New Capabilities

- `audits`（**新目錄類別，非 spec 樹的一部分**）：時點性診斷快照的儲存位置，含日期戳

### Modified Capabilities

- `writing-management`：
  - `pre-chapter-checklist.md` + `ai-session-brief.md` 合併為單一 Chapter Brief 流程
  - 新增 `chapter-sync.md`（合併 post-chapter-sync 5 問與 mini-sync 5 欄位的單一文件）
  - `foreshadowing-tracker.md` 新增「最遲揭露章」欄
- `plot-structure`：
  - `foreshadowing-list.md` 新增「最遲揭露章」欄
- （條件性 P1）`writing-management` 與其他 specs：若批准 P1-A，相關文件改為 link 形式
- （條件性 P1）若批准 P1-B，55 章正文 git mv 至 `manuscript/vol1/`

### Unchanged

- 第一卷 55 章正文（vol1-optimization 已處理過）
- 第二卷以後章節大綱
- OpenSpec 工作流本身（不換工具）
- 大部分既有 spec（除 P1-A/B 動到的少數檔案外）

## Impact

- **本 change 的範圍刻意比 audit 發現的問題小**——大部分發現延到 vol2 ch10 用真實資料判斷，而不是現在憑推測架空疊加
- **預期執行成本**：類別 A（audit + action-plan + inline P2）約半個 session；類別 B（3 項 P0）約 1 個 session；類別 C（P1 視使用者拍板）半個到一個 session。**總成本應 ≤ 2 個 session，必須在 7 天內完成**
- **對檔案結構的影響**：
  - 新增 3 個檔案：`audits/vol1-2026-05/audit.md`、`audits/vol1-2026-05/action-plan.md`、`writing-management/chapter-sync.md`
  - 合併 1 對檔案：pre-chapter-checklist 進 ai-session-brief
  - 擴充 2 個檔案：foreshadowing-tracker 與 foreshadowing-list 各加一欄
  - inline 動作：top 3 P2 寫進 vol2 第一份 ai-session-brief 內文（非新檔案）
- **對 vol1-chapters 的影響**：零（除非 P1-B 通過則涉及 git mv）
- **與前一版 proposal 的差異**：P0 從 8 砍到 3、P1 從 5 砍到 2、audit 從 2 份合併為 1 份、加入 7 天 stop condition、改用「正文引用率」客觀標準替代主觀 P1/P2/P3 分級

## Self-applied note

前一版 proposal 在範圍上違反了它自己診斷的問題：spec 通膨、P0 失去意義（8 項全部會被當「中等優先」處理）、缺 stop condition、靠連結記憶（vol2-action-plan 重蹈 pre-chapter-checklist 同病）。本修訂版套用了那些診斷於自身。**這份修訂後的 proposal 仍不算精簡，但明確比前一版瘦——這就是 audit 對自己誠實的最低門檻**。
