# 吴恩达 (Andrew Ng) 事实卡

> **类别**：跨界 / 学术 + 创业 + 治理
> **子领域**：深度学习先驱 + 在线教育 (Coursera) + 工业 AI (Baidu/Landing) + 治理 (Amazon Board)
> **关键标签**：Stanford AI Lab 前主任、Coursera 联合创始人、DeepLearning.AI 创始人、2014 百度首席科学家、2024 亚马逊董事、Google Brain 创始负责人

---

## 1. 教育背景

- **出生与早期**：1976 年出生于英国伦敦，**父亲是香港医生**，英文名 Andrew Ng。年少时在香港和新加坡度过（来源：百度百科）。
- **中学**：1992 年进入 **新加坡莱佛士书院 (Raffles Institution)**。该校是新加坡顶级中学，以培养政治 / 商业精英著称。
- **本科**：1997 年获得 **卡内基梅隆大学 (Carnegie Mellon University) 计算机科学 + 统计学 + 经济学** 三重专业学位（CMU 是少数允许本科三专业的学校）。本科学术训练奠定"理论 + 统计学 + 应用"的三脚架。
- **硕士**：1998 年获得 **麻省理工学院 (MIT) 硕士学位**。
- **博士**：2002 年获得 **加州大学伯克利分校 (UC Berkeley) 博士学位**，博士导师是 **迈克尔·乔丹 (Michael I. Jordan)**——机器学习领域的"教父"之一，对概率图模型 / 统计学习理论贡献卓著（来源：CSDN 文库介绍）。
- **博士论文**：《Shaping and Policy Search in Reinforcement Learning》(2003)。这是强化学习早期奠基性工作之一，"Shaping"（奖励塑形）的思想影响了后续 RLHF 范式。
- **跨学科烙印**：CMU 的"理论派" + MIT 的"系统派" + Berkeley Jordan 实验室的"统计派"三足鼎立，构成 Ng 学术训练的多元底色。

## 2. 早期职业轨迹

- **2002 起 Stanford 助理教授 → 副教授**：CS + 电气工程双聘，**任 Stanford AI Lab (SAIL) 主任**。SAIL 是全球 AI 研究的"圣地"之一，Ng 担任主任期间将其推到深度学习时代最前线。
- **斯坦福自动控制直升机项目 (2000s 中期)**：Ng 团队开发了**世界上最先进的自动控制直升机之一**——能表演特技飞行动作。这项工作是后续 **Pieter Abbeel 博士论文 (Stanford)** 的核心，也是深度强化学习在机器人控制中的早期里程碑。
- **2008 Stanford Engineering Everywhere (SEE) 项目**：把斯坦福多门课程免费放到网上，是 **MOOC 运动的早期先驱**（比 Coursera 早 4 年）。
- **2008-2009 机器学习课程 (CS229) 公开化**：把 CS229 的视频讲义全部免费放上网，是 YouTube 上最早的"系统性 ML 教学"内容之一。
- **2010 加入 Google XLab 兼职**：与 Jeff Dean 等顶级工程师合作启动 **Google Brain** 项目（2011 正式成立）。
- **2011-2014 Google Brain 创始负责人 + 斯坦福兼职**：在 Google 期间用 **16000 个 CPU 核心** 训练出**十亿参数**的神经网络，**在没有先验知识的情况下，仅通过观看无标注的 YouTube 视频学会识别"猫"**——这就是著名的"**Google Cat**"事件（2012 年公开）。是深度学习从实验室走向工业的标志性时刻。
- **2012 联合创办 Coursera**：与斯坦福同事 **Daphne Koller** 共同创办。**Coursera 名字来源于"Course"+"Era"**。成为全球最大的 MOOC 平台。
- **2014.5 加入百度任首席科学家**：负责百度研究院 + Baidu Brain 计划。**这是中国互联网公司迄今为止引进的最重量级人物**（来源：MIT Technology Review 2014）。

## 3. 核心研究方向 / 技术贡献

Ng 的技术贡献横跨**学术研究 + 工业系统 + 教育普及**三个轴。

- **UFLDL (Unsupervised Feature Learning and Deep Learning) 教程 (2011)**：是 Ng 在 Stanford 期间整理的深度学习开源教程，**比 Geoffrey Hinton 的 Coursera 课程还早**——被视为中文世界深度学习的"启蒙教材"。
- **Google Brain "猫脸识别" (2012)**：16000 CPU 核心 + 10 亿参数神经网络，**无监督学习** YouTube 视频中"猫"的概念。证明了深度学习在大规模无标注数据上的可行性，直接催生了**深度学习的"大模型 + 大数据 + 大算力"三件套**。
- **Deep Learning with COTS HPC Systems (ICML 2013, 与 Adam Coates 等)**：用**消费级 HPC 系统 + 大量 GPU** 训练大规模深度网络——**这一工作是后来 AI 算力基础设施演进的奠基性论文**。
- **Sparse Filtering (NIPS 2011)**：提出无监督特征学习新方法。
- **Building High-Level Features using Large Scale Unsupervised Learning (ICML 2012)**：和 Quoc Le、Jeff Dean 合作，**是 Google Cat 论文的正式学术发表版本**。
- **Reinforcement Learning 早期工作 (2000s)**：Ng 早期研究的"反直升机""Shaping and Policy Search"等论文是现代 RL 算法的雏形之一，影响了后续 DQN、PPO 等算法的设计哲学。
- **ROS (Robot Operating System) (ICRA 2009)**：Ng 参与开发，**后来成为机器人领域的"Linux"**——全球最广泛使用的开源机器人软件平台。
- **Autonomous Helicopter (2008 前后)**：Andrew Ng 团队通过**学徒学习 (Apprenticeship Learning)** 让直升机自主表演特技，被《Tech Review》评为当年十大突破技术之一。
- **UFLDL / DeepLearning.AI 系列课程**：包括 **Deep Learning Specialization (Coursera 五门课)**、**AI for Everyone**、**Machine Learning (Coursera 经典课，累计学习者数百万)**、**Generative AI for Everyone (2023)**、**Reasoning with o1 (2024-2025)** 等。**是全球 AI 教育的"基础设施"**。
- **200+ 篇学术论文**：涵盖机器学习、机器人、计算机视觉、自然语言处理、强化学习。

## 4. 标志性成就 / 获奖 / 里程碑

| 时间 | 事件 | 来源 |
|---|---|---|
| 1997 | CMU 本科三学位 | 百度百科 |
| 2002 | UC Berkeley 博士 (导师 Michael I. Jordan) | CSDN 文库 |
| 2002 | 加入 Stanford | 百度百科 |
| 2007 | **斯隆奖 (Sloan Fellowship)** | 百度百科 |
| 2008 | **MIT Technology Review TR35**（35 岁以下 35 位顶级创新者） | 百度百科 |
| 2008 | SEE 项目（MOOC 早期） | 百度百科 |
| 2010-2011 | 启动 Google Brain | 百度百科 / 网易科技 |
| 2011 | 创办 Google Brain + "猫"项目启动 | 百度百科 |
| 2011 | "计算机与思想奖" | 百度百科 |
| 2012 | 联合创办 Coursera | 百度百科 |
| 2012 | Google Cat 论文公开 | arXiv 2012 |
| 2013 | 入选 **《时代》全球最具影响力 100 人** | 百度百科 |
| 2014.5 | 加入百度任首席科学家 | PR Newswire 2014 |
| 2014.5 | 在硅谷 Sunnyvale 开设百度美国研究院 | PR Newswire 2014 |
| 2017 | 创办 **Landing.ai**（制造业 AI / 计算机视觉） | 百度百科 |
| 2017 | 创办 **AI Fund**（早期 AI 创业孵化基金） | 百度百科 |
| 2017 | 创办 **DeepLearning.AI**（AI 教育平台） | 百度百科 |
| 2017 | 担任 Woebot 董事长（心理健康 chatbot） | 百度百科 |
| 2017.3 | 离开百度 | 百度百科 |
| 2019.2 | 第一个孩子 Nova Athena Ng 出生 | 百度百科 |
| 2021 | 入选**福布斯中国·北美华人精英 TOP 60** | 百度百科 |
| 2022.2 | 公开感染新冠，7 天后转阴 | 百度百科 |
| 2023 | 入选 **TIME 100 AI**（时代周刊 AI 百人榜） | andrewng.org |
| 2024.4 | **加入亚马逊董事会**（任期自 2024-04-09 起） | 蓝点网 / 网易 |
| 2024.8 | 辞去 **Landing AI CEO** 职务 | 百度百科 |
| 2024+ | 持续主理 DeepLearning.AI + AI Fund + Coursera 主席 | andrewng.org |

## 5. 创业 / 领导经历

- **Coursera 联合创始人 + 主席 (2012-)**：与 Daphne Koller 共同创办。**当前 Coursera 已是全球最大的 MOOC 平台之一**——累计 1 亿+ 学习者、3500+ 课程、与 200+ 顶尖大学合作。Ng 担任 Co-Chairman 至 2014，之后担任主席。
- **Landing.ai 创始人 + CEO (2017-2024.8)**：专注**制造业 AI** + 计算机视觉——为制造业客户提供**小数据场景下的视觉检测解决方案**。提出"data-centric AI"概念，强调**数据质量比模型架构更重要**。2024.8 辞去 CEO，转为顾问角色。
- **AI Fund 管理合伙人 (2017-)**：早期 AI 创业孵化基金，已投出多家人工智能公司（Landing AI、Woebot 等均出自该基金）。
- **DeepLearning.AI 创始人 (2017-)**：教育技术公司，**核心产品是 Coursera 上的 Deep Learning Specialization + AI for Everyone + Generative AI 系列课**。是 Ng 现阶段投入最多的"产品"。
- **Woebot 董事长 (2017-)**：心理健康 chatbot 公司。
- **百度首席科学家 + 副总裁 (2014-2017)**：领导百度研究院 + Baidu Brain 计划。任内推动百度从"搜索公司"向"AI 公司"转型，建立北京 + 硅谷双中心研究院，**招募了 Adam Coates、彭军、楼天城、Adam Yala 等一批人才**。
- **Google Brain 创始负责人 (2011-2014)**：与 Jeff Dean 共同发起。
- **Stanford AI Lab 主任 (?-2014)**：SAIL 是 Stanford 的 AI 旗舰实验室，Ng 任内培养出 Pieter Abbeel、Quoc Le、Ian Goodfellow 等一批学生。
- **2024 亚马逊董事会成员**：是 Ng 首次进入**顶级科技公司董事会**——被解读为亚马逊对标"微软 + OpenAI"组合的关键布局。

## 6. 跨界 / 影响力溢出

- **教育普及**：**全球 AI 教育的"基础设施"**——Ng 主导的 Coursera 课程累计学习者数百万，被《Fast Company》评为"教育界最具影响力的创业者之一"。**"让世界上每个人接受高质量免费教育"是 Ng 公开的使命宣言**。
- **"翻转教室"理念**：把在线视频 + 自动化作业评分 + 线下互动结合，是 MOOC 教学法的奠基者之一。
- **中国 AI 行业催化**：2014-2017 担任百度首席科学家期间，**为中国 AI 行业培养了一批人才**（楼天城、彭军等），把"深度学习 + 大数据 + 大算力"三件套的工程范式引入中国。
- **政策 / 治理**：2024 加入亚马逊董事会后，**被定位为亚马逊在 AI 治理和战略上的"首席顾问"**——尤其在 AWS 与 Anthropic 合作、Alexa GenAI 化、零售 AI 应用方面提供战略输入。
- **公众沟通 / 公共写作**：通过 The Batch (DeepLearning.AI 周刊)、andrewng.org 博客、Twitter、X、播客等持续输出"AI for Everyone"型内容。**"AI 不是魔法，是工程"** 是 Ng 反复强调的反炒作叙事。
- **"data-centric AI" 运动**：在 NIPS 2021 等场合公开提出"数据质量比模型架构更重要"，推动 ML 社区从"model-centric"向"data-centric"转移。
- **AI Agent 倡导**：2024-2025 多次公开演讲强调"AI Agent 是下一波浪潮"，亲自推动 Agentic AI 课程和工具。
- **2022 新冠阳性 → 转阴**：通过 X 公开个人健康数据，强调疫苗作用，是"科学家 + 公众传播"的典型案例。

## 7. 性格特质与认知风格

> 性格特质基于多次公开访谈、Coursera 课程风格、推特发言、The Batch 周刊、播客推断。

- **"老师型创始人" 气质**：Coursera + DeepLearning.AI + AI Fund 三位一体，**核心身份认同是"老师"**——不仅做研究，还把研究变成教育产品。Ng 公开说"AI 革命的最大瓶颈不是技术，是人才"。
- **温和 + 务实 + 反炒作**：在多次访谈中明确"AI 不是人脑的模拟，它距离真正的 AI 还相当遥远"——**主动戳破 AI 炒作泡沫**。这种"克制的乐观"是 Ng 的标志性风格。
- **"系统性思考 + 渐进式落地"**：从研究到教育到工业到治理——**每一步都建立在上一步基础上**。"先把事情搞对，再讨论大事"是 Ng 的一贯方法论。
- **"AI for Everyone" 叙事**：与 Sam Altman 等"AGI 即将来临"叙事形成对比——Ng 强调**AI 是工具，需要被大众理解才能发挥价值**。"教育的规模化"是其 AI 哲学的核心。
- **工程师 / 落地导向**：在《程序员》2014 专访中强调"数据 + 计算基础架构 + 工程师培养"是深度学习三大要素——**对"工程化"的偏好贯穿始终**。
- **国际化 / 跨文化适应**：在香港 / 新加坡 / 英国 / 美国 / 中国 5 个文化中长大和工作，**是中国 AI 圈最受信任的西方科学家之一**。在百度期间其妻 Carol Reiley 评价"我从未见过你如此努力又如此开心"。
- **"乐观 + 行动派"**：与 Stuart Russell / Bostrom 的"AI 风险"叙事形成对比，Ng 倾向于"先行动起来"——**风险存在但不应阻止进步**。
- **家庭导向**：2019 长女 Nova 出生后，多次在 X 分享家庭生活。

## 8. 失败 / 争议 / 挫折

- **百度任期的"中国水土不服" 争议**：2014-2017 担任百度首席科学家期间，**百度内部 AI 战略执行存在争议**——陆奇加入后（2017）才开始"AI 平台化"实质性推进。Ng 离职后百度的 AI 战略多有调整，被部分评论者解读为"百度的 AI 战略更多是公关价值"（来源：网易科技 / 蓝点网综合报道）。
- **Coursera 商业化困境**：Coursera 长期在"教育使命 vs 商业可持续"之间摇摆。**多次裁员 + 2020 IPO 后股价长期承压**。
- **Landing.ai 数据中心化方法学的局限**：data-centric AI 虽在制造业有应用，**但在通用大模型时代被边缘化**——大模型时代大家重新把"模型 + 算力"放在第一位。
- **"未达到 Google 内部预期" 的内部争议**：Google Cat 公开后，Google 内部对 Brain 团队的资源分配有争议；Jeff Dean 等更倾向于把资源给搜索 / 广告业务。**这导致部分 Google Brain 早期员工离开**（如 Pieter Abbeel 离开 Google 后去 Berkeley 任教授、创办 Covariant）。
- **学术影响力 vs 工业影响力的错位**：在学术圈，Ng 长期被视为"更擅长教学而非 SOTA 研究"——这是学术界对其部分看法的偏颇，但也说明 Ng 的真正贡献是"放大"而非"原创"。
- **"教育普及" 的边际收益递减**：Coursera 用户数已超 1 亿，但**完课率 / 证书含金量 / 就业转化率** 一直被质疑。**Ng 自己在 X 上也承认"完成课程的人数比例不高"**。
- **"AGI 末日论" 立场的边缘化**：在 2023-2024 的 AI 风险大讨论中，Ng 倾向于"乐观派 + 行动派"立场，与 Hinton / Bengio / Russell 的"警示派"形成对比——**被部分评论者视为"过于乐观"**。

## 9. 协作网络

- **导师 / 学术谱系**：
  - **Michael I. Jordan**（UC Berkeley 博士导师，机器学习教父）
  - **Stuart Russell**（UC Berkeley 教授同事，Ng 在 Berkeley 读博时 Russell 是其老师之一）
  - **Pieter Abbeel**（Stanford 博士，Ng 学生 → 伯克利教授 → Covariant 创始人）
  - **Quoc V. Le**（Stanford 博士生，Google Cat 共同一作 → Google Brain 主力）
  - **Adam Coates**（Stanford 博士生 → 百度硅谷 AI 实验室主任）
  - **Ian Goodfellow**（Stanford 短期学生 → GAN 发明者）
  - **Daphne Koller**（Stanford 同事 → Coursera 联合创始人 → Insitro 创始人）
  - **Richard Socher**（Stanford 学生 → Salesforce 首席科学家 → You.com 创始人）
  - **Carol Reiley**（妻子，机器人 / 医疗 AI 研究员）
- **工业网络**：
  - **Jeff Dean**（Google Brain 共同负责人，Google Cat 共同一作）
  - **陆奇**（百度 COO，Ng 离职后接任部分 AI 战略）
  - **李开复**（创新工场，Ng 中国 AI 圈的重要同行）
  - **Jensen Huang**（英伟达，AI 算力生态紧密合作）
  - **Andy Jassy**（Amazon CEO，2024 邀请 Ng 加入董事会）
- **Coursera 联合创始人**：**Daphne Koller**（2012 共同创办，2016 离开创办 Insitro）
- **百度时期同事**：王劲、余凯、徐伟、彭军、楼天城、Adam Coates 等
- **AI Fund 投资组合**：Landing AI、Woebot、多个 AI 创业公司
- **政策 / 治理网络**：
  - 亚马逊董事会（自 2024.4）
  - 美国国家 AI 顾问委员会
  - 与白宫 / 商务部在 AI 教育 / 监管上的对话

## 10. 个人哲学 / 方法论

可凝练为以下 5 点（多源自多次公开访谈、Coursera 课程、The Batch 周刊）：

1. **"AI 不是人脑模拟，距离真正的 AI 还相当遥远"**（2014《程序员》专访）：明确反对"AI 是人脑的模拟"叙事，强调"AI 主要是从海量数据中学习，理解数据"。**这种"祛魅"立场贯穿 Ng 一生**。
2. **"教育的规模化"是 AI 革命的最大瓶颈**：在 Stanford 期间发起 SEE 项目 → 创办 Coursera → 创办 DeepLearning.AI，**用 20 年时间把"教育规模化"做到极致**。"让世界上每个人接受高质量免费教育"是公开使命。
3. **"data-centric AI > model-centric AI"**：2021 起的公开主张——**模型架构已经成熟，数据质量才是瓶颈**。"要更聪明地工作，而不是更辛苦地工作"。
4. **"AI Agent 是下一波浪潮" (2024-2025)**：在多次播客中明确"AI Agent 将重塑所有软件形态""AGI 不是单一事件，是渐进过程"——**这种渐进叙事与 Sam Altman 的"AGI 即将来临"形成对比**。
5. **"先把事情搞对，再讨论大事"**：从 Helicopter → Coursera → Baidu → Landing → DeepLearning.AI → Amazon Board——**每一步都建立在上一步基础上**。"避免被炒作裹挟"是 Ng 的方法论核心。

---

## 一手来源 / 引用清单

- 个人主页：https://www.andrewng.org
- Coursera：https://www.coursera.org/instructor/andrewng
- DeepLearning.AI：https://www.deeplearning.ai
- Landing AI：https://landing.ai
- AI Fund：https://aifund.ai
- 百度百科：https://baike.baidu.com/item/吴恩达
- 2014-05-16 PR Newswire：Baidu Opens Silicon Valley Lab, Appoints Andrew Ng as Head of Baidu Research
- 2014《程序员》专访《Andrew Ng 谈 Deep Learning》CSDN / 腾讯转载
- 2024-04-12 蓝点网：亚马逊宣布任命吴恩达博士担任董事会成员
- 2024-04-12 网易：刚刚，吴恩达已被亚马逊纳入其董事会（任命邮件原文）
- 2017 i 黑马《Andrew Ng 是谁?凭什么他能和"百度大脑"擦出火花?》
- 200+ 篇 ML/RL/CV 学术论文（NIPS/ICML/ICLR/CVPR 2009-2014）
- TIME 100 AI 2023 榜单

## 数据可信度自评

- **教育 / 早期职业**：高（多源一致，导师、毕业时间、学术奖项都可查证）
- **Coursera 联合创办 + 商业化数据**：高（Coursera 财报 + 多源报道）
- **Google Brain + Google Cat 事件**：高（arXiv 论文 + MIT Technology Review + 网易科技详述）
- **百度任期评价**：中-高（多源报道 + 内部人士访谈）
- **Landing AI / AI Fund / DeepLearning.AI 状态**：中-高（公司官网 + 2024-2025 公开报道）
- **亚马逊董事会任命**：高（亚马逊官方邮件原文 + 多家媒体同步报道）
- **性格特质**：中（基于公开访谈 + 课程风格推断）
- **未确认**：Ng 个人净资产、AI Fund 投资组合完整名单
