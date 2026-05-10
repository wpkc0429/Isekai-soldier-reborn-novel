#!/usr/bin/env python3
"""一次性腳本：從 manuscript/vol1/ch*.md 抽 metadata 產生 vol1-chapters/index.md。"""
import io
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "manuscript/vol1"
OUT = ROOT / "openspec/specs/vol1-chapters/index.md"

rows = []
for f in sorted(SRC.glob("ch*.md")):
    text = f.read_text(encoding="utf-8")
    chno = int(f.stem.replace("ch", ""))
    title_m = re.search(r"章節標題\s*\|\s*(.+?)\s*\|", text)
    rhythm_m = re.search(r"節奏標記\s*\|\s*(.+?)\s*\|", text)
    target_m = re.search(r"目標字數\s*\|\s*(.+?)\s*\|", text)
    actual_m = re.search(r"實際字數\s*\|\s*(.+?)\s*\|", text)
    rows.append({
        "no": chno,
        "title": title_m.group(1) if title_m else "?",
        "rhythm": rhythm_m.group(1) if rhythm_m else "?",
        "target": target_m.group(1) if target_m else "?",
        "actual": actual_m.group(1) if actual_m else "?",
    })

with OUT.open("w", encoding="utf-8") as f:
    f.write("# vol1-chapters / Index\n\n")
    f.write("> 第一卷 55 章的 metadata 索引。**正文已搬至 [`manuscript/vol1/`](../../../manuscript/vol1/)**（依 vol1-2026-05 audit P1-B）。\n\n")
    f.write("> 本檔案是純索引，不放正文。重新產生請跑 `python tools/build_vol1_index.py`。\n\n")
    f.write("## 章節索引\n\n")
    f.write("| # | 標題 | 節奏 | 目標字數 | 實際字數 | 正文檔案 |\n")
    f.write("|---|------|------|---------|---------|---------|\n")
    for r in rows:
        link = f"[ch{r['no']:03d}.md](../../../manuscript/vol1/ch{r['no']:03d}.md)"
        f.write(f"| {r['no']} | {r['title']} | {r['rhythm']} | {r['target']} | {r['actual']} | {link} |\n")
    f.write(f"\n共 {len(rows)} 章。\n")

print(f"✓ 已寫入 {OUT.relative_to(ROOT)}（共 {len(rows)} 章）")
