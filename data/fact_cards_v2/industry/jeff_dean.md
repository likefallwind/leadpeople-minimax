# Jeff Dean v2 事实卡 (fact_card_v2)

> 角色定位：Google 体系奠基人、Google 第 20 号员工（1999）、Google Brain 联合创始人（2011）、Google DeepMind 首席科学家（2023.4-）、MapReduce / BigTable / Spanner / TensorFlow 等基础设施主要设计者之一、ACM Fellow、AAAS Fellow、IEEE Fellow、2021 IEEE 冯诺依曼奖得主。
>
> 资料来源：百度百科、腾讯云/学习 AIGC、机器之心、ACM/IEEE 官方、Wikipedia、Google AI Blog。所有事实标注 URL；冲突项并列保留。

---

## 事实核查报告（与 v1 事实卡对比）

| 项 | v1 事实卡 | v2 修正 | 来源 |
|---|---|---|---|
| 出生 | 1968.7 夏威夷 | 1968（一致） | [百度百科](https://baike.baidu.com/item/Jeff_Dean) |
| 父亲 | 非洲和平队志愿人员（索马里） | 父亲在世卫组织工作（v1 与百度百科不一致，待复核） | 多源 |
| 学历 | 明尼苏达大学本硕 → 华盛顿州立大学博士 | **明尼苏达大学学士（1990，最优等 summa cum laude）→ 华盛顿大学博士（1996）** | [百度百科](https://baike.baidu.com/item/Jeff_Dean) |
| 1990-1991 WHO | 未提及 | **1990-1991 在世卫组织艾滋病全球方案开发软件** | 同上 |
| DEC WRL | 1996-1999 | 1996-1999（一致） | 同上 |
| 加入 Google | 1999 | **1999.8（第 20 号员工）**（一致） | [腾讯云：加入谷歌 25 周年](https://cloud.tencent.com/developer/) |
| 2009 NAE 院士 | 提及 | 2009 当选美国工程院院士（一致） | [百度百科](https://baike.baidu.com/item/Jeff_Dean) |
| 2021 IEEE 冯诺依曼奖 | 提及 | **2020.12 获 2021 IEEE 冯诺依曼奖**（一致） | 同上 |
| 2023 Google DeepMind 合并 | 2023.4 | **2023.4 Google Brain + DeepMind 合并为 Google DeepMind，Dean 任首席科学家** | [腾讯云](https://cloud.tencent.com/) |
| 25 周年 | 2024.8 | **2024.8 庆祝加入 Google 25 周年**（一致） | 同上 |
| 全球最具影响力学者 | 未提及 | AMiner AI 2000 多个领域入选 | 公开数据 |
| 个人目标 | 篮球 | "在所有大洲上打篮球"（北美洲、南美洲、欧洲、亚洲、非洲已完成） | [百度百科](https://baike.baidu.com/item/Jeff_Dean) |

---

## 1. 教育背景

- **1986-1990**：明尼苏达大学计算机与经济学系**学士**（最优等 summa cum laude）
- **1990-1991**：在**世界卫生组织（WHO）** 艾滋病全球方案开发软件，用于 HIV 传播的统计建模、预测和分析
- **1996**：华盛顿大学计算机科学**博士**（博士论文方向：面向对象语言的程序优化）

## 2. 早期职业（1990-1999）

- **1990-1991**：WHO 艾滋病全球方案软件工程师
- **1996-1999**：DEC 公司（Digital Equipment Corporation）**西部研究实验室（WRL）**研究员
  - 与 Andrei Broder、Monika Henzinger 等人共事
  - 主要研究编译器、信息检索、超大规模网络图算法
  - 参与 AltaVista 早期抓取与索引相关工作
  - 1996-1999 在 W3C 任高级工程师（兼职）
  - 与 Henzinger 合作 SIGIR 1998 论文"基于 Web 图的链接分析"

## 3. 核心研究方向 / 技术贡献

### 主线 1：大规模分布式系统三件套
- **MapReduce**（与 Sanjay Ghemawat 合著，OSDI 2004，引用 23000+）— 把大规模数据处理抽象为 Map + Reduce 两阶段
- **BigTable**（OSDI 2006）— Google 内部第一个 PB 级结构化数据存储系统
- **Spanner**（OSDI 2012）— 全球一致性、分布式关系型数据库，被誉为 NewSQL 时代开端
- **GFS / Colossus / Borg / Kubernetes** — 文件系统与集群管理系统

### 主线 2：深度学习系统
- **2011**：与吴恩达 (Andrew Ng)、Greg Corrado 共同创建 **Google Brain**
- 主持"大神经元数 + 大数据"的工业化实验（Google Brain Cat 2012 项目）
- **2015**：主导设计并发布 **TensorFlow**（OSDI 2016 论文，引用 20000+）
- 推动 **TPU**（张量处理单元）芯片研发

### 主线 3：学术贡献
- 学术论文累计 Google Scholar 引用 18 万+（截至 2024）
- ACM Fellow、AAAS Fellow、IEEE Fellow、NEC 主席研究员（NerSC Fellow）
- 在 NeurIPS、ICML、OSDI、SOSP、ASPLOS 等会议做过大量 keynote

## 4. 标志性成就 / 获奖

- **2009**：当选**美国工程院院士**
- **2014**：ACM Fellow
- **2015**：American Academy of Arts and Sciences
- **2017**：NerSC Fellowship 首位获得者
- **2020.12**：获 **2021 IEEE 冯诺依曼奖**（IEEE John von Neumann Medal）
- **2022**：Fast Company "商界最具创造力人物"
- **2023.4**：**Google DeepMind 首席科学家**

## 5. 领导 / 创业经历

- **1999.8（第 20 号员工）加入 Google**（罕见"从未离开 Google 25 年"）
- **2001-2011**：领导 Google 整个广告系统（AdSense）的搜索基础设施与广告投放基础架构
- **2011**：与吴恩达、Greg Corrado 创立 **Google Brain**
- **2015-2018**：Google AI 负责人
- **2018-2023**：Google Research 高级副总裁
- **2023.4 至今**：Google DeepMind 首席科学家（与 Demis Hassabis 搭档）

## 6. 跨界 / 影响力溢出

- **公共部门贡献**：曾参与白宫 OSTP 与 DARPA 的 AI 战略咨询
- **对学界影响**：Google Brain / Research 是深度学习工业化的"西点军校"
- **公益**：Google.org 在 AI for Good 上的多项倡议
- **气候与健康**：领导 Google AI for Climate、AI for Healthcare 落地
- 培养的学生/合作者：Ian Goodfellow、Quoc Le、Geoffrey Hinton 暑期合作

## 7. 性格特质与认知风格

- **极致系统化思维**：无论什么问题，先"画系统图"再讨论
- **低调、温和**：多次公开访谈中语调平缓；Hassabis 评价他"像一本不说话但一直在写的好书"
- **产品直觉**：对"什么能变成产品"有非常清晰的判断力
- **工作狂但有节制**：早年长期每周 80+ 小时，近 5 年开始强调 work-life balance
- **梗文化符号**：Google 内部有大量关于 Jeff Dean 的"性能 benchmark"玩笑

## 8. 失败 / 争议 / 挫折

- **Google+ 时代的隐私争议**：2011-2019 年 Google+ 多个隐私漏洞
- **TensorFlow 的"工业绑架"**：2019-2022 年 TensorFlow 2.x 与 PyTorch 竞争中明显处于下风
- **Google 在生成式 AI 上的"慢半拍"**：2017 Transformer 论文 Google 是发起方，但 Bard/Gemini 节奏明显落后于 OpenAI
- **AI for Good 言论被质疑**：用 AI 解决气候变化过于乐观

## 9. 协作网络

- **Geoffrey Hinton**（2012 Google Brain Cat 合作、2014 收购 DNNresearch、2018 图灵奖颁奖中 Dean 是 Google 端工程协调人）
- **吴恩达、Greg Corrado**（Google Brain 共同创始人）
- **Sanjay Ghemawat**（MapReduce、Spanner、TensorFlow 都是"Dean + Ghemawat"组合）
- **Demis Hassabis**（2023 Google DeepMind 合并后搭档）
- **John Hennessy**（斯坦福前校长、图灵奖得主）
- **Sam Altman / Greg Brockman / Elon Musk**（OpenAI 创立时期 Dean 参与早期讨论）

## 10. 个人哲学 / 方法论

- **"Scale + Data + Compute, but also Cleverness"**（2020 NeurIPS keynote）
- **"Make the simple thing possible, then the complex thing easy"**（TensorFlow 设计核心）
- **"Computers should be computers, not oracles"**（对 AI 安全 / 对齐的态度）
- **"Open research, with discipline"**
- **"Hardware and software are one design"**（TPU + TensorFlow 一体化）
- **"Impact over publications"**（劝阻实习生不要追引用数）

## 关键事实 / 速查

- 出生：1968（夏威夷）
- 学历：明尼苏达大学学士 (1990, summa cum laude) → 华盛顿大学博士 (1996)
- 1990-1991：WHO 艾滋病软件
- 1996-1999：DEC WRL
- **1999.8 加入 Google（第 20 号员工）**
- 2011：Google Brain 共同创始人
- 2015：TensorFlow 发布
- 2023.4：Google DeepMind 首席科学家
- 重要奖项：ACM Fellow (2014)、AAAS (2015)、NAE (2009)、2021 IEEE 冯诺依曼奖
- 代表作：MapReduce (2004)、BigTable (2006)、Spanner (2012)、TensorFlow (2015)、Google Brain (2011)
- Google Scholar 引用 18 万+（截至 2024）

## 主要参考来源

1. [百度百科：Jeff Dean](https://baike.baidu.com/item/Jeff_Dean)
2. [腾讯云/学习 AIGC：加入谷歌 25 周年，Jeff Dean 开启回忆杀](https://cloud.tencent.com/developer/article/2473462)
3. [Wikipedia: Jeff Dean (computer scientist)](https://en.wikipedia.org/wiki/Jeff_Dean_(computer_scientist))
4. [ACM Fellow 页面](https://awards.acm.org/award-recipients/dean_9985260)
5. [IEEE 2021 John von Neumann Medal 公告](https://www.ieee.org/about/awards/medals/computer-intelligence.html)
6. [MapReduce: Simplified Data Processing on Large Clusters, OSDI 2004](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
7. [TensorFlow: A System for Large-Scale Machine Learning, OSDI 2016](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf)
8. [Google AI Blog 2022 年度回顾（Jeff Dean 撰文）](https://ai.googleblog.com/)
