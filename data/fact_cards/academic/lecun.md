# 杨立昆 (Yann LeCun) 事实卡

> "我对 LLM 的看法没变:它们是了不起的工程奇迹,但不能通向人类级智能。"  
> —— 2025 年 11 月 17 日 MIT 研讨会发言

**基本信息**:1960 年 7 月 8 日生于法国巴黎,法国裔美籍计算机科学家。Meta(原 Facebook)副总裁兼首席 AI 科学家、纽约大学 Courant 数学科学研究所 Silver 终身教授、FAIR(Facebook AI Research)创始主任。2018 年图灵奖得主、卷积神经网络 (CNN) 之父、ICLR 会议联合创始人。

---

## 1. 教育背景

- **ESIEE Paris (1983)**:获电子工程工程师文凭(Diplôme d'Ingénieur)。
- **Université Pierre et Marie Curie (巴黎第六大学, 现 Sorbonne Université)**:1987 年获计算机科学博士学位,博士论文方向即为神经网络中一种早期形式的反向传播算法。
- 博士期间受 Hinton 1986 年 Nature 论文、LeCun 本人 1985 年在巴黎遇见的 Terry Sejnowski 等影响,坚定了神经网络路线。
- **博士后 (1987–1988)**:在多伦多大学 Geoffrey Hinton 实验室做博士后,这是 Hinton 与 LeCun 学术关系正式建立的起点。

## 2. 早期职业

- **1988–1996 贝尔实验室 (AT&T Bell Labs)**:加入自适应系统研究部 Adaptive Systems Research Department,主任 Larry Jackel 是其伯乐。与 Vladimir Vapnik(支持向量机 SVM 之父)、John Denker、Léon Bottou 同组。
- **1996–2003 AT&T Labs Research**:1996 年 AT&T 拆分,LeCun 留 AT&T 实验室,任图像处理研究部门主管,期间带领团队完成 LeNet-5 等系统,但因 1990s 神经网络寒冬而遇到研究困难。
- **2003 纽约大学**:加入 NYU Courant 数学科学研究所任教授,开始横跨工业界/学术界的双重身份。
- **2013 Facebook / Meta**:被 Mark Zuckerberg 亲自招入,创建 FAIR 实验室,任创始主任。
- **2018 起**:晋升为 Meta 首席 AI 科学家(Chief AI Scientist),领导整个公司 AI 研究方向。

## 3. 核心研究方向/技术贡献

- **卷积神经网络 (CNN)**:1989 年发表《Backpropagation applied to handwritten zip code recognition》(Neural Computation 1(4):541-551),首次将反向传播与卷积结构结合用于手写字符识别,被广泛视为现代 CNN 起点。来源: https://direct.mit.edu/neco/article/1/4/541/5515
- **LeNet-5 (1998)**:与 Léon Bottou、Yoshua Bengio、Patrick Haffner 合著《Gradient-based learning applied to document recognition》(Proceedings of the IEEE 86(11):2278-2324),1990s 末被 NCR 等公司部署用于美国约 10-20% 支票识别。来源: https://ieeexplore.ieee.org/document/726791
- **Optimal Brain Damage (1990)**:早期神经网络剪枝工作,与 Denker、Solla 合著,提出"剪枝"概念。
- **Siamese Networks (1994)**:用于签名验证,后续度量学习、对比学习重要先驱。
- **Energy-Based Models / EBGAN (2016)**:提出基于能量的生成式对抗网络。
- **DropConnect (2013)**:神经网络正则化方法。
- **Deep Learning 三巨头综述 (2015)**:与 Bengio、Hinton 合著《Deep learning》Nature 521(7553):436-444,迄今引用过 10 万次,是该领域最具影响力的综述。来源: https://www.nature.com/articles/nature14539
- **JEPA / 世界模型 (World Models, 2022–)**:近期核心方向,主张通过视频与多模态自监督学习"世界模型"才是通往 AGI 的正道。

## 4. 标志性成就/获奖

- **2018 ACM 图灵奖**:与 Hinton、Bengio 共获。
- **2025 Queen Elizabeth Prize for Engineering (伊丽莎白女王工程奖)**:与黄仁勋、李飞飞等 6 位共获(2025 年 11 月 6 日公布)。
- **2014 IEEE Neural Networks Pioneer Award**。
- **2015 IEEE PAMI Distinguished Researcher Award**。
- **2016 墨西哥 IPN 荣誉博士**。
- **2018 Légion d'honneur (法国荣誉军团骑士)**。
- 入选美国国家科学院、美国国家工程院、法国科学院院士。

## 5. 领导/创业经历

- **FAIR 实验室 (2013)**:与 Mark Zuckerberg 共同创建,任创始主任。FAIR 推出 PyTorch(被 AI 社区广泛采用)、发布 Llama 系列(累计下载超 8 亿次)。
- **ICLR 会议 (2013)**:与 Yoshua Bengio 共同创办 International Conference on Learning Representations,目前已成为 ML 三大顶会之一(与 NeurIPS、ICML 并列)。
- **NYU 数据科学中心 (2013)**:任创始主任。
- **2025 年宣布离职创业 (2026 年 1 月生效)**:据 Reuters / Financial Times 2025 年 11 月 11 日报道,LeCun 计划于 2025 年底离开 Meta,创办以"高级机器智能(AMI, Advanced Machine Intelligence)"为核心方向的新公司,继续推动"世界模型"路线。来源: 雪球 / 51CTO / 腾讯网 (2025-11-11) https://www.51cto.com/article/336124.html

## 6. 跨界/影响力溢出

- 推动 **PyTorch 开源生态**:成为全球最广泛使用的深度学习框架之一(被 ChatGPT、Stable Diffusion 等核心项目采用)。
- 推动 **Llama 开源战略**:FAIR 是 Meta 整个开源 AI 路线的灵魂,2025 年讨论是否"再闭源"时,LeCun 是坚定的开源派。
- 多次**访华**,在清华、上海交大、台大、中科院模式识别国家重点实验室演讲。
- 与**音乐/文化**有深厚联系:热爱巴洛克与硬波普爵士,曾表示欣赏从他外祖母阿尔萨斯传来的传统文化。
- 在与 NYU 心理学教授 Gary Marcus 的长期 Twitter 公开辩论中,LeCun 一直代表"深度学习派"立场,这一辩论是 2017 年以来 AI 学界最有名的公开论战。

## 7. 性格特质与认知风格

- **工程师思维 + 学术独立**:对 LLM 路线的公开批评,显示出他宁愿与公司战略不同步也要坚持技术观点。
- **法国式的雄辩与浪漫**:演讲充满比喻(把 LeNet 比作"机器学习界的果蝇"),辩论中喜用反问。
- **生活侧**:业余飞行员(其父是工程师,影响他对飞行器的热爱)、业余音乐家、对动物智能有强烈兴趣。
- **认知风格**:注重"long-term research 优先于 short-term wins",这是他与 Meta 战略冲突的根源。
- **表达**:英语带法语口音,语速快,笑声大,演讲中常用工程直觉而非数据说话。

## 8. 失败/争议/挫折

- **1990s 神经网络寒冬**:LeNet 在商业上成功(读支票)却没能挽救神经网络整体的学术地位,业界转向 SVM。
- **2000s 早期**:CNN 专利被 AT&T 拆分后划归 NCR 公司,LeCun 本人无法继续相关研究。
- **2023–2025 与 Meta 战略冲突**:Mark Zuckerberg 2024–2025 重押"超级智能实验室",把 Scale AI 创始人 Alexandr Wang 招入任"首席 AI 官",LeCun 汇报线被改。
- **Llama 4 表现不及预期**:2025 年发布后被中国开源模型(DeepSeek、Qwen 等)反超,开源战略受质疑。
- **"少数派"批评**:他在多场演讲中坚持"LLM 不能通向 AGI"被部分人认为"逆潮流"。
- 2018 年左右,LeCun 与 Hinton 在 AI 风险议题上公开分歧 —— LeCun 反对 Hinton 那种"AI 灭绝论"调子,主张更工程化地解决 AI 安全。

## 9. 协作网络

- **深度学习三巨头**:Hinton(博士后导师)、Bengio(ICLR 联合创始人、LeNet 共同作者)。
- **贝尔实验室"双星"**:与 Vladimir Vapnik(同在 Jackel 手下)曾立著名"2000 年 vs 2005 年神经网络赌局",见证人即 LeCun 本人(Jackel 与 Vapnik 平分了 2000 年那顿晚餐)。
- **FAIR 同事**:Joelle Pineau(2025 年 5 月离职去 Cohere)、Rob Fergus、Leon Bottou、Devi Parikh。
- **学生/合作者**:Léon Bottou、Sumit Chopra、Marc'Aurelio Ranzato、Arthur Szlam 等。
- **论战对手**:Gary Marcus(NYU 心理学教授)、Stuart Russell、Geoffrey Hinton(温和分歧)。

## 10. 个人哲学/方法论

- **"LLM 是必要的工程但不是智能的本质"**:这是 LeCun 过去 5 年最鲜明的观点,在 MIT 2025 年 11 月发言中重申"任何头脑清醒的人,3-5 年内都不会再使用今天的 LLM"。
- **世界模型 (World Models)**:他认为真正的 AGI 需要从视频、传感器数据中学习物理世界的因果结构,这是 JEPA(联合嵌入预测架构)项目的核心。
- **"开源 vs 闭源是 AI 时代真正的竞争"**:在巴黎最新纪录片中表示,"真正决定未来的是开放世界与封闭生态的对抗"。
- **"AI 安全是工程问题,不是哲学问题"**:他反对"AI 威胁论"的科幻叙事,主张通过目标驱动架构 (goal-driven architecture) 和安全护栏解决。
- **个人座右铭**:"不要让负面故事阻碍你前进"(对其学生常说的话)。

---

**主要来源**
- LeCun 个人主页: https://yann.lecun.com/
- Meta FAIR: https://ai.facebook.com/
- LeCun, Bengio, Hinton, "Deep learning", Nature 521:436-444 (2015): https://www.nature.com/articles/nature14539
- LeCun et al., "Gradient-based learning applied to document recognition", Proc. IEEE 1998
- ACM Turing Award 2018: https://amturing.acm.org/by_year.cfm
- 雪球 / 51CTO / 腾讯网 (2025-11-11 离职报道) https://www.51cto.com/article/336124.html
- 纪录片《Yann LeCun: AI 教父的双面人生》(2025) https://youtu.be/l3Emh_cekZo
