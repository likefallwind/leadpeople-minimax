# AGENTS.md — AI 领军人才画像研究 · 项目结构导航

> **给未来的我（agent）看的项目结构说明**。每次接手这个项目，**先读这个文件**。
> 用户面向的简介见 `README.md`；本文件面向"协作 agent"，重点是**目录、数据流、怎么继续**。

---

## 1. 项目一句话定位

**研究"AI 领军人才应该是什么样"** —— 基于 60 位公认 AI 领军人物样本，通过扎根理论（Grounded Theory）三阶段编码 + K-means 聚类，抽象出 **8 个核心维度** + **6 个领军人才原型**，最终服务**北京中关村学院博士生培养目标**。

**完成时间**：2026-06-03
**作者**：Mavis（AI 研究协调员）+ 60 个并行 worker session
**最终交付**：`docs/portrait_final.md` + `docs/portrait.html`

---

## 2. 技术栈与工具

| 类别 | 内容 |
|---|---|
| 文件格式 | Markdown（.md）+ HTML（嵌入 SVG/CSS/JS，单文件可独立打开） |
| 研究方法 | 扎根理论三阶段编码（开放→轴心→选择） + K-means 聚类 |
| 工具链 | 无构建步骤；HTML 文件即开即用（直接浏览器打开） |
| 协作工具 | mavis 框架 + `mavis team plan` 多 worker 并行研究 |
| 临时文件 | `.mavis/plans/*.yaml`（daemon 状态），`.opencode/tmp/*`（node 临时）—— **不入仓** |

**重点**：这个项目是**研究文档项目**，**没有代码、没有 CI、没有部署**。所有"工作"都是写 markdown / 改 HTML。

---

## 3. 目录树（含每层作用）

```
leadpeople/
├── AGENTS.md                       # ← 你正在读这个
├── README.md                       # 用户面向的项目简介
├── 第一批60人名单.md                # 原始研究样本清单（不入分类目录）
│
├── data/                           # 原始研究数据（手动维护，禁止自动改）
│   ├── fact_cards/                 # 60 张事实卡
│   │   ├── academic/               # 10 人：bengio, e_weinan, he_kaiming, hinton,
│   │   │                           #       lecun, li_feifei, xie_saining, yan_shuicheng,
│   │   │                           #       zhang_xiangyu, zhu_songchun
│   │   ├── domestic_cn/            # 13 人：gao_wen, huang_tiejun, jia_jiaya, lin_dahua,
│   │   │                           #       liu_tieyan, liu_zhiyuan, sun_maosong, tang_jie,
│   │   │                           #       tang_xiaou, zhang_bo, zhang_yaqin, zhou_zhihua, zhu_jun
│   │   ├── industry/               # 10 人：ian_goodfellow, ilya_sutskever, jeff_dean,
│   │   │                           #       li_hang, shen_xiangyang, tian_qi, wang_haifeng,
│   │   │                           #       xuedong_huang, zhang_zhengyou, zhou_jingren
│   │   ├── entrepreneur_cn/        # 16 人（中文文件名）：李开复 / 印奇 / 张亚勤 / 张一鸣 /
│   │   │                           #       周鸿祎 / 王兴 / 王小川 / 雷军 / 王慧文 /
│   │   │                           #       李志飞 / 楼天城 / 黄仁勋 / 沈向洋 / 汤晓鸥 等
│   │   └── entrepreneur_mixed/     # 11 人：aidan_gomez, andrej_karpathy, andrew_ng,
│   │                               #       chris_olah, dario_amodei, demis_hassabis,
│   │                               #       nick_bostrom, paul_christiano, richard_sutton,
│   │                               #       sam_altman, stuart_russell
│   │
│   ├── atomic_abilities/           # 60 张原子能力文件（与 fact_cards 一一对应）
│   │   ├── group1/                 # ← academic 10 人
│   │   ├── group2/                 # ← domestic_cn 13 人 + industry 10 人 + entrepreneur_cn 16 人
│   │   │   └── group2_summary.md   #   第二组合并的摘要
│   │   └── group3/                 # ← entrepreneur_mixed 11 人
│   │       └── group3_summary.md   #   第三组摘要
│   │
│   └── clusters/                   # 聚类结果（手动维护，最终成稿）
│       ├── clusters.md             # 20 个二级能力簇（20 secondary clusters）
│       ├── dimensions.md           # 8 个核心维度（D1-D8）
│       ├── matrix.md               # 60 人 × 8 维打分矩阵
│       ├── prototypes.md           # 6 个领军人才原型（P1-P6）
│       └── portrait_summary.md     # 画像总览
│
├── docs/                           # 最终交付（用户/读者面向）
│   ├── portrait_final.md           # 终极报告（60 人画像总览 + 8 维 + 6 原型 + 关键发现）
│   ├── phd_recommendations.md      # 博士生培养建议（5 方向 + 3 路径 + 6 建议）
│   ├── portrait.html               # 画像总览可视化（6 原型 radar + 60×8 矩阵热图）
│   ├── methodology.html            # 方法论全景（编码流程 + 20→8 路径 + Hinton 12 原子实例）
│   └── scoring_process.html        # 6 人打分明细（Hinton/Jeff Dean/刘铁岩/张林峰/Sam Altman/Demis）
│
├── data/list_files.ps1             # 临时 PowerShell 调试脚本（**已 gitignore，下次别加进去**）
└── .mavis/                         # daemon 计划状态（不入仓）
```

**关键设计**：
- 60 张事实卡和 60 张原子能力文件**按人物分文件**，文件名 = 人物标识符（拼音/英文）
- 原子能力目录按"研究阶段分组"（group1=第一批 10 人 / group2=合并第二批 / group3=第三批 11 人），与 fact_cards 的"人物类型分组"不一致 —— 这是**研究历史的痕迹**，不是 bug
- 中文人物用中文文件名（创业中国组），西方人物用拼音/英文（其他四组）

---

## 4. 数据流（从样本到画像）

```
60 位 AI 领军人才（第一批60人名单.md）
         │
         ▼
   60 张事实卡（data/fact_cards/）
   每张含 10 维度：教育/职业/研究/成就/性格/失败/哲学/…
   每张 1500-3000 字
         │
         ▼
   60 份原子能力文件（data/atomic_abilities/）
   共 600+ 原子能力（每个 6-12 个）
         │
         ▼
   20 个二级能力簇（data/clusters/clusters.md）
   聚类开放编码 → 合并相似原子
         │
         ▼
   8 个核心维度 D1-D8（data/clusters/dimensions.md）
   选择性编码 → 8 维空间
         │
         ▼
   60 人 × 8 维打分矩阵（data/clusters/matrix.md）
         │
         ▼
   6 个领军人才原型 P1-P6（data/clusters/prototypes.md）
   K-means 聚类
         │
         ▼
   最终报告 + HTML（docs/）
```

---

## 5. 关键概念与术语

| 术语 | 含义 |
|---|---|
| **事实卡** (fact card) | 单个人物的定性研究笔记，10 维度，约 2000 字 |
| **原子能力** (atomic ability) | 从事实卡中抽象出的最小能力单元（动词性短语，如"反向传播发明"） |
| **二级簇** (secondary cluster) | 相似原子能力的聚类，约 20 个 |
| **核心维度** (dimension) | 选择性编码抽象出的高阶能力维度，固定为 8 个 D1-D8 |
| **原型** (prototype) | 60 人在 8 维空间 K-means 聚类得到的 6 个领军画像 P1-P6 |
| **扎根理论** (Grounded Theory) | Glaser & Strauss 方法论，三阶段编码（开放→轴心→选择） |
| **K-means 聚类** | 8 维向量空间下，将 60 人聚成 6 类 |

**8 个核心维度**（固定不变）：
- D1 原创算法贡献
- D2 系统工程能力
- D3 学术机构地位
- D4 创业能力
- D5 政策治理参与
- D6 长期主义深度
- D7 跨界整合能力
- D8 公共影响力

**6 个领军人才原型**（中西方分工清晰）：
- P1 学术源流派（11 人，西方主导）
- P2 工业研究院领袖（13 人，中美各半）
- P3 学术+AI 创业派（15 人，**中国独有**）
- P4 跨界整合多栖型（9 人，西方为主）
- P5 AI 治理/安全旗手（4 人，**西方独有**）
- P6 商业/硬件创业型（8 人，**中国独有**）

---

## 6. 60 人完整名单

### academic（10 人）— 学术源流
- bengio（Yoshua Bengio，蒙特利尔大学）
- e_weinan（鄂维南，北京大学/普林斯顿）
- he_kaiming（何恺明，MIT/Meta/FAIR）
- hinton（Geoffrey Hinton，多伦多大学/Google）
- lecun（Yann LeCun，NYU/Meta FAIR）
- li_feifei（李飞飞，斯坦福）
- xie_saining（谢赛宁，Meta FAIR）
- yan_shuicheng（颜水成，360/快手）
- zhang_xiangyu（张祥雨，Megvii）
- zhu_songchun（朱松纯，北京通用人工智能研究院）

### domestic_cn（13 人）— 中国学术/研究
- gao_wen（高文，北大）
- huang_tiejun（黄铁军，北大）
- jia_jiaya（贾佳亚，港中文/思谋）
- lin_dahua（林达华，港中文/上海期智）
- liu_tieyan（刘铁岩，微软亚研）
- liu_zhiyuan（刘知远，清华）
- sun_maosong（孙茂松，清华）
- tang_jie（唐杰，清华）
- tang_xiaou（汤晓鸥，港中文/商汤）
- zhang_bo（张钹，清华）
- zhang_yaqin（张亚勤，智能产业）
- zhou_zhihua（周志华，南大）
- zhu_jun（朱军，清华）

### industry（10 人）— 工业研究院
- ian_goodfellow（GAN 之父）
- ilya_sutskever（OpenAI 联合创始人）
- jeff_dean（Google Research）
- li_hang（李航，华为/字节）
- shen_xiangyang（沈向洋，微软/IDG 资本）
- tian_qi（田奇，华为诺亚）
- wang_haifeng（王海峰，百度 CTO）
- xuedong_huang（黄学东，Zoom/前微软）
- zhang_zhengyou（张正友，腾讯/微软）
- zhou_jingren（周靖人，阿里云）

### entrepreneur_cn（16 人，中文文件名）— 中国创业/治理
- 包含：李开复 / 印奇（旷视）/ 张亚勤（已并入 industry） / 张一鸣（字节）/ 周鸿祎（360）/ 王兴（美团）/ 王小川（百川）/ 雷军（小米）/ 王慧文 / 李志飞（出门问问）/ 楼天城（小马智行）/ 黄仁勋（英伟达）/ 沈向洋（已并入 industry） / 汤晓鸥（已并入 domestic_cn） 等
- **注意**：此组与 industry / domestic_cn 存在人物重叠（张亚勤、沈向洋、汤晓鸥等）—— 研究时**以人物在不同维度的表现为准**，分组是研究批次，不是互斥

### entrepreneur_mixed（11 人）— 全球前沿创业/治理
- aidan_gomez（Cohere CEO，Transformer 作者）
- andrej_karpathy（特斯拉 AI 总监 / Eureka Labs）
- andrew_ng（吴恩达，DeepLearning.AI）
- chris_olah（Anthropic 可解释性）
- dario_amodei（Anthropic CEO）
- demis_hassabis（DeepMind 创始人，诺奖得主）
- nick_bostrom（哲学家，Future of Life Institute）
- paul_christiano（ARC Evals / OpenAI 对齐）
- richard_sutton（强化学习之父）
- sam_altman（OpenAI CEO）
- stuart_russell（UC Berkeley AI 安全）

---

## 7. 命名约定

- **西方人物**：用拼音或英文（`hinton.md` 而非 `杰弗里·辛顿.md`）
- **中国人物**：用拼音（`he_kaiming.md` 而非 `何恺明.md`）
- **中国创业家**（entrepreneur_cn）：**用中文文件名**（`李开复.md`、`王兴.md`）—— 这是研究早期的惯例，与其他组不一致，**不要改**
- 文件名 = 人物唯一标识符（贯穿 data/ 和 docs/）

---

## 8. 如何继续工作

### 添加新人物
1. 在 `data/fact_cards/<合适分组>/` 新建 `person_id.md`（1500-3000 字，10 维度）
2. 在 `data/atomic_abilities/<合适分组>/` 新建 `person_id.md`（6-12 个原子能力）
3. 在 `data/clusters/matrix.md` 补充 8 维打分
4. 在 `data/clusters/prototypes.md` 判断该人物属于哪个 P1-P6 原型
5. 同步更新 `docs/portrait.html` 矩阵热图 + `docs/portrait_final.md`

### 修改某个原型
1. 先看 `data/clusters/prototypes.md` 确认原型边界
2. 用 `data/clusters/matrix.md` 检查受影响的 60 个评分
3. 修改后**必须**同步 `docs/portrait.html`（radar + 矩阵）

### 修改某个 HTML
- HTML 都是**单文件可独立打开**的（内嵌 SVG/CSS/JS），无外部依赖
- 用 `read` 找到要改的部分，**整段替换**而不是 patch
- 改完后**用浏览器打开**验证视觉效果（可让用户截图确认）

### 添加新维度
1. 先在 `data/clusters/dimensions.md` 加 D9，定义边界
2. 对 60 人**全部重打分**（这是大改，工作量 = 0.5 人天）
3. 同步 `matrix.md` + `prototypes.md` + 3 个 HTML

---

## 9. 已知约束与坑

### 9.1 文件名编码（PowerShell 5.1 + Windows 终端）
- `data/fact_cards/entrepreneur_cn/` 和 `data/atomic_abilities/group2/` 中的**中文文件名**，在 PowerShell 5.1 终端显示为乱码（`ӡ��.md`），但**文件本身正常**（UTF-8）
- **不要"修复"这些文件名**——会破坏 git 历史和跨平台一致性
- 用 `git ls-files` 或文件管理器查看时是中文

### 9.2 .gitignore 已配置
- `.mavis/` — daemon 临时计划
- `.opencode/` — node 临时文件
- `data/list_files.ps1` — 临时调试脚本
- `*.log` / `.DS_Store` / `Thumbs.db`

### 9.3 Git 配置
- **不要修改 git config**（user.email / user.name 已就绪：likefallwind@163.com / likefallwind）
- **不要 force push** 到 master
- 当前默认分支是 **`master`**（git init 默认），不是 `main`
- 远端：`git@github.com:likefallwind/leadpeople-minimax.git`（SSH）

### 9.4 研究方法学约束
- **字数不压缩**：每张事实卡 1500-3000 字，原子能力文件 200-500 字
- **HTML 优先**：用户多次要求"以 HTML 形式呈现"，任何最终展示优先做 HTML
- **不要凭空补全**：所有评分必须有事实卡或原子能力依据
- **跨太平洋训练**是核心发现之一（D6 长期主义 + 太平洋学术网络），不要漏

### 9.5 已删除的失败尝试
- ❌ 第一版 5 轨 10-16 人超大并发 → 30 min hard cap 卡死，已废弃
- ❌ 第二版 plan_2 → 字数被压缩到 500-1000 字，用户叫停，已废弃
- ✅ 第三版 11 轨 3-5 人细颗粒度 → 字数恢复 1500-3000，最终交付

---

## 10. 用户偏好速查

| 维度 | 偏好 |
|---|---|
| 语言 | 中文 |
| 沟通 | 直接、不啰嗦；停顿会被骂"又卡住了" |
| 字数 | 深度优先，不压缩 |
| 格式 | HTML 优先于 Markdown |
| 工具 | mavis 框架 + 并行 worker（不要串行做大批量） |
| 决策 | 关键节点问，中间不停 |
| Git | 不动 git config，不 force push |

---

## 11. 30 秒自检（接手时跑一遍）

```
□ 读 README.md → 项目目标
□ 读 AGENTS.md → 你正在读
□ 看 docs/portrait.html → 知道最终交付长什么样
□ 数 data/fact_cards/ 下文件总数 → 应该是 60（academic 10 + domestic_cn 13 + industry 10 + entrepreneur_cn 16 + entrepreneur_mixed 11）
□ 跑 git status → 工作目录干净
□ 跑 git log --oneline -5 → 知道最近 5 次提交是什么
```

如果以上都过了，**这个项目你已经 100% 接手了**。
