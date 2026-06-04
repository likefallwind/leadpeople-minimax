"""Extract L1 列表 from atomic_abilities.md → 干净 markdown"""
import re
from pathlib import Path

src = Path("data/clusters/atomic_abilities.md").read_text(encoding="utf-8")

# Extract by group section: ## 一、academic / ## 二、domestic_cn / ## 三、industry / ## 四、entrepreneur_cn / ## 五、entrepreneur_mixed
groups = {}
current_group = None
for line in src.split("\n"):
    m = re.match(r"^### (.+)$", line)
    if m and "（" in m.group(1):
        current_group = m.group(1).strip()
        groups[current_group] = []
        continue
    if current_group is None:
        continue
    # Table row (4 columns: 人物 | 编号 | L1 能力 | 关键 L0 支撑)
    m = re.match(r"^\|\s*(.+?)\s*\|\s*(AB-[A-Z]+-\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
    if m:
        name, code, ability, evidence = m.groups()
        groups[current_group].append({
            "name": name.strip(),
            "code": code.strip(),
            "ability": ability.strip(),
            "evidence": evidence.strip(),
        })

# Print summary
print(f"Found {len(groups)} groups")
for g, items in groups.items():
    print(f"  {g}: {len(items)} L1")

# Build output markdown
total = sum(len(v) for v in groups.values())
out = [f"# 60 人 × L1 原子能力全清单 v3（{total} 条）", ""]
out.append("> **研究方法**：扎根理论（Grounded Theory）开放编码——从 60 张 v2 事实卡 + 720+ L0 原子事实抽象出 L1 原子能力")
out.append(f"> **数据规模**：60 人 × 平均 {total/60:.1f} 条 L1 原子能力 = **{total} 条 L1**（v3 完整提取；v2 阶段 2 把'事件'与'能力'混在一起，v3 严格区分 3 层）")
out.append("> **数据来源**：`data/atomic_abilities/{group1,group2,group3}/<人物>.md` + `data/clusters/atomic_abilities.md`")
out.append("> **判断标准**：1 L1 = 1 个具体能力（不过宽不过窄），不写'事件'（那是 L0），不写'外界称号'（那是 D 维证据）")
out.append("> **关键约束**：每 L1 必须可追溯到 1+ L0 事实；1 L0 事实可支撑 1+ L1")
out.append("")

# Stats
total = sum(len(v) for v in groups.values())
out.append(f"## 总览")
out.append(f"")
out.append(f"- **总 L1 数**：{total}")
out.append(f"- **总人物数**：{len(set(item['name'] for items in groups.values() for item in items))}")
out.append(f"- **平均每人 L1**：{total / 60:.1f}")
out.append(f"")
out.append("| 组 | 人数 | L1 数 | 平均 L1/人 |")
out.append("|---|---|---|---|")
for g, items in groups.items():
    names = set(item['name'] for item in items)
    out.append(f"| {g} | {len(names)} | {len(items)} | {len(items) / len(names):.1f} |")
out.append("")

# Per-group tables
out.append("---")
out.append("")
for g, items in groups.items():
    out.append(f"## {g}（{len(items)} 条 L1）")
    out.append("")
    # Group by person
    by_person = {}
    for item in items:
        by_person.setdefault(item['name'], []).append(item)
    for name in sorted(by_person.keys()):
        person_items = by_person[name]
        out.append(f"### {name}（{len(person_items)} 条 L1）")
        out.append("")
        out.append("| 编号 | L1 原子能力 | 关键 L0 支撑 |")
        out.append("|---|---|---|")
        for item in person_items:
            out.append(f"| {item['code']} | {item['ability']} | {item['evidence']} |")
        out.append("")

# Write file
Path("docs/l1_atomic_abilities_full.md").write_text("\n".join(out), encoding="utf-8")
print(f"\nWrote docs/l1_atomic_abilities_full.md ({len(chr(10).join(out))} chars)")
