## Why

第一卷 55 章已撰寫完畢。通讀樣本（ch001/020/025/033/041/052/053/054/055）並比對管理文件後，發現兩類性質不同的優化空間：

**類別 A：管理文件的補同步**

依本專案的工作流（CLAUDE.md 與 vol1-writing/design.md Decision 3）：
- 正文是事實源
- 管理文件（`writing-management/`）與設定文件（`protagonist-settings/` 等）跟著正文走，撰寫中發現空白就直接在 spec 補
- vol1-writing tasks.md §7 是「卷末同步」的一次性任務，已標記完成

但這個卷末同步沒跑徹底，留下幾處正文與管理/設定文件互相不一致的尾巴：
- 妹妹莉亞年齡：原設定 6 歲，正文 ch001 已落地為「一歲多」，設定沒回頭更新
- ch052 主角對塔利說「重生」這個詞，但 `info-asymmetry-table.md` 的「永遠不知道」表還寫著「直到第 5 卷塔利才知道」
- `info-asymmetry-table.md` 第一卷結束欄寫「塔利知道主角武者覺醒」，但 ch041 主角刻意對塔利隱藏覺醒
- `foreshadowing-tracker.md` F009 編號重複（同號兩行）

這不是「bug 修復」，是 vol1-writing §7 沒做完的延伸維護。但若不收尾，第二卷起每寫一章都要先決定「以哪個為準」，反覆的隱性對齊成本會比一次性同步高得多。

**類別 B：章節層級的文體飄移**

這是與設定同步無關的、純粹章節品質的問題：
- 字數曲線：ch029 起 27 章全部寫到 2,500 字下限（少約 14,000 字）——後半卷系統性貼底
- 整章內心獨白：ch033（格子系統列表）、ch043（試手獨白）、ch047（不是現在的內心宣告）、ch053（全章列表盤點）、ch055（卷末純內心收束）違反 `internal-monologue-guide.md` 與 CLAUDE.md「不讓主角做大段的自我解釋式內心獨白」的禁令
- 卷末沒有「往前拉」鉤子：ch055 結尾「往下走就好了」是封閉式收束，違反「每章結尾必須有往前拉的元素」
- 重複成型語：「讓 X 在 Y 裡待一下／沉下去／存進去」、「在腦子裡過了一遍」在後半卷反覆出現

這類問題本身不會被「設定文件跟著章節更新」的工作流自動修掉，需要重寫。

## What Changes

### 類別 A：補完 vol1-writing §7 沒跑完的同步

- 統一妹妹莉亞的年齡：以正文（ch001 一歲多 → ch050 八歲，比主角小 6–7 歲）為準，回頭更新所有設定文件（character-card、family-cards、past-life-complete、character-state-cards、vol1-chapter-outline ch2、protagonist-settings/spec.md、vol45-overview）
- 同步 `info-asymmetry-table.md` 與正文事實：塔利在第一卷末的知情狀態（不知覺醒、知道重生）；移除/修改「永遠不知道」表中已被 ch052 推翻的條目
- 同步 `character-state-cards.md` 第一卷結束欄，使其與 info-asymmetry-table 互相一致
- 移除 `foreshadowing-tracker.md` 中 F009 的重複行，並比對 event-log 補入遺漏的伏筆條目
- 重新評估 F006「前次那樣的結果」失言在第五卷的設計：因為 ch052 已揭露重生，原計劃「第五卷塔利問話才知道死過一次」需要調整

### 類別 B：鎖定 6 章重寫，把文體飄移拉回標準

依「整章超過 50% 為主角內心活動或列表式自我盤點」**或**「結尾沒有往前拉的鉤子」二擇一的硬指標，鎖定六章：
- **ch033「計劃外的人」**：刪減「格子系統」清單列舉，改以梅拉的具體動作展現「這個格子填不下去」
- **ch043「試探」**：壓縮策略獨白，補環境感知與塔利的觀察反應
- **ch047「只需要知道」**：把「不是現在」的內心確認改寫為一個外部觸發場景
- **ch052「你想幹嘛」**：對白瘦身（去除「我確認了哪些說了哪些沒說」的後設總結），保留塔利「我跟著你」的力道
- **ch053「第一卷總結」**：取消「全章獨白盤點」結構，改以一個下午的具體場景（父親擦馬具、塔利磨石頭、妹妹追貓）承載相同的進度確認
- **ch055「現在開始」**：去掉內心列表，補一個外部鉤子（信件／父親提的明年客人／塔利的觀察），結尾要有明確的「往前拉」

### 類別 C：把這次的教訓寫進 checklist，讓問題不再復發

- 在 `pre-chapter-checklist.md` 增列兩個硬性檢查項：「本章是否有外部場景（不能整章為主角內心）？」「結尾最後一個意象是否帶有懸念、期待或情緒餘韻？」
- 在 `rhythm-tracker.md` 補一條：卷末連續 ▼▼ 收束時，最後一章必須在尾段補一個外部信號，不能以純內心宣告作結
- 在 `vol1-writing` 的 §7 模板裡（如有沿用到下卷）補上「sync 必查清單」：莉亞年齡這類設定 vs 正文的逐項比對，不只是「確認伏筆已記錄」這種單向動作

## Capabilities

### Modified Capabilities

- `vol1-chapters`：6 章（ch033/043/047/052/053/055）的正文內容更新；其他章節不動
- `protagonist-settings`：妹妹年齡欄位回頭同步至正文事實
- `supporting-characters`：family-cards 莉亞年齡欄位同步
- `plot-structure`：vol1-chapter-outline ch2 與 vol45-overview 妹妹年齡同步、foreshadowing-list 與 tracker 同步
- `writing-management`：character-state-cards、info-asymmetry-table、foreshadowing-tracker 同步至卷末事實；pre-chapter-checklist、rhythm-tracker 補硬性檢查項

### New Capabilities

- 無（純同步 + 重寫 + checklist 補強）

## Impact

- **這個 change 不在挑 vol1-writing 的錯**——而是把它的 §7 補到位，並處理 §7 範圍外的章節層級問題
- **6 章重寫的字數預期**：每章從 ~2,500 字提升到 2,800–3,200 字，補回約 3,000–4,000 字的內容密度（不嘗試補滿少寫的 14,000 字）
- **不重寫 ch001–ch032 與大部分中段章節**：以 ch001、ch014、ch025 等樣本確認品質達標
- **不延遲第二卷**：完成後即可開始 vol2-writing；第二卷的 ai-session-brief 可以直接信任管理文件，不必每次重新對齊
- **ch052「重生」揭露的處理**：保留為預設（方案 A）。若使用者選擇收回（方案 B），需多重寫一段對白，視 `/opsx:apply` 前的確認結果
