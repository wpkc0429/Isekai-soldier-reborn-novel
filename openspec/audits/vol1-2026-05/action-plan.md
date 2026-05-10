# Vol1 Audit · Action Plan

> 一頁 action plan。**P0 三項**（7 天內完成）/ **P1 兩項**（拍板後 7 天內完成，逾期砍）/ **P2 inline**（已內嵌 vol2 第一份 brief）/ **Vol2 ch10 checkpoint 待評估清單**。
>
> Apply 起算日：**2026-05-10**。Deadline：**2026-05-17**。

## P0 — 7 天內必做

| # | 動作 | 驗證 | 狀態 |
|---|------|------|------|
| P0-1 | Chapter Brief 整併（pre-chapter-checklist + ai-session-brief 合併為單一一張紙；舊 checklist 改 stub） | `ai-session-brief.md` 為單頁、含 7 項硬性確認 + 末尾「章寫完跑 chapter-sync.md quick 版」；CLAUDE.md「開始寫一章前必做」改為「填一張 Chapter Brief」 | ✓ |
| P0-2 | `writing-management/chapter-sync.md`（合併 post-chapter-sync 5 問 + mini-sync 5 欄位 + 開放欄） | §A 每章 5 分鐘 reverse-pass 5 題；§B 每 10 章 5 欄位掃描 + §B.6 開放欄「本次有沒有發現新類型不一致」；§B 5 欄位明示「來自 vol1-optimization 修補類型統計，非直覺」 | ✓ |
| P0-3 | foreshadowing 截止日欄（tracker + list 各加「最遲揭露章」+ alert 規則） | 17 條伏筆全部填值；alert 規則寫入「最遲揭露章 ≤ 當前章 + 10」掃描；chapter-sync.md §B 引用此規則 | ✓ |

## P1 — 拍板後 7 天內完成；逾期砍移 checkpoint

| # | 動作 | 使用者決定 | 狀態 |
|---|------|----------|------|
| P1-A | **分裂執行**：知情狀態做 SSOT（`info-asymmetry-table.md` = 唯一來源；event-log/foreshadowing-tracker/team-dynamics/character-state-cards 知情欄改 link）；年齡/位置/能力**不做檔案級 SSOT**，改「欄位級擁有權 + 驗證腳本」 | 執行（分裂） | ✓ |
| P1-B | git mv `specs/vol1-chapters/ch001-055.md` → `manuscript/vol1/`；specs 樹只留 metadata index | 執行 | ✓ |

## P2 — Top 3 已 inline 進 vol2 第一份 ai-session-brief（不開新檔案、不靠連結）

| # | 動作 | 已 inline 位置 |
|---|------|--------------|
| P2-1 | 第二卷必須安排至少 2 次「主角會失敗 / 計算錯」的場景 | `ai-session-brief.md` §「本卷重點提醒」 |
| P2-2 | 賽門 / 艾拉前 20 章內各有一次完整的「正面戲」（對話 + 共同行動） | 同上 |
| P2-3 | 替「他把這個收進去 / 放著 / 過一遍」找替代收束工具，每三章至少一章用「外部事件 / 對話 / 動作」收尾 | 同上 |
| P2-4（不 inline） | 第二卷 ch001 必須在前 1000 字內讓「會看天氣的孩子」鉤子有後續 | 留在 action-plan 與 vol2 outline |

## Vol2 ch10 Checkpoint — 真實資料判斷

> 第二卷寫到 ch010 時觸發。屆時跑「正文引用率掃描」（自動），對每份 spec 統計被引用次數，零引用 = P3 候選。其餘以 vol2 前 10 章工作流實際運作資料判斷以下項目是否啟動：

- [ ] glossary 三欄擴充（看是否真的需要「跨多檔查塔利現在在哪」）
- [ ] scene-beat template（看 vol2 前 10 章是否仍貼底字數）
- [ ] voice-corpus（先試 5 段試水）
- [ ] emotion-distance-table（先試 3 對 × 試 10 章）
- [ ] 規則正反對照（先處理當前最常違反的 3 條禁令）
- [ ] spec 瘦身（用引用率掃描客觀分級，不主觀分級）
- [ ] 自動化腳本擴充（v1 字數統計已隨 P1-A 提早出現；v2 待 frontmatter 統一）

## Stop condition

本 change（vol1-review-and-architecture-audit）必須在 `/opsx:apply` 後 7 天內 archive。逾期：
- 未完成的 P1 自動標記為 `cut`，移入 vol2 ch10 checkpoint 清單
- audit / action-plan 仍以當下狀態 archive
- 記入 `writing-management/timeline-changes.md`
