## Context

本 change 經一次大幅修訂。修訂前提出 8 P0 + 5 P1 + 7 個子 decision，被批為「audit 自己變成它在診斷的 spec 通膨範本」。修訂後砍至 3 P0 + 2 P1，加入 7 天 stop condition，並把所有「靠推測判斷的事」延到 vol2 ch10 checkpoint 用真實資料決定。

設計核心：**audit 的可信度來自願意自我約束**。

## Goals / Non-Goals

**Goals**

- 產出 1 份合併 audit + 1 頁 action plan，作為時點性診斷快照（**不進 spec 樹**）
- 在 7 天內執行 3 項真正配得上 P0 的工作流調整
- 把所有「靠推測判斷」的優化建議延到 vol2 ch10 用真實資料判斷
- 把 top 3 P2 inline 進 vol2 第一份 ai-session-brief，不靠連結記憶

**Non-Goals**

- 不在 audit 中產生任何「永久規格」式的斷言（finding 必須附 confidence label）
- 不主觀 P1/P2/P3 分級任何 spec（改用 vol2 ch10 的引用率掃描）
- 不在本 change 做任何屬於 vol2 ch10 checkpoint 範圍的事
- 不把 audit 放進 `openspec/specs/`
- 不重寫第一卷正文
- 不換工具

## Decisions

### Decision 1：P0 嚴格定義，上限 5 項

**選擇**：P0 = 立刻能做、低成本、不需拍板、可逆。本 change 最終 3 項 P0：
- Chapter Brief 整併
- chapter-sync.md（合併 post + mini）
- foreshadowing 截止日欄

**理由**：前一版 8 項 P0 違反 P0 自己的定義。voice-corpus 是 4–6 小時批判性閱讀；emotion-distance-table 維護成本高；scene-beat 屬中等成本；glossary 三欄屬中等價值。一旦 P0 超過 5 項，這個級別失去意義——使用者會把全部當「中等優先」處理。

**不選的方案**：保留 8 項並加重要性排序（仍會稀釋）；保留 4 項含 scene-beat（border line，砍掉更乾淨）。

### Decision 2：Audit 不進 specs 樹

**選擇**：放 `openspec/audits/vol1-2026-05/`，加日期戳。

**理由**：spec 系統的語義是「當前事實」。audit 是「點時間的診斷快照」——半年後工作流改了，這份 audit 留在 specs/ 會看起來像對過去行為的不公正攻擊。`openspec/audits/<date>/` 明確標記為歷史性文件。

**不選的方案**：放 `specs/vol1-review/`（語義錯誤）；放 repo 根目錄（失去結構）。

### Decision 3：每條 finding 附 confidence label

**選擇**：四級標籤：
- **[strong]** = 直接證據（檔案明確記錄、樣本一致、無例外）
- **[pattern]** = 多章節重複出現的模式（≥3 個樣本）
- **[single]** = 單一章節或單一檔案的觀察
- **[inferred]** = 從間接證據推論（如「pre-chapter-checklist 大概率沒在勾」是從 ch033/053/055 的失敗反推）

**理由**：保留犀利措辭的同時標清楚信心強度。「pre-chapter-checklist 大概率沒在勾」是基於 16/55 章樣本的 [inferred]，不該被三個月後重讀的人當 [strong] 引用。

**操作**：每條 finding 結尾用 `[label]` 格式標記。reviewer 可依 label 決定是否採納。

### Decision 4：post-chapter-sync + mini-sync 合併為 chapter-sync.md

**選擇**：單一文件，兩種 cadence：
- **每章 quick 版（5 分鐘）**：5 個固定問題的 reverse-pass
- **每 10 章 full 版（含基準掃描）**：5 個固定欄位 + 一條開放欄「本次有沒有發現新類型的不一致？若有，加入下次 sync 範圍」

**理由**：前一版 post-chapter-sync 的 Q1（spec 沒寫但發生了）≈ mini-sync 欄位 5（character-state-cards 增量更新）——兩個「5 件事」清單其實是同一張表的不同 cadence。分兩個文件會讓使用者搞混職責。合併為單一 source 後，每章 quick 版的累積結果 = 每 10 章 full 版的輸入。

**開放欄的存在處理 mini-sync「鎖死 5 個欄位」的回溯式定義缺陷**——下次出問題的會是還沒被抓過的那種，所以必須留增量欄位的入口。

**不選的方案**：
- 保留兩個文件：職責不清
- 完全廢掉 mini-sync 的固定欄位、只用開放欄：失去基線

### Decision 5：vol1-optimization 修補類型統計作為 audit 證據基底

**選擇**：audit §1 第一節先做「vol1-optimization 修補類型統計」——把它的 tasks.md 中實際修了哪幾類問題分類計數，作為其後 finding（特別是 chapter-sync 鎖哪些欄位）的證據根。

**理由**：前一版 mini-sync 的 5 欄位是直覺判斷（「過去三次 sync 抓出問題的全部欄位」）。vol1-optimization 的 changelog 是更可靠的證據——它精確記錄了第一卷哪些類型的不一致實際發生了。從證據導出 sync 範圍，比從直覺導出更可信。

**操作**：統計類別建議含：人物年齡漂移、知情狀態漂移、伏筆編號重複、整章獨白違規、結尾無鉤子違規、字數貼底違規。每類附「次數 / 總章數」與「設定能否在開章前發現」標籤。

### Decision 6：spec 瘦身改為「正文引用率」客觀標準

**選擇**：不在本 change 做主觀 P1/P2/P3 分級。改為延到 vol2 ch10：
- 自動掃描每份 spec 在 vol2 前 10 章被引用幾次
- 零引用 = P3 候選（遷移至 `author-reference/` 或刪除）
- 1–2 次 = P2 候選（壓縮）
- ≥3 次 = P1 保留

**理由**：前一版 Decision 7f 把瘦身範圍鎖在 faction-politics + cities-guide 是政治安全（不動爭議大的 world-settings/factions-detail、geography-detail），不是診斷完整。客觀標準不需要選範圍——所有 spec 一視同仁，引用率自動分級。

**不選的方案**：
- 現在做主觀分級：易爭議、易誤判
- 全部 spec 主觀分級：工作量爆炸、且仍主觀

### Decision 7：Top 3 P2 inline 進 vol2 第一份 ai-session-brief

**選擇**：把 vol2-action-plan 的 top 3 P2 條目（依優先排序）**直接寫進 vol2 第一份 `ai-session-brief.md` 的內文**，不另開檔案、不靠連結。

**理由**：「靠記得去查 vol2-action-plan.md」跟原本 pre-chapter-checklist 工作流故障的根因一樣——基於記憶的提醒在實戰會被跳過。inline 進使用者「不可能不看到」的路徑（每章開寫前必看的 brief）才能真正生效。

**top 3 P2 暫定**（最終由 audit §2 quality findings 排序決定）：
1. 第二卷必須安排至少 2 次「主角會失敗 / 計算錯」的場景
2. 賽門/艾拉前 20 章內各有一次完整的「正面戲」
3. 替「他把這個收進去 / 放著 / 過一遍」找替代收束工具

**操作**：寫進 `ai-session-brief.md` 模板的「本卷重點提醒」段（若無則新增）。

**不選的方案**：
- 只在 action-plan 列出靠連結：複製 vol1 失敗模式
- 全部 P2 都 inline：稀釋焦點

### Decision 8：Stop condition — 7 天 hard deadline

**選擇**：本 change 在 `/opsx:apply` 後 7 天內必須 archive。逾期：
- 未完成 P1 自動砍，記入 timeline-changes.md
- audit / action-plan 仍以當下狀態 archive（不可拖）
- 砍掉的項目移至 vol2 ch10 checkpoint 清單

**理由**：voice-corpus 是 rolling 的、emotion-table 是 rolling 的、spec 瘦身可以無限擴大——沒有 deadline 的 audit 會慢慢變成它自己的長期 project，重蹈 vol1-writing §7 的失敗。7 天 deadline 強制收斂。

**為什麼是 7 天而不是 3 或 14**：3 天不夠執行 3 P0 + 2 P1 拍板；14 天會給「再延一下」的藉口。7 天是「壓力剛好夠 + 仍可執行」的中位。

**不選的方案**：
- 無 deadline：見上述
- 「等 P0 都做完才 archive」：開放性過大
- 30 天：等於沒 deadline

## Risks / Trade-offs

- **風險：3 P0 太少，遺漏優化機會**
  - 緩解：vol2 ch10 checkpoint 用真實資料補。延後不等於放棄

- **風險：7 天 deadline 太緊，使用者倉促拍 P1 決定**
  - 緩解：明示 deadline 是設計選擇而非武斷數字；P1 拒絕也是合法決定（不是「必須通過」）

- **風險：top 3 P2 inline 進 ai-session-brief 後，brief 變長**
  - 緩解：inline 三條合計上限 200 字；超過則只保留 1–2 條

- **風險：confidence label 變成保護傘，所有 finding 都標 [inferred] 規避責任**
  - 緩解：[strong] 與 [pattern] 必須引用具體章節編號 / 檔案行號；[inferred] 標籤不能與「必須 / 一定 / 大概率」搭配使用

- **風險：vol1-optimization 修補類型統計拆得太細，§1 變主體**
  - 緩解：限制統計表格 ≤ 1 頁；類別 ≤ 8 類

- **風險：vol2 ch10 checkpoint 到時被忘記跑**
  - 緩解：在 vol2-writing change 的 design.md（若已開）或 `volume-outline-template.md` 加 ch10 checkpoint 提醒；vol2 ch010.md 的章節 metadata 直接寫一行「本章寫完跑 vol2-ch10-checkpoint」

- **Trade-off：放棄完整的設定瘦身**
  - 接受：用 vol2 ch10 引用率掃描代替主觀分級；客觀但延後 2 個月

- **Trade-off：本 change 仍非最簡——8 個 decision 是 audit 內容應有的最小集**
  - 接受：相比前一版（7 個子 decision + 7 條額外 risk）已大幅瘦身；自我誠實的最低門檻是「明顯比前一版瘦」，而非「絕對精簡」

## Self-applied note

本 change 從前一版到此版的瘦身：
- P0：8 → 3（砍 voice-corpus、emotion-distance-table、scene-beat、glossary、mini-sync 獨立化、post-chapter-sync 獨立化）
- P1：5 → 2（砍規則正反對照、spec 瘦身、自動化腳本——全延 checkpoint）
- audit 文件：2 份 → 1 份合併
- Decision：14 個（含 7a–7g）→ 8 個
- 新增：7 天 deadline、confidence label、客觀引用率標準、inline P2

這份修訂套用了 audit 對自己的批評。第二卷起若有第二輪 audit，應該套用同樣的自我約束於那一輪。
