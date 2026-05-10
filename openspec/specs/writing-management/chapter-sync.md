# Chapter Sync

> 章後同步流程。**§A 每章 5 分鐘 quick 版**；**§B 每 10 章 full 版**。
>
> 沿革：原 mini-sync（每 10 章卷中同步）+ post-chapter-sync（章後 reverse-pass）合併為單一文件，於 2026-05-10 依 vol1-2026-05 audit P0-2 建立。
>
> §A 與 §B 不是兩個流程，是同一張表的兩個 cadence——§A 累積結果 = §B 的輸入。

---

## §A：每章 quick 版（5 分鐘 reverse-pass）

每章寫完後立即執行。每題答 ≤ 1 行。發現需回流 spec 即場補。

### Q1：這章有什麼是 spec 沒寫但發生了的？
例：某 NPC 突然有名字、某地點細節原 spec 沒寫、某物品功能擴充。

### Q2：角色講的話有沒有超出 character-card 授權？
語氣、用詞、知識、情緒範圍是否在角色卡定義內。

### Q3：有沒有用到沒寫進 world-rules / cities-guide 的設定？
地理細節、物品、習俗、季節、距離。

### Q4：有沒有暗示一個還沒記入 foreshadowing-tracker 的伏筆？
甚至是「我寫的時候沒意識到，但讀者會記得」的暗示。

### Q5：是否動到了某個追蹤表的欄位但忘記同步？
人物年齡 / 位置 / 能力（→ character-state-cards）、知情狀態（→ info-asymmetry-table）、伏筆狀態（→ foreshadowing-tracker）、事件（→ event-log）、情感距離（若已啟用）。

---

### 回流動作清單（§A 答完後立即執行）

```
本章：第 N 卷第 X 章
日期：YYYY-MM-DD

Q1: [答案 / 無]
Q2: [答案 / 無]
Q3: [答案 / 無]
Q4: [答案 / 無]
Q5: [答案 / 無]

回流動作：
- [ ] [動作 1：例「補入 character-state-cards 塔利欄『右肩練到第二層邊緣』」]
- [ ] [動作 2]
```

---

## §B：每 10 章 full 版（基準掃描 + 開放欄）

每 10 章（ch010、ch020、ch030 …）跑一次。**5 個基準欄位來自 vol1-optimization 修補類型統計**（見 audit §1.2），不是直覺判斷。

### B.1 人物年齡 vs 正文一致性
- 對照來源：最近 10 章正文（含次要人物）
- 對照目標：character-state-cards.md（年齡欄位擁有者）+ family-cards / character-card / past-life-complete 等副本
- 工具：跑 `tools/state_validator.py`（見 P1-A 驗證腳本）；報告任何不一致
- 動作：以 character-state-cards 為擁有者修正所有副本

### B.2 班底知情狀態 vs 最近 10 章一致性
- 對照來源：最近 10 章正文中該角色實際說了 / 看了 / 被告知什麼
- 對照目標：info-asymmetry-table.md（SSOT；其他檔案的知情欄已改為 link）
- 動作：直接更新 info-asymmetry-table；其他檔案因 link 自動跟上

### B.3 伏筆編號去重
- 對照來源：foreshadowing-tracker.md + foreshadowing-list.md
- 檢查：F0XX 編號無重複；新增伏筆已分配連號
- 額外檢查（**P0-3 新增**）：「最遲揭露章 ≤ 當前章 + 10」的 alert 條目——掃描出來、列入下一輪 brief 的「需揭露伏筆」欄

### B.4 event-log「待兌現」欄清理
- 對照來源：event-log-template.md「待兌現的後果」欄
- 動作：本卷已閉合的事件 → 清空該欄；長期未兌現項 → 標「持續累積」或推進到下一輪

### B.5 character-state-cards 增量更新
- 不等卷末才大改；每 10 章把該卷正文已落地的人物變化補入「滾動狀態」段
- 包含：年齡（隨時間自動）、位置變化、能力升級、關係轉變、情緒狀態

---

### B.6【開放欄】本次有沒有發現新類型的不一致？

**這是 mini-sync 鎖死回溯式定義的解藥**。下次出問題的會是還沒被抓過的那種。

```
本次 10 章 sync 發現的新類型不一致：
- [ ] 類型 A：[簡述]
- [ ] 類型 B：[簡述]
- [ ] 無

若有：加入下次 sync 範圍（更新本檔案 §B 加新欄位）。
```

---

### 額外規則：複查 §A 紀錄

跑 §B 時，順便複查最近 10 章的 §A 答題紀錄：
- 連續 5 章以上 Q1-Q5 全答「無」 → 警示：可能是跳檢 / 形式主義
- 對照 §A 標記的回流動作清單，確認都已執行

---

## 觸發時機快查

| 時機 | 動作 |
|------|------|
| 每章寫完 | §A 5 分鐘 reverse-pass |
| ch010 / ch020 / ch030 / ch040 / ... | §B full 版 |
| 卷末 | Chapter Brief 模板的「卷末 sync 必查清單」（不是本檔案） |
