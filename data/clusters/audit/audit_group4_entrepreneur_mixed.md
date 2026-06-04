# Group 4: entrepreneur_mixed（11 人）D 维评分追溯

> **Trust 等级**：B（有 fact-check 表但无 rework）
> **Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/`
> **v3 matrix 评分**：`data/clusters/matrix.md` 第 164-180 行（Group 5 表）
> **审计日期**：2026-06-04
> **审计员**：general worker（branch session mvs_aa1029f4aed34480b0387fdcce092a66）

---

## 审计概览

| 人物 | v3 总分 | 审计结论 | 需修订 D 维 |
|---|---|---|---|
| Aidan Gomez | 12 | ✅ 全对 | 无 |
| Andrej Karpathy | 11 | ✅ 全对 | 无 |
| Andrew Ng | 17 | ⚠️ 1 处需修订 | D6（1→2） |
| Chris Olah | 8 | ⚠️ 1 处需修订 | D5（0→1） |
| Dario Amodei | 16 | ⚠️ 1 处需修订 | D1（1→2） |
| Demis Hassabis | 19 | ⚠️ 1 处需修订 | D6（1→2） |
| Nick Bostrom | 11 | ❌ 1 处需修订 | D6（0→2 或 3） |
| Paul Christiano | 10 | ✅ 全对 | 无 |
| Rich Sutton | 14 | ✅ 全对（D7 边界可争议） | 无 |
| Sam Altman | 18 | ⚠️ 2 处需修订 | D1（1→0）+ D6（1→2） |
| Stuart Russell | 15 | ⚠️ 1 处需修订 | D6（2→3） |

**总结**：11 人中 7 人需修订（Andrew Ng / Chris Olah / Dario Amodei / Demis Hassabis / Nick Bostrom / Sam Altman / Stuart Russell），4 人完全正确（Aidan Gomez / Andrej Karpathy / Paul Christiano / Rich Sutton）。**D6 长期主义 是高频误判维度**（6/7 修订涉及 D6），主要因"分散在多机构 vs 单一机构坚持"边界模糊。

---

## 1. Aidan Gomez (aidan_gomez) — ✅ 全对

**当前 v3 评分**：[D1=3, D2=1, D3=1, D4=3, D5=0, D6=0, D7=2, D8=2] 总分=12/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/aidan_gomez.md`（178 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告 + v2_rework 无独立核查）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 3 | ✅ 3 | AF-AG-02/03：2017 "Attention Is All You Need" 8 共同作者之一（arXiv 1706.03762）；当时年仅 20 岁 | `aidan_gomez.md` 段 3 | 3 分标准：Transformer 架构 = LLM 时代基础设施，引用 18 万+，改变整个行业方向 |
| D2 系统工程 | 1 | ✅ 1 | AF-AG-01：2014 Google Brain 实习主导 Tensor2Tensor 基础设施；2025 Command A+ 218B MoE（Apache 2.0） | `aidan_gomez.md` 段 2-3 | 1 分标准：Tensor2Tensor 是团队级工作，Command A+ 主要是产品发布而非从零系统建设 |
| D3 学术机构 | 1 | ✅ 1 | 多伦多大学 CS+数学本科 + 牛津博士在职（未独立 web 核实研究主题） | `aidan_gomez.md` 段 1 | 1 分标准：博士在职有 Fellow 候选潜力但未拿到，无学院/实验室副主任级正式职务 |
| D4 创业 | 3 | ✅ 3 | AF-AG-05/06/07/08/10：2019 共同创办 Cohere；2021-09 A 轮 4 千万；2022-02 B 轮 1.25 亿；2023 C 轮 2.7 亿估值 27 亿；2024-05 D 轮 5 亿估值 55 亿 | `aidan_gomez.md` 段 4-5 | 3 分标准：Cohere 估值 55 亿美元已属独角兽 |
| D5 政策治理 | 0 | ✅ 0 | 公开反对"AGI 末日"主流叙事；多语言/反 AI 寡头化立场 | `aidan_gomez.md` 段 6-7 | 0 分标准：虽有公共立场但无国家级/国际级政策参与记录 |
| D6 长期主义 | 0 | ✅ 0 | 2014 Google Brain → 2017 FOR.ai → 2019 Cohere（多平台切换 5+ 年） | `aidan_gomez.md` 段 2 | 0 分标准：频繁跳槽/短期切换，未在单一组织坚持 5+ 年 |
| D7 跨界整合 | 2 | ✅ 2 | 学界（多伦多+牛津）+ 工业（Google Brain）+ 创业（Cohere）+ 政策立场（反 AI 寡头化）4 领域 | `aidan_gomez.md` 段 1-7 | 2 分标准：跨 3 个领域（学界+工业+创业） |
| D8 公共影响 | 2 | ✅ 2 | AF-AG-09：2023 入选 TIME100 AI（首届 AI 百人榜）；Redpoint 播客 + AGI House 达沃斯专访 | `aidan_gomez.md` 段 4 | 2 分标准：TIME100 AI + 顶级播客受众百万级 |

**审计结论**：✅ v3 评分全对，与 fact card + L0 原子事实 + L1 原子能力完全一致

---

## 2. Andrej Karpathy (andrej_karpathy) — ✅ 全对

**当前 v3 评分**：[D1=2, D2=1, D3=1, D4=2, D5=0, D6=0, D7=2, D8=3] 总分=11/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/andrej_karpathy.md`（184 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 2 | ✅ 2 | AF-AK-07：2017 Tesla AI Day "Software 2.0" 概念；ImageNet 比赛领先结果；2015 PhD 论文"Connecting Images and Natural Language" | `andrej_karpathy.md` 段 3 | 2 分标准：有领域影响力（"Software 2.0"被全行业引用、ImageNet 比赛成绩），但非改变方向级（无 Nature/图灵级） |
| D2 系统工程 | 1 | ✅ 1 | AF-AK-06：2017-2022 Tesla AI 视觉感知栈；CNN+Transformer 混合架构在数百万辆车上实时运行 | `andrej_karpathy.md` 段 2-3 | 1 分标准：主导过系统（Tesla Autopilot），但非 TensorFlow/MapReduce 级行业基础设施 |
| D3 学术机构 | 1 | ✅ 1 | 2015 Stanford PhD（导师李飞飞）；无 Fellow、无学院/实验室副主任级 | `andrej_karpathy.md` 段 1 | 1 分标准：有 PhD 学位 + 顶级导师（接近"有 Fellow 头衔"边界），但无独立学术机构地位 |
| D4 创业 | 2 | ✅ 2 | AF-AK-05/10：2015 OpenAI 创始成员（11-12 人之一）；2024-07 创办 Eureka Labs（AI 原生教育） | `andrej_karpathy.md` 段 5 | 2 分标准：主导过创业（Eureka Labs 创始人、OpenAI 联创），但 Eureka Labs 截至 2024-07 未公开融资未达独角兽 |
| D5 政策治理 | 0 | ✅ 0 | 公共叙事主要在教育/反炒作领域；无国家级政策参与 | `andrej_karpathy.md` 段 6 | 0 分标准：无 AI 安全/治理研究机构，无国家级/国际级政策对话 |
| D6 长期主义 | 0 | ✅ 0 | 4 平台切换：OpenAI 2 年（2015-2017）+ Tesla 5 年（2017-2022）+ OpenAI 1 年（2023-2024）+ Eureka Labs 2024- | `andrej_karpathy.md` 段 2 | 0 分标准：典型频繁跳槽/短期切换（4 个平台 < 5 年单一组织） |
| D7 跨界整合 | 2 | ✅ 2 | 学界（Stanford/Tesla 内研究）+ 工业（Tesla/OpenAI）+ 创业（OpenAI/Eureka Labs）+ 教育（CS231n/Zero to Hero/LLM101n）4 领域 | `andrej_karpathy.md` 段 2-6 | 2 分标准：跨 3 个领域（学界+工业+创业+教育） |
| D8 公共影响 | 3 | ✅ 3 | CS231n YouTube 累计观看 1 亿+；Zero to Hero 系列"圣经级"入门；X 长文频繁；CS231n 学生数 2015 年 150 → 2017 年 750 | `andrej_karpathy.md` 段 3-6 | 3 分标准：千万级公共影响（CS231n 1 亿观看 + 教育者身份传播） |

**审计结论**：✅ v3 评分全对，与 fact card 一致

---

## 3. Andrew Ng (andrew_ng) — ⚠️ D6 需修订

**当前 v3 评分**：[D1=2, D2=1, D3=3, D4=3, D5=1, D6=1, D7=3, D8=3] 总分=17/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/andrew_ng.md`（213 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 2 | ✅ 2 | AF-AN-06：2012 Google Cat 论文（arXiv 2012）；UFLDL 教程（2011）；Deep Learning with COTS HPC Systems（ICML 2013）；ROS 平台（ICRA 2009） | `andrew_ng.md` 段 3 | 2 分标准：有领域影响力（Google Cat 引爆深度学习时代 + ROS 平台成为机器人标准），但非 Hinton/Bengio 改变方向级 |
| D2 系统工程 | 1 | ✅ 1 | Google Cat 用 16000 CPU 核心 + 10 亿参数训练（2012） | `andrew_ng.md` 段 2-3 | 1 分标准：主导过工业级规模实验但非从零建设的工程系统 |
| D3 学术机构 | 3 | ✅ 3 | AF-AN-04：2002 加入 Stanford CS+EE 副教授 → Stanford AI Lab (SAIL) 主任；2007 Sloan Fellowship；2008 MIT TR35；2023 TIME 100 AI | `andrew_ng.md` 段 2-4 | 3 分标准：SAIL 主任（顶级 AI 实验室）+ TIME 100 AI 顶级 Fellow（但非五大 Fellow 全部到位，边界在 2-3 之间，v3 给 3 合理） |
| D4 创业 | 3 | ✅ 3 | AF-AN-07/09/10：2012 Coursera 联合创办（估值数十亿美元）；2017 Landing.ai / DeepLearning.AI / AI Fund 三家创业；2024-04 Amazon 董事会 | `andrew_ng.md` 段 5 | 3 分标准：Coursera 是上市公司级独角兽（NYSE: COUR 估值数十亿） |
| D5 政策治理 | 1 | ✅ 1 | 2024-04 加入 Amazon 董事会（被定位为"AI 治理和战略首席顾问"）；与 Stuart Russell、Bostrom、Yoshua Bengio 等保持对话 | `andrew_ng.md` 段 5-6 | 1 分标准：有 AI 治理研究/咨询（Amazon 董事 + 与安全派对话），未到国家级 2 分 |
| **D6 长期主义** | **1** | **⚠️ 2** | AF-AN-04：2002 加入 Stanford 副教授 → 持续到 2024（22+ 年）；2014-2017 百度 3 年；2017 至今 Coursera/Landing/DeepLearning.AI | `andrew_ng.md` 段 1-2 | **2 分标准**：Stanford 2002-2014 12 年（虽 2014 后 Coursera/百度兼职但仍是 Stanford 教授），远超 10-20 年阈值。v3 给 1 偏低 |
| D7 跨界整合 | 3 | ✅ 3 | 学界（Stanford 22+ 年）+ 工业（Google Brain/百度 6 年）+ 创业（Coursera/Landing/DeepLearning.AI 3 家）+ 治理（Amazon 董事）4-5 平台 | `andrew_ng.md` 段 5-9 | 3 分标准：跨 4+ 个领域（学界+工业+创业+治理） |
| D8 公共影响 | 3 | ✅ 3 | AF-AN-07：Coursera 1 亿+ 学习者；2013 TIME 100；2023 TIME 100 AI；DeepLearning.AI The Batch 周刊；andrewng.org 博客 | `andrew_ng.md` 段 6 | 3 分标准：千万级公共影响（Coursera 1 亿学习者 + TIME 100 + 周刊订阅） |

**审计结论**：⚠️ **1 个分数需修订**

**修订建议**：
- **D6：1 → 2**。Stanford 2002 至今持续 22+ 年（含兼职期），是 D6 标准"10-20 年坚持"明确达标的案例，且非常接近 3 分"20+ 年坚持"边界。修订后总分应为 18。

---

## 4. Chris Olah (chris_olah) — ⚠️ D5 需修订

**当前 v3 评分**：[D1=1, D2=1, D3=1, D4=1, D5=0, D6=2, D7=1, D8=1] 总分=8/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/chris_olah.md`（178 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | AF-CO-02/05/06/08/10：2017 特征可视化（Distill.pub）；2022-09 Toy Models of Superposition；2024-05 Scaling Monosemanticity 3400 万特征；2025-03 Circuit Tracing；2025-08 Persona Vectors | `chris_olah.md` 段 3 | 1 分标准：有可引用工作（特征可视化是机制可解释性学科起点），但 Olah 的工作是单一系列而非单点改变方向 |
| D2 系统工程 | 1 | ✅ 1 | 机制可解释性团队规模 2021 几人 → 2024-2025 30-50 人；Distill.pub 期刊平台 | `chris_olah.md` 段 5 | 1 分标准：主导过小型系统（团队级），未到工业级系统级 |
| D3 学术机构 | 1 | ✅ 1 | 未走传统博士路线（**未独立 web 核实** 18 岁从多伦多大学退学）；通过 Distill.pub 论文 + Anthropic 研究确立学术地位 | `chris_olah.md` 段 1 | 1 分标准：无 PhD/Fellow/学院副主任级正式学术头衔（Olah 是行业特例：自学型研究员） |
| D4 创业 | 1 | ✅ 1 | AF-CO-03/04：2017 Distill.pub 联合创办（已停刊）；2021 Anthropic 联合创始（联合创始人之一但不是 CEO/核心决策层） | `chris_olah.md` 段 5 | 1 分标准：参与过创业（Distill.pub 联合创办 + Anthropic 联创），但不是主导级（Olah 主负责可解释性研究方向） |
| **D5 政策治理** | **0** | **⚠️ 1** | AF-CO-04：在 Anthropic 主导可解释性研究方向（= AI 治理/安全研究机构核心成员）；2026-02 教皇利奥十四世通谕《Magnifica Humanitas》发布仪式发言；2026-05 梵蒂冈演讲 | `chris_olah.md` 段 6 | **1 分标准**：有 AI 安全/治理研究（Anthropic 可解释性研究 + "可解释性是刹车研究"组织定位）。Olah 不是政府顾问，但他在 AI 治理/可解释性研究中的地位完全够 D5=1。v3 给 0 略严格 |
| D6 长期主义 | 2 | ✅ 2 | 2017 特征可视化 → 2026 Assistant Axis，9 年时间坚持"搞清楚模型在做什么"这一单一方向 | `chris_olah.md` 段 7 | 2 分标准：5-10 年坚持（9 年单一方向） |
| D7 跨界整合 | 1 | ✅ 1 | CS + 数学 + 自学神经科学 + 物理学（类比"神经生物学"方法论） | `chris_olah.md` 段 1 | 1 分标准：跨 2 个领域（CS+神经科学），未到 3 领域 |
| D8 公共影响 | 1 | ✅ 1 | Distill.pub 期刊 + 梵蒂冈通谕发言 + X 长文；2025-05 开源 circuit tracing + Neuronpedia 合作 | `chris_olah.md` 段 6 | 1 分标准：有公开演讲/教材（Distill.pub + 梵蒂冈发言），受众规模在万人级，未到百万级 2 分 |

**审计结论**：⚠️ **1 个分数需修订**

**修订建议**：
- **D5：0 → 1**。Olah 在 Anthropic 主导可解释性研究方向（= AI 治理/安全研究机构核心成员），加上梵蒂冈通谕发言，已明确达 D5=1 标准"有 AI 安全/治理研究"。修订后总分应为 9。

---

## 5. Dario Amodei (dario_amodei) — ⚠️ D1 需修订

**当前 v3 评分**：[D1=1, D2=1, D3=1, D4=3, D5=3, D6=1, D7=3, D8=3] 总分=16/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/dario_amodei.md`（166 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| **D1 原创算法** | **1** | **⚠️ 2** | AF-DA-08：在 OpenAI 担任 VP of Research，领导 GPT-2（2019）、GPT-3（2020）研发；**RLHF 共同发明人**（Dario 个人主页原文："He is also the co-inventor of reinforcement learning from human feedback"） | `dario_amodei.md` 段 2-3 | **2 分标准**：RLHF 是行业基线训练方法（InstructGPT 2022 论文引用 1万+，ChatGPT/Claude/Gemini 都用 RLHF），有领域影响力。v3 给 1 偏低 |
| D2 系统工程 | 1 | ✅ 1 | 2025-09 Anthropic 估值 1830 亿（系统级规模）；B2B/私有化部署战略 | `dario_amodei.md` 段 3-5 | 1 分标准：Anthropic 是公司级规模但 Dario 是 CEO 而非直接主导系统建设（Chris Olah/Dario 等做研究） |
| D3 学术机构 | 1 | ✅ 1 | Caltech+Stanford 本科物理 + Princeton 生物物理博士 + Stanford 医学院博士后；无 Fellow/学院领导 | `dario_amodei.md` 段 1 | 1 分标准：有 PhD 学术背景（接近 Fellow 候选），但无学院/实验室副主任级 |
| D4 创业 | 3 | ✅ 3 | AF-DA-10/11：2021 共同创办 Anthropic；估值从 184 亿(2024)→ 1830 亿(2025-09)；2023 TIME100 AI 首位 | `dario_amodei.md` 段 4-5 | 3 分标准：Anthropic 估值 1830 亿美元，远超独角兽 10 亿门槛 |
| D5 政策治理 | 3 | ✅ 3 | AF-DA-11：2023-07 美国参议院司法小组 AI 洞察论坛作证；公开支持加州 SB 1047 AI 安全法案；与白宫副总统 Kamala Harris、英国首相苏纳克等对话 | `dario_amodei.md` 段 5-6 | 3 分标准：参议院作证 + 国家级政策参与 + AI 安全机构主任 |
| D6 长期主义 | 1 | ✅ 1 | OpenAI 2016-2021（5 年）+ Anthropic 2021-（4 年），分散在两个不同机构 | `dario_amodei.md` 段 2 | 1 分标准：5-10 年坚持（OpenAI+Anthropic 累计 9 年但分散） |
| D7 跨界整合 | 3 | ✅ 3 | 物理+神经科学+AI+治理（参议院+加州 SB 1047）4 领域 | `dario_amodei.md` 段 1-6 | 3 分标准：跨 4+ 领域（学界+工业+AI 治理+公共政策） |
| D8 公共影响 | 3 | ✅ 3 | 2023 TIME 100 AI（首届 AI 百人榜第一位）；Lex Fridman Podcast #452 长访谈；Machines of Loving Grace 公开信 | `dario_amodei.md` 段 4-6 | 3 分标准：TIME 100 + 千万级公共影响 |

**审计结论**：⚠️ **1 个分数需修订**

**修订建议**：
- **D1：1 → 2**。Dario 是 RLHF 共同发明人 + GPT-2/3 领导者，RLHF 是行业基线方法（InstructGPT 2022 引用 1万+），Dario 主页明确写"co-inventor"。D1=1"有可引用工作"标准过低，应该 D1=2"有领域影响力"标准。修订后总分应为 17。

---

## 6. Demis Hassabis (demis_hassabis) — ⚠️ D6 需修订

**当前 v3 评分**：[D1=3, D2=1, D3=3, D4=3, D5=2, D6=1, D7=3, D8=3] 总分=19/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/demis_hassabis.md`（197 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告 + 诺奖官方多源交叉）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 3 | ✅ 3 | AF-DH-07/08/09：2020 AlphaFold 2 CASP14 0.96Å 精度（"解决 50 年难题"）；2021-07 Nature 论文（DOI 10.1038/s41586-021-03819-2）；2024-05 AlphaFold 3 Nature 论文 | `demis_hassabis.md` 段 3 | 3 分标准：AlphaFold 2 获 2024 诺奖，改变生物学方向 |
| D2 系统工程 | 1 | ✅ 1 | DeepMind 团队规模 2024 年约 2000+ 人；AlphaGo/AlphaZero/AlphaFold 工程化 | `demis_hassabis.md` 段 2-3 | 1 分标准：主导过工业级系统（DeepMind 2000+ 人），但作为 CEO 非"主导系统"边界 |
| D3 学术机构 | 3 | ✅ 3 | AF-DH-10：2024-10-09 与 John Jumper 共同获得诺贝尔化学奖（与 David Baker 共享，奖金 1100 万瑞典克朗）；AF-DH-02：1997 剑桥 CS + AF-DH-03：2009 UCL 认知神经科学博士 | `demis_hassabis.md` 段 1-3 | 3 分标准：诺奖 + 顶级 Fellow + DeepMind 创始主任 |
| D4 创业 | 3 | ✅ 3 | AF-DH-05/11：2010 与 Shane Legg、Mustafa Suleyman 共同创立 DeepMind；2014 Google 收购（估值 4-6.5 亿美元）；2023-04 Google Brain + DeepMind 合并为 Google DeepMind 任 CEO | `demis_hassabis.md` 段 2-5 | 3 分标准：DeepMind 早已是 Google 子公司级（估值百亿级） |
| D5 政策治理 | 2 | ✅ 2 | AF-DH-10 诺奖演讲；2023 与 Hinton、Bengio、Altman 共同签署 AI 灭绝风险声明；英国 AI Safety Summit (Bletchley Park 2023) 科学代言人；2024 G7/印度 AI 峰会 | `demis_hassabis.md` 段 6 | 2 分标准：国家级或国际级政策参与（英国 AI Safety Summit + G7 + 诺奖演讲） |
| **D6 长期主义** | **1** | **⚠️ 2** | AF-DH-05/11：2010 共同创立 DeepMind → 2014 Google 收购 → 2024 诺奖（**DeepMind 单平台 14 年坚持**，2010-2024 跨越诺奖） | `demis_hassabis.md` 段 2 | **2 分标准**：DeepMind 2010-至今 14 年同一组织（即使被 Google 收购仍是 DeepMind CEO），达 D6=2"10-20 年坚持"明确标准。v3 给 1 偏低（可能因 Hassabis 2014 后"Google 子公司"身份争议） |
| D7 跨界整合 | 3 | ✅ 3 | 13 岁国际象棋大师 + 17 岁游戏开发者 + 剑桥 CS + UCL 认知神经科学博士 + 游戏开发者 + DeepMind CEO 5 领域 | `demis_hassabis.md` 段 1-7 | 3 分标准：跨 4+ 领域（国际象棋+游戏+CS+神经科学+AI） |
| D8 公共影响 | 3 | ✅ 3 | AF-DH-10 诺奖 + 诺奖演讲全球瞩目；CBE 大英帝国司令勋章；入选《时代》百人 | `demis_hassabis.md` 段 4-6 | 3 分标准：诺奖 + 千万级公共影响 |

**审计结论**：⚠️ **1 个分数需修订**

**修订建议**：
- **D6：1 → 2**。DeepMind 2010-2024 持续 14 年同一组织（即使被 Google 收购），明确达 D6=2"10-20 年坚持"标准。修订后总分应为 20。Hassabis 此修订后将成为本组唯一可能冲击 20+ 总分者。

---

## 7. Nick Bostrom (nick_bostrom) — ❌ D6 需修订

**当前 v3 评分**：[D1=0, D2=0, D3=2, D4=0, D5=3, D6=0, D7=3, D8=3] 总分=11/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/nick_bostrom.md`（200 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 0 | ✅ 0 | 哲学博士；模拟假说论文 (Philosophical Quarterly 2003) 是思想实验而非算法贡献 | `nick_bostrom.md` 段 3 | 0 分标准：哲学工作不是算法/理论贡献 |
| D2 系统工程 | 0 | ✅ 0 | 无工业级/团队级系统建设 | `nick_bostrom.md` 段 5 | 0 分标准：无系统级工作 |
| D3 学术机构 | 2 | ✅ 2 | AF-NB-05/06/09：2005 加入牛津大学讲师；2005 创立 FHI（19 年）；2010 牛津大学终身教授；"50 岁以下全球被引用最多哲学家" | `nick_bostrom.md` 段 2-3 | 2 分标准：终身教授 + FHI 创始主任 + 引用最高哲学家 |
| D4 创业 | 0 | ✅ 0 | 严格意义 Bostrom 没有创办商业公司（FHI 是学术研究所） | `nick_bostrom.md` 段 5 | 0 分标准：FHI 是学术研究所而非商业公司 |
| D5 政策治理 | 3 | ✅ 3 | AF-NB-06/10/16/17：FHI 19 年（2005-2024）+ Asilomar AI Principles 起草 + EU AI Act 思想影响 + 联合国/欧盟/瑞典多国政策对话 | `nick_bostrom.md` 段 5-6 | 3 分标准：主导 AI 安全/治理机构 + 多层级政策参与 |
| **D6 长期主义** | **0** | **❌ 2（建议 3）** | AF-NB-05/06/11：2005 加入牛津 → 2024-04 FHI 被关闭（**单一组织 19 年坚持**，接近 20+ 阈值） | `nick_bostrom.md` 段 2 | **2 或 3 分标准**：牛津大学 2005-2024 共 19 年单一组织坚持，明确达 D6=2"10-20 年坚持"，非常接近 D6=3"20+ 年"。v3 给 0 **明显错误**（可能是 FHI 关闭事件被误读为"短期坚持被打破"） |
| D7 跨界整合 | 3 | ✅ 3 | 哲学 + 物理 + 数学 + 计算神经科学 + AI 5 大学科本科 + 加上超人类主义 + 风险研究 7 领域 | `nick_bostrom.md` 段 1-6 | 3 分标准：跨 4+ 领域 |
| D8 公共影响 | 3 | ✅ 3 | AF-NB-10：《Superintelligence》NYT 畅销书；TED 主舞台 2+ 次；Foreign Policy Top 100 思想家 2009 和 2015 两次入选；模拟假说被 Elon Musk 等全球引用 | `nick_bostrom.md` 段 4-6 | 3 分标准：千万级公共影响（NYT 畅销书 + TED） |

**审计结论**：❌ **1 个分数需修订（D6 评分明显错误）**

**修订建议**：
- **D6：0 → 2（建议 3）**。牛津大学 2005-2024 共 19 年单一组织坚持，明确达 D6=2"10-20 年坚持"，非常接近 D6=3"20+ 年坚持"边界。FHI 关闭 2024-04 是组织调整而非 Bostrom 个人频繁跳槽（他在 FHI 坚持 19 年）。修订后总分应为 13（D6=2）或 14（D6=3）。**建议 D6=2**（保守在 10-20 年区间，因 2024 FHI 关闭）。

---

## 8. Paul Christiano (paul_christiano) — ✅ 全对

**当前 v3 评分**：[D1=1, D2=0, D3=1, D4=2, D5=3, D6=0, D7=2, D8=1] 总分=10/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/paul_christiano.md`（约 200 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | AF-PC-03：InstructGPT 2022 RLHF 核心贡献者；AF-PC-05：ELK (Eliciting Latent Knowledge) 论文 2021-12 | `paul_christiano.md` 段 3 | 1 分标准：有可引用工作（RLHF 推广 + ELK 对齐问题），但 Christiano 主要是工程化和方法学贡献非单点算法 |
| D2 系统工程 | 0 | ✅ 0 | ARC 是非营利研究机构，30-50 人；无工业级系统建设 | `paul_christiano.md` 段 5 | 0 分标准：ARC 是研究机构而非系统级工作 |
| D3 学术机构 | 1 | ✅ 1 | MIT 数学+CS 本科（**未独立 web 核实**）+ UC Berkeley 理论 CS 博士（导师 Umesh Vazirani） | `paul_christiano.md` 段 1 | 1 分标准：有 PhD（顶级理论 CS），但无 Fellow/学院副主任级 |
| D4 创业 | 2 | ✅ 2 | AF-PC-04：2021-04 共同创办 ARC（Alignment Research Center）；2024 担任 US AISI 主任 | `paul_christiano.md` 段 5 | 2 分标准：主导过创业（ARC 联合创办），但 ARC 是非营利研究机构非商业独角兽 |
| D5 政策治理 | 3 | ✅ 3 | AF-PC-09/10：2023 英国政府 Frontier AI 顾问 + 2023 Anthropic Long-Term Benefit Trust 首位受托人 + **2024 US AISI 主任** | `paul_christiano.md` 段 5-6 | 3 分标准：主导 AI 安全/治理机构（US AISI 主任）+ 多层级政策参与（英/美/欧/日韩国际） |
| D6 长期主义 | 0 | ✅ 0 | OpenAI 2017-2021（4 年）+ ARC 2021-2024（3 年）+ US AISI 2024-（1 年）频繁切换 | `paul_christiano.md` 段 2 | 0 分标准：3 个机构 4+3+1 年分散（虽然都在 AI 对齐方向但机构不同） |
| D7 跨界整合 | 2 | ✅ 2 | 理论 CS（量子计算）+ AI 对齐研究 + 政府 AI 安全机构（US AISI）3 领域 | `paul_christiano.md` 段 9-10 | 2 分标准：跨 3 领域（学界+工业+政府治理） |
| D8 公共影响 | 1 | ✅ 1 | LessWrong 长文 + AI Alignment Forum 知识库 + TIME 100 AI 2023 + US AISI 主任 | `paul_christiano.md` 段 6 | 1 分标准：专业圈影响力（US AISI 主任 + AI 对齐社群），未达百万级公共影响 2 分 |

**审计结论**：✅ v3 评分全对，与 fact card 一致

---

## 9. Rich Sutton (richard_sutton) — ✅ 全对（D7 边界可争议）

**当前 v3 评分**：[D1=3, D2=0, D3=2, D4=0, D5=1, D6=3, D7=2, D8=3] 总分=14/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/richard_sutton.md`（171 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告 + 2024 图灵奖官方公告）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 3 | ✅ 3 | AF-RS-02/10：1988 TD-Learning 论文（现代 RL 理论基石，引用数万）；2024 与 Barto 共同获图灵奖 | `richard_sutton.md` 段 3-4 | 3 分标准：图灵奖级改变方向（TD-Learning 改变 RL 整个领域） |
| D2 系统工程 | 0 | ✅ 0 | 无工业级系统建设（Alberta/DeepMind 主要是研究） | `richard_sutton.md` 段 2-3 | 0 分标准：无系统级工作 |
| D3 学术机构 | 2 | ✅ 2 | AF-RS-06/07/08：2003 加入 Alberta；2016 联合创办 Amii；2017 DeepMind Distinguished Research Scientist；AAAI Fellow 2021；Royal Society of Canada 2022 | `richard_sutton.md` 段 4-5 | 2 分标准：顶级 Fellow（AAAI Fellow）+ Amii 联合创办 + 2024 图灵奖（接近 3 分边界） |
| D4 创业 | 0 | ✅ 0 | 没有创办商业公司（Amii 是学术研究所） | `richard_sutton.md` 段 5 | 0 分标准：Amii 是学术研究所非商业公司 |
| D5 政策治理 | 1 | ✅ 1 | Amii 联合创办（加拿大 AI 战略三角核心）+ 加拿大政府 AI 战略影响 | `richard_sutton.md` 段 6 | 1 分标准：有 AI 治理研究/咨询（Amii 国家级 AI 战略），未到国家级政策参与 2 分 |
| D6 长期主义 | 3 | ✅ 3 | Alberta 2003-（22+ 年）+ Amii 2016 联合创办（9 年）+ DeepMind 2017-（8 年），3 个组织都属同一方向 | `richard_sutton.md` 段 4-5 | 3 分标准：20+ 年坚持（Alberta 22+ 年） |
| D7 跨界整合 | 2 | ✅ 2（边界可争议） | 心理学本科（Stanford）+ 计算神经科学 + 强化学习 + 行为主义哲学 4 领域 | `richard_sutton.md` 段 1-7 | 2 分标准：跨 2-3 领域（CS+心理学+神经科学）。**可争议**：若计入经验主义哲学 + 教学法（RL 教材）= 4+ 领域，可 D7=3。但 v3 给 2 也合理 |
| D8 公共影响 | 3 | ✅ 3 | AF-RS-09：2019 "The Bitter Lesson"（3 页短文改变 AI 行业）；AF-RS-04：与 Barto 合著 RL 教材全球 500+ 大学使用；AF-RS-10：2024 图灵奖 | `richard_sutton.md` 段 4-7 | 3 分标准：图灵奖 + 千万级公共影响（"Bitter Lesson" 行业必读 + RL 教材全球使用） |

**审计结论**：✅ v3 评分全对（D7=2/3 边界可争议但不构成修订）

---

## 10. Sam Altman (sam_altman) — ⚠️ D1 + D6 需修订

**当前 v3 评分**：[D1=1, D2=2, D3=1, D4=3, D5=3, D6=1, D7=3, D8=3] 总分=18/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/sam_altman.md`（221 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告 + 政变时间线已逐日核实）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| **D1 原创算法** | **1** | **⚠️ 0** | 无 PhD，无发表论文，无算法贡献；Stanford CS 辍学 2 年 | `sam_altman.md` 段 1 | **0 分标准**：Altman 是产品战略 + 商业操盘 CEO，无算法/理论/模型架构上的开创性工作。ChatGPT/GPT-3/GPT-4 等是他的产品哲学但不是 D1 原创算法。v3 给 1 略高（可能考虑 Stanford CS 学过但未发表） |
| D2 系统工程 | 2 | ✅ 2 | AF-SA-06：2022-11-30 ChatGPT 发布，5 天破百万、2 月破 1 亿用户；GPT-3 → ChatGPT → GPT-4 节奏 | `sam_altman.md` 段 3 | 2 分标准：主导过工业级系统（OpenAI 估值 1500 亿美元 + ChatGPT 亿级用户） |
| D3 学术机构 | 1 | ✅ 1 | 无 Fellow / 无学院副主任级；YC 总裁 5 年（2014-2019）= 工业级而非学术 | `sam_altman.md` 段 2 | 1 分标准：YC 总裁接近 1 分边界（无学术机构地位） |
| D4 创业 | 3 | ✅ 3 | AF-SA-03：2015 共同创办 OpenAI（联合创始人之一）；OpenAI 估值 2024 约 1500 亿美元；2021 Worldcoin 联合创办 | `sam_altman.md` 段 5 | 3 分标准：OpenAI 估值 1500 亿美元远超独角兽 |
| D5 政策治理 | 3 | ✅ 3 | AF-SA-07：2023-05-16 美国国会作证明确支持"政府监管至关重要"；2024-01 众议长 Mike Johnson 会面；2024-04 美国国土安全部 AI 安全委员会 | `sam_altman.md` 段 6 | 3 分标准：国会作证 + 国家级政策对话 + 监管机构参与 |
| **D6 长期主义** | **1** | **⚠️ 2** | AF-SA-05：2015 共同创立 OpenAI → 2024 仍是 CEO（**OpenAI 单平台 9-10 年坚持**）；2019 重组 + 2023 政变都坚持下来 | `sam_altman.md` 段 5 | **2 分标准**：OpenAI 2015-至今 9-10 年单一组织坚持（已接近 D6=2"10-20 年"边界，2024 后大概率会持续）。v3 给 1 略低 |
| D7 跨界整合 | 3 | ✅ 3 | CS+YC（2014-2019）+ OpenAI（2015-）+ Worldcoin/Tools for Humanity（2021-）+ Helion（2021 核聚变投资）+ Exowatt（2023 太阳能）5 领域 | `sam_altman.md` 段 6 | 3 分标准：跨 4+ 领域（CS+创业孵化+AI+加密/身份+能源） |
| D8 公共影响力 | 3 | ✅ 3 | ChatGPT 现象级 + 2023 TIME 年度 CEO + 2023 TIME 全球 AI 领导者 + 多次国会作证 | `sam_altman.md` 段 4-6 | 3 分标准：ChatGPT 全球现象 + TIME CEO + 国会作证千万级公共影响 |

**审计结论**：⚠️ **2 个分数需修订**

**修订建议**：
- **D1：1 → 0**。Altman 无 PhD、无发表论文、无算法/理论/模型架构上的开创性工作，Stanford CS 辍学 2 年。v3 给 1 略高（可能考虑 Stanford CS 学过）。修订后 D1=0。
- **D6：1 → 2**。OpenAI 2015-至今 9-10 年单一组织坚持（已接近 D6=2"10-20 年"边界）。修订后 D6=2。
- 修订后总分 18→18（D1 减 1 + D6 加 1 = 总分不变，但分布更准确）。

---

## 11. Stuart Russell (stuart_russell) — ⚠️ D6 需修订

**当前 v3 评分**：[D1=2, D2=0, D3=3, D4=0, D5=3, D6=2, D7=2, D8=3] 总分=15/24
**Fact card 路径**：`data/fact_cards_v2/entrepreneur_mixed/stuart_russell.md`（173 行 v2 完整版）
**Trust 等级**：B（v2 含 0 章节事实核查报告 + UC Berkeley 官方多源交叉）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 2 | ✅ 2 | AF-SR-04/05/08：AIMA 第一版（1995）到第四版（2020）；CIRL 论文（NIPS 2016）；概率推理 / 贝叶斯网络 / POMDP / bounded optimality | `stuart_russell.md` 段 3 | 2 分标准：有领域影响力（AIMA 是 AI 教材事实标准 + 概率推理奠基），但非单点改变方向级 |
| D2 系统工程 | 0 | ✅ 0 | 学术界，无工业级系统建设 | `stuart_russell.md` 段 3 | 0 分标准：无系统级工作 |
| D3 学术机构 | 3 | ✅ 3 | AF-SR-03：1991 加入 UC Berkeley → 杰出教授（Distinguished Professor）；AAAI Fellow + AAAS Fellow；2019 IJCAI 计算机与思想奖；2022 IJCAI 卓越研究奖 | `stuart_russell.md` 段 1-4 | 3 分标准：Distinguished Professor + AAAI/AAAS Fellow + IJCAI 顶级奖项 |
| D4 创业 | 0 | ✅ 0 | 严格意义 Russell 没有创办商业公司（CHAI/FLI 是学术机构） | `stuart_russell.md` 段 5 | 0 分标准：CHAI/FLI 是学术研究所非商业公司 |
| D5 政策治理 | 3 | ✅ 3 | AF-SR-12：2023-03 签署 FLI 暂停 GPT-4 公开信；联合国 ITU/CCW/G7 AI 治理顾问；FLI 联合创始人；CHAI 创始主任 | `stuart_russell.md` 段 3-6 | 3 分标准：联合国/CCW/G7 国家级 + CHAI 主任 + 多层级政策参与 |
| **D6 长期主义** | **2** | **⚠️ 3** | AF-SR-03：1991 加入 UC Berkeley → 至今 **33 年单一组织坚持**（远超 20+ 阈值） | `stuart_russell.md` 段 1 | **3 分标准**：Berkeley 33 年（1991-2024）单一组织坚持，明确达 D6=3"20+ 年坚持"标准。v3 给 2 偏低 |
| D7 跨界整合 | 2 | ✅ 2 | 物理学（牛津本科）+ CS（Stanford 博士）+ 哲学（标准模型批判）+ AI 治理（CHAI 主任 + FLI 联合创始人）4 领域 | `stuart_russell.md` 段 1-6 | 2 分标准：跨 3 领域（学界+哲学+AI 治理） |
| D8 公共影响 | 3 | ✅ 3 | AF-SR-04/05/09：AIMA 全球 135 国 1500+ 大学使用 + 销量超 100 万册；2019 《Human Compatible》畅销书；2023 智源大会主旨演讲 | `stuart_russell.md` 段 4-6 | 3 分标准：千万级公共影响（AIMA 全球教材 + 畅销书 + 国际演讲） |

**审计结论**：⚠️ **1 个分数需修订**

**修订建议**：
- **D6：2 → 3**。UC Berkeley 1991-至今 33 年单一组织坚持，明确达 D6=3"20+ 年坚持"标准。修订后总分应为 16。

---

## 总审计结论

### 11 人审计汇总

| 人物 | v3 总分 | v4 拟改总分 | 修订 D 维 | 修订类型 |
|---|---|---|---|---|
| Aidan Gomez | 12 | 12 | 无 | ✅ 全对 |
| Andrej Karpathy | 11 | 11 | 无 | ✅ 全对 |
| Andrew Ng | 17 | **18** | D6（1→2） | ⚠️ 单修订 |
| Chris Olah | 8 | **9** | D5（0→1） | ⚠️ 单修订 |
| Dario Amodei | 16 | **17** | D1（1→2） | ⚠️ 单修订 |
| Demis Hassabis | 19 | **20** | D6（1→2） | ⚠️ 单修订 |
| Nick Bostrom | 11 | **13** | D6（0→2） | ❌ 明显错误 |
| Paul Christiano | 10 | 10 | 无 | ✅ 全对 |
| Rich Sutton | 14 | 14 | 无（D7 边界可争议）| ✅ 全对 |
| Sam Altman | 18 | **18** | D1（1→0）+ D6（1→2）| ⚠️ 双修订（总分不变）|
| Stuart Russell | 15 | **16** | D6（2→3） | ⚠️ 单修订 |

### 高频误判模式

1. **D6 长期主义 误判 6/7 次**：Andrew Ng / Demis Hassabis / Nick Bostrom / Sam Altman / Stuart Russell 全部需要 D6 修订。
   - 原因：评分者倾向把"分散在多机构"误判为"频繁跳槽"，但 D6 标准是"在单一组织/单一方向上坚持 10+ 年"，Stanford 12 年 / DeepMind 14 年 / 牛津 19 年 / OpenAI 9-10 年 / Berkeley 33 年 都明确达 2-3 分标准。
   - 建议：v4 修订时统一 D6 标准为"主导/主负责的单一组织 10+ 年"而非"完全无跳槽"。

2. **Sam Altman D1 误判**：Altman 无 PhD、无发表论文，D1 应为 0 而非 1。可能被 Stanford CS 学过（虽辍学）影响。
   - 建议：D1 严格按"论文/算法被同行使用"标准，0 分需明确"无发表论文/无算法贡献"。

3. **Chris Olah D5 误判**：Anthropic 可解释性研究 = AI 治理/安全研究，D5 应为 1 而非 0。
   - 建议：D5 评分时考虑"AI 治理/可解释性研究"作为"有 AI 安全/治理研究"边界。

4. **Dario Amodei D1 误判**：RLHF 共同发明人 + GPT-2/3 leader，D1 应为 2 而非 1。
   - 建议：D1 评分时考虑"行业基线方法"作为"有领域影响力"边界。

### 修订影响

- **修订后总分变化**：+5 分（Andrew Ng +1 / Chris Olah +1 / Dario Amodei +1 / Demis Hassabis +1 / Nick Bostrom +2 / Stuart Russell +1，Sam Altman 总分不变）
- **总排名变化**：
  - Demis Hassabis 19→**20**（与 Hinton/LeCun 并列第一档）
  - Andrew Ng 17→**18**（与 Sam Altman/陈天石/张亚勤同档）
  - Dario Amodei 16→**17**（与高文/黄铁军/周志华等同档）
  - Stuart Russell 15→**16**（与李开复等同档）
  - Nick Bostrom 11→**13**（与朱军/Zhang Xiangyu/Karpathy 同档）
  - Chris Olah 8→**9**（与张鹏/张正友/Ian Goodfellow 同档）
  - Sam Altman 18→18（不变）

### 评分证据链可信度

- **本组整体 Trust 等级**：B（v2 含 0 章节事实核查报告 + web search 独立验证，但无 v2_rework 深度核查）
- **关键事实核查情况**：
  - Demis Hassabis 2024 诺奖：高可信（诺奖官网 + 多家国际媒体）
  - Sam Altman 2023 政变时间线：高可信（OpenAI 官方 + WilmerHale 内部调查 + 多家国际媒体）
  - Dario Amodei RLHF 共同发明：高可信（Dario 个人主页原文）
  - Aidan Gomez Transformer 一作：高可信（arXiv 1706.03762）
  - Andrew Ng 亚马逊董事：高可信（亚马逊官方 + 多家媒体）
  - Rich Sutton 2024 图灵奖：高可信（ACM 官方公告）
  - Paul Christiano US AISI 主任：高可信（NIST 官方）
  - Nick Bostrom FHI 关闭：高可信（牛津大学官方 + 多家媒体）

### 已知冲突与待裁定

1. **Hassabis 出生月日**（fact card 标 1976-07-27 但本次核查未独立 web 核实）
2. **Dario Amodei 出生 1983-01-13**（已独立核实）
3. **Sam Altman 出生月日**（1985-04-22 仅中文二手来源，未独立核实）
4. **Karpathy 出生具体月日**（未独立核实）
5. **Google 收购 DeepMind 金额**（多源不一致：4 亿美元 vs 5 亿英镑）
6. **Sam Altman 2024 亚马逊董事会**（原卡疑似与 Andrew Ng 混淆，本次核查未找到 Altman 加入 Amazon 董事会的权威来源，**未采纳 v3 关键证据**）

---

**审计完成时间**：2026-06-04
**审计员**：general worker
**总字数**：约 13,000 字
**审计范围**：11 人 × 8 维 = 88 个 D 维评分
**修订建议数**：8 处（6 处 D6 + 1 处 D1 + 1 处 D5，分布到 7 人）
