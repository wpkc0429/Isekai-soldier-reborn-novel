## ADDED Requirements

### Requirement: 第一卷章節正文

每章正文 SHALL 存放在獨立的 `.md` 檔案中，路徑格式為 `specs/vol1-chapters/ch001.md`（三位數字編號）。

每章檔案 SHALL 包含以下開頭資訊：
- 章節號與卷次
- 章節標題
- 帝曆時間
- 主角年齡
- 節奏標記（▲/→/▼）
- 目標字數與實際字數

#### Scenario: 章節檔案格式
- **WHEN** 建立新章節檔案
- **THEN** 檔案開頭包含標準資訊區塊，正文緊接其後

#### Scenario: 字數範圍
- **WHEN** 章節正文完成
- **THEN** 字數在 2,500–3,500 字之間（特殊章節允許至 4,000 字）

### Requirement: 章節正文寫作規範

正文 SHALL 遵循 `writing-style-guide/` 下定義的全部規範：
- 限制第三人稱視角，緊貼主角
- 前世記憶每次不超過 3 句，立刻回到當下
- 情感靠具體感知細節呈現，不靠大段心理描寫
- 每章結尾 SHALL 有「往前拉」的元素

#### Scenario: 前世記憶呈現
- **WHEN** 章節中需要呈現主角的前世知識
- **THEN** 以判斷和行動體現，不出現「因為前世記憶所以……」的句式

#### Scenario: 章節結尾
- **WHEN** 章節正文結束
- **THEN** 最後一個意象或句子帶有懸念、期待或情緒餘韻，讓讀者想繼續讀

### Requirement: 管理文件同步更新

每章完成後 SHALL 立即更新以下管理文件：
- `writing-management/event-log-template.md`：記錄本章新增事件
- `writing-management/foreshadowing-tracker.md`：記錄新埋伏筆或揭露伏筆
- `writing-management/story-calendar.md`：確認時間錨點一致
- `writing-management/rhythm-tracker.md`：記錄本章節奏標記

#### Scenario: 新事件記錄
- **WHEN** 章節中發生重要事件（改變人物關係、改變局勢、知情者新增）
- **THEN** 在事件日誌新增一行，包含章節號、事件描述、知情者、待兌現後果

#### Scenario: 伏筆更新
- **WHEN** 章節中埋設新伏筆或揭露既有伏筆
- **THEN** 在伏筆追蹤器更新對應欄位的狀態
