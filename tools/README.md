# tools/

> 小型驗證腳本。Python 3.8+ 標準庫，無外部依賴。

## state_validator.py

驗證人物年齡 / 位置 / 能力欄位在多個檔案間的一致性。

### 用途

使用者選擇「欄位級擁有權 + 驗證腳本」（vol1-2026-05 audit P1-A 分裂執行）：
- **擁有者**：`openspec/specs/writing-management/character-state-cards.md` 末尾的 JSON 區塊
- **副本**：`protagonist-settings/`、`supporting-characters/` 等檔案保留人類可讀的副本
- **腳本**：定期掃描副本是否與擁有者一致，報告偏差（容忍 ±1 歲）

### 執行

```bash
python tools/state_validator.py
```

輸出 `tools/output/state-mismatches.txt`。Exit code 0 = 全部一致；1 = 有不一致。

### 觸發時機

- 每次更新 `character-state-cards.md` 的 JSON 區塊後
- `chapter-sync.md` §B（每 10 章 full sync）執行時
- 卷末 sync 必跑

### v1 範圍（最小實現）

- ✓ 年齡比對（容忍 ±1 歲）
- ✗ 位置比對（v2）
- ✗ 能力比對（v2）
- ✗ 章節 frontmatter 字數/節奏統計（vol2 ch10 checkpoint 後再決定，依 audit）

擴充新欄位時，更新 `extract_*_for()` 函式 + JSON schema。

### 已知限制

- 只看「人物名/別名 ± 30 字內出現的歲數」，可能誤判（例：「父親 38 歲時主角 8 歲」這類複合句會抓到兩個年齡）
- 解決方式：在 `state-mismatches.txt` 報告中人工 triage；偽陽性可加入 ignore list（v2 功能）
