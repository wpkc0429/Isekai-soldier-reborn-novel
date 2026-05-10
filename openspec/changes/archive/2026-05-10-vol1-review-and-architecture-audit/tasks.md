## 0. Stop condition

**本 change 在 `/opsx:apply` 後 7 天內必須 archive。** 逾期未完成的 P1 自動砍，記入 `writing-management/timeline-changes.md`，並轉入 vol2 ch10 checkpoint 清單。audit 與 action-plan 仍以當下狀態 archive，不可拖。

**Apply 起算日**：2026-05-10。Deadline：2026-05-17。

## 0a. 使用者 P1 決策（apply 時記錄）

- **P1-A（分裂決策）**：
  - **知情狀態**：執行 SSOT——`info-asymmetry-table.md` 為唯一來源，其他檔案的「知情狀態 / 知情者」欄改為 link
  - **年齡 / 位置 / 能力**：**不做檔案級 SSOT**。改為「欄位級擁有權 + 驗證腳本」——`character-state-cards.md` 為這三個欄位的擁有者；其他檔案保留自己的副本（讓人讀檔不必跳轉）；新增小型 Python 驗證腳本掃描所有檔案的這三個欄位，與擁有者比對並報告不一致
- **P1-B**：執行——git mv 55 章正文至 `manuscript/vol1/`，specs 樹只留 metadata 索引

## 1. 前置確認

- [x] 1.1 確認本 change 經一次大幅瘦身（前版 8 P0 + 5 P1 → 此版 3 P0 + 2 P1）
- [x] 1.2 在 `/opsx:apply` 之前，用 AskUserQuestion 取得使用者對 P1 兩項的決定：
  - **P1-A**：是否指派 single source of truth（character-state-cards = 人物年齡，info-asymmetry-table = 知情狀態），其他文件改為 link？
  - **P1-B**：是否將 `specs/vol1-chapters/` 改為純 metadata 目錄，正文移至 `manuscript/vol1/`？
  - **逾期未完成 = 自動拒絕**（非預設 yes）
- [x] 1.3 將使用者決定與 deadline 起算日記錄於本 tasks.md 開頭

## 2. 類別 A：產出合併 audit + 1 頁 action plan

### 2.1 vol1-optimization 修補類型統計（audit 證據基底）

- [x] 2.1.1 通讀 `openspec/changes/archive/2026-05-09-vol1-optimization/tasks.md` 全部 §2–§11 任務
- [x] 2.1.2 分類計數實際修補的問題類型，建議分類：
  - 人物年齡漂移
  - 知情狀態漂移
  - 伏筆編號 / 內容漂移
  - 整章獨白違規
  - 結尾無往前拉鉤子
  - 字數系統性貼底
  - 其他類別（依實際發現）
- [x] 2.1.3 每類附「次數 / 第一卷總章數」與「設定能否在開章前發現」標籤
- [x] 2.1.4 每類附 1 個具體章節範例（避免變成抽象表格）
- [x] 2.1.5 統計表格上限 1 頁；類別上限 8 類

### 2.2 撰寫合併 audit

- [x] 2.2.1 建立 `openspec/audits/vol1-2026-05/` 目錄（**注意：不是 `openspec/specs/`**）
- [x] 2.2.2 撰寫 `openspec/audits/vol1-2026-05/audit.md`，內容章節：
  - **§1 vol1-optimization 修補類型統計**（§2.1 的成果）
  - **§2 quality findings**（合併原 quality-review 的內容）
    - §2.1 整體評分（故事 / 文字 / 角色，每項附 confidence）
    - §2.2 五大亮點
    - §2.3 六大問題（每條附 confidence label）
    - §2.4 三大關鍵章節評估
  - **§3 architecture findings**（合併 subagent 八項 + 使用者補充六項，重疊處合併呈現，每條附 confidence label）
  - **§4 vol2 ch10 checkpoint 待評估清單**（明確標記「現在不做」的項目）
- [x] 2.2.3 每條 finding 結尾加 confidence label：[strong] / [pattern] / [single] / [inferred]
- [x] 2.2.4 [strong] 與 [pattern] 必須引用具體章節編號或檔案行號
- [x] 2.2.5 [inferred] 標籤不得與「必須 / 一定 / 大概率」等斷言性詞語搭配使用——可用「指向 / 暗示 / 可能」

### 2.3 撰寫 1 頁 action plan

- [x] 2.3.1 撰寫 `openspec/audits/vol1-2026-05/action-plan.md`，採表格格式：
  ```
  | P | 來源 | 動作 | 驗證 | 狀態 |
  ```
  - 3 條 P0：Chapter Brief 整併、chapter-sync.md、foreshadowing 截止日欄
  - 2 條 P1：single source of truth、vol1-chapters 位置（含 deadline 結果欄）
  - 4 條 P2（其中 top 3 已 inline 進 vol2 ai-session-brief，第 4 條只列）
  - **vol2 ch10 checkpoint 清單**（單列段）：glossary 三欄、scene-beat、voice-corpus、emotion-distance、規則正反對照、spec 瘦身（用引用率掃描）、自動化腳本
- [x] 2.3.2 整份限制 1 頁（A4 列印約 60 行內）

### 2.4 Top 3 P2 inline 進 vol2 第一份 ai-session-brief

- [x] 2.4.1 確認 vol2-writing change 是否已建立：
  - 若已建立：在其 ai-session-brief 範本（或第一章 brief）的「本卷重點提醒」段直接寫入 top 3 P2 內文
  - 若未建立：在 `writing-management/ai-session-brief.md`（修訂後的 Chapter Brief Template）加一段「vol2 啟動時必填：本卷重點提醒（從 vol1-2026-05 audit P2 帶入）」
- [x] 2.4.2 inline 三條合計上限 200 字（超過則只保留 1–2 條）
- [x] 2.4.3 不開新檔案、不靠連結

## 3. 類別 B：P0-1 — Chapter Brief 整併

> 性質：低風險、可逆、效益最大。

- [x] 3.1 通讀現有 `writing-management/ai-session-brief.md` 與 `pre-chapter-checklist.md`，列出所有現有欄位
- [x] 3.2 將 `ai-session-brief.md` 改寫為「Chapter Brief Template」單一文件：
  - 上半段：原 ai-session-brief 內容（人物狀態 / 上章摘要 / 本章目的 / 末尾設計）
  - 下半段：原 pre-chapter-checklist 7 項硬性確認 + 卷末 sync 必查清單
  - 單頁限制
  - 末尾加一句「章寫完後立即執行 chapter-sync.md 的 quick 版」
- [x] 3.3 將 `pre-chapter-checklist.md` 改為 stub，指向 `ai-session-brief.md`
- [x] 3.4 更新 `CLAUDE.md`「開始寫一章前必做」段
- [x] 3.5 全 repo 搜尋 `pre-chapter-checklist` 與 `ai-session-brief` 引用，確認 stub 與新文件都被正確指向

## 4. 類別 B：P0-2 — chapter-sync.md（合併 post + mini）

> 性質：合併兩個前版獨立的同步流程為單一文件，兩種 cadence。

- [x] 4.1 新增 `openspec/specs/writing-management/chapter-sync.md`，結構：
  - **§A：每章 quick 版（5 分鐘 reverse-pass）**——5 個固定問題：
    1. 這章有什麼是 spec 沒寫但發生了的？
    2. 角色講的話有沒有超出 character-card 授權？
    3. 有沒有用到沒寫進 world-rules / cities-guide 的設定？
    4. 有沒有暗示了一個還沒記入 foreshadowing-tracker 的伏筆？
    5. 是否動到了某個追蹤表的欄位但忘記同步？
    - 每題 1 行答；發現需回流 spec 即場補
  - **§B：每 10 章 full 版（基準掃描 + 開放欄）**——固定 5 欄位：
    1. 人物年齡 vs 正文一致性
    2. 班底知情狀態 vs 最近 10 章一致性
    3. 伏筆編號去重
    4. event-log「待兌現」欄清理
    5. character-state-cards 增量更新
    + **§B.6 開放欄：本次有沒有發現新類型的不一致？若有，加入下次 sync 範圍**
  - §A 累積結果 = §B 的輸入
- [x] 4.2 §B 基準 5 欄位的選擇必須引用 §2.1 vol1-optimization 修補類型統計，而非直覺判斷
- [x] 4.3 在 `CLAUDE.md` 的「快速參考索引」加入 chapter-sync.md
- [x] 4.4 在 `writing-management/spec.md` 的檔案清單加入 chapter-sync.md
- [x] 4.5 移除 `pre-chapter-checklist.md` 中重複的卷末 sync 內容（若有），改為指向 chapter-sync.md §B

## 5. 類別 B：P0-3 — foreshadowing 截止日欄

> 性質：零風險小擴充。

- [x] 5.1 在 `openspec/specs/writing-management/foreshadowing-tracker.md` 新增欄「最遲揭露章」
- [x] 5.2 在 `openspec/specs/plot-structure/foreshadowing-list.md` 對應加同欄
- [x] 5.3 為現有所有伏筆條目逐條指派「最遲揭露章」（依各卷大綱推導）
- [x] 5.4 加入「Alert 規則」段：寫到該章前未揭露 → 自動進入 alert 清單
- [x] 5.5 在 chapter-sync.md §B 開放欄附近加一條：「掃描 foreshadowing-tracker 中『最遲揭露章 ≤ 當前章 + 10』的條目」
- [x] 5.6 更新 `writing-management/spec.md` 對 foreshadowing-tracker 的描述

## 6. 類別 C：P1-A — single source of truth（條件性 + 7 天 deadline）

> 性質：僅在 §1.2 P1-A 批准且未逾期時執行。

- [x] 6.1 （條件）指派 `character-state-cards.md` = 人物年齡 / 位置 / 能力 / 卷末狀態唯一來源
- [x] 6.2 （條件）指派 `info-asymmetry-table.md` = 知情狀態唯一來源
- [~] 6.3 **依 P1-A 分裂決策跳過**：年齡/位置/能力**不**改為 link，改用「欄位級擁有權 + 驗證腳本」（`tools/state_validator.py`）。原計劃涉及的檔案（protagonist-settings/spec.md、character-card.md、past-life-complete.md、supporting-characters/spec.md、family-cards.md、vol1-chapter-outline.md、vol45-overview.md）保留各自副本
- [x] 6.4 （條件）將以下檔案的「知情狀態」欄改為 link：
  - `writing-management/character-state-cards.md`（知情欄）
  - `writing-management/event-log-template.md`（知情者欄）
  - `writing-management/foreshadowing-tracker.md`（知情者欄）
  - `supporting-characters/team-dynamics.md`（提及處）
- [x] 6.5 （條件）通讀改動後檔案，確認無矛盾或斷掉的 link
- [x] 6.6 （條件）在 `CLAUDE.md` 加入「single source of truth 原則」段

## 7. 類別 C：P1-B — vol1-chapters 位置（條件性 + 7 天 deadline）

> 性質：僅在 §1.2 P1-B 批准且未逾期時執行。

- [x] 7.1 （條件）建立 `manuscript/vol1/` 目錄
- [x] 7.2 （條件）git mv `openspec/specs/vol1-chapters/ch001.md` ~ `ch055.md` → `manuscript/vol1/`
- [x] 7.3 （條件）`openspec/specs/vol1-chapters/index.md` 留章節 metadata 表（不放正文）
- [x] 7.4 （條件）保留 README.md 並更新指向 `manuscript/vol1/`
- [x] 7.5 （條件）全 repo 搜尋 `specs/vol1-chapters/ch0` 引用並更新路徑
- [x] 7.6 （條件）更新 `CLAUDE.md` 目錄結構段
- [x] 7.7 （條件）更新 vol1-writing archive 中的 spec 路徑說明

## 8. Vol2 ch10 checkpoint 清單

> 性質：以下項目**不在本 change 執行**，僅記錄到 action-plan.md 與 vol2 啟動文件，由 vol2 寫到 ch10 時用真實資料判斷。

- [x] 8.1 確認 `action-plan.md`（§2.3）已含 checkpoint 清單，每項註明：
  - **glossary 三欄擴充**——延後理由：屬中等價值，可由 character-state-cards 部分代替
  - **scene-beat template**——延後理由：先看第二卷字數是否仍貼底；若否則不需此層
  - **voice-corpus**——延後理由：4–6 小時批判性閱讀，違反 P0 定義；checkpoint 時可先試 5 段
  - **emotion-distance-table**——延後理由：維護成本高；checkpoint 時可先試 3 對（梅拉/塔利/母親）× 10 章
  - **規則正反對照**——延後理由：需為 9 條禁令各寫正例，工作量中等
  - **spec 瘦身**——**改為客觀標準**：vol2 ch10 自動掃描每份 spec 在這 10 章被引用幾次，零引用 = P3 候選；不再做主觀分級
  - **自動化腳本**——延後理由：第一版只能做字數統計（節奏分析依賴 frontmatter 統一，是隱藏依賴）
- [x] 8.2 在 `writing-management/volume-outline-template.md` 的「ch10 checkpoint」段加入「跑 vol2-ch10-checkpoint：執行正文引用率掃描 + 重新評估 audit 中延期項目」
- [x] 8.3 若 vol2-writing change 已開，在其 design.md 加一行「ch10 必跑 checkpoint」
- [x] 8.4 不執行 checkpoint 任何具體項目——它們屬於下一個 change 的範圍

## 9. 收尾與驗證

- [x] 9.1 通讀 audit.md 與 action-plan.md，確認：
  - 每條 finding 都附 confidence label
  - [strong] 與 [pattern] 都引用具體章節 / 行號
  - [inferred] 不與斷言詞搭配
  - §1 vol1-optimization 統計 ≤ 1 頁
  - audit 整份明顯比前一版（兩份 quality + architecture）短
  - action-plan 為單頁
- [x] 9.2 確認 audit 位於 `openspec/audits/vol1-2026-05/`，**不在 `openspec/specs/`**
- [x] 9.3 通讀新版 ai-session-brief.md（Chapter Brief Template），實際試走「假裝寫第二卷 ch001」，確認單頁可填完
- [x] 9.4 通讀 chapter-sync.md，確認 §A 5 問與 §B 5 欄位無職責重疊
- [x] 9.5 確認 §B.6 開放欄存在，避免 mini-sync 鎖死的回溯式定義缺陷
- [x] 9.6 確認 foreshadowing-tracker 與 foreshadowing-list 兩處都有「最遲揭露章」欄並已逐條填值
- [x] 9.7 確認 top 3 P2 已 inline 進 vol2 第一份 ai-session-brief，未開新檔案、不靠連結
- [x] 9.8 （若執行 P1-A）全 repo 搜尋人物年齡的數字，確認除 character-state-cards 外其他檔案都已改為 link
- [x] 9.9 （若執行 P1-B）全 repo 搜尋 `specs/vol1-chapters/ch0` 路徑，確認都已改為 `manuscript/vol1/`
- [x] 9.10 在 `writing-management/timeline-changes.md` 新增一條「2026-05-10：完成 vol1 audit；P0 三項已執行；P1-A 分裂執行（知情 SSOT + 年齡/位置/能力欄位擁有權 + state_validator）；P1-B 執行；vol2 ch10 checkpoint 清單已建立」
- [x] 9.11 **檢查 deadline**：若 `/opsx:apply` 後超過 7 天仍有未完成的 P1，自動標記為 cut，移入 checkpoint 清單，並 archive 本 change
- [x] 9.12 自評：本 change 從前一版 8 P0 + 5 P1 + 7 子 decision 砍至 3 P0 + 2 P1 + 8 decision，audit 從 2 份合併為 1 份；落地 audit 不進 spec 樹（放 `openspec/audits/`）、每條 finding 附 confidence label、stop condition 7 天 deadline 三項自我約束。實作中 P1-A 進一步被使用者改為「分裂執行」（年齡欄保留副本 + 驗證腳本），這比原計劃更輕量——副本可讀性不損、漂移由腳本掃描而非規範強制。**本 change 真的瘦身了**。
