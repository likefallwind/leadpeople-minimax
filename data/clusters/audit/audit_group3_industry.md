# Group 3: industry（10 人）D 维评分追溯

> **Trust 等级**：B（v2 fact card 有核查表，但无 v2_rework 独立 web 核查）
> **Fact card 路径**：`data/fact_cards_v2/industry/`
> **v3 matrix 评分**：`data/clusters/matrix.md` 第 122-133 行
> **审计时间**：2026-06-04

## 总体审计结论（先看这里）

| 人物 | v3 总分 | 审计结论 | 修订建议 |
|---|---|---|---|
| Ian Goodfellow | 9 | ⚠️ 2 个分数需修订 | D5: 0→1 / D6: 1→0 |
| Ilya Sutskever | 17 | ✅ 评分全对 | 无 |
| Jeff Dean | 15 | ✅ 评分全对 | 无 |
| 李航 | 10 | ⚠️ 2 个分数需修订 | D5: 0→1 / D8: 3→2 |
| 沈向洋 | 17 | ✅ 评分全对 | 无 |
| 田奇 | 10 | ⚠️ 1 个分数需修订 | D6: 2→3 |
| 王海峰 | 15 | ⚠️ 2 个分数需修订 | D4: 1→0 / D6: 3→2 |
| Xuedong Huang | 14 | ⚠️ 1 个分数需修订 | D4: 1→0 |
| 张正友 | 9 | ⚠️ 2 个分数需修订 | D1: 1→2 / D6: 2→3 |
| 周靖人 | 8 | ⚠️ 2 个分数需修订 | D4: 1→0 / D6: 1→2 |

**汇总**：60 个 D 维分数（10 人 × 6 维非零）中有 **12 个建议修订**，3 人（Ilya/Jeff Dean/沈向洋）完全准确，7 人有 1-2 个分数需调整。**最严重错误是周靖人 D4 错记为"字节豆包"**（v1 错误），但 v3 矩阵 D4=1 的问题更微妙——他在阿里 10 年是公司职位而非创业。

---

## 1. Ian Goodfellow (ian_goodfellow)

**当前 v3 评分**：[D1=3, D2=1, D3=1, D4=0, D5=0, D6=1, D7=1, D8=2] 总分=9/24
**Fact card 路径**：`data/fact_cards_v2/industry/ian_goodfellow.md`（150 行 v2 含 fact-check 表）
**Trust 等级**：B（v2 有核查表）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 3 | ✅ 3 | GAN 2014 NeurIPS 一作（85000+ 引用）+ 2024 NeurIPS Test of Time Award | `ian_goodfellow.md` 主线 1 | 3 分标准：改变方向（GAN 是图像生成两大基础之一）|
| D2 系统工程 | 1 | ✅ 1 | Apple Special Projects Group ML Director (1000 director 之一) | `ian_goodfellow.md` 段 2 | 1 分标准：主导过小型系统（部门级 / 1000 director）|
| D3 学术机构 | 1 | ✅ 1 | Stanford 本科 (Andrew Ng) + Montreal 博士 (Bengio) + MIT TR35 (2017) | `ian_goodfellow.md` 段 1 | 1 分标准：有 Fellow/学院副主任级（MIT TR35 = 行业重要认可 + 双师承 = 学术界影响力）|
| D4 创业 | 0 | ✅ 0 | "未参与创业" | `ian_goodfellow.md` 段 5 | 0 分标准：无 |
| D5 政策治理 | 0 | ⚠️ **1** | 2014 揭示 DL 脆弱性论文 + 2015 FGSM 攻击 + 公开质疑 AGI 炒作 | `ian_goodfellow.md` 主线 2 + 主线 4 | **建议改为 1 分**：FGSM/对抗鲁棒性是 AI 安全/治理研究核心工作（dimensions.md 1 分标准："有 AI 安全/治理研究（论文/机构）"），但 Goodfellow 确实无政策对话，0.5-1 分区间。|
| D6 长期主义 | 1 | ⚠️ **0** | 2013 Google 实习 → 2014-2015 Google Brain → 2017-2019 Google Brain（2 次）→ 2019.3-2022.5 Apple → 2022.7-DeepMind（5 个平台）| `ian_goodfellow.md` 段 2 | **建议改为 0 分**：5 个平台频繁切换，无单平台 5+ 年坚持。Google Brain 5 年（2014-2019）勉强，但 Apple 3 年后离开。|
| D7 跨界整合 | 1 | ✅ 1 | 学界 (Stanford/MILA) → 工业 (Google/Apple/DeepMind) | `ian_goodfellow.md` 段 1+2 | 1 分标准：跨 2 领域（学界+工业）|
| D8 公共影响力 | 2 | ✅ 2 | 花书 27000+ 引用 + NeurIPS 2024 ToT + MIT TR35 + Wired 等 | `ian_goodfellow.md` 主线 3 | 2 分标准：影响力博客/百万级观众（教材+ToT 奖+Wired）|

**审计结论**：⚠️ 2 个分数需修订（D5 0→1 / D6 1→0）
**修订建议**：
1. **D5: 0 → 1**：FGSM（2015）是 AI 安全研究核心工作（dimensions.md 1 分标准："有 AI 安全/治理研究"），但 Goodfellow 确实未参与政策对话，可保留 1 分或 0 分。
2. **D6: 1 → 0**：5 个平台频繁切换（Google 实习 → Google Brain → Google Brain → Apple → DeepMind），无单平台 5+ 年坚持。Google Brain 5 年（2014-2019）可能勉强，但典型"频繁跳槽"。

---

## 2. Ilya Sutskever (ilya_sutskever)

**当前 v3 评分**：[D1=3, D2=1, D3=2, D4=3, D5=2, D6=1, D7=2, D8=3] 总分=17/24
**Fact card 路径**：`data/fact_cards_v2/industry/ilya_sutskever.md`（188 行 v2 含完整 fact-check 表）
**Trust 等级**：B（v2 有详细 fact-check）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 3 | ✅ 3 | AlexNet 2012 NeurIPS 一作（120000+ 引用）+ Seq2Seq 2014 NIPS (27000+ 引用) + 2024 NeurIPS Test of Time Award（双论文获奖）| `ilya_sutskever.md` 主线 1+2 | 3 分标准：改变方向（AlexNet 是深度学习进入工业界"发令枪"；Seq2Seq 是 Google Translate 神经化基础）|
| D2 系统工程 | 1 | ✅ 1 | OpenAI 首席科学家 (2015-2024) + GPT-3/InstructGPT/ChatGPT 路径主导 + RLHF 推动 | `ilya_sutskever.md` 主线 4 | 1 分标准：主导过小型系统（OpenAI 9 年首席科学家 = 公司核心研究角色）|
| D3 学术机构 | 2 | ✅ 2 | 多伦多大学博士 (Hinton) + 英国皇家学会 FRS (2022) + Nature's 10 (2023.12.14) + UofT 荣誉博士 (2025.6.6) | `ilya_sutskever.md` 段 4 | 2 分标准：顶级 Fellow 五大到位之一（FRS + Nature's 10 接近诺奖/图灵级）|
| D4 创业 | 3 | ✅ 3 | OpenAI 联合创始人 (2015.12) + SSI 联合创始人 (2024.6.19) + SSI 估值 320 亿美元 (2025.3) | `ilya_sutskever.md` 主线 6 | 3 分标准：主导过独角兽（SSI 估值 320 亿美元 > 10 亿美元）|
| D5 政策治理 | 2 | ✅ 2 | 2023.7 Superalignment 团队共同领导 (20% 算力) + 2024 SSI 创办（"安全优先"路线）+ 2023.11 董事会事件 | `ilya_sutskever.md` 主线 5+6 | 2 分标准：机构建设（Superalignment 团队是 OpenAI 安全研究标志；SSI 是独立 AI 安全机构）|
| D6 长期主义 | 1 | ✅ 1 | OpenAI 9 年 (2015-2024.5) + SSI 1+ 年 (2024.6-) | `ilya_sutskever.md` 段 5+6 | 1 分标准：5-10 年坚持（OpenAI 9 年）|
| D7 跨界整合 | 2 | ✅ 2 | 4 国身份（俄→以→加→美）+ 学术/工业/创业/治理 4 领域 | `ilya_sutskever.md` 段 6 | 2 分标准：跨 3 领域（学术+工业+创业+安全治理）|
| D8 公共影响力 | 3 | ✅ 3 | Nature's 10 (2023) + ChatGPT 全球影响 + 多次多伦多大学/UofT/公开演讲 + SSI 公开 | `ilya_sutskever.md` 段 6 | 3 分标准：诺奖/图灵/《时代》百大 + 千万级（Nature's 10 类似《时代》百大）|

**审计结论**：✅ v3 评分全对（与 fact card 完全一致）

---

## 3. Jeff Dean (jeff_dean)

**当前 v3 评分**：[D1=1, D2=3, D3=3, D4=0, D5=1, D6=3, D7=2, D8=2] 总分=15/24
**Fact card 路径**：`data/fact_cards_v2/industry/jeff_dean.md`（146 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | MapReduce (2004, 23000+ 引) + BigTable (2006) + Spanner (2012) + TensorFlow (2015, 20000+ 引) | `jeff_dean.md` 主线 1+2 | 1 分标准：有可引用工作（这些是系统级而非算法级）|
| D2 系统工程 | 3 | ✅ 3 | MapReduce + BigTable + Spanner + TensorFlow + TPU + GFS/Colossus/Borg/Kubernetes | `jeff_dean.md` 主线 1+2 | 3 分标准：定义行业的基础设施（TensorFlow/MapReduce 级，开源生态基础）|
| D3 学术机构 | 3 | ✅ 3 | NAE 院士 (2009) + ACM Fellow (2014) + AAAS (2015) + IEEE Fellow + NerSC Fellowship 首位 (2017) + 2021 IEEE 冯诺依曼奖 | `jeff_dean.md` 段 4 | 3 分标准：顶级 Fellow + 重大奖项（NAE 院士 + IEEE 冯诺依曼奖 = 接近 3 分）|
| D4 创业 | 0 | ✅ 0 | "未参与创业" | `jeff_dean.md` 段 5 | 0 分标准：无（仅 Google 25 年）|
| D5 政策治理 | 1 | ✅ 1 | OSTP/DARPA AI 战略咨询 + AI for Climate/Healthcare | `jeff_dean.md` 段 6 | 1 分标准：有 AI 治理研究/咨询（白宫咨询 + AI for Good）|
| D6 长期主义 | 3 | ✅ 3 | Google 25 年 (1999-2024)，第 20 号员工 → 首席科学家 | `jeff_dean.md` 段 5 | 3 分标准：20+ 年坚持（Google 25 年）|
| D7 跨界整合 | 2 | ✅ 2 | 跨 3 领域（学界 DEC → 工业 Google → 政策咨询 OSTP/DARPA）| `jeff_dean.md` 段 6 | 2 分标准：跨 3 领域（学界+工业+政策）|
| D8 公共影响力 | 2 | ✅ 2 | NeurIPS/ICML/OSDI/SOSP/ASPLOS keynote + Google 内部"Jeff Dean 梗文化" + Fast Company 2022 | `jeff_dean.md` 段 6+7 | 2 分标准：影响力博客/百万级观众（多次 keynote + 文化符号）|

**审计结论**：✅ v3 评分全对

---

## 4. 李航 (li_hang)

**当前 v3 评分**：[D1=1, D2=1, D3=2, D4=0, D5=0, D6=1, D7=2, D8=3] 总分=10/24
**Fact card 路径**：`data/fact_cards_v2/industry/li_hang.md`（154 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查，**已修正 v1 重大错误**：南京大学→京都大学）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | SVM/CRF/MaxEnt/IR 论文 + Google Scholar 5 万+ 引用 | `li_hang.md` 主线 1+2 | 1 分标准：有可引用工作（5 万+ 引用，统计学习领域代表）|
| D2 系统工程 | 1 | ✅ 1 | NEC 7 年 + MSRA 11 年 + 华为诺亚方舟创始主任 5 年 + 字节 AI Lab 6+ 年（团队建设） | `li_hang.md` 段 2 | 1 分标准：主导过小型系统（华为诺亚方舟 + 字节 AI Lab = 团队级）|
| D3 学术机构 | 2 | ✅ 2 | IEEE Fellow + ACM Distinguished Scientist + ACL Fellow (2019) + CCF 杰出贡献奖 (2014) | `li_hang.md` 段 4 | 2 分标准：顶级 Fellow 五大到位（IEEE + ACM + ACL 三大到位）|
| D4 创业 | 0 | ✅ 0 | "未参与创业" | `li_hang.md` 段 5 | 0 分标准：无 |
| D5 政策治理 | 0 | ⚠️ **1** | 参与中国新一代 AI 规划咨询 + ACL 资深审稿人/领域主席 | `li_hang.md` 段 6 | **建议改为 1 分**：参与国家级政策咨询 = 1 分标准（"有 AI 安全/治理研究/咨询"）|
| D6 长期主义 | 1 | ✅ 1 | 4 平台（NEC 11 + MSRA 11 + 华为 5 + 字节 6+） | `li_hang.md` 段 2 | 1 分标准：5-10 年坚持（每个平台 5+ 年）|
| D7 跨界整合 | 2 | ✅ 2 | NEC + MSRA + 华为 + 字节 + 北大/南大兼职 = 4 平台/学界+工业/中日跨国 | `li_hang.md` 段 2+6 | 2 分标准：跨 3 领域（学界+工业+教育）|
| D8 公共影响力 | 3 | ⚠️ **2** | 《统计学习方法》50 万+ 册 + ACL Fellow + CCF 杰出贡献奖 | `li_hang.md` 主线 3 | **建议改为 2 分**：蓝宝书 50 万册 ≈ 百万级观众（dimensions.md 2 分标准），未到千万级。3 分标准需"诺奖/图灵/《时代》百大 + 千万级公共影响"，李航未到。|

**审计结论**：⚠️ 2 个分数需修订（D5 0→1 / D8 3→2）
**修订建议**：
1. **D5: 0 → 1**：参与中国新一代 AI 规划咨询 = 国家级政策咨询 = 1 分标准。
2. **D8: 3 → 2**：50 万册 = 百万级观众级别，未到 3 分"千万级"标准。

---

## 5. 沈向洋 (shen_xiangyang)

**当前 v3 评分**：[D1=1, D2=1, D3=3, D4=1, D5=2, D6=3, D7=3, D8=3] 总分=17/24
**Fact card 路径**：`data/fact_cards_v2/industry/shen_xiangyang.md`（171 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查，**已修正 v1 错误**：院长→创院理事长）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | 1994 第一个三维全真模型 + 1996 同心拼图方法 + CVPR/ICCV/SIGGRAPH 100+ 论文 + 美国专利 50+ 项 | `shen_xiangyang.md` 段 3 | 1 分标准：有可引用工作（基础研究代表）|
| D2 系统工程 | 1 | ✅ 1 | MSRA 体系建设（2004-2007 第三任院长）+ Bing 搜索 + 小冰（中国首个大规模对话 AI）+ 2016 微软 152 层残差图像识别 | `shen_xiangyang.md` 段 3 | 1 分标准：主导过小型系统（MSRA 院长 + Bing 团队 = 部门级）|
| D3 学术机构 | 3 | ✅ 3 | NAE 外籍院士 (2017.2.8) + 英国皇家工程院外籍院士 (2018.9.18) + IEEE Fellow + ACM Distinguished Scientist + MSRA 院长 (2004-2007) | `shen_xiangyang.md` 段 4 | 3 分标准：图灵/诺奖 + 五大 Fellow 全到位（NAE + 英国皇家 + IEEE = 接近 3 分）|
| D4 创业 | 1 | ✅ 1 | IDEA 研究院创院理事长 (2020.11) | `shen_xiangyang.md` 主线 5 | 1 分标准：参与过创业（IDEA 研究院 = 事业单位，"创院理事长"勉强算 1 分，0-1 分区间）|
| D5 政策治理 | 2 | ✅ 2 | 参与中国新一代 AI 规划 + 万科独立董事 (2023.6.30) + 港科大校董会主席 (2023.2.28) | `shen_xiangyang.md` 段 6 | 2 分标准：国家级政策参与 + 跨界治理 |
| D6 长期主义 | 3 | ✅ 3 | 微软 23 年 (1996-2020) + IDEA 6 年 (2020-) = 30+ 年坚守 | `shen_xiangyang.md` 段 5 | 3 分标准：20+ 年坚持（微软 23 年）|
| D7 跨界整合 | 3 | ✅ 3 | 跨 4+ 领域（学术 + 工业 + 政策 + 商业）= MSRA 院长 → EVP → IDEA 理事长 → 港科大校董会 → 万科独董 | `shen_xiangyang.md` 段 5+6 | 3 分标准：跨 4+ 领域 |
| D8 公共影响力 | 3 | ✅ 3 | 微软 EVP (华人最高) + NAE/英国皇家工程院 + 港科大校董会主席 + 万科独董 + CMU Raj Reddy 学生 | `shen_xiangyang.md` 段 4+6 | 3 分标准：诺奖/图灵/《时代》百大 + 千万级（NAE/英国皇家工程院 + 微软 EVP）|

**审计结论**：✅ v3 评分全对

---

## 6. 田奇 (tian_qi)

**当前 v3 评分**：[D1=1, D2=2, D3=3, D4=0, D5=0, D6=2, D7=1, D8=1] 总分=10/24
**Fact card 路径**：`data/fact_cards_v2/industry/tian_qi.md`（147 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查，**已修正 v1 错误**：1979 清华→1992 清华）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | 多媒体信息检索 + Pangu-Weather (Nature 2023, Science 2023 十大突破) + 420+ 论文 + 引用 11000+ | `tian_qi.md` 主线 1+3 | 1 分标准：有可引用工作（多媒体领域代表 + Pangu-Weather 工业化算法）|
| D2 系统工程 | 2 | ✅ 2 | 华为云盘古大模型 + Pangu-Weather 工业化 + 平安城市/自动驾驶/网络运维大脑 | `tian_qi.md` 主线 3+4 | 2 分标准：主导过工业级系统（华为云大模型 = 亿级用户）|
| D3 学术机构 | 3 | ✅ 3 | IEEE Fellow (2016) + ACM Fellow (2025.1) + CAAI Fellow (2022) + IEAS 院士 (2021) + 吴文俊 AI 杰出贡献奖 (2021) | `tian_qi.md` 段 4 | 3 分标准：五大 Fellow 全到位（IEEE + ACM + CAAI 三大到位 + IEAS 院士 + 吴文俊奖）|
| D4 创业 | 0 | ✅ 0 | "未参与创业" | `tian_qi.md` 段 5 | 0 分标准：无 |
| D5 政策治理 | 0 | ✅ 0 | 教育部长江学者 + 中科院海外评审专家 + 国家自科基金会评 | `tian_qi.md` 段 6 | 0 分合适：长江学者/中科院海外评审/国家自科基金均属"学术服务"而非"政策治理"。**但长江学者+国家自科基金 = 国家级政策咨询 = 1 分区间**，可考虑改为 1 分。|
| D6 长期主义 | 2 | ⚠️ **3** | UTSA 17 年 (2002-2019) + 华为诺亚方舟 2 年 (2018-2020) + 华为云 5+ 年 (2020-) = 24 年+ | `tian_qi.md` 段 2 | **建议改为 3 分**：UTSA 17 + 华为 7+ = 24 年（即使分段，单平台最长 17 年 + 5+ 年，但整体海外/海外归来 24 年。dimensions.md "3 分 = 20+ 年坚持 或 学术寒冬 30+ 年坚持"。UTSA 17 年已超阈值，加上华为 7+ 年 = 24 年 = 3 分。|
| D7 跨界整合 | 1 | ✅ 1 | UTSA 学术 → 华为工业（多媒体 → CV → 盘古大模型）| `tian_qi.md` 主线 1+2 | 1 分标准：跨 2 领域（学界+工业）|
| D8 公共影响力 | 1 | ✅ 1 | 多媒体信息检索学界影响 + 长江学者 + 420+ 论文 | `tian_qi.md` 段 6 | 1 分标准：学界影响，万人级 |

**审计结论**：⚠️ 1 个分数需修订（D6 2→3）
**修订建议**：
1. **D6: 2 → 3**：UTSA 17 年 + 华为 7+ 年 = 24 年 ≥ 20 年，符合 dimensions.md 3 分标准"20+ 年坚持"。

---

## 7. 王海峰 (wang_haifeng)

**当前 v3 评分**：[D1=1, D2=3, D3=2, D4=1, D5=1, D6=3, D7=2, D8=2] 总分=15/24
**Fact card 路径**：`data/fact_cards_v2/industry/wang_haifeng.md`（164 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | 1999 博士论文神经网络机器翻译 + 百度翻译 2015 互联网 NMT 率先 + 百度知识图谱 (50 亿实体 / 5500 亿事实) | `wang_haifeng.md` 主线 1+2 | 1 分标准：有可引用工作（百度翻译 + 知识图谱 + 早期 NMT 研究）|
| D2 系统工程 | 3 | ✅ 3 | 飞桨 PaddlePaddle (2016 中国首个自主开源深度学习平台) + ERNIE/文心大模型 + 百度大脑 (日均 1 万亿次) + 双 11 智能计算 | `wang_haifeng.md` 主线 3+4+5 | 3 分标准：定义行业的基础设施（飞桨是中国首个工业级深度学习框架）|
| D3 学术机构 | 2 | ✅ 2 | ACL 50 年首位华人主席 (2013.1.10) + ACL Fellow (2016, 首位中国大陆) + IEEE Fellow + CAAI Fellow + IEAS 院士 | `wang_haifeng.md` 段 4 | 2 分标准：顶级 Fellow + 学会主席（ACL 主席 = 领域最高职位之一）|
| D4 创业 | 1 | ⚠️ **0** | 联通董事 + 爱奇艺董事 + 东软控股董事 + 百度投资管理董事 + 北京 AI 产业联盟理事长 | `wang_haifeng.md` 段 7 | **建议改为 0 分**：这些是公司董事/独董/联盟理事长职位，非"创业（联创/早期员工/天使）"。严格按 dimensions.md 1 分标准"参与过创业（联创/早期员工/天使）"——他没参与任何商业公司创业。**0 分合适**。|
| D5 政策治理 | 1 | ✅ 1 | 联通/爱奇艺/东软等董事 + 北京 AI 产业联盟理事长 (2021.6-) + 参与中国新一代 AI 规划 | `wang_haifeng.md` 段 6 | 1 分标准：行业组织治理 + 政策咨询 |
| D6 长期主义 | 3 | ⚠️ **2** | 百度 15+ 年 (2010-) + 哈工大 10 年 (1989-1999) + 微软中国研究院 11 年 (1999-2010) = 36 年（含 1999-2010 微软段）；百度单平台 15 年 (2010-) | `wang_haifeng.md` 段 2 | **建议改为 2 分**：百度 15+ 年 = 10-20 年区间（dimensions.md 3 分 = 20+ 年单平台）。如果算 1999-2010 微软段 + 2010-至今 百度段，整体 26 年但分两个平台。**严格按单平台 2 分**。|
| D7 跨界整合 | 2 | ✅ 2 | 哈工大学术 → 微软中国研究院 → 百度工业（搜索/翻译/AI）→ 联通/爱奇艺/东软董事 = 跨 3 领域 | `wang_haifeng.md` 段 2+7 | 2 分标准：跨 3 领域（学界+工业+治理）|
| D8 公共影响力 | 2 | ✅ 2 | ACL 50 年首位华人主席 + 哈工大教授 + 国家卓越工程师 (2024.1.19) + 光华工程科技奖 (2020) + 联通/爱奇艺/东软董事 | `wang_haifeng.md` 段 4+7 | 2 分标准：百万级观众（ACL 主席 + 国家奖项 + 多个公司董事）|

**审计结论**：⚠️ 2 个分数需修订（D4 1→0 / D6 3→2）
**修订建议**：
1. **D4: 1 → 0**：王海峰是公司董事/独董/联盟理事长，不是"创业（联创/早期员工/天使）"。严格按标准 0 分。
2. **D6: 3 → 2**：百度 15+ 年 = 10-20 年区间（2010-至今 ≈ 16 年），未到 3 分"20+ 年单平台"标准。

---

## 8. Xuedong Huang (xuedong_huang)

**当前 v3 评分**：[D1=1, D2=3, D3=2, D4=1, D5=0, D6=3, D7=2, D8=2] 总分=14/24
**Fact card 路径**：`data/fact_cards_v2/industry/xuedong_huang.md`（181 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查，**已修正 v1 错误**：1963→1962）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ✅ 1 | Sphinx-II 1992 (60000 词 DARPA 评测第一) + Switchboard WER 5.1% (2017.8, 超人类) + Z-Code 多语言翻译 + 2018 newstest2017 中译英达人工水平 | `xuedong_huang.md` 主线 1 | 1 分标准：有可引用工作（语音识别先驱 + Switchboard 突破）|
| D2 系统工程 | 3 | ✅ 3 | SAPI 1995 (业界首个 Windows 语音 API) + CNTK 2014-2016 (TensorFlow 之前主流框架) + 微软 30 年 Speech Platforms 总经理 + Azure AI CTO (2020) | `xuedong_huang.md` 主线 2+3 | 3 分标准：定义行业的基础设施（CNTK + SAPI + Azure AI 认知服务）|
| D3 学术机构 | 2 | ✅ 2 | NAE 院士 (2023.2) + AAAS 院士 (2023.4) + IEEE Fellow (2000) + ACM Fellow (2017) + Microsoft Technical Fellow (2017, 首位华人) + Allen Newell 奖 (1992, 首位华人) | `xuedong_huang.md` 段 4 | 2 分标准：顶级 Fellow + 重大奖项（NAE + AAAS 双院士 + Technical Fellow 首位华人）|
| D4 创业 | 1 | ⚠️ **0** | 2023.6 加入 Zoom 任 CTO | `xuedong_huang.md` 段 5 | **建议改为 0 分**：Zoom CTO 是公司职位，非"创业（联创/早期员工/天使）"。严格按标准 0 分。|
| D5 政策治理 | 0 | ✅ 0 | "1990s 曾被邀参与国内多家语音公司早期组建，但选择留在微软" | `xuedong_huang.md` 段 5 | 0 分合适：无政策参与（选择留在微软而非国内政策对话）|
| D6 长期主义 | 3 | ✅ 3 | 微软 30 年 (1993-2023.6) + Zoom 3 年 (2023.6-) = 33 年 | `xuedong_huang.md` 段 5 | 3 分标准：20+ 年坚持（微软 30 年）|
| D7 跨界整合 | 2 | ✅ 2 | CMU 学界 → 微软工业 → Zoom 商业（3 领域）| `xuedong_huang.md` 段 5 | 2 分标准：跨 3 领域（学界+工业+商业）|
| D8 公共影响力 | 2 | ✅ 2 | Microsoft Technical Fellow (全球仅 20 人) + Allen Newell 奖 (首位华人) + Wired 2016 + SpeechTek "语言领域十大领军人物" + NAE/AAAS 双院士 | `xuedong_huang.md` 段 4+6 | 2 分标准：百万级观众（Technical Fellow 首位华人 + 多次榜单）|

**审计结论**：⚠️ 1 个分数需修订（D4 1→0）
**修订建议**：
1. **D4: 1 → 0**：Zoom CTO 是公司职位，非"创业（联创/早期员工/天使）"。严格按标准 0 分。

---

## 9. 张正友 (zhang_zhengyou)

**当前 v3 评分**：[D1=1, D2=1, D3=3, D4=0, D5=0, D6=2, D7=1, D8=1] 总分=9/24
**Fact card 路径**：`data/fact_cards_v2/industry/zhang_zhengyou.md`（173 行 v2 含详细 fact-check）
**Trust 等级**：B（v2 有详细核查，**已修正 v1 错误**：1958→1965.8.1）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 1 | ⚠️ **2** | 张氏标定法 1998 ECCV 论文 (50500+ 引用截至 2025.6) + 2013 IEEE Helmholtz 时间考验奖 | `zhang_zhengyou.md` 主线 1 | **建议改为 2 分**：50500+ 引用 + IEEE Helmholtz 时间考验奖 = "有领域影响力"（dimensions.md 2 分标准："论文引用数千+或被广泛使用"）。未到 3 分（无 Nature/图灵/诺奖级）。|
| D2 系统工程 | 1 | ✅ 1 | Roundtable 系统 (2007.10 比尔盖茨作为正式产品发布) + 腾讯 AI Lab + Robotics X | `zhang_zhengyou.md` 主线 4 | 1 分标准：主导过小型系统（Roundtable 360 度全景视频系统 + 腾讯 AI Lab 主任）|
| D3 学术机构 | 3 | ✅ 3 | IEEE Fellow (2005) + ACM Fellow (2020) + 2013 IEEE Helmholtz 时间考验奖 + 250+ 论文 | `zhang_zhengyou.md` 段 4 | 3 分标准：图灵/诺奖级奖项 + 五大 Fellow（IEEE + ACM 双 Fellow + Helmholtz 奖）|
| D4 创业 | 0 | ✅ 0 | "未参与创业" | `zhang_zhengyou.md` 段 7 | 0 分标准：无 |
| D5 政策治理 | 0 | ✅ 0 | 参与中国新一代 AI 规划 | `zhang_zhengyou.md` 段 8 | 0 分合适：政策咨询级而非政策对话级 |
| D6 长期主义 | 2 | ⚠️ **3** | INRIA 11 年 (1987-1998) + MSR 20 年 (1998-2018) + 腾讯 7+ 年 (2018-) = 38 年+ | `zhang_zhengyou.md` 段 2+3+4 | **建议改为 3 分**：MSR 20 年单平台 = 20+ 年坚持（dimensions.md 3 分标准）。|
| D7 跨界整合 | 1 | ✅ 1 | 跨 2 领域（学界 INRIA → 工业 MSR/腾讯）| `zhang_zhengyou.md` 段 3+4 | 1 分标准：跨 2 领域 |
| D8 公共影响力 | 1 | ✅ 1 | 250+ 论文 + 50500+ 引用 + Siggraph 等顶会 + 近 200 项专利 | `zhang_zhengyou.md` 段 5+6 | 1 分标准：学界影响，万人级（引用 5 万+ 在学界属高，但公众认知度低）|

**审计结论**：⚠️ 2 个分数需修订（D1 1→2 / D6 2→3）
**修订建议**：
1. **D1: 1 → 2**：张氏标定法引用 50500+ + IEEE Helmholtz 时间考验奖 = "有领域影响力"，符合 dimensions.md 2 分标准。
2. **D6: 2 → 3**：MSR 20 年单平台 = 20+ 年坚持，符合 dimensions.md 3 分标准。

---

## 10. 周靖人 (zhou_jingren)

**当前 v3 评分**：[D1=0, D2=3, D3=1, D4=1, D5=0, D6=1, D7=1, D8=1] 总分=8/24
**Fact card 路径**：`data/fact_cards_v2/industry/zhou_jingren.md`（166 行 v2 含详细 fact-check，**v1 有重大错误"加入字节"已修正**）
**Trust 等级**：B（v2 有详细核查）

| D 维 | v3 分数 | v4 拟改 | L0 事实支撑 | fact card 路径 | 评分理由 |
|---|---|---|---|---|---|
| D1 原创算法 | 0 | ✅ 0 | 中科大 + 哥伦比亚大学 CS 博士 (2004) + 微软 11 年 + 阿里云/达摩院 | `zhou_jingren.md` 段 1+2 | 0 分合适：研究领域是数据库/查询处理/分布式系统，无算法原创贡献（不是深度学习算法）|
| D2 系统工程 | 3 | ✅ 3 | 阿里云 2018 双 11 17 亿条/秒 + 通义/Qwen 6 亿+ 下载 + MAU 2.03 亿 + 通义 300+ 款开源模型 + 增速 553% | `zhou_jingren.md` 主线 2+3 | 3 分标准：定义行业的基础设施（Qwen 是全球顶级开源大模型之一）|
| D3 学术机构 | 1 | ✅ 1 | IEEE Fellow (2018, 云计算和大规模分布式系统) + ACM Fellow (2024) + 哥伦比亚大学博士 | `zhou_jingren.md` 段 4 | 1 分标准：有 Fellow 头衔（IEEE + ACM 2/5 Fellow，未到五大 Fellow 全到位）|
| D4 创业 | 1 | ⚠️ **0** | 2025.12 入选阿里合伙人 (最高决策层) | `zhou_jingren.md` 段 4 | **建议改为 0 分**：阿里合伙人是公司最高决策层职位，不是"创业（联创/早期员工/天使）"。严格按 dimensions.md 1 分标准 0 分。|
| D5 政策治理 | 0 | ✅ 0 | 阿里 1+6+N 变革推动者 + 清华/北大/浙大战略合作 | `zhou_jingren.md` 段 7 | 0 分合适：企业变革+学术合作，非政策治理 |
| D6 长期主义 | 1 | ⚠️ **2** | 微软 11 年 (2004-2015) + 阿里 10 年 (2015/2016-) = 21 年+（两个平台分别 11 和 10 年）| `zhou_jingren.md` 段 2+3 | **建议改为 2 分**：微软 11 年单平台 = 10-20 年坚持（dimensions.md 2 分标准）。|
| D7 跨界整合 | 1 | ✅ 1 | 哥大学术 → 微软/阿里工业（数据库/查询处理/搜索/推荐/广告/大模型）| `zhou_jingren.md` 主线 1+2+3 | 1 分标准：跨 2 领域（学界+工业）|
| D8 公共影响力 | 1 | ✅ 1 | 通义/Qwen 全球开源（6 亿+ 下载）+ 阿里合伙人 | `zhou_jingren.md` 段 4+主 2 | 1 分标准：万人级（开源社区影响，公众认知度低）|

**审计结论**：⚠️ 2 个分数需修订（D4 1→0 / D6 1→2）
**修订建议**：
1. **D4: 1 → 0**：阿里合伙人是公司最高决策层职位，不是"创业（联创/早期员工/天使）"。严格按标准 0 分。
2. **D6: 1 → 2**：微软 11 年单平台 = 10-20 年坚持，符合 dimensions.md 2 分标准。

---

## 总结与全局修订建议

### A. 高置信度修订（强烈建议）

| 修订 | 原分 | 建议 | 原因 | 受影响人物 |
|---|---|---|---|---|
| **D4 = 公司职位 ≠ 创业** | 1 | 0 | 王海峰/Xuedong/周靖人 是公司董事/独董/合伙人/CTO，不是"创业（联创/早期员工/天使）" | 王海峰 / Xuedong Huang / 周靖人 |
| **张正友 D1 1→2** | 1 | 2 | 50500+ 引用 + IEEE Helmholtz 时间考验奖 = 有领域影响力（dimensions.md 2 分标准）| 张正友 |
| **张正友/田奇 D6 2→3** | 2 | 3 | MSR/MSR+UTSA 单平台 17-20+ 年 = 20+ 年坚持（dimensions.md 3 分标准）| 张正友 / 田奇 |
| **周靖人 D6 1→2** | 1 | 2 | 微软 11 年单平台 = 10-20 年坚持 | 周靖人 |
| **王海峰 D6 3→2** | 3 | 2 | 百度 15+ 年 = 10-20 年（未到 3 分"20+ 年单平台"标准）| 王海峰 |

### B. 中等置信度修订（建议考虑）

| 修订 | 原分 | 建议 | 原因 | 受影响人物 |
|---|---|---|---|---|
| **Ian Goodfellow D5 0→1** | 0 | 1 | FGSM/对抗鲁棒性 = AI 安全研究核心工作（dimensions.md 1 分标准："有 AI 安全/治理研究（论文/机构）"）| Ian Goodfellow |
| **Ian Goodfellow D6 1→0** | 1 | 0 | 5 个平台频繁切换（Google 实习 → 2× Google Brain → Apple → DeepMind），无 5+ 年单平台坚持 | Ian Goodfellow |
| **李航 D5 0→1** | 0 | 1 | 参与中国新一代 AI 规划咨询 = 国家级政策咨询（1 分标准）| 李航 |
| **李航 D8 3→2** | 3 | 2 | 《统计学习方法》50 万册 ≈ 百万级观众，未到 3 分"千万级"标准 | 李航 |

### C. 待用户/PM 决策的边界案例

- **沈向洋 D4 = 1**：IDEA 研究院是"创院理事长"（非商业公司），是 0 还是 1？**建议保留 1 分**（研究院建设 = 类创业）
- **沈向洋 D3 = 3**：NAE + 英国皇家工程院 外籍院士 + IEEE Fellow + ACM DS + MSRA 院长，足够支撑 3 分。
- **Ilya Sutskever D5 = 2**：Superalignment 团队 + SSI 安全机构 = 主导 AI 安全机构建设，但缺少国家级政策参与。**建议保留 2 分**（机构建设权重）。

### D. 修订对总分的影响

如果按 A+B 全部修订：
- Ian Goodfellow: 9 → 8（D5 0→1 + D6 1→0 = 净 0）
- 李航: 10 → 10（D5 0→1 + D8 3→2 = 净 0）
- 田奇: 10 → 11（D6 2→3 = +1）
- 王海峰: 15 → 13（D4 1→0 + D6 3→2 = -2）
- Xuedong Huang: 14 → 13（D4 1→0 = -1）
- 张正友: 9 → 11（D1 1→2 + D6 2→3 = +2）
- 周靖人: 8 → 9（D4 1→0 + D6 1→2 = +1）

排名变化：
- 王海峰 15→13（可能跌出 Top 15）
- 张正友 9→11（接近贾佳亚/朱军水平）
- 周靖人 8→9（仍属末位）
- 田奇 10→11（与张正友接近）

### E. 已正确 v1→v2 重大事实修正（v2 已完成）

- **周靖人**：v1 写"2023 加入字节豆包" → v2 修正为"阿里云 CTO + 通义实验室负责人 + 2025.12 阿里合伙人"，**v1 重大错误已修正**。
- **李航**：v1 写"南京大学数学本科" → v2 修正为"京都大学电气电子工程系本科"
- **田奇**：v1 写"1979 清华" → v2 修正为"1992 清华"
- **Ian Goodfellow**：v1 写"2017 OpenAI" → v2 修正为"未在 OpenAI 任职"
- **Ian Goodfellow**：v1 写"2022-2023 Apple 第二次" → v2 修正为"未发生"
- **Xuedong Huang**：v1 写"1963" → v2 修正为"1962"
- **沈向洋**：v1 写"IDEA 院长" → v2 修正为"IDEA 创院理事长"
- **张正友**：v1 写"1958" → v2 修正为"1965.8.1"

这些事实修正本身很扎实，但部分 D 维评分未跟上事实修正（如周靖人 D4）。

---

**审计完成时间**：2026-06-04 15:00
**审计人**：general worker
**审计方法**：逐人 8 维比对 v3 matrix vs v2 fact card vs L0 atomic facts vs L1 atomic abilities
**审计深度**：B 级（独立核查所有 v2 fact card + L0/L1，未做 v2_rework 独立 web 核查）
