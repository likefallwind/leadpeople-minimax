"""Extract L2 cluster list from clusters.md → 干净 markdown"""
import re
from pathlib import Path

src = Path("data/clusters/clusters.md").read_text(encoding="utf-8")

# Find the 5th h2 section (82 L2 mapping)
section_start = src.find("## 五、82 L2")
if section_start < 0:
    raise SystemExit("Section not found")

# Parse cluster blocks - split by ### 簇 headers
section = src[section_start:]
parts = re.split(r"^### (簇 \d+.*?)$", section, flags=re.MULTILINE)
# parts: ['', '簇 1 ...', 'body1', '簇 2 ...', 'body2', ...]
blocks = []
for i in range(1, len(parts), 2):
    header = parts[i]
    body = parts[i+1] if i+1 < len(parts) else ""
    # Stop at end of section (before ## 六)
    if "## 六" in body:
        body = body.split("## 六")[0]
    blocks.append((header, body))

# Build D 维归属 mapping (from dimensions.md)
dim_src = Path("data/clusters/dimensions.md").read_text(encoding="utf-8")
# Structure: `## D1 原创算法 / 理论贡献...` then "- 对应 L2 簇: 簇 1 ... 簇 2 ..."
dim_clusters = {}  # cluster_name -> dim_name
current_dim = None
for line in dim_src.split("\n"):
    m = re.match(r"^## (D\d+ .+)$", line.strip())
    if m:
        current_dim = m.group(1).strip()
    if current_dim and "簇 " in line:
        for cnum in re.findall(r"簇\s*(\d+)", line):
            dim_clusters[f"簇 {cnum}"] = current_dim

# Build output
out = ["# 60 人画像编码框架 v3 · 82 条 L2 二级能力簇全清单", ""]
out.append("> **研究方法**：扎根理论（Grounded Theory）选择性编码——从 472 条 L1 原子能力聚类形成 82 条 L2 二级能力簇")
out.append(f"> **数据规模**：472 条 L1 原子能力 → **{len(blocks)} 条 L2 能力簇**（部分簇已合并，实际编号到 82）")
out.append("> **数据来源**：`data/clusters/clusters.md` + `data/clusters/dimensions.md`（D 维归属）")
out.append("> **判断标准**：1 L2 簇 = 1 个能力主题（5-30 条 L1 能力支撑）；每 L1 归属唯一 L2（不跨组）")
out.append("> **D 维归属**：8 维 D1-D8 中每个 D 维对应 5-11 个 L2 簇（D 维 ↔ L2 簇映射）")
out.append("")

# Statistics
total_l1 = sum(len(re.findall(r"- ", b[1])) for b in blocks)
out.append(f"## 总览")
out.append(f"")
out.append(f"- **L2 簇数**：{len(blocks)}（编号到 82，部分合并）")
out.append(f"- **L1 总数**：{total_l1} 条（已聚合到 472 总数）")
out.append(f"- **平均每 L2 簇含 L1**：{total_l1 / len(blocks):.1f}")
out.append(f"")
out.append("| D 维 | L2 簇数 | 含义 |")
out.append("|---|---|---|")
# Count by D
from collections import Counter
dim_count = Counter()
for b in blocks:
    cluster_name = b[0].split("（")[0].strip()
    # Extract cluster number
    m = re.match(r"簇\s*(\d+)", cluster_name)
    if m:
        cnum = int(m.group(1))
        dim = dim_clusters.get(f"簇 {cnum}", "未分类")
        dim_count[dim] += 1
for d, n in sorted(dim_count.items(), key=lambda x: -x[1]):
    out.append(f"| {d} | {n} | |")
out.append("")

# Per-cluster detail
out.append("---")
out.append("")
for i, (header, body) in enumerate(blocks, 1):
    out.append(f"## {i}. {header}")
    out.append("")
    # Extract L1 list
    items = re.findall(r"^- (.+)$", body, re.MULTILINE)
    cluster_name = header.split("（")[0].strip()
    m = re.match(r"簇\s*(\d+)", cluster_name)
    dim = "未分类"
    if m:
        dim = dim_clusters.get(f"簇 {m.group(1)}", "未分类")
    out.append(f"**D 维归属**：{dim}")
    out.append("")
    out.append(f"**包含 L1 原子能力**（{len(items)} 条）：")
    out.append("")
    for item in items:
        out.append(f"- {item}")
    out.append("")

Path("docs/l2_clusters_full.md").write_text("\n".join(out), encoding="utf-8")
print(f"Wrote docs/l2_clusters_full.md ({sum(len(b) for h, b in blocks)} chars in {len(blocks)} clusters)")
