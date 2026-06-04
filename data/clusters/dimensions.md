# 60 人 8 维核心能力模型 v3（D1-D8）

> 基于 82 条 L2 二级能力簇（clusters.md）的选择性编码（Selective Coding）。
> 8 维是 L2 簇的高阶聚合，每个 D 维度对应 6-10 个 L2 簇。
> 60 人 × 8 维打 0-3 分（0=无/1=有/2=有影响力/3=改变方向）。
> v3 与 v2 的 8 维名称保持一致（避免破坏 portrait.html 用户识别），v3 进一步把评分证据从 L0 升级为"L0 → L1 → L2 → D"完整证据链。

## v3 评分证据链（关键差异）

v2 阶段评分证据：直接引用 L0 事实（"2018 博士毕业"+ ResNet 论文 → D1=3 分"）
v3 阶段评分证据：L0 事实 → L1 能力（具体能力抽象）→ L2 簇（主题聚类）→ D 维（高阶聚合）→ 评分

**示例：何恺明 D1=3 分**
- L0 事实：`AF-HK-01` 2015 ResNet（Nature 2015 论文，引用 25 万+）+ `AF-HK-02` 2021 MAE
- L1 能力：`AB-HK-01` 深度学习架构设计能力（ResNet+MAE+暗通道）→ **簇 1 深度学习核心算法贡献**
- L2 簇：簇 1 深度学习核心算法贡献
- D 维：D1 原创算法 / 理论贡献
- 评分：3 分（改变方向，引用 25 万+）

**这个证据链的意义**：
- L0 → L1：表明"哪些事实能证明这个能力"（可追溯到原始事实）
- L1 → L2：表明"这个能力属于哪个主题聚类"（可与他人 L1 对比）
- L2 → D：表明"这个主题聚类对应哪个高阶能力维度"（8 维的核心逻辑）

**为什么 v3 优于 v2**：
- v2 跳过 L1 层，评分证据直接从 L0 到 D，**容易被 L0 数量而非 L0 质量主导**（如"30 篇论文" vs "1 篇引用 10 万次论文"）
- v3 通过 L1 层强制做"能力抽象"判断，**质量优先于数量**
- 472 条 L1 能力可与他人 L1 横向对比，**形成更可信的能力档案**

---

（原 v2 内容继续保留，仅在评分时使用 v3 证据链）



---

## D1 原创算法 / 理论贡献（R&D Originality）

- **定义**：在 AI 算法、理论、模型架构上有可被引用、可改变方向的开创性工作（不限于 LLM/RL/CV/NLP 等具体子领域）。
- **对应 L2 簇**：
  - 簇 1 深度学习核心算法贡献（反向传播/玻尔兹曼机/ResNet 等）
  - 簇 2 Transformer / LLM 核心贡献（Transformer 共同作者/RLHF/XLNet/Seq2Seq 等）
  - 簇 3 强化学习理论贡献（TD-Learning/Bitter Lesson/CIRL 等）
  - 簇 4 计算机视觉核心算法（GAN/ResNeXt/ConvNeXt/NIN/ShuffleNet 等）
  - 簇 5 大模型架构创新（MoE/Mamba/MLA/DiT 等）
  - 簇 6 AI for Science 算法贡献（Neural ODE/DeePMD/HMM 等）
  - 簇 7 NLP/多模态核心算法（神经概率语言模型/ERNIE/MiniCPM 等）
  - 簇 54 数学/物理基础理论（梯度消失/深度森林/学件/统计视觉等）
  - 簇 55 认知/哲学/AGI 理论（小数据大任务/UV 双系统/祖母细胞等）
- **评分标准**：
  - **0** = 无
  - **1** = 有可引用工作（论文/算法被同行使用）
  - **2** = 有领域影响力（论文引用数千+或被广泛使用）
  - **3** = 改变方向（Nature/图灵/诺奖级别，引用万+ 改变行业方向）
- **典型 3 分**：Hinton、LeCun、Bengio、He Kaiming、Xie Saining、Ilya Sutskever、Aidan Gomez、Demis Hassabis、鄂维南、张祥雨、Yan Shuicheng
- **典型 0 分**：王小川（搜狗创业+百川大模型 主营产品）、闫俊杰（M 系列 主营工程化）、李开复（创新工场+零一万物 主营商业化）
- **典型 1-2 分**：Zhang Bo（中国 AI 领域首位 IJCAI 论文 1984，奠基性但非 3 分级）、Goodfellow（GAN 一作 85000+ 引 2.5-3 分区间）、E Weinan（Neural ODE/DeePMD 2.5 分）、Yang Zhilin（XLNet 第一作者 2 分）

---

## D2 系统工程能力（Systems Engineering）

- **定义**：把算法工程化为可大规模运行的系统（万卡训练/亿级用户/工业级框架/AI 芯片）。
- **对应 L2 簇**：
  - 簇 8 分布式系统基础设施（MapReduce/BigTable/Spanner/TensorFlow/TPU 设计）
  - 簇 9 深度学习框架构建（TensorFlow/飞桨/PyTorch/OpenMMLab）
  - 簇 10 工业级大模型训练系统（通义/Qwen/Command A）
  - 簇 11 AI 芯片 / 加速器（寒武纪思元/地平线征程/求索/TPU）
  - 簇 60 软硬一体化基础设施（TensorFlow+TPU+Azure AI）
  - 簇 72 AI 训练/推理基础设施（通义/Qwen 6 亿+下载）
  - 簇 73 大模型架构工程化（GLM 工程化/M 系列 MoE 工程化）
- **评分标准**：
  - **0** = 无系统级工作
  - **1** = 主导过小型系统（团队级/部门级）
  - **2** = 主导过工业级系统（公司级/亿级用户）
  - **3** = 主导过定义行业的基础设施（TensorFlow/MapReduce 级）
- **典型 3 分**：Jeff Dean（MapReduce/BigTable/Spanner/TensorFlow/TPU 全部）、周靖人（通义/Qwen 6 亿+下载 + 2018 阿里 17 亿条/秒）
- **典型 0-1 分**：多数纯学术人物（朱军 0-1、Xie Saining 0-1、E Weinan 0-1）
- **典型 2 分**：Wang Haifeng（飞桨 + 文心 ERNIE）、Lin Dahua（OpenMMLab）、陈天石（思元 590）、余凯（征程 J 系列）、Xuedong Huang（Azure AI）

---

## D3 学术机构地位 / 顶级 Fellow 头衔（Academic Position）

- **定义**：在顶级学术机构/学院/实验室担任核心领导，或获得图灵/诺贝尔/中科院院士/五大 Fellow 等顶级学术荣誉。
- **对应 L2 簇**：
  - 簇 12 AI 学术机构/学院创建（LAMDA/MMLab/清华 AI 院/北大 AI 院/上海 AI Lab）
  - 簇 13 国家级实验室创建（鹏城实验室/中关村人工智能研究院/通义实验室）
  - 簇 14 AI 研究机构商业化（Mila/Element AI/OpenMMLab/上海 AI Lab）
  - 簇 15 中国本土研究机构生态（智源/IDEA/清华 AIR/上海 AI Lab）
  - 簇 31 学界长期坚守（30+ 年单机构）
  - 簇 48 诺贝尔/图灵奖级别
  - 簇 49 国际 Fellow 头衔（IEEE/ACM/AAAI/NAE/AAAS）
  - 簇 50 中国本土最高学术荣誉（中科院/工程院院士/国家自然科学一等奖）
- **评分标准**：
  - **0** = 无
  - **1** = 有 Fellow 头衔或学院/实验室副主任级
  - **2** = 顶级 Fellow 五大到位之一 或 院长/所长级
  - **3** = 图灵/诺贝尔/中科院院士 + 五大 Fellow 全到位（华人 5 人：Zhou Zhihua/Wang Haifeng/Zhang Zhengyou/Tian Qi/Zhu Jun）+ 学院创始院长
- **典型 3 分**：Hinton、LeCun、Bengio（3 人共获图灵奖 + Bengio 共同创立 Mila）、Zhou Zhihua（五大 Fellow + 中科院院士 + LAMDA 创始人 + 南大副校长）、Sutton（图灵 2024）、Demis Hassabis（诺奖 2024 + DeepMind CEO）
- **典型 2 分**：Wang Haifeng（ACL Fellow 首位中国大陆 + IEEE + CAAI + 国家卓越工程师）、Zhang Zhengyou（IEEE + ACM Fellow）、Tian Qi（IEEE + ACM + CAAI 院士）、Zhu Jun（IEEE + AAAI Fellow + 生数创始人）
- **典型 1 分**：杨植麟（清华助理教授 + 引用 2 万）

---

## D4 创业 / 商业化能力（Entrepreneurship）

- **定义**：创办过 AI/科技公司或担任 CEO/CTO 推动产品商业化、融资、上市。
- **对应 L2 簇**：
  - 簇 37 通用大模型创业（OpenAI/SSI/Anthropic/DeepMind/Cohere/DeepSeek/Moonshot/智谱/面壁/生数/MiniMax/阶跃/百川/零一万物）
  - 簇 38 AI for Science 创业（Isomorphic/深势）
  - 簇 39 行业 AI 创业（思谋/Landing.ai/百川医疗）
  - 簇 40 智能驾驶/机器人创业（地平线/宇树）
  - 簇 41 AI 芯片/算力创业（寒武纪/地平线/求索）
  - 簇 42 AI 应用/工具创业（Eureka Labs/Coursera/DeepLearning.AI/创新工场）
  - 簇 43 互联网时代连续创业→AI（小米/美团/字节/光年之外/零一万物/Landing.ai）
  - 簇 44 跨周期连续创业（循环→月之暗面/幻方→DeepSeek/MSRA→阶跃/ARCI→US AISI）
- **评分标准**：
  - **0** = 无
  - **1** = 参与过创业（联创/早期员工/天使投资人）
  - **2** = 主导过创业（CEO/CTO/创始人，融过 A 轮+）
  - **3** = 主导过独角兽/上市公司（估值 10 亿美元+ 或已上市）
- **典型 3 分**：Sam Altman（OpenAI 估值 1500 亿）、Dario Amodei（Anthropic 估值 1840 亿）、Ilya Sutskever（SSI 32B 估值）、Demis Hassabis（DeepMind→Google DeepMind）、Aidan Gomez（Cohere 55 亿）、陈天石（寒武纪 6600 亿）、雷军（小米 8000 亿+）、张一鸣（字节 2.25 万亿）、余凯（地平线 2024-10 上市）、Ilya Sutskever、Demis Hassabis、Aidan Gomez
- **典型 2 分**：梁文锋（DeepSeek 2026 估值 180 亿美元）、杨植麟（月之暗面 180 亿美元）、唐杰/张鹏（智谱 574 亿港元上市）、姜大昕（阶跃 20 亿美元）、王慧文（光年之外独角兽 10 亿美元被美团收购 20.65 亿）、王兴兴（宇树 70% 全球份额）
- **典型 1 分**：朱军（生数科技联合创始）、沈向洋（IDEA 创院理事长，非商业化）
- **典型 0 分**：鄂维南（学术）、张钹（学术）、汤晓鸥（学术+商汤创始人部分已故）

---

## D5 政策治理参与（Policy & Governance）

- **定义**：直接进入国家级政策对话、政协/人大、监管制度设计、国际治理机构、AI 安全/对齐研究机构。
- **对应 L2 簇**：
  - 簇 24 国家级政策参与（全国政协/全国人大）
  - 簇 25 国务院/中央政策对话
  - 簇 26 国际治理/标准/规则（联合国/G7/ITU/CCW/ISO）
  - 簇 27 AI 对齐研究（RLHF/ELK/scalable oversight）
  - 簇 28 AI 治理/制度研究（公开信/国会作证/AI 安全路线）
  - 簇 29 AI 安全机构建设（AISI/ARC/CHAI/SSI/LawZero/FHI）
  - 簇 30 AI 可解释性/机制理解（Distill.pub/Anthropic 可解释性）
- **评分标准**：
  - **0** = 无
  - **1** = 有 AI 安全/治理研究（论文/机构）
  - **2** = 国家级或国际级政策参与（国务院/政协/参议院作证/联合国顾问）
  - **3** = 主导 AI 安全/治理机构 + 多层级政策参与（政协/国务院/国际/机构主任）
- **典型 3 分**：高文（2018 政治局集体学习 + 第十四届人大代表 + 鹏城实验室主任）、Stuart Russell（联合国/G7/ITU/CCW + CHAI 主任 + AIMA 对齐章节）、Dario Amodei（Anthropic + 2023 参议院作证 + TIME 100 AI）、雷军（全国工商联副主席 + 第十三届政协常委）
- **典型 2 分**：Bengio（联合国 AI 顾问 + 2025 LawZero 3000 万）、Paul Christiano（US AISI 主任 + Anthropic Trust 受托人 + ARC 创始人）、Hinton（2023 辞职 Google 公开 + 诺奖演讲）、LeCun（公开反对 LLM 路线）
- **典型 1 分**：Ilya Sutskever（SSI 创办）、Chris Olah（Anthropic 可解释性）、Xie Saining（2023 紧急辟谣 Sora 误传 + 2023 NAIA Fellow）

---

## D6 长期主义深度（Long-termism）

- **定义**：在单一组织/单一方向上坚持 10+ 年（甚至 30+ 年），或在 AI 大模型/AGI 方向上长期投入不追短期热点。
- **对应 L2 簇**：
  - 簇 31 学界长期坚守（30+ 年单机构）
  - 簇 32 工业界单平台深耕（20+ 年）
  - 簇 33 大模型/AI 长期主义路线
  - 簇 36 创始团队连环创业
  - 簇 66 学术寒冬/产品失误（寒冬期坚持）
- **评分标准**：
  - **0** = 频繁跳槽/短期切换
  - **1** = 5-10 年坚持
  - **2** = 10-20 年坚持
  - **3** = 20+ 年坚持 或 学术寒冬 30+ 年坚持
- **典型 3 分**：Zhang Bo（清华 71 年）、Zhou Zhihua（南大 32 年）、Hinton（多伦多 30+ 年 + 30 年神经网络寒冬坚持）、Sutton（70 年苦涩教训 + 30 年 RL 坚持）、Jeff Dean（Google 25 年）、Xuedong Huang（微软 30 年）、陈天石（寒武纪 14 年磨剑）、王兴兴（宇树 8 年）
- **典型 2 分**：梁文锋（幻方 8 年 + DeepSeek 3 年）、张林峰（深势 7 年）、Zhang Zhengyou（MSR 20 年 + 腾讯 7 年）
- **典型 0-1 分**：颜水成（5 平台切换）、李航（4 平台）、Karpathy（4 平台）

---

## D7 跨界整合能力（Cross-domain Integration）

- **定义**：在 2+ 个不同领域（学界/工业/创业/政策/跨学科/跨国）跨界整合形成新方向。
- **对应 L2 簇**：
  - 簇 19 跨学科整合（数学/物理/认知/神经科学）
  - 簇 20 商业+技术整合
  - 簇 21 政策+技术整合
  - 簇 22 学术+工业整合（双栖）
  - 簇 23 学术+创业整合
  - 簇 34 学界↔工业界切换
  - 簇 35 跨国平台流动
  - 簇 78 AI 时代组织/管理创新
- **评分标准**：
  - **0** = 单一领域
  - **1** = 跨 2 个领域（如学界+创业 或 数学+AI）
  - **2** = 跨 3 个领域（如学界+工业+政策 或 物理+神经科学+AI）
  - **3** = 跨 4+ 个领域 或 形成新交叉学科
- **典型 3 分**：Demis Hassabis（国际象棋+CS+神经科学+AI 4 领域）、Dario Amodei（物理+神经科学+医学+AI 4 领域）、Sam Altman（CS+YC+OpenAI+Helion+Worldcoin 5 领域）、LeCun（CS+工程+FAIR+AMI 4 领域）、Zhang Linfeng（数学+物理+CS+AI for Science 4 领域）、Hinton（心理学+物理+CS+AI 4 领域）
- **典型 2 分**：Karpathy（Stanford+Tesla+OpenAI+Eureka 4 平台）、Andrew Ng（Stanford+Google+百度+Landing.ai+亚马逊 5 平台）、Andrew Ng 4-5 平台）、雷军（CS+金山+小米+小米汽车 4 领域）、张一鸣（字节+私募 2 领域）
- **典型 1 分**：多数纯学术人物（Zhang Bo 1、E Weinan 1）

---

## D8 公共影响力（Public Influence）

- **定义**：在公众舆论、政策倡导、媒体、教材、公开演讲、公众写作上有广泛影响力。
- **对应 L2 簇**：
  - 簇 45 海外业务规模化
  - 簇 46 国际化团队/产品/客户
  - 簇 47 跨境投资/合作
  - 簇 48 诺贝尔/图灵奖级别
  - 簇 50 中国本土最高学术荣誉
  - 簇 51 AI 经典教材编写
  - 簇 52 大众教育/MOOC
  - 簇 53 公共写作/思想传播
  - 簇 78 AI 时代"摩尔定律"洞察
  - 簇 81 公众舆论/政策倡导
  - 簇 82 AI 时代公共讨论
- **评分标准**：
  - **0** = 无公共发声
  - **1** = 有公开演讲/教材/MOOC（影响万人级）
  - **2** = 有影响力博客/畅销书/百万级观众（影响百万级）
  - **3** = 诺奖/图灵/《时代》百大 + 千万级公共影响
- **典型 3 分**：Hinton（TED《Godfather of AI》数千万次 + 诺奖 + TIME 100）、Sam Altman（OpenAI blog + 2023-05 国会作证）、Demis Hassabis（诺奖 2024）、Dario Amodei（参议院作证 + TIME 100 AI 首位 + Machines of Loving Grace 公开信）、梁文锋（2025-04 TIME 100 + 2025-12《自然》年度十大）、Andrew Ng（Coursera 1 亿学习者）
- **典型 2 分**：Li Kaifu（创新工场 + AI·未来 畅销书 + 《时代》首届 AI 百人）、Bengio（联合国顾问 + 图灵奖 + LawZero 公开信）、Stuart Russell（FLI 公开信 + Human Compatible 畅销书 + AIMA 第四版）、Karpathy（CS231n 1 亿观看 + Eureka Labs）、王小川（IOI 金牌 + 政协委员 + 公开演讲）、Zhang Bo（中国 AI 教育 7 本书 + 院士 + 吴文俊奖）
- **典型 1 分**：多数技术派（纯做技术不写书的）

---

## 8 维交叉观察

| 观察 | 证据 |
|---|---|
| **学术+创业双栖** 在中国大模型时代比例极高 | 唐杰/刘知远/朱军/张鹏/杨植麟/梁文锋/汤晓鸥（已故）7 人同时 D3 高分 + D4 高分 |
| **D1 原创算法 + D6 长期主义** 是西方学派的传统 | Hinton、Sutton、Bengio、LeCun、He Kaiming、Xie Saining 都是 D1=3 + D6=3 |
| **D4 创业 + D5 政策** 是中国创业领军特色 | 雷军、陈天石、王小川、王慧文、印奇、闫俊杰、梁文锋 都有 D4=3 + D5 较高 |
| **D8 公共影响力** 在诺奖/图灵奖后跨越式提升 | Hinton 2024 诺奖后 → 全球最具影响力 AI 公众人物；LeCun 2018 图灵奖后 |
| **D7 跨界整合** 与年龄呈反比、与事业阶段呈正比 | 早期深耕单一领域（如 D1 学术期），成熟期跨界（创业+政策+学术三栖） |
| **D3 学术地位 + D6 长期主义** 是 D1 原创算法的"加速器" | Hinton 30 年多伦多 + LeCun 30 年 NYU/FAIR + 张钹 71 年清华 → D1 全部 3 分 |
| **D5 政策治理** 在中西方切入点不同 | 西方：D5=3 通常通过 AI 安全机构（Russell/Christiano/Hassabis）；东方：D5=3 通常通过政协/国务院（高文/雷军/梁文锋） |
| **D1 原创 + D4 创业** 在大模型时代开始融合 | Aidan Gomez（Transformer 一作 + Cohere CEO）、Ilya Sutskever（AlexNet/Seq2Seq + OpenAI 联合创始人 + SSI 创始人）、Yang Zhilin（XLNet 一作 + 月之暗面 CEO） |

---

## v2 评分 vs v1 评分的差异

| 维度 | v1 评分 | v2 评分差异 |
|---|---|---|
| D1 原创算法 | 简单按"是否有 N 篇高引论文" | 严格按 9 个 L2 簇（深度学习/Transformer/RL/CV/MoE/AI4Science/NLP/理论/AGI）加权，区分"改变方向"vs"领域有影响"vs"可引用工作" |
| D2 系统工程 | 简单按"是否在大公司" | 严格按 7 个 L2 簇（分布式/框架/训练系统/芯片/软硬一体/基础设施/工程化）加权，区分"MapReduce 级基础设施"vs"亿级用户系统"vs"团队级" |
| D3 学术地位 | 主要看 Fellow 头衔 | 综合 8 个 L2 簇（机构创建/国家实验室/商业化/中国本土研究机构/长期坚守/诺奖图灵/Fellow/中国院士） |
| D4 创业 | 主要看"是否开过公司" | 严格按 8 个 L2 簇（大模型/AI4Science/行业/智驾/芯片/工具/互联网连续/跨周期连续）+ 估值分（独角兽/上市公司） |
| D5 政策治理 | 主要看"是否参与政策对话" | 严格按 7 个 L2 簇（国家级/国务院/国际/对齐/治理/机构建设/可解释性） |
| D6 长期主义 | 主要按年限打分 | 按 5 个 L2 簇（学界坚守/工业深耕/AI 长期主义/连环创业/寒冬期坚持） |
| D7 跨界整合 | 简单按"是否跨过界" | 按 8 个 L2 簇（跨学科/商业+技术/政策+技术/学术+工业/学界+工业/学界+创业/跨国/组织创新）按跨界领域数 1-4+ 打分 |
| D8 公共影响力 | 主要看"是否上过 TED" | 按 11 个 L2 簇（出海/国际化/跨境投资/诺奖图灵/中国院士/教材/MOOC/思想传播/AI 时代洞察/公共倡导/公共讨论）按受众规模 1-千万级 打分 |

---

## 与原型 P1-P6 的关系

8 维 D1-D8 通过聚类（K-means 或人工）产生 6 个原型 P1-P6：
- **P1 学术源流**（11 人）= D1=3 + D3=3 + D6=3 + D5/D7/D8 较低
- **P2 工业研究院**（13 人）= D1/D2 中高 + D3/D6 较高 + D4/D5 较低
- **P3 学术+AI 创业**（15 人，中国独有）= D1/D3/D4/D7 都高
- **P4 跨界整合多栖**（9 人，西方为主）= D1/D2/D5/D7/D8 高
- **P5 AI 治理/安全旗手**（4 人，西方独有）= D5/D3 高 + D1/D4 低
- **P6 商业/硬件创业**（8 人，中国独有）= D4/D2/D5 高 + D1/D3 较低

具体见 prototypes.md。
