# CLAUDE.md

## 專案說明

這是一部長篇小說的撰寫專案。

- **類型**：異世界重生（同一個世界，重生回自己的童年）
- **主角**：艾登・莫爾，普通士兵，23歲死於石河谷之戰，重生回8歲，帶著完整的前世記憶
- **規模**：100萬字，5卷，約333章，每章平均3,000字
- **核心主題**：不是征服世界，而是建立根基、保護家人、傳承知識

---

## 目錄結構

```
openspec/specs/               ← 所有設定文件（已發布）
├── world-settings/           ← 地理、歷史、城市、勢力、世界規則
├── protagonist-settings/     ← 主角設定（前世記憶、角色卡、成長路線、戰鬥時間線）
├── supporting-characters/    ← 配角（家人、班底、反派、NPC）
├── faction-politics/         ← 四大勢力的政治分析
├── magic-power-system/       ← 力量體系與覺醒機制
├── plot-structure/           ← 各卷章節大綱、伏筆清單、感情線
├── writing-style-guide/      ← 寫作規範、名詞對照表、試寫稿
├── writing-management/       ← 撰寫管理模板（日誌、日曆、角色狀態卡等）
└── vol1-chapters/            ← 純 metadata 索引（正文不在這裡）

manuscript/                   ← 章節正文（依 vol1-2026-05 audit P1-B）
└── vol1/                     ← 第一卷 55 章 ch001.md – ch055.md

openspec/audits/              ← 時點性診斷快照（不進 spec 樹）
└── vol1-2026-05/             ← 第一卷品質與架構審查（audit + action-plan）

tools/                        ← 驗證腳本（state_validator、build_vol1_index）
```

---

## 寫作規則

### 基調
- **克制，不沉悶**——情感靠具體感知細節呈現，不靠大段心理描寫
- **每章必須有「往前拉」的元素**——懸念、期待或情緒餘韻
- 敘事視角：**限制第三人稱**，緊貼主角視角

### 前世記憶的呈現
- 不用系統框框，不說「觸發前世記憶」
- 呈現**判斷和行動**，不解釋來源
- 每次前世記憶片段不超過3句，立刻回到當下

### 對白
- 少但精準，每句都有功能
- 主角說話老成，不解釋，讓對方填空

### 情感表達
- 不說「我愛你」，說「你受傷了，進來我幫你看」
- 情感高點用更少的文字

### 章節字數
- 正常章節：2,500–3,500字
- 不得低於2,500字，不得超過4,000字

---

## 開始寫一章前必做

**填一張 Chapter Brief**：`openspec/specs/writing-management/ai-session-brief.md`（單頁，含上半段 brief + 下半段 7 項硬性確認 + 本卷重點提醒）。

引用的兩個 SSOT：
- `character-state-cards.md` —— 人物年齡 / 位置 / 能力（欄位級擁有者）
- `info-asymmetry-table.md` —— 知情狀態（檔案級 SSOT）

## 章寫完後必做

跑 `openspec/specs/writing-management/chapter-sync.md` §A 的 5 題 quick 版（5 分鐘 reverse-pass）。每 10 章跑一次 §B 的 full 版。

---

## 快速參考索引

| 需要查什麼 | 去哪裡找 |
|-----------|---------|
| 人名/地名標準寫法 | `writing-style-guide/terminology-glossary.md` |
| 主角的完整背景 | `protagonist-settings/past-life-complete.md` |
| 主角的性格與底線 | `protagonist-settings/character-card.md` |
| 各卷章節大綱 | `plot-structure/vol1-chapter-outline.md` 等 |
| 某個配角的詳細設定 | `supporting-characters/<角色名>-card.md` |
| 各卷伏筆的埋設與揭露 | `plot-structure/foreshadowing-list.md` |
| 感情線進度 | `plot-structure/romance-timeline.md` |
| 力量等級對照 | `magic-power-system/power-level-table.md` |
| 政治派系分析 | `faction-politics/daylon-internal-factions.md` |
| 節奏追蹤 | `writing-management/rhythm-tracker.md` |
| 已改變的時間線 | `writing-management/timeline-changes.md` |
| 各角色知道多少秘密 | `writing-management/info-asymmetry-table.md` |

---

## 重要設定摘要

### 主角的力量成長
- 12歲：武者覺醒
- 16歲：菁英武者
- 18-19歲：覺醒者（感知系，刺殺觸發）
- 全書不是最強的人，但「用力量最有效率的人」

### 石河谷之戰
- 前世：帝曆261年全軍覆沒
- 本世：帝曆273年，目標是「代價超出帝國預期，暫停吞併計劃」
- 主角此時23歲

### 核心班底（完整名單）
塔利、賽門、艾拉・布蘭、凱斯・多蘭、尤拉

### 梅拉的特殊原則
她是主角唯一「不在任何計劃裡」的人，寫她的場景時主角不做評估和計算。

---

## 禁止事項

- 不加系統框框或數值通知
- 不讓主角做大段的自我解釋式內心獨白
- 不讓任何人說出「因為前世記憶，所以……」這樣的句子
- 不讓主角對梅拉進行策略性評估
- 連續3章以上相同節奏標記（▲▲▲ 或 ▼▼▼）需要打破

---

## 寫作管理模板位置

| 模板 | 用途 |
|------|------|
| `writing-management/event-log-template.md` | 記錄重要事件與知情者 |
| `writing-management/foreshadowing-tracker.md` | 追蹤未兌現伏筆 |
| `writing-management/timeline-changes.md` | 記錄時間線改變節點 |
| `writing-management/story-calendar.md` | 故事內部時間對照 |
| `writing-management/rhythm-tracker.md` | 情感節奏追蹤 |
| `writing-management/character-registry.md` | 人物名冊（A/B/C級） |
