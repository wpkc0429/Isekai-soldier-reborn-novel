## Why

第一卷的設定文件已完備，需要正式開始撰寫第一卷正文（第1-55章），並在撰寫過程中同步維護管理文件（事件日誌、伏筆追蹤、時間線節點、人物狀態卡）。

## What Changes

- 撰寫第一卷全部55章正文（約165,000字）
- 每章完成後更新事件日誌、伏筆追蹤器、故事日曆
- 每卷結束後更新人物狀態卡
- 發現設定不足或需補充時，同步更新對應的設定文件

## Capabilities

### New Capabilities

- `vol1-chapters`: 第一卷正文章節（第1-55章的實際文字內容）

### Modified Capabilities

- `writing-management`: 新增實際填寫的日誌內容（事件日誌、伏筆追蹤、時間線節點、人物狀態卡各卷末更新）
- `plot-structure`: 撰寫過程中若章節細節需要調整，更新各卷章節大綱

## Impact

- 新增 `openspec/specs/vol1-chapters/` 目錄，存放各章節正文
- 撰寫過程中可能小幅修改現有設定文件以填補細節空白
- 每章完成後需更新 `writing-management/` 下的管理模板
