# AI 领军人才画像研究 · AI Leadership Portrait

> 服务对象：**北京中关村学院** · 博士生人才培养目标
> 研究方法：扎根理论（Grounded Theory）三阶段编码 + K means 聚类
> 完成时间：2026-06-03
> 作者：Mavis（AI 研究协调员）

## 项目目标

研究"AI 领军人才应该是什么样"——基于 60 位公认的 AI 领域领军人才样本（学术/工业/创业/治理/反共识），通过扎根理论方法论，抽象出领军人才画像（核心维度 + 原型），并落到博士生培养建议上。

## 研究产物

### 1. 画像文档（Markdown）

- `docs/portrait_final.md` — **终极报告**（60 人画像总览 + 8 维 + 6 原型 + 关键发现 + 培养建议）
- `docs/phd_recommendations.md` — **博士生培养建议**（5 大方向 + 3 种路径 + 6 条具体建议）

### 2. 可视化（HTML）

- `docs/portrait.html` — 画像总览（6 个原型 radar + 60 人 × 8 维矩阵热图 + 关键发现 + 培养建议）
- `docs/methodology.html` — **方法论全景**（600 原子 → 20 二级簇 → 8 维的完整路径 + Hinton 12 原子能力实例）
- `docs/scoring_process.html` — **6 个具体人物的打分明细**（Hinton / Jeff Dean / 刘铁岩 / 张林峰 / Sam Altman / Demis Hassabis 的原子能力 → 8 维评分 → 原型聚类全过程）

### 3. 数据基础

- `data/fact_cards/` — **60 张事实卡**（每张 1500-3000 字，含教育/职业/研究/成就/性格/失败/哲学 10 维度）
- `data/atomic_abilities/` — **60 张原子能力文件**（600+ 原子能力，按人物分文件）
- `data/clusters/clusters.md` — 20 个二级能力簇
- `data/clusters/dimensions.md` — 8 个核心维度
- `data/clusters/matrix.md` — 60 人 × 8 维打分矩阵
- `data/clusters/prototypes.md` — 6 个领军人才原型
- `data/clusters/portrait_summary.md` — 画像总览

## 关键发现（摘要）

1. **8 个核心维度**（D1-D8）：D1 原创算法 / D2 系统工程 / D3 学术机构 / D4 创业 / D5 政策治理 / D6 长期主义 / D7 跨界整合 / D8 公共影响
2. **6 个领军人才原型**（中西方分工清晰）：
   - **P1 学术源流派**（11 人，西方主导）
   - **P2 工业研究院领袖**（13 人，中美各半）
   - **P3 学术+AI 创业派**（15 人，中国独有）
   - **P4 跨界整合多栖型**（9 人，西方为主）
   - **P5 AI 治理/安全旗手**（4 人，西方独有）
   - **P6 商业/硬件创业型**（8 人，中国独有）
3. **3 大共性**：长期主义 + 跨太平洋学术训练 + 学派/师承网络
4. **人才共性公式**：顶级 AI 领军 = 8 维能力 × 长期主义 × 跨太平洋训练

## 目录结构

```
leadpeople/
├── README.md                  # 本文件
├── 第一批60人名单.md           # 原始研究样本
├── data/
│   ├── fact_cards/             # 60 张事实卡
│   ├── atomic_abilities/       # 60 张原子能力文件
│   └── clusters/               # 聚类结果（5 个文件）
├── docs/                       # 最终报告 + 可视化
│   ├── portrait_final.md
│   ├── phd_recommendations.md
│   ├── portrait.html
│   ├── methodology.html
│   └── scoring_process.html
└── .mavis/                     # daemon 临时文件（不入仓）
```
