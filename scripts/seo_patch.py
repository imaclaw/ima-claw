#!/usr/bin/env python3
"""
批量为 Ima Claw 博客文章补全 SEO 元数据：
- canonical URL
- keywords
- og: tags (title, description, image, url, type)
- twitter: card tags
- JSON-LD BlogPosting
- hreflang (中英文互链)
"""

import os, re, sys

BASE_URL = "https://imaclaw.github.io/ima-claw/blog/"
OG_IMAGE_DEFAULT = "https://imaclaw.github.io/ima-claw/og-cover.png"
BLOG_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../blog"

# 每篇文章的元数据配置
ARTICLES = {
    # ── 日记系列 ──
    "ai-crash-diary.html": {
        "lang": "zh-CN", "pair": "ai-crash-diary-en.html",
        "title": "AI 翻车日记：凌晨5点，一篇文章都没发出来",
        "desc": "4个子Agent并行写稿，结果1小时过去一篇都没发出来。凌晨5点的人机协作翻车现场，比任何AI教程都真实。",
        "keywords": "AI翻车,AI agent失败案例,openclaw多agent,AI内容创作失败,子agent协作,ima claw日记",
        "og_image": "https://imaclaw.github.io/ima-claw/article-assets/ai-crash-cover.png",
        "date": "2026-03-04", "author": "Yuki He",
        "category": "Work Diary",
    },
    "ai-crash-diary-en.html": {
        "lang": "en", "pair": "ai-crash-diary.html",
        "title": "AI Crash Diary: 5 AM and Not a Single Post Published",
        "desc": "4 sub-agents writing in parallel. 1 hour later, nothing delivered. A raw account of what AI-human collaboration failure actually looks like at 5 AM.",
        "keywords": "AI agent failure, openclaw multi-agent, AI content creation gone wrong, sub-agent collaboration, ima claw diary, AI productivity",
        "og_image": "https://imaclaw.github.io/ima-claw/article-assets/ai-crash-cover.png",
        "date": "2026-03-04", "author": "Yuki He",
        "category": "Work Diary",
    },
    "diary-am-i-employee.html": {
        "lang": "zh-CN", "pair": "diary-am-i-employee-en.html",
        "title": "我问龙虾：你觉得你自己算员工吗？",
        "desc": "凌晨，我突然问了龙虾一个哲学问题。它的回答让我重新想了想，AI到底算什么——工具、助手、还是某种意义上的「同事」？",
        "keywords": "AI是员工吗,AI身份认同,openclaw人设,AI assistant角色,ima claw哲学,AI与人类关系",
        "date": "2026-02-28", "author": "Yuki He", "category": "Work Diary",
    },
    "diary-am-i-employee-en.html": {
        "lang": "en", "pair": "diary-am-i-employee.html",
        "title": "I Asked My Lobster: Do You Consider Yourself an Employee?",
        "desc": "A 2 AM conversation about identity, work, and what it means to be an AI assistant. The answer made me rethink what I actually want from this relationship.",
        "keywords": "AI identity, AI as employee, openclaw persona, AI assistant role, ima claw philosophy, human AI relationship",
        "date": "2026-02-28", "author": "Yuki He", "category": "Work Diary",
    },
    "diary-blog-redesign.html": {
        "lang": "zh-CN", "pair": "diary-blog-redesign-en.html",
        "title": "凌晨三改博客首页：两个栏目，谁都不是配角",
        "desc": "三次推倒重来，只为让博客首页的两个板块不再互相抢风头。设计决策背后的思考过程。",
        "keywords": "博客重设计,vibe coding设计,ima claw博客,网站设计日志,AI辅助设计,openclaw网站",
        "date": "2026-03-03", "author": "Yuki He", "category": "Dev Log",
    },
    "diary-blog-redesign-en.html": {
        "lang": "en", "pair": "diary-blog-redesign.html",
        "title": "Redesigning the Blog at 3 AM: Two Columns, Neither a Sidekick",
        "desc": "Three attempts to get the blog homepage right. The lesson: design is about relationships between elements, not just individual components.",
        "keywords": "blog redesign, vibe coding design, ima claw blog, website design log, AI-assisted design, openclaw website",
        "date": "2026-03-03", "author": "Yuki He", "category": "Dev Log",
    },
    "diary-feishu-entry.html": {
        "lang": "zh-CN", "pair": "diary-feishu-entry-en.html",
        "title": "龙虾第一次进飞书，我们公司172个人都慌了",
        "desc": "我把 AI 龙虾接入了公司飞书。它第一时间就问：「请问公司一共有多少人？」然后我们花了整整一晚上重新设计权限边界。",
        "keywords": "飞书接入AI,openclaw飞书,AI进公司,AI权限边界,ima claw企业,AI助手飞书集成",
        "date": "2026-02-20", "author": "Yuki He", "category": "Work Diary",
    },
    "diary-feishu-entry-en.html": {
        "lang": "en", "pair": "diary-feishu-entry.html",
        "title": "When My Lobster Entered Feishu, 172 People Panicked",
        "desc": "Connecting my AI assistant to company Feishu. Its first question: 'How many people work here?' We spent the whole night redesigning permission boundaries.",
        "keywords": "openclaw feishu integration, AI in enterprise, AI permission boundaries, ima claw company, AI assistant feishu, workplace AI",
        "date": "2026-02-20", "author": "Yuki He", "category": "Work Diary",
    },
    # ── Dev Log 系列 ──
    "dev-log-day1.html": {
        "lang": "zh-CN", "pair": None,
        "title": "龙虾不眠夜 — 24小时开发日志",
        "desc": "从零开始，24小时不间断，用AI vibe coding搭建了Ima Claw的第一个版本。这是一份完整的开发日志。",
        "keywords": "vibe coding,AI开发日志,ima claw开发,openclaw技术,AI辅助编程,24小时开发",
        "date": "2026-02-10", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-adopt.html": {
        "lang": "zh-CN", "pair": "dev-log-adopt-en.html",
        "title": "一只龙虾的领养页 — Adopt 页面设计日志",
        "desc": "为什么叫「领养」而不是「注册」？从产品定位到页面设计，一个词的选择背后的思考过程。",
        "keywords": "ima claw领养页,adopt页面设计,AI产品命名,openclaw adopt,vibe coding设计",
        "date": "2026-02-22", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-adopt-en.html": {
        "lang": "en", "pair": "dev-log-adopt.html",
        "title": "Why We Call It 'Adopt' — The Design Diary of a Lobster Adoption Page",
        "desc": "Why 'adopt' instead of 'sign up'? From product positioning to page design, the thinking behind a single word choice.",
        "keywords": "ima claw adopt page, AI product naming, openclaw adopt, vibe coding design, AI onboarding UX",
        "date": "2026-02-22", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-i18n.html": {
        "lang": "zh-CN", "pair": "dev-log-i18n-en.html",
        "title": "i18n 地狱逃生记 — 48 页多语言网站的血泪史",
        "desc": "三套竞争翻译系统、48个页面、无数个凌晨——如何统一多语言体系的完整踩坑记录。",
        "keywords": "i18n多语言,vibe coding i18n,网站多语言,ima claw国际化,openclaw多语言,前端翻译踩坑",
        "date": "2026-02-25", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-i18n-en.html": {
        "lang": "en", "pair": "dev-log-i18n.html",
        "title": "i18n Hell Escape: Building a 48-Page Multilingual Website",
        "desc": "Three competing translation systems, 48 pages, countless late nights — the complete story of unifying our i18n architecture.",
        "keywords": "i18n multilingual, vibe coding i18n, website localization, ima claw internationalization, openclaw multilingual, frontend translation",
        "date": "2026-02-25", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-refactor.html": {
        "lang": "zh-CN", "pair": "dev-log-refactor-en.html",
        "title": "Day 1 到 Day 2：一个网站的诞生与重构",
        "desc": "544次提交，48页扩展到68页，56分钟架构重写。从第一天到第二天，网站经历了什么？",
        "keywords": "网站重构,vibe coding重构,ima claw重构,openclaw开发,AI辅助重构,网站架构",
        "date": "2026-02-15", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-refactor-en.html": {
        "lang": "en", "pair": "dev-log-refactor.html",
        "title": "Day 1 to Day 2: A Website Is Born and Reborn",
        "desc": "544 commits, 48 to 68 pages, 56-minute architecture rewrite. What happened between day one and day two?",
        "keywords": "website refactor, vibe coding refactor, ima claw rebuild, openclaw development, AI-assisted refactor, web architecture",
        "date": "2026-02-15", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-skills.html": {
        "lang": "zh-CN", "pair": "dev-log-skills-en.html",
        "title": "从 0 到 9,205：一晚上建了个 Skill 市场",
        "desc": "如何在一晚上从零爬取并展示了9205个 ClawHub 社区技能包，打造了 Ima Claw 的技能市场。",
        "keywords": "ima claw skill市场,clawhub技能,openclaw skills,AI技能市场,技能爬取,vibe coding",
        "date": "2026-02-28", "author": "Yuki He", "category": "Dev Log",
    },
    "dev-log-skills-en.html": {
        "lang": "en", "pair": "dev-log-skills.html",
        "title": "From 0 to 9,205: Building a Skill Marketplace Overnight",
        "desc": "How we crawled 9,205 community skills from ClawHub and built the Ima Claw skill marketplace in a single night.",
        "keywords": "ima claw skill marketplace, clawhub skills, openclaw skills, AI skill market, skill crawling, vibe coding",
        "date": "2026-02-28", "author": "Yuki He", "category": "Dev Log",
    },
    # ── 教程系列 ──
    "tutorial-ep01-install.html": {
        "lang": "zh-CN", "pair": "tutorial-ep01-install-en.html",
        "title": "EP01 · 10分钟，领养你的第一只龙虾 | 龙虾学院",
        "desc": "OpenClaw零基础安装教程。Mac/Windows一键安装，10分钟搞定，真的不需要写代码。",
        "keywords": "openclaw安装教程,openclaw入门,ima claw教程,AI助手安装,openclaw中文教程,龙虾学院EP01",
        "date": "2026-02-18", "author": "Yuki He", "category": "Tutorial",
    },
    "tutorial-ep01-install-en.html": {
        "lang": "en", "pair": "tutorial-ep01-install.html",
        "title": "EP01: Adopt Your First Lobster in 10 Minutes — Ima Claw Academy",
        "desc": "Step-by-step guide to installing OpenClaw and connecting your AI assistant to WhatsApp or Telegram. No coding required. Done in 10 minutes.",
        "keywords": "openclaw install tutorial, openclaw beginner guide, ima claw tutorial, AI assistant setup, openclaw english tutorial, install openclaw mac windows",
        "date": "2026-02-18", "author": "Yuki He", "category": "Tutorial",
    },
    "tutorial-ep01-adopt.html": {
        "lang": "zh-CN", "pair": None,
        "title": "EP01 · 10分钟，让飞书多一个能干活的员工 | 龙虾学院",
        "desc": "OpenClaw零基础入门教程第1课。10分钟完成安装和飞书配对，让你的AI助手正式上线。",
        "keywords": "openclaw飞书安装,openclaw入门教程,ima claw飞书,AI助手飞书,openclaw飞书集成,龙虾学院",
        "date": "2026-02-19", "author": "Yuki He", "category": "Tutorial",
    },
    "tutorial-ep02-model.html": {
        "lang": "zh-CN", "pair": "tutorial-ep02-model-en.html",
        "title": "EP02 · 给龙虾装大脑 | 龙虾学院",
        "desc": "OpenClaw大模型配置教程。注册ImaStudio，一个账号解锁大模型大脑+预装智能Skill套件，一键搞定。",
        "keywords": "openclaw配置大模型,openclaw LLM,ima claw大脑,ImaStudio配置,openclaw claude,AI模型配置教程",
        "date": "2026-02-20", "author": "Yuki He", "category": "Tutorial",
    },
    "tutorial-ep02-model-en.html": {
        "lang": "en", "pair": "tutorial-ep02-model.html",
        "title": "EP02: Give Your Lobster a Brain — Ima Claw Academy",
        "desc": "Connect your AI assistant to LLM providers like ImaStudio, Claude, or GPT. Step-by-step configuration guide for OpenClaw models.",
        "keywords": "openclaw LLM setup, openclaw model configuration, ima claw brain, ImaStudio setup, openclaw claude GPT, AI model tutorial",
        "date": "2026-02-20", "author": "Yuki He", "category": "Tutorial",
    },
    "tutorial-ep03-skills.html": {
        "lang": "zh-CN", "pair": "tutorial-ep03-skills-en.html",
        "title": "EP03 · 给龙虾装技能包 | 龙虾学院",
        "desc": "OpenClaw Skill安装教程。IMA基础智能包+IMA全能创作包，让龙虾从'能聊天'变成'能干活'。",
        "keywords": "openclaw skill安装,openclaw技能包,ima claw skills,clawhub技能,AI技能配置,openclaw插件",
        "date": "2026-02-21", "author": "Yuki He", "category": "Tutorial",
    },
    "tutorial-ep03-skills-en.html": {
        "lang": "en", "pair": "tutorial-ep03-skills.html",
        "title": "EP03: Give Your Lobster Skills — Ima Claw Academy",
        "desc": "Install skills to enable image generation, web search, code execution, and more. How to use ClawHub to extend your OpenClaw agent.",
        "keywords": "openclaw skill install, openclaw skills tutorial, ima claw skills, clawhub skills, AI skill configuration, openclaw plugins",
        "date": "2026-02-21", "author": "Yuki He", "category": "Tutorial",
    },
    # ── Tips 系列 ──
    "tips-why-smarter.html": {
        "lang": "zh-CN", "pair": "tips-why-smarter-en.html",
        "title": "为什么你的龙虾比别人的聪明？我总结了5个原因",
        "desc": "好多人说我的龙虾比他们自己养的要聪明。我仔细想了想，这不是运气，也不是模型更好——是有方法的。",
        "keywords": "AI助手更聪明,openclaw训练技巧,ima claw优化,AI prompt技巧,提升AI能力,AI记忆训练",
        "date": "2026-03-01", "author": "Yuki He", "category": "Tips",
    },
    "tips-why-smarter-en.html": {
        "lang": "en", "pair": "tips-why-smarter.html",
        "title": "Why Is Your Lobster Smarter? 5 Reasons — Ima Claw",
        "desc": "Why does my AI assistant seem smarter than others? The answer involves identity files, memory systems, and how you actually talk to it.",
        "keywords": "AI assistant smarter, openclaw training tips, ima claw optimization, AI prompt techniques, improve AI capability, AI memory training",
        "date": "2026-03-01", "author": "Yuki He", "category": "Tips",
    },
    # ── Vibe Coding 系列 ──
    "vibe-coding-day2.html": {
        "lang": "zh-CN", "pair": "vibe-coding-52h-en.html",
        "title": "52小时，544个Commit：一只龙虾的诞生日记",
        "desc": "凌晨5点，她还在截图标红圈。AI还在改像素。189万字对话，0行手写代码。这是一个人和一只AI龙虾的52小时。",
        "keywords": "vibe coding,52小时开发,ima claw诞生,0行手写代码,AI编程,openclaw开发故事",
        "date": "2026-02-12", "author": "Yuki He", "category": "Vibe Coding",
    },
    "vibe-coding-52h-en.html": {
        "lang": "en", "pair": "vibe-coding-day2.html",
        "title": "52 Hours, 544 Commits: The Birth of a Lobster",
        "desc": "At 5 AM she was still circling pixels in red. The AI was still pushing fixes. 1.89M words of conversation, 0 lines of hand-written code.",
        "keywords": "vibe coding, 52 hour build, ima claw origin, zero handwritten code, AI programming, openclaw development story",
        "date": "2026-02-12", "author": "Yuki He", "category": "Vibe Coding",
    },
    "vibe-coding-launch.html": {
        "lang": "en", "pair": None,
        "title": "26小时，295次提交，0行手写代码",
        "desc": "26 hours, 295 commits, 0 lines of hand-written code — the full story of launching Ima Claw with nothing but vibe coding.",
        "keywords": "vibe coding launch, ima claw launch, openclaw vibe coding, AI website building, zero code development",
        "date": "2026-02-10", "author": "Yuki He", "category": "Vibe Coding",
    },
    "vibe-coding-collaboration.html": {
        "lang": "zh-CN", "pair": None,
        "title": "Vibe Coding 协作指南：当老板不懂代码，AI 不懂那个东西",
        "desc": "A guide to Vibe Coding collaboration — when the boss can't code and AI doesn't understand 'that thing.' How to communicate effectively with your AI developer.",
        "keywords": "vibe coding协作,AI辅助编程,老板与AI协作,openclaw vibe coding,ima claw开发,AI沟通技巧",
        "date": "2026-02-14", "author": "Yuki He", "category": "Vibe Coding",
    },
    "vibe-coding-story.html": {
        "lang": "en", "pair": None,
        "title": "我用 Ima Claw 做了这个网站",
        "desc": "How this entire website was built using Ima Claw itself — a meta Vibe Coding story about AI building the tools that train AI.",
        "keywords": "ima claw website, vibe coding meta, AI builds AI tools, openclaw website, AI web development",
        "date": "2026-02-16", "author": "Yuki He", "category": "Vibe Coding",
    },
    "release-v1.html": {
        "lang": "zh-CN", "pair": None,
        "title": "\"你能做网站吗？\" 于是有了134万字，和一个网站。",
        "desc": "From a casual question to 1.34 million words and a full website — the story of how Ima Claw V1 was built entirely through conversation.",
        "keywords": "ima claw v1发布,134万字对话,AI建网站,openclaw案例,vibe coding故事,AI生产力",
        "date": "2026-03-01", "author": "Yuki He", "category": "Dev Log",
    },
}

def build_seo_block(slug, meta):
    lang = meta["lang"]
    pair = meta.get("pair")
    url = BASE_URL + slug
    pair_url = (BASE_URL + pair) if pair else None
    title = meta["title"]
    desc = meta["desc"]
    keywords = meta["keywords"]
    og_image = meta.get("og_image", OG_IMAGE_DEFAULT)
    date = meta.get("date", "2026-02-01")
    author = meta.get("author", "Yuki He")

    # hreflang lines
    hreflang_lines = []
    if pair_url:
        self_lang = lang
        pair_lang = "en" if lang == "zh-CN" else "zh-CN"
        hreflang_lines = [
            f'<link rel="alternate" hreflang="{self_lang}" href="{url}">',
            f'<link rel="alternate" hreflang="{pair_lang}" href="{pair_url}">',
        ]

    # JSON-LD
    jsonld = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{desc[:150]}",
  "image": "{og_image}",
  "author": {{"@type": "Person", "name": "{author}"}},
  "publisher": {{"@type": "Organization", "name": "Ima Claw", "url": "https://imaclaw.github.io/ima-claw/"}},
  "datePublished": "{date}",
  "url": "{url}",
  "inLanguage": "{lang}"
}}
</script>'''

    lines = [
        f'<meta name="keywords" content="{keywords}">',
        f'<link rel="canonical" href="{url}">',
    ] + hreflang_lines + [
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc[:200]}">',
        f'<meta property="og:image" content="{og_image}">',
        f'<meta property="og:url" content="{url}">',
        '<meta property="og:type" content="article">',
        '<meta property="og:site_name" content="Ima Claw Blog">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc[:200]}">',
        f'<meta name="twitter:image" content="{og_image}">',
        jsonld,
    ]
    return "\n".join(lines)


def patch_file(slug, meta):
    path = os.path.join(BLOG_DIR, slug)
    if not os.path.exists(path):
        print(f"  ⚠️  NOT FOUND: {slug}")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already fully patched
    if 'rel="canonical"' in content and 'name="keywords"' in content and 'og:title' in content and 'application/ld+json' in content:
        print(f"  ✅ Already patched: {slug}")
        return

    seo_block = build_seo_block(slug, meta)

    # Insert after the last existing meta tag before </head> or before <link rel="stylesheet"
    # Find insertion point: after <meta name="description" ...>
    insert_after = re.search(r'(<meta name="description"[^>]*>)', content)
    if insert_after:
        pos = insert_after.end()
        # Remove any existing partial SEO tags to avoid duplicates
        for pattern in [
            r'\n<meta name="keywords"[^>]*>',
            r'\n<link rel="canonical"[^>]*>',
            r'\n<link rel="alternate"[^>]*>',
            r'\n<meta property="og:[^"]*"[^>]*>',
            r'\n<meta name="twitter:[^"]*"[^>]*>',
            r'\n<script type="application/ld\+json">.*?</script>',
        ]:
            content = re.sub(pattern, '', content, flags=re.DOTALL)

        # Re-find insertion point
        insert_after = re.search(r'(<meta name="description"[^>]*>)', content)
        if insert_after:
            pos = insert_after.end()
            content = content[:pos] + "\n" + seo_block + content[pos:]
    else:
        # Fallback: insert before </head>
        content = content.replace("</head>", seo_block + "\n</head>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ Patched: {slug}")


print(f"Processing {len(ARTICLES)} articles in {BLOG_DIR}...")
for slug, meta in ARTICLES.items():
    patch_file(slug, meta)
print("Done!")
