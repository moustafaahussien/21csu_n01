#!/usr/bin/env python3
"""Generate 6 program pages for the 21st Century Skills Unit website."""

import os
import json

OUTPUT_DIR = "/home/user/workspace/21st-century-skills/programs"

# Common head and scripts
HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{ar_name} | وحدة مهارات القرن 21</title>
  <meta name="description" content="{description}" />

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Tajawal:wght@300;400;500;700&display=swap" rel="stylesheet" />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400;500;600;700&display=swap" rel="stylesheet" />

  <!-- Styles -->
  <link rel="stylesheet" href="../css/style.css" />

  <!-- Favicon -->
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%23070b16'/><text x='50' y='65' font-size='50' font-weight='bold' text-anchor='middle' fill='%2306b6d4' font-family='sans-serif'>21</text></svg>" />
</head>
<body>

  <!-- Animated Background -->
  <div class="bg-dots"></div>

  <!-- Navbar -->
  <nav class="navbar" aria-label="القائمة الرئيسية">
    <div class="navbar-inner">
      <a href="../index.html" class="nav-logo">
        <div class="logo-placeholder">21</div>
        <div class="nav-logo-text">
          <span class="ar">وحدة مهارات القرن 21</span>
          <span class="en">21st Century Skills Unit</span>
        </div>
      </a>

      <ul class="nav-links">
        <li><a href="../index.html#home">الرئيسية</a></li>
        <li><a href="../index.html#about">عن الوحدة</a></li>
        <li><a href="../index.html#programs">البرامج</a></li>
        <li><a href="../index.html#why">لماذا الوحدة؟</a></li>
        <li><a href="../index.html#impact">الأثر والإنجاز</a></li>
        <li><a href="../index.html#gallery">المعرض</a></li>
      </ul>

      <div class="nav-actions">
        <button class="theme-toggle" data-theme-toggle aria-label="تبديل المظهر"></button>
        <button class="nav-toggle" aria-label="القائمة" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>
"""

# SVG icons for each program
ICONS = {
    "emotional-intelligence": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>',
    "scientific-research": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 2v6l-4 6v8h14v-8l-4-6V2"/><line x1="9" y1="2" x2="15" y2="2"/></svg>',
    "design-for-change": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0-1 19.96"/><path d="M12 2a14.5 14.5 0 0 1 1 19.96"/><path d="M2 12h20"/></svg>',
    "entrepreneurship": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "robotics-3d-printing": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>',
    "stem": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2v7.5"/><path d="M14 2v7.5"/><path d="M7 9.5h10"/><path d="M7 9.5v12.5h10V9.5"/><path d="M10 14h4"/></svg>',
}

PROGRAMS = [
    {
        "slug": "emotional-intelligence",
        "number": "01",
        "ar_name": "الذكاء العاطفي",
        "en_name": "Emotional Intelligence",
        "icon": "emotional-intelligence",
        "tagline": "اعرف نفسك • اختر نفسك • امنح نفسك",
        "description": "برنامج يبني وعي الطالب بذاته ومشاعره وينمي قدرته على إدارة انفعالاته وفهم الآخرين.",
        "about": "الذكاء العاطفي هو القدرة على التعرف على مشاعرنا ومشاعر الآخرين، وفهم أثرها، واستخدام هذا الفهم لتوجيه السلوك والتفاعلات. في هذا البرنامج، يتعلم الطلاب كيف يفهمون أنفسهم أعمق، وكيف يديرون انفعالاتهم في المواقف المختلفة، وكيف يبنون علاقات إيجابية مع من حولهم. البرنامج لا يقتصر على المعرفة النظرية، بل يرتبط بتجارب حقيقية يعيشها الطالب يومياً في المدرسة والبيت والمجتمع.",
        "why": "الذكاء العاطفي ليس مهارة ناعمة ثانوية — بل هو الأساس الذي تقوم عليه كل المهارات الأخرى. الطالب الذي يفهم مشاعره ويديرها يستطيع أن يتعلم أفضل، ويتعاون بفعالية، ويقود بثقة، ويتعامل مع التحديات دون أن ينهار. الأبحاث تؤكد أن الذكاء العاطفي يساهم بنسبة كبيرة في النجاح الأكاديمي والمهني والاجتماعي.",
        "objectives": [
            "تنمية الوعي الذاتي والقدرة على التعرف على المشاعر",
            "تطوير مهارات إدارة الانفعالات والضغوط",
            "بناء مهارات التعاطف وفهم وجهات نظر الآخرين",
            "تعزيز مهارات التواصل الفعال وبناء العلاقات",
            "تنمية القدرة على اتخاذ القرارات المسؤولة",
            "بناء مفهوم إيجابي للذات والثقة بالنفس",
        ],
        "outcomes": [
            "طالب واعٍ بمشاعره وقادر على التعبير عنها بشكل صحي",
            "قدرة على إدارة الغضب والقلق والضغط النفسي",
            "مهارات تعاطف وفهم لمشاعر الزملاء والمعلمين",
            "علاقات إيجابية وبناءة مع المحيط",
            "ثقة بالنفس وقدرة على القيادة والمبادرة",
            "صحة نفسية أفضل ومقاومة للتحديات",
        ],
        "journey": [
            "الوعي الذاتي — معرفة الذات والمشاعر",
            "إدارة الذات — تنظيم الانفعالات والسلوك",
            "الوعي الاجتماعي — فهم الآخرين والتعاطف",
            "إدارة العلاقات — بناء التواصل والتعاون",
            "التطبيق — ممارسة المهارات في مواقف حقيقية",
        ],
        "activities": [
            "ورش التعبير عن المشاعر بالفن والكتابة",
            "تمارين التأمل والاسترخاء والوعي الذاتي",
            "أدوار تمثيلية لمواقف اجتماعية متنوعة",
            "مشاريع خدمة مجتمعية تعزز التعاطف",
            "جلسات نقاشية مفتوحة حول التحديات",
            "يوميات الانعكاس الذاتي والتقييم المستمر",
        ],
        "projects": [
            "مشروع «رسالة لذاتي» — رسائل إيجابية للنفس",
            "مشروع «فهم الآخر» — دراسة تجارب مختلفة",
            "مبادرة «ال kindness Challenge» — تحدي اللطف",
            "مشروع «خريطة المشاعر» — تتبع وتحليل المشاعر",
        ],
    },
    {
        "slug": "scientific-research",
        "number": "02",
        "ar_name": "البحث العلمي",
        "en_name": "Scientific Research",
        "icon": "scientific-research",
        "tagline": "اسأل • استقصِ • حلّل • استنتج",
        "description": "برنامج يحول فضول الطالب إلى بحث علمي منظم يخدم المجتمع ويصنع المعرفة.",
        "about": "البحث العلمي برنامج يعلّم الطلاب منهجية التفكير العلمي — من طرح الأسئلة وتكوين الفرضيات، إلى جمع البيانات وتحليلها، ثم الوصول إلى الاستنتاجات وعرضها. يتحول الطالب من متلقٍ للمعرفة إلى باحث يصنعها، ويكتشف أن العلم ليس مجرد معلومات في كتاب، بل عملية حية للبحث والاكتشاف وحل المشكلات.",
        "why": "في عصر تتدفق فيه المعلومات من كل جهة، أصبحت القدرة على البحث والتحليل والتمييز بين الحقائق والادعاءات مهارة بقاء. البحث العلمي يعلّم الطالب كيف يفكر نقدياً، وكيف يبني المعرفة بالأدلة، وكيف يقدم حلولاً مبنية على بيانات لا على آراء. هذه المهارات أساسية للنجاح في أي مجال في المستقبل.",
        "objectives": [
            "تنمية مهارات طرح الأسئلة العلمية",
            "تعلّم منهجية البحث العلمي خطوة بخطوة",
            "تطوير مهارات جمع البيانات وتحليلها",
            "بناء القدرة على تكوين الفرضيات واختبارها",
            "تنمية مهارات كتابة التقارير وعرض النتائج",
            "ربط البحث العلمي بحل المشكلات الواقعية",
        ],
        "outcomes": [
            "طالب قادر على طرح أسئلة بحثية واضحة",
            "إتقان منهجية البحث العلمي الأساسية",
            "مهارات تحليل البيانات واستخراج الاستنتاجات",
            "قدرة على كتابة تقارير علمية منظمة",
            "مهارات عرض تقديمي للمشاريع البحثية",
            "تفكير نقدي قائم على الأدلة والمنطق",
        ],
        "journey": [
            "الفضول — طرح الأسئلة والملاحظة",
            "الفرضية — تكوين توقعات قابلة للاختبار",
            "الاستقصاء — تصميم وتنفيذ التجارب",
            "التحليل — معالجة البيانات واستخراج النتائج",
            "العرض — مشاركة النتائج والاستنتاجات",
        ],
        "activities": [
            "ورش صياغة الأسئلة البحثية",
            "تجارب علمية عملية في المعمل",
            "جمع البيانات الميدانية واستبيانات",
            "تحليل البيانات باستخدام أدوات مناسبة",
            "كتابة التقارير والعروض التقديمية",
            "زيارات للمراكز البحثية والمختبرات",
        ],
        "projects": [
            "مشروع بحث علمي كامل من الفكرة للعرض",
            "دراسة ميدانية لظاهرة في المجتمع المحلي",
            "تجربة معملية مع تحليل البيانات",
            "عرض تقديمي في معرض البحث العلمي",
        ],
    },
    {
        "slug": "design-for-change",
        "number": "03",
        "ar_name": "التصميم من أجل التغيير",
        "en_name": "Design for Change",
        "icon": "design-for-change",
        "tagline": "أحس • تخيّل • نفّذ • شارك",
        "description": "برنامج يمكّن الطلاب من تحديد المشكلات وتصميم حلول مبتكرة تصنع أثراً إيجابياً.",
        "about": "التصميم من أجل التغيير منهجية عالمية تتبع مساراً من أربع خطوات: الإحساس بالمشكلة، تخيل الحلول، تنفيذ الفكرة، ومشاركة الأثر. البرنامج ينقل الطالب من الشكوى إلى الفعل، ومن الانتظار إلى المبادرة. يتعلم الطلاب كيف يحددون مشكلة حقيقية في محيطهم، ويصممون حلاً مبتكراً لها، ثم ينفذونه ويشاركونه مع المجتمع.",
        "why": "العالم لا يحتاج إلى من يشتكي من المشكلات، بل إلى من يحلها. هذا البرنامج يعلّم الطلاب أنهم قادرون على إحداث تغيير حقيقي، مهما كانوا صغاراً. يبنى ثقة بالنفس ومهارات القيادة والمبادرة، ويوضح أن التعلم ليس في الفصل فقط — بل في حل مشكلات حقيقية تخدم الناس.",
        "objectives": [
            "تنمية حس الملاحظة واكتشاف المشكلات",
            "تطوير مهارات التفكير الإبداعي والحلول",
            "تعلّم منهجية التصميم من أجل التغيير",
            "بناء مهارات التخطيط والتنفيذ",
            "تنمية مهارات العرض والتواصل",
            "تعزيز روح المبادرة والقيادة",
        ],
        "outcomes": [
            "طالب قادر على تحديد المشكلات في محيطه",
            "مهارات توليد أفكار إبداعية وحلول مبتكرة",
            "قدرة على تخطيط وتنفيذ المشاريع",
            "مهارات عرض ومشاركة الأثر",
            "روح مبادرة وقيادية",
            "وعي بمسؤوليته تجاه المجتمع",
        ],
        "journey": [
            "الإحساس — اكتشاف المشكلة",
            "التخيل — توليد الحلول المبتكرة",
            "التنفيذ — بناء الحل وتطبيقه",
            "المشاركة — عرض الأثر وإلهام الآخرين",
        ],
        "activities": [
            "جولات ميدانية لرصد المشكلات",
            "ورش العصف الذهني وتوليد الأفكار",
            "تدريبات النماذج الأولية السريعة",
            "تنفيذ مشاريع تغيير حقيقية",
            "أيام العرض والمشاركة مع المجتمع",
            "زيارات لمبادرات ومشاريع ملهمة",
        ],
        "projects": [
            "مشروع تغيير كامل من الإحساس للمشاركة",
            "مبادرة لتحسين بيئة المدرسة",
            "حملة توعوية لقضية مجتمعية",
            "حل مبتكر لمشكلة يواجهها الطلاب",
        ],
    },
    {
        "slug": "entrepreneurship",
        "number": "04",
        "ar_name": "ريادة الأعمال",
        "en_name": "Entrepreneurship",
        "icon": "entrepreneurship",
        "tagline": "أفكار • فرص • حلول • قيمة",
        "description": "برنامج ينقل الطالب من الفكرة إلى المشروع — من اكتشاف الفرص إلى بناء الحلول ذات القيمة.",
        "about": "ريادة الأعمال ليست مجرد تأسيس شركات — بل عقلية. عقلية تبحث عن الفرص في المشكلات، وتحوّل الأفكار إلى حلول ذات قيمة. في هذا البرنامج، يتعلم الطلاب كيف يكتشفون الحاجات، ويولّدون أفكاراً تجارية، ويبنون نماذج أولية، ويقدّمون عروضاً استثمارية. البرنامج يربط بين الإبداع والواقع، وبين الفكرة والتنفيذ.",
        "why": "مستقبل الاقتصاد يعتمد على رواد الأعمال والابتكار. تعليم ريادة الأعمال في سن مبكرة يبني عقلية المبادرة والمسؤولية والابتكار. الطالب الذي يجرّب بناء مشروع — حتى لو صغيراً — يكتسب مهارات لا يقدمها أي منهج تقليدي: التفكير الاستراتيجي، إدارة الموارد، التسويق، العمل الجماعي، والقدرة على التعامل مع الفشل والتعلم منه.",
        "objectives": [
            "تنمية عقلية ريادة الأعمال والابتكار",
            "تطوير مهارات اكتشاف الفرص والحاجات",
            "تعلّم بناء نماذج أولية وتطوير المنتجات",
            "بناء مهارات العرض الاستثماري",
            "تنمية مهارات العمل الجماعي والقيادة",
            "فهم أساسيات التسويق وإدارة الموارد",
        ],
        "outcomes": [
            "طالب يفكر بعقلية ريادية وابتكارية",
            "قدرة على تحويل الأفكار إلى مشاريع",
            "مهارات بناء نماذج أولية واختبارها",
            "مهارات عرض وتسويق المشاريع",
            "فهم أساسيات نموذج العمل التجاري",
            "قدرة على العمل ضمن فريق ريادي",
        ],
        "journey": [
            "الاكتشاف — رصد الفرص والحاجات",
            "الفكرة — توليد الأفكار واختيار الأفضل",
            "النموذج — بناء نموذج أولي قابل للتطبيق",
            "العرض — تقديم المشروع للمستثمرين",
            "الإطلاق — تشغيل المشروع وقياس الأثر",
        ],
        "activities": [
            "ورش اكتشاف الفرص والتحليل السوقي",
            "تدريبات العصف الذهني للأفكار",
            "بناء نماذج أولية بالمواد المتاحة",
            "يوم العرض الاستثماري (Pitch Day)",
            "زيارات لشركات ناشئة ورواد أعمال",
            "محاكاة إدارة مشروع صغير",
        ],
        "projects": [
            "بناء مشروع ريادي كامل من الفكرة للإطلاق",
            "نموذج عمل تجاري لمنتج مبتكر",
            "عرض استثماري احترافي (Pitch)",
            "سوق المشاريع الطلابية",
        ],
    },
    {
        "slug": "robotics-3d-printing",
        "number": "05",
        "ar_name": "الروبوت والطباعة ثلاثية الأبعاد",
        "en_name": "Robotics & 3D Printing",
        "icon": "robotics-3d-printing",
        "tagline": "برمج • صمّم • ابنِ • اصنع",
        "description": "برنامج يدمج البرمجة والهندسة والتصميم والتصنيع الرقمي لجعل الطالب صانعاً للتكنولوجيا.",
        "about": "في عالم تسيطر عليه التكنولوجيا، لا يكفي أن نعلّم الطلاب كيف يستخدمونها — بل كيف يصنعونها. برنامج الروبوت والطباعة ثلاثية الأبعاد يدمج البرمجة والهندسة والتصميم والتصنيع الرقمي في تجارب عملية ومثيرة. يتعلم الطلاب كيف يبنون روبوتات ويبرمجونها، وكيف يصممون نماذج ثلاثية الأبعاد ويطبعونها، محولين أفكارهم من الشاشة إلى الواقع.",
        "why": "الروبوتات والتصنيع الرقمي يشكلان مستقبل الصناعة والابتكار. الطالب الذي يتعلم كيف يصمم ويبني ويبرمج يكتسب مهارات القرن 21 الأساسية: التفكير الحاسوبي، حل المشكلات الهندسية، الإبداع التقني، والقدرة على تحويل الأفكار إلى منتجات ملموسة. هذا البرنامج يجعل الطالب صانعاً ومبتكراً، لا مجرد مستهلك للتكنولوجيا.",
        "objectives": [
            "تعلّم أساسيات البرمجة والتفكير الحاسوبي",
            "بناء وتجميع الروبوتات وبرمجتها",
            "تطوير مهارات التصميم ثلاثي الأبعاد",
            "إتقان استخدام الطابعات ثلاثية الأبعاد",
            "ربط التكنولوجيا بحل المشكلات الواقعية",
            "تنمية مهارات العمل الجماعي والهندسي",
        ],
        "outcomes": [
            "طالب قادر على بناء وبرمجة الروبوتات",
            "مهارات تصميم نماذج ثلاثية الأبعاد",
            "قدرة على استخدام الطابعات ثلاثية الأبعاد",
            "فهم أساسيات التفكير الحاسوبي",
            "مهارات حل المشكلات الهندسية",
            "قدرة على تحويل الأفكار إلى منتجات ملموسة",
        ],
        "journey": [
            "الأساس — تعلّم البرمجة والمنطق",
            "البناء — تجميع الروبوت وتشغيله",
            "التصميم — نمذجة ثلاثية الأبعاد",
            "التصنيع — الطباعة والإنتاج",
            "الابتكار — مشروع متكامل يجمع المهارات",
        ],
        "activities": [
            "ورش البرمجة الأساسية والمتقدمة",
            "تجميع وبرمجة الروبوتات التعليمية",
            "تدريبات التصميم ثلاثي الأبعاد",
            "جلسات الطباعة ثلاثية الأبعاد العملية",
            "تحديات الروبوت والمسابقات",
            "مشاريع تصنيع رقمي متكاملة",
        ],
        "projects": [
            "بناء وبرمجة روبوت كامل",
            "تصميم وطباعة نموذج ثلاثي الأبعاد",
            "مشروع حل مشكلة بالروبوت والتقنية",
            "المشاركة في مسابقة الروبوت",
        ],
    },
    {
        "slug": "stem",
        "number": "06",
        "ar_name": "STEM",
        "en_name": "STEM Education",
        "icon": "stem",
        "tagline": "علوم • تكنولوجيا • هندسة • رياضيات",
        "description": "بيئة تعليمية تكاملية تجمع العلوم والتكنولوجيا والهندسة والرياضيات في مشروعات واقعية.",
        "about": "STEM ليس مجرد اختصار لأربع مواد — بل فلسفة تعليمية تكاملية تكسر الحدود بين التخصصات. في بيئة STEM، لا يتعلم الطلاب العلوم والرياضيات بشكل منفصل، بل يوظفونها معاً لحل مشكلات وتحديات واقعية. البرنامج يبني التفكير العلمي والهندسي، ويجعل التعلم تجربة عملية ومترابطة وقابلة للتطبيق.",
        "why": "أكثر المهن طلباً في المستقبل تتطلب فهماً تكاملياً للعلوم والتكنولوجيا والهندسة والرياضيات. تعليم STEM يربط بين المعرفة النظرية والتطبيق العملي، ويجعل الطلاب يرون كيف ترتبط المواد الدراسية ببعضها وبالواقع. هذا النهج يبني مهارات حل المشكلات والابتكار والتفكير التحليلي — مهارات لا غنى عنها في اقتصاد المستقبل.",
        "objectives": [
            "تطوير التفكير العلمي والهندسي المتكامل",
            "ربط العلوم والرياضيات بالتطبيق العملي",
            "بناء مهارات حل المشكلات الواقعية",
            "تنمية مهارات البحث والتجريب",
            "تعزيز العمل الجماعي متعدد التخصصات",
            "تطوير مهارات التحليل والتفكير النقدي",
        ],
        "outcomes": [
            "طالب يفهم الترابط بين العلوم والرياضيات والتكنولوجيا",
            "قدرة على تطبيق المعرفة في مشاريع واقعية",
            "مهارات تفكير علمي وهندسي",
            "قدرة على العمل في فرق متكاملة",
            "مهارات بحث وتجريب وتحليل",
            "استعداد لمسارات أكاديمية ومهنية في مجالات STEM",
        ],
        "journey": [
            "التحدي — استقبال مشكلة أو سؤال واقعي",
            "الاستكشاف — بحث وتجريب وتحليل",
            "التصميم — بناء حل أو نموذج",
            "الاختبار — تجربة الحل وتقييمه",
            "العرض — مشاركة النتائج والتحسين",
        ],
        "activities": [
            "مشاريع STEM متكاملة ومتعددة التخصصات",
            "تجارب علمية وهندسية عملية",
            "تحديات بناء وحل مشكلات",
            "زيارات للمراكز العلمية والتقنية",
            "ورش تجمع بين العلوم والتكنولوجيا",
            "مسابقات STEM ومعارض المشاريع",
        ],
        "projects": [
            "مشروع STEM متكامل يحل مشكلة واقعية",
            "تجربة علمية هندسية مع تحليل بيانات",
            "بناء نموذج يجمع بين العلوم والرياضيات",
            "عرض في معرض STEM السنوي",
        ],
    },
]


def generate_program_page(program):
    """Generate a single program page HTML."""
    slug = program["slug"]
    icon_svg = ICONS.get(program["icon"], ICONS["stem"])

    objectives_html = "\n          ".join(f"<li>{o}</li>" for o in program["objectives"])
    outcomes_html = "\n          ".join(f"<li>{o}</li>" for o in program["outcomes"])
    journey_html = "\n          ".join(f"<li>{j}</li>" for j in program["journey"])
    activities_html = "\n          ".join(f"<li>{a}</li>" for a in program["activities"])
    projects_html = "\n          ".join(f"<li>{p}</li>" for p in program["projects"])

    html = HEAD_TEMPLATE.format(
        ar_name=program["ar_name"],
        description=program["description"],
    )

    html += f"""
  <!-- Program Hero -->
  <section class="program-hero">
    <div class="hero-bg"><canvas></canvas></div>
    <div class="program-hero-content">
      <div class="hero-eyebrow">برنامج {program['number']} · Program {program['number']}</div>
      <h1>{program['ar_name']}</h1>
      <div class="en-title">{program['en_name']}</div>
      <p class="tagline">{program['tagline']}</p>
    </div>
    <div class="hero-scroll">
      <span>اكتشف البرنامج</span>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
    </div>
  </section>

  <!-- About -->
  <section class="program-section">
    <div class="container container-narrow">
      <div class="program-section-header">
        <div class="en">About the Program</div>
        <h2>عن البرنامج</h2>
      </div>
      <div class="program-content">
        <p>{program['about']}</p>
      </div>
    </div>
  </section>

  <!-- Why It Matters -->
  <section class="program-section">
    <div class="container container-narrow">
      <div class="program-section-header">
        <div class="en">Why It Matters</div>
        <h2>لماذا نُدرّس هذا البرنامج؟</h2>
      </div>
      <div class="program-content">
        <p>{program['why']}</p>
      </div>
    </div>
  </section>

  <!-- Objectives -->
  <section class="program-section">
    <div class="container">
      <div class="program-section-header">
        <div class="en">Objectives</div>
        <h2>الأهداف</h2>
      </div>
      <ul class="program-list">
        {objectives_html}
      </ul>
    </div>
  </section>

  <!-- Student Outcomes -->
  <section class="program-section">
    <div class="container">
      <div class="program-section-header">
        <div class="en">Student Outcomes</div>
        <h2>مخرجات تعلّم الطالب</h2>
      </div>
      <ul class="program-list">
        {outcomes_html}
      </ul>
    </div>
  </section>

  <!-- Learning Journey -->
  <section class="program-section">
    <div class="container">
      <div class="program-section-header">
        <div class="en">Learning Journey</div>
        <h2>رحلة التعلّم</h2>
      </div>
      <ul class="program-list">
        {journey_html}
      </ul>
    </div>
  </section>

  <!-- Activities -->
  <section class="program-section">
    <div class="container">
      <div class="program-section-header">
        <div class="en">Activities</div>
        <h2>الأنشطة</h2>
      </div>
      <ul class="program-list">
        {activities_html}
      </ul>
    </div>
  </section>

  <!-- Projects -->
  <section class="program-section">
    <div class="container">
      <div class="program-section-header">
        <div class="en">Projects</div>
        <h2>المشاريع</h2>
      </div>
      <ul class="program-list">
        {projects_html}
      </ul>
    </div>
  </section>

  <!-- Gallery Placeholder -->
  <section class="program-section">
    <div class="container">
      <div class="program-section-header">
        <div class="en">Gallery</div>
        <h2>معرض الصور والفيديوهات</h2>
      </div>
      <div class="gallery-grid gallery-grid-3">
        <div class="gallery-item">
          <div class="gallery-item-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>
            <span>صورة — {program['ar_name']}</span>
          </div>
        </div>
        <div class="gallery-item">
          <div class="gallery-item-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
            <span>فيديو — نشاط</span>
          </div>
        </div>
        <div class="gallery-item">
          <div class="gallery-item-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>
            <span>صورة — مشروع</span>
          </div>
        </div>
        <div class="gallery-item">
          <div class="gallery-item-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>
            <span>صورة — إنجاز</span>
          </div>
        </div>
        <div class="gallery-item">
          <div class="gallery-item-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
            <span>فيديو — عرض</span>
          </div>
        </div>
        <div class="gallery-item">
          <div class="gallery-item-placeholder">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>
            <span>صورة — فعالية</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Back to Programs -->
  <section class="program-back">
    <div class="container">
      <a href="../index.html#programs" class="btn btn-ghost">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        العودة لمنظومة البرامج
      </a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-logo">
            <div class="logo-placeholder">21</div>
            <div class="nav-logo-text">
              <span class="ar">وحدة مهارات القرن 21</span>
              <span class="en">21st Century Skills Unit</span>
            </div>
          </div>
          <p>منظومة تعليمية متكاملة تبني مهارات المستقبل — من الذكاء العاطفي إلى التصنيع الرقمي.</p>
        </div>

        <div class="footer-col">
          <h4>روابط سريعة</h4>
          <ul>
            <li><a href="../index.html#home">الرئيسية</a></li>
            <li><a href="../index.html#about">عن الوحدة</a></li>
            <li><a href="../index.html#programs">البرامج</a></li>
            <li><a href="../index.html#gallery">المعرض</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>البرامج</h4>
          <ul>
            <li><a href="emotional-intelligence.html">الذكاء العاطفي</a></li>
            <li><a href="scientific-research.html">البحث العلمي</a></li>
            <li><a href="design-for-change.html">التصميم للتغيير</a></li>
            <li><a href="entrepreneurship.html">ريادة الأعمال</a></li>
            <li><a href="robotics-3d-printing.html">الروبوت والطباعة</a></li>
            <li><a href="stem.html">STEM</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>تواصل معنا</h4>
          <ul>
            <li><a href="#">البريد الإلكتروني</a></li>
            <li><a href="#">الموقع الإلكتروني</a></li>
            <li><a href="#">وسائل التواصل</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <span>© 2026 وحدة مهارات القرن 21 — جميع الحقوق محفوظة</span>
        <span>Empowering Students for the Future</span>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="../js/main.js"></script>
</body>
</html>
"""
    return html


# Generate all program pages
for program in PROGRAMS:
    html = generate_program_page(program)
    filepath = os.path.join(OUTPUT_DIR, f"{program['slug']}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {filepath}")

print(f"\nDone! Generated {len(PROGRAMS)} program pages.")
