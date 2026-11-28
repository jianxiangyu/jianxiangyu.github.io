---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<section class="home-hero" markdown="1">
<p class="hero-lead">I am currently a third-year Ph.D. Student at the School of Data Science and Engineering, East China Normal University (ECNU), under the supervision of <a href="https://lixiang3776.github.io/">Prof. Xiang Li</a> in the PLANING lab. My research interests lie in graph learning and large language models (LLMs). My previous research focused on graph representation learning and graph foundation models. Recently, I have been particularly interested in LLM agents, including agent skills, adaptive routing, and harness evolution. I also explore the applications of graph learning and LLMs in scientific research and risk detection.</p>

<!-- <p class="hero-lead">I am currently an intern at Baidu AI Cloud in the Agent Strategy Group in Beijing. Previously, I interned at Tencent WeChat in Guangzhou through the Tencent Rhinoceros-Bird Program, at Ant Group in Shanghai, and at Huawei's 2012 Labs (Advance Computing and Storage Lab) in Shanghai.</p> -->


<p class="hero-lead">
  I am currently an intern at
  <img src="./images/logos/baidu.png" class="company-logo" alt="Baidu">
  <strong>Baidu AI Cloud</strong>
  (Agent Policy Group, Beijing).
  Previously, I interned at
  <img src="./images/logos/weixin.png" class="company-logo" alt="Tencent">
  <strong>Tencent WeChat</strong>
  (Guangzhou, Tencent Rhinoceros-Bird Program),
  <img src="./images/logos/ant_group1.png" class="company-logo" alt="Ant Group">
  <strong>Ant Group</strong> (Shanghai), and
  <img src="./images/logos/huawei1.png" class="company-logo" alt="Huawei">
  <strong>Huawei 2012 Labs</strong>

  (Advanced Computing and Storage Lab, Shanghai).

</p>

<div class="hero-focus" markdown="1">
<div class="hero-section-label">Research Interests</div>

<!-- - **LLM Agents & Harness:** agent skills, harness evolution, agentic routing, agentic RL -->
<!-- - **LLM for Science:** scientific applications of large language models -->
<!-- - **Graph Data Mining:** graph neural networks, heterogeneous graph mining -->
<!-- - **Integration of GNNs and LLMs:** graph foundation models, graph prompt learning -->

- **LLM Agents & Harness:** agent skills [[MASA](https://arxiv.org/abs/2605.30723)], agentic RL [[Skill0.5 (EMNLP’26)](https://arxiv.org/abs/2605.28424)], adaptive routing, harness evolution
- **LLMs for Science:** automated peer review [[SEA (EMNLP’24)](https://arxiv.org/abs/2407.12857)], scientific knowledge retrieval [[SEAGraph (IJCNLP-AACL’25)](https://arxiv.org/abs/2412.11939)], research agents [[APEX (EMNLP’26)](https://arxiv.org/abs/2601.04794)]
- **Graph Foundation Models:** graph pre-training and generalization [[REEF (NeurIPS’26)](https://arxiv.org/abs/2505.12027)], graph prompt learning [[RELIEF (KDD’25)](https://arxiv.org/abs/2408.03195), [Self-Pro (ECML-PKDD’24)](https://arxiv.org/abs/2310.10362v2)]
- **Graph Learning & Mining:** LLM-enhanced graph learning [[LLM4NG (AAAI’25)](https://arxiv.org/abs/2310.09872)], heterogeneous graph contrastive learning [[MEOW (SDM’23)](https://epubs.siam.org/doi/abs/10.1137/1.9781611977653.ch5), [AdaMEOW (TKDE’24)](https://ieeexplore.ieee.org/abstract/document/10487103)], generative graph learning [[HQA-GAE (WWW’25)](https://dl.acm.org/doi/abs/10.1145/3696410.3714656), [GraMI (KDD’25)](https://arxiv.org/abs/2311.07929)]
- **AI for Trust & Safety**: graph anomaly detection [[N2NSC (EMNLP’26)](https://arxiv.org/abs/2606.30009)], harmful content detection [[C²TU (EMNLP’26)](https://arxiv.org/abs/2505.22184)]



</div>

<p class="hero-contact">🎉🎉🎉 Feel free to reach out to me for academic discussions and collaborations!</p>
</section>

<!-- My research interests include data mining, especially graph mining. The research work I have been involved in encompasses heterogeneous graph mining and weakly supervised learning on graphs. -->
<!-- Currently I am exploring the integration of Large Language Models (LLMs) with Graph Neural Networks (GNNs). -->

<!-- https://scholar.google.com.hk/citations?user=EH6ntM0AAAAJ&hl=zh-CN&oi=ao -->

<!-- 🎉✨🎆 Let’s welcome the New Year together! -->

<!-- # 🔥 News -->
<!-- - *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

<span class='anchor' id='publications'></span>

{% include_relative includes/pub.md %}


<span class='anchor' id='preprint'></span>

# 📑 Preprint


<div class='paper-box'><div class='paper-box-image'><div>
<img src='../../images/publications/masa.png' alt="sym" width="98%"></div></div>
<div class='paper-box-text' markdown="1">
[Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents](https://arxiv.org/abs/2605.30723) &nbsp; 
<!-- [![](https://img.shields.io/github/stars/jianxiangyu/MEOW?style=social&label=Code+Stars)](https://github.com/jianxiangyu/MEOW) &nbsp; <a href='https://www.bilibili.com/video/BV1uF4m1K7Zz/'><img src="https://img.shields.io/badge/Bilibili-AdaMEOW-blue?logo=bilibili&logoColor=white"></a> \\ -->
\\
**Jianxiang Yu**, Jiapeng Zhu, Bochen Lin, Qier Cui, Zichen Ding, Xiang Li.
- A model-aware skill alignment framework for LLM agents. 🧩
- Effective adaptation and generalization across models and tasks.  🔄
</div>
</div>



# 💻 Internships
<div class="internship-list">
 <div class="internship-item">
    <div class="internship-date">2026.09 - Present</div>
    <div class="internship-body">
      <span>Baidu AI Cloud, Dumate Strategy Group, Beijing, China</span>
      <img src="./images/logos/dumate-icon.png" alt="Dumate logo">
      <img src="./images/logos/baidu.png" alt="Baidu logo">
    </div>
  </div>
  <div class="internship-item">
    <div class="internship-date">2025.10 - 2026.06</div>
    <div class="internship-body">
      <span>Tencent WeChat group, Guangzhou, China (Participated in Tencent Rhinoceros-Bird Program)</span>
      <img src="./images/logos/weixin.png" alt="WeChat logo">
    </div>
  </div>
  <div class="internship-item">
    <div class="internship-date">2024.06 - 2025.02</div>
    <div class="internship-body">
      <span>Ant Group, Shanghai, China</span>
      <img src="./images/logos/ant_group.png" alt="Ant Group logo">
    </div>
  </div>
  <div class="internship-item">
    <div class="internship-date">2023.07 - 2023.12</div>
    <div class="internship-body">
      <span>Advance Computing and Storage Lab, 2012 Labs, Huawei Technologies, Shanghai, China</span>
      <img src="./images/logos/huawei1.png" alt="Huawei logo">
    </div>
  </div>
</div>



<!-- <span class='anchor' id='experience'></span>

# 🌟 Experience
<div class="timeline-list timeline-list--dated" markdown="1">
- *2024.11* Attend EMNLP 2024 in Miami, USA.
- *2024.10* Give a talk at EMNLP 2024 pre-presentation event organized by AI TIME.
</div> -->


<span class='anchor' id='education'></span>

# 📖 Education
<div class="education-list">
  <div class="education-item">
    <div class="education-date">2024.09 - now</div>
    <div class="education-body">
      <strong>Ph.D. Student</strong>
      <span>School of Data Science and Engineering, East China Normal University</span>
      <img src="./images/logos/ecnu.png" alt="East China Normal University logo">
    </div>
  </div>
  <div class="education-item">
    <div class="education-date">2021.09 - 2024.06</div>
    <div class="education-body">
      <strong>Master</strong>
      <span>School of Data Science and Engineering, East China Normal University</span>
      <img src="./images/logos/ecnu.png" alt="East China Normal University logo">
    </div>
  </div>
  <div class="education-item">
    <div class="education-date">2017.09 - 2021.06</div>
    <div class="education-body">
      <strong>Undergraduate</strong>
      <span>Honor College, Hangzhou Dianzi University</span>
      <img src="./images/logos/hdu.png" alt="Hangzhou Dianzi University logo">
    </div>
  </div>
</div>

<span class='anchor' id='honors'></span>

# 🎖 Honors and Awards
<div class="timeline-list timeline-list--dated" markdown="1">
- *2024.05* Outstanding Graduate, East China Normal University
- *2023.11* Second Prize Enterprise Scholarship, School of Data Science and Engineering, East China Normal University
</div>



<span class='anchor' id='services'></span>

# 🔍 Services
<div class="timeline-list services-list" markdown="1">
I have served as a reviewer or program committee member for:

- **Conferences:** ICML'27, ICLR'27, AAAI'27, NeurIPS'26, ICML'26, AAAI'26 (Main & AI Alignment), KDD'26 (Datasets & Benchmarks).

- **Journals:** JAS, IEEE TKDE.


<!-- - AAAI 2027 -->
<!-- - NeurIPS 2026 -->
<!-- - ICML 2026 -->
<!-- - AAAI 2026 -->
<!-- - KDD 2026 Datasets and Benchmark Track -->
</div>

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

