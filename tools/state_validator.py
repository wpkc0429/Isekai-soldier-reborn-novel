#!/usr/bin/env python3
"""
state_validator.py — 驗證人物年齡 / 位置 / 能力欄位的一致性

來源（唯一）：openspec/specs/writing-management/character-state-cards.md 末尾的 JSON 區塊
掃描目標：其他保留人物副本的檔案（family-cards、character-card、past-life-complete 等）

設計理由：使用者選擇「欄位級擁有權 + 驗證腳本」而非「檔案級 SSOT」，
讓副本檔案保留可讀性，由腳本確保一致性。

執行：python tools/state_validator.py
輸出：tools/output/state-mismatches.txt
"""

import io
import json
import re
import sys
from pathlib import Path

# 強制 stdout 用 utf-8（Windows cp950 默認會炸）
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "openspec/specs/writing-management/character-state-cards.md"
OUTPUT = ROOT / "tools/output/state-mismatches.txt"

TARGETS = [
    "openspec/specs/protagonist-settings/spec.md",
    "openspec/specs/protagonist-settings/character-card.md",
    "openspec/specs/protagonist-settings/past-life-complete.md",
    "openspec/specs/supporting-characters/spec.md",
    "openspec/specs/supporting-characters/family-cards.md",
    "openspec/specs/supporting-characters/mera-card.md",
    "openspec/specs/supporting-characters/yura-card.md",
    "openspec/specs/supporting-characters/keth-card.md",
    "openspec/specs/supporting-characters/antagonist-card.md",
    "openspec/specs/plot-structure/vol1-chapter-outline.md",
    "openspec/specs/plot-structure/vol45-overview.md",
]

AGE_PATTERN = re.compile(r"(\d+)\s*歲")


def load_source():
    """從 character-state-cards.md 末尾的 JSON 區塊讀取機器可讀資料。"""
    text = SOURCE.read_text(encoding="utf-8")
    # 找第一個 ```json 區塊
    m = re.search(r"```json\s*\n(.*?)\n```", text, re.DOTALL)
    if not m:
        print(f"ERROR: 在 {SOURCE} 找不到 ```json 區塊")
        sys.exit(1)
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON 解析失敗: {e}")
        sys.exit(1)


def closest_alias(line, age_pos, all_aliases_by_char):
    """回傳該 age_pos 最接近的 (character_name, distance)；考慮所有人物的所有別名。"""
    best = (None, float("inf"))
    for char_name, aliases in all_aliases_by_char.items():
        for alias in aliases:
            pos = line.find(alias)
            if pos < 0:
                continue
            d = abs(pos - age_pos)
            if d < best[1]:
                best = (char_name, d)
    return best


def extract_ages_for(alias, char_name, content, all_aliases_by_char):
    """掃描 content，列出所有「alias 附近 (前後 30 字) 出現的歲數」。
    過濾：若該歲數的最近別名屬於別人，跳過（避免「父親 38 歲」被歸到艾登）。"""
    findings = []  # (line_no, line_text, age_int)
    for ln_no, line in enumerate(content.split("\n"), 1):
        if alias not in line:
            continue
        for m in AGE_PATTERN.finditer(line):
            alias_pos = line.find(alias)
            age_pos = m.start()
            if abs(alias_pos - age_pos) > 30:
                continue
            # 過濾：該歲數的最近別名必須屬於本人
            closest_char, _ = closest_alias(line, age_pos, all_aliases_by_char)
            if closest_char and closest_char != char_name:
                continue
            findings.append((ln_no, line.strip(), int(m.group(1))))
    return findings


def parse_source_age(age_text):
    """從 source 的 age_text（例：'12歲', '約8歲', '1歲多'）取出主數字。"""
    m = AGE_PATTERN.search(age_text)
    if m:
        return int(m.group(1))
    return None


def main():
    data = load_source()
    issues = []
    info_lines = []

    # 預構建：所有人物的所有別名
    all_aliases_by_char = {
        char["name"]: [char["name"]] + char.get("aliases", [])
        for char in data["characters"]
    }

    for char in data["characters"]:
        name = char["name"]
        aliases = all_aliases_by_char[name]
        # 用 vol1_end 的年齡作為當前事實源
        source_age = parse_source_age(char["vol1_end"]["age_text"])
        if source_age is None:
            info_lines.append(
                f"INFO: {name} 的 vol1_end.age_text='{char['vol1_end']['age_text']}' 無數字，跳過數字比對"
            )
            continue

        for tgt_rel in TARGETS:
            tgt = ROOT / tgt_rel
            if not tgt.exists():
                continue
            content = tgt.read_text(encoding="utf-8")

            for alias in aliases:
                findings = extract_ages_for(alias, name, content, all_aliases_by_char)
                for ln_no, line_text, found_age in findings:
                    # 容忍 ±1（例如「約 8 歲」對「8 歲」與「9 歲」都允許）
                    if abs(found_age - source_age) > 1:
                        issues.append({
                            "character": name,
                            "target": tgt_rel,
                            "line": ln_no,
                            "found_age": found_age,
                            "source_age": source_age,
                            "context": line_text[:120],
                        })

    # 輸出
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        f.write(f"# state_validator 報告\n\n")
        f.write(f"來源：{SOURCE.relative_to(ROOT)}\n")
        f.write(f"掃描目標數：{len(TARGETS)}\n")
        f.write(f"發現潛在不一致：{len(issues)}\n\n")
        if info_lines:
            f.write("## INFO\n\n")
            for line in info_lines:
                f.write(f"- {line}\n")
            f.write("\n")
        if issues:
            f.write("## 潛在不一致清單\n\n")
            for i in issues:
                f.write(f"- [{i['character']}] {i['target']}:{i['line']}\n")
                f.write(f"    found {i['found_age']} 歲（source vol1_end={i['source_age']} 歲）\n")
                f.write(f"    context: {i['context']}\n\n")
        else:
            f.write("## 結果\n\n全部一致（容忍 ±1 歲）。\n")

    print(f"✓ 報告已輸出至 {OUTPUT.relative_to(ROOT)}")
    print(f"  掃描 {len(TARGETS)} 個檔案，發現 {len(issues)} 個潛在不一致")
    if issues:
        print(f"  請開啟報告查看細節")
    sys.exit(0 if not issues else 1)


if __name__ == "__main__":
    main()
