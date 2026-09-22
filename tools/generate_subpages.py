#!/usr/bin/env python3
"""Generate 6 self-contained program subpages matching the index.html design exactly."""

import os, json

OUTPUT_DIR = "/home/user/workspace/21st-century-skills/programs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PROGRAMS = [
    {
        "slug": "emotional-intelligence", "number": "01",
        "ar_name": "الذكاء العاطفي", "en_name": "Emotional Intelligence",
        "color": "#FF4D8D",
        "icon": '<path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6C19 16.5 12 21 12 21z"/>',
        "ar_tagline": "اعرف نفسك • اختر نفسك • امنح نفسك",
        "en_tagline": "Know Yourself • Choose Yourself • Give Yourself",
        "ar_desc": "بناء وعي الطالب بذاته ومشاعره، وتنمية قدرته على إدارة انفعالاته وفهم الآخرين وبناء علاقات أكثر إيجابية.",
        "en_desc": "Building students' awareness of themselves and their emotions, and developing their ability to manage feelings, understand others, and build more positive relationships.",
        "ar_about": "الذكاء العاطفي هو القدرة على التعرف على مشاعرنا ومشاعر الآخرين، وفهم أثرها، واستخدام هذا الفهم لتوجيه السلوك والتفاعلات. في هذا البرنامج، يتعلم الطلاب كيف يفهمون أنفسهم أعمق، وكيف يديرون انفعالاتهم في المواقف المختلفة، وكيف يبنون علاقات إيجابية مع من حولهم. البرنامج لا يقتصر على المعرفة النظرية، بل يرتبط بتجارب حقيقية يعيشها الطالب يومياً في المدرسة والبيت والمجتمع.",
        "en_about": "Emotional Intelligence is the ability to recognize our own feelings and those of others, understand their impact, and use this understanding to guide behavior and interactions. In this program, students learn to understand themselves more deeply, manage their emotions in different situations, and build positive relationships with those around them.",
        "ar_why": "الذكاء العاطفي ليس مهارة ناعمة ثانوية — بل هو الأساس الذي تقوم عليه كل المهارات الأخرى. الطالب الذي يفهم مشاعره ويديرها يستطيع أن يتعلم أفضل، ويتعاون بفعالية، ويقود بثقة، ويتعامل مع التحديات دون أن ينهار. الأبحاث تؤكد أن الذكاء العاطفي يساهم بنسبة كبيرة في النجاح الأكاديمي والمهني والاجتماعي.",
        "en_why": "Emotional Intelligence is not a soft secondary skill — it is the foundation upon which all other skills are built. A student who understands and manages their emotions can learn better, collaborate effectively, lead with confidence, and face challenges without breaking down. Research confirms that emotional intelligence contributes significantly to academic, professional, and social success.",
        "ar_objectives": [
            "تنمية الوعي الذاتي والقدرة على التعرف على المشاعر",
            "تطوير مهارات إدارة الانفعالات والضغوط",
            "بناء مهارات التعاطف وفهم وجهات نظر الآخرين",
            "تعزيز مهارات التواصل الفعال وبناء العلاقات",
            "تنمية القدرة على اتخاذ القرارات المسؤولة",
            "بناء مفهوم إيجابي للذات والثقة بالنفس",
        ],
        "en_objectives": [
            "Developing self-awareness and the ability to recognize emotions",
            "Developing emotion and stress management skills",
            "Building empathy and understanding others' perspectives",
            "Enhancing effective communication and relationship-building",
            "Developing the ability to make responsible decisions",
            "Building a positive self-concept and self-confidence",
        ],
        "ar_outcomes": [
            "طالب واعٍ بمشاعره وقادر على التعبير عنها بشكل صحي",
            "قدرة على إدارة الغضب والقلق والضغط النفسي",
            "مهارات تعاطف وفهم لمشاعر الزملاء والمعلمين",
            "علاقات إيجابية وبناءة مع المحيط",
            "ثقة بالنفس وقدرة على القيادة والمبادرة",
            "صحة نفسية أفضل ومقاومة للتحديات",
        ],
        "en_outcomes": [
            "A student aware of their emotions and able to express them healthily",
            "Ability to manage anger, anxiety, and psychological pressure",
            "Empathy skills and understanding of peers' and teachers' feelings",
            "Positive and constructive relationships with their environment",
            "Self-confidence and ability to lead and take initiative",
            "Better mental health and resilience to challenges",
        ],
        "ar_journey": [
            "الوعي الذاتي — معرفة الذات والمشاعر",
            "إدارة الذات — تنظيم الانفعالات والسلوك",
            "الوعي الاجتماعي — فهم الآخرين والتعاطف",
            "إدارة العلاقات — بناء التواصل والتعاون",
            "التطبيق — ممارسة المهارات في مواقف حقيقية",
        ],
        "en_journey": [
            "Self-Awareness — knowing oneself and emotions",
            "Self-Management — regulating emotions and behavior",
            "Social Awareness — understanding others and empathy",
            "Relationship Management — building communication and cooperation",
            "Application — practicing skills in real situations",
        ],
        "ar_activities": [
            "ورش التعبير عن المشاعر بالفن والكتابة",
            "تمارين التأمل والاسترخاء والوعي الذاتي",
            "أدوار تمثيلية لمواقف اجتماعية متنوعة",
            "مشاريع خدمة مجتمعية تعزز التعاطف",
            "جلسات نقاشية مفتوحة حول التحديات",
            "يوميات الانعكاس الذاتي والتقييم المستمر",
        ],
        "en_activities": [
            "Workshops on expressing emotions through art and writing",
            "Meditation, relaxation, and self-awareness exercises",
            "Role-playing diverse social situations",
            "Community service projects that enhance empathy",
            "Open discussion sessions about challenges",
            "Self-reflection journals and continuous assessment",
        ],
        "ar_projects": [
            "مشروع «رسالة لذاتي» — رسائل إيجابية للنفس",
            "مشروع «فهم الآخر» — دراسة تجارب مختلفة",
            "مبادرة «ال Kindness Challenge» — تحدي اللطف",
            "مشروع «خريطة المشاعر» — تتبع وتحليل المشاعر",
        ],
        "en_projects": [
            "Project 'A Letter to Myself' — positive self-messages",
            "Project 'Understanding Others' — studying diverse experiences",
            "Initiative 'Kindness Challenge'",
            "Project 'Emotion Map' — tracking and analyzing emotions",
        ],
    },
    {
        "slug": "scientific-research", "number": "02",
        "ar_name": "البحث العلمي", "en_name": "Scientific Research",
        "color": "#16B8E0",
        "icon": '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l6 6"/>',
        "ar_tagline": "اسأل • استقصِ • حلّل • استنتج",
        "en_tagline": "Ask • Investigate • Analyze • Conclude",
        "ar_desc": "تحويل فضول الطالب إلى أسئلة، والأسئلة إلى بحث، والبحث إلى معرفة وحلول.",
        "en_desc": "Turning students' curiosity into questions, questions into research, and research into knowledge and solutions.",
        "ar_about": "البحث العلمي برنامج يعلّم الطلاب منهجية التفكير العلمي — من طرح الأسئلة وتكوين الفرضيات، إلى جمع البيانات وتحليلها، ثم الوصول إلى الاستنتاجات وعرضها. يتحول الطالب من متلقٍ للمعرفة إلى باحث يصنعها، ويكتشف أن العلم ليس مجرد معلومات في كتاب، بل عملية حية للبحث والاكتشاف وحل المشكلات.",
        "en_about": "The Scientific Research program teaches students the methodology of scientific thinking — from formulating questions and hypotheses, to collecting and analyzing data, then reaching conclusions and presenting them. The student transforms from a receiver of knowledge to a researcher who creates it, discovering that science is not just information in a book, but a living process of inquiry, discovery, and problem-solving.",
        "ar_why": "في عصر تتدفق فيه المعلومات من كل جهة، أصبحت القدرة على البحث والتحليل والتمييز بين الحقائق والادعاءات مهارة بقاء. البحث العلمي يعلّم الطالب كيف يفكر نقدياً، وكيف يبني المعرفة بالأدلة، وكيف يقدم حلولاً مبنية على بيانات لا على آراء. هذه المهارات أساسية للنجاح في أي مجال في المستقبل.",
        "en_why": "In an age where information flows from every direction, the ability to research, analyze, and distinguish between facts and claims is a survival skill. Scientific research teaches students how to think critically, build knowledge with evidence, and present solutions based on data rather than opinions. These skills are essential for success in any field in the future.",
        "ar_objectives": [
            "تنمية مهارات طرح الأسئلة العلمية",
            "تعلّم منهجية البحث العلمي خطوة بخطوة",
            "تطوير مهارات جمع البيانات وتحليلها",
            "بناء القدرة على تكوين الفرضيات واختبارها",
            "تنمية مهارات كتابة التقارير وعرض النتائج",
            "ربط البحث العلمي بحل المشكلات الواقعية",
        ],
        "en_objectives": [
            "Developing skills in formulating scientific questions",
            "Learning the scientific research methodology step by step",
            "Developing data collection and analysis skills",
            "Building the ability to form and test hypotheses",
            "Developing report writing and result presentation skills",
            "Linking scientific research to real-world problem-solving",
        ],
        "ar_outcomes": [
            "طالب قادر على طرح أسئلة بحثية واضحة",
            "إتقان منهجية البحث العلمي الأساسية",
            "مهارات تحليل البيانات واستخراج الاستنتاجات",
            "قدرة على كتابة تقارير علمية منظمة",
            "مهارات عرض تقديمي للمشاريع البحثية",
            "تفكير نقدي قائم على الأدلة والمنطق",
        ],
        "en_outcomes": [
            "A student able to formulate clear research questions",
            "Mastering the basic scientific research methodology",
            "Data analysis and conclusion extraction skills",
            "Ability to write organized scientific reports",
            "Presentation skills for research projects",
            "Critical thinking based on evidence and logic",
        ],
        "ar_journey": [
            "الفضول — طرح الأسئلة والملاحظة",
            "الفرضية — تكوين توقعات قابلة للاختبار",
            "الاستقصاء — تصميم وتنفيذ التجارب",
            "التحليل — معالجة البيانات واستخراج النتائج",
            "العرض — مشاركة النتائج والاستنتاجات",
        ],
        "en_journey": [
            "Curiosity — asking questions and observation",
            "Hypothesis — forming testable predictions",
            "Investigation — designing and conducting experiments",
            "Analysis — processing data and extracting results",
            "Presentation — sharing results and conclusions",
        ],
        "ar_activities": [
            "ورش صياغة الأسئلة البحثية",
            "تجارب علمية عملية في المعمل",
            "جمع البيانات الميدانية واستبيانات",
            "تحليل البيانات باستخدام أدوات مناسبة",
            "كتابة التقارير والعروض التقديمية",
            "زيارات للمراكز البحثية والمختبرات",
        ],
        "en_activities": [
            "Workshops on formulating research questions",
            "Practical science experiments in the lab",
            "Field data collection and surveys",
            "Data analysis using appropriate tools",
            "Writing reports and presentations",
            "Visits to research centers and laboratories",
        ],
        "ar_projects": [
            "مشروع بحث علمي كامل من الفكرة للعرض",
            "دراسة ميدانية لظاهرة في المجتمع المحلي",
            "تجربة معملية مع تحليل البيانات",
            "عرض تقديمي في معرض البحث العلمي",
        ],
        "en_projects": [
            "A complete scientific research project from idea to presentation",
            "A field study of a phenomenon in the local community",
            "A lab experiment with data analysis",
            "A presentation at the science research fair",
        ],
    },
    {
        "slug": "design-for-change", "number": "03",
        "ar_name": "التصميم من أجل التغيير", "en_name": "Design for Change",
        "color": "#7BC62D",
        "icon": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
        "ar_tagline": "أحس • تخيّل • نفّذ • شارك",
        "en_tagline": "Feel • Imagine • Do • Share",
        "ar_desc": "تمكين الطلاب من تحديد المشكلات الحقيقية من حولهم، وتصميم حلول مبتكرة قابلة للتطبيق تُحدث أثرًا إيجابيًا.",
        "en_desc": "Empowering students to identify real problems around them and design innovative, feasible solutions that make a positive impact.",
        "ar_about": "التصميم من أجل التغيير منهجية عالمية تتبع مساراً من أربع خطوات: الإحساس بالمشكلة، تخيل الحلول، تنفيذ الفكرة، ومشاركة الأثر. البرنامج ينقل الطالب من الشكوى إلى الفعل، ومن الانتظار إلى المبادرة. يتعلم الطلاب كيف يحددون مشكلة حقيقية في محيطهم، ويصممون حلاً مبتكراً لها، ثم ينفذونه ويشاركونه مع المجتمع.",
        "en_about": "Design for Change is a global methodology that follows a four-step path: Feel the problem, Imagine solutions, Do the idea, and Share the impact. The program moves students from complaining to acting, from waiting to initiating. Students learn how to identify a real problem in their environment, design an innovative solution, then implement and share it with the community.",
        "ar_why": "العالم لا يحتاج إلى من يشتكي من المشكلات، بل إلى من يحلها. هذا البرنامج يعلّم الطلاب أنهم قادرون على إحداث تغيير حقيقي، مهما كانوا صغاراً. يبنى ثقة بالنفس ومهارات القيادة والمبادرة، ويوضح أن التعلم ليس في الفصل فقط — بل في حل مشكلات حقيقية تخدم الناس.",
        "en_why": "The world doesn't need people who complain about problems, but people who solve them. This program teaches students that they are capable of making real change, no matter how young they are. It builds self-confidence, leadership skills, and initiative, and shows that learning isn't just in the classroom — but in solving real problems that serve people.",
        "ar_objectives": [
            "تنمية حس الملاحظة واكتشاف المشكلات",
            "تطوير مهارات التفكير الإبداعي والحلول",
            "تعلّم منهجية التصميم من أجل التغيير",
            "بناء مهارات التخطيط والتنفيذ",
            "تنمية مهارات العرض والتواصل",
            "تعزيز روح المبادرة والقيادة",
        ],
        "en_objectives": [
            "Developing observation skills and problem discovery",
            "Developing creative thinking and solution skills",
            "Learning the Design for Change methodology",
            "Building planning and execution skills",
            "Developing presentation and communication skills",
            "Enhancing initiative and leadership spirit",
        ],
        "ar_outcomes": [
            "طالب قادر على تحديد المشكلات في محيطه",
            "مهارات توليد أفكار إبداعية وحلول مبتكرة",
            "قدرة على تخطيط وتنفيذ المشاريع",
            "مهارات عرض ومشاركة الأثر",
            "روح مبادرة وقيادية",
            "وعي بمسؤوليته تجاه المجتمع",
        ],
        "en_outcomes": [
            "A student able to identify problems in their environment",
            "Skills in generating creative ideas and innovative solutions",
            "Ability to plan and execute projects",
            "Presentation and impact-sharing skills",
            "Initiative and leadership spirit",
            "Awareness of their responsibility toward society",
        ],
        "ar_journey": [
            "الإحساس — اكتشاف المشكلة",
            "التخيل — توليد الحلول المبتكرة",
            "التنفيذ — بناء الحل وتطبيقه",
            "المشاركة — عرض الأثر وإلهام الآخرين",
        ],
        "en_journey": [
            "Feel — discovering the problem",
            "Imagine — generating innovative solutions",
            "Do — building and applying the solution",
            "Share — presenting the impact and inspiring others",
        ],
        "ar_activities": [
            "جولات ميدانية لرصد المشكلات",
            "ورش العصف الذهني وتوليد الأفكار",
            "تدريبات النماذج الأولية السريعة",
            "تنفيذ مشاريع تغيير حقيقية",
            "أيام العرض والمشاركة مع المجتمع",
            "زيارات لمبادرات ومشاريع ملهمة",
        ],
        "en_activities": [
            "Field tours to observe problems",
            "Brainstorming workshops and idea generation",
            "Rapid prototyping exercises",
            "Implementing real change projects",
            "Community showcase and sharing days",
            "Visits to inspiring initiatives and projects",
        ],
        "ar_projects": [
            "مشروع تغيير كامل من الإحساس للمشاركة",
            "مبادرة لتحسين بيئة المدرسة",
            "حملة توعوية لقضية مجتمعية",
            "حل مبتكر لمشكلة يواجهها الطلاب",
        ],
        "en_projects": [
            "A complete change project from Feel to Share",
            "An initiative to improve the school environment",
            "An awareness campaign for a social issue",
            "An innovative solution to a problem students face",
        ],
    },
    {
        "slug": "entrepreneurship", "number": "04",
        "ar_name": "ريادة الأعمال", "en_name": "Entrepreneurship",
        "color": "#FF9A1F",
        "icon": '<path d="M3 17l6-6 4 4 8-8M14 7h7v7"/>',
        "ar_tagline": "أفكار • فرص • حلول • قيمة",
        "en_tagline": "Ideas • Opportunities • Solutions • Value",
        "ar_desc": "نقل الطالب من التفكير في الأفكار إلى بناء الحلول، واكتشاف الفرص، وتحويل الأفكار إلى مشاريع ذات قيمة.",
        "en_desc": "Moving students from thinking about ideas to building solutions, discovering opportunities, and turning ideas into projects of value.",
        "ar_about": "ريادة الأعمال ليست مجرد تأسيس شركات — بل عقلية. عقلية تبحث عن الفرص في المشكلات، وتحوّل الأفكار إلى حلول ذات قيمة. في هذا البرنامج، يتعلم الطلاب كيف يكتشفون الحاجات، ويولّدون أفكاراً تجارية، ويبنون نماذج أولية، ويقدّمون عروضاً استثمارية. البرنامج يربط بين الإبداع والواقع، وبين الفكرة والتنفيذ.",
        "en_about": "Entrepreneurship is not just about starting companies — it's a mindset. A mindset that seeks opportunities in problems and turns ideas into valuable solutions. In this program, students learn how to discover needs, generate business ideas, build prototypes, and pitch to investors. The program bridges creativity and reality, between idea and execution.",
        "ar_why": "مستقبل الاقتصاد يعتمد على رواد الأعمال والابتكار. تعليم ريادة الأعمال في سن مبكرة يبني عقلية المبادرة والمسؤولية والابتكار. الطالب الذي يجرّب بناء مشروع — حتى لو صغيراً — يكتسب مهارات لا يقدمها أي منهج تقليدي: التفكير الاستراتيجي، إدارة الموارد، التسويق، العمل الجماعي، والقدرة على التعامل مع الفشل والتعلم منه.",
        "en_why": "The future of the economy depends on entrepreneurs and innovation. Teaching entrepreneurship at an early age builds a mindset of initiative, responsibility, and innovation. A student who tries building a project — even a small one — gains skills that no traditional curriculum offers: strategic thinking, resource management, marketing, teamwork, and the ability to deal with failure and learn from it.",
        "ar_objectives": [
            "تنمية عقلية ريادة الأعمال والابتكار",
            "تطوير مهارات اكتشاف الفرص والحاجات",
            "تعلّم بناء نماذج أولية وتطوير المنتجات",
            "بناء مهارات العرض الاستثماري",
            "تنمية مهارات العمل الجماعي والقيادة",
            "فهم أساسيات التسويق وإدارة الموارد",
        ],
        "en_objectives": [
            "Developing an entrepreneurial and innovation mindset",
            "Developing opportunity and need discovery skills",
            "Learning to build prototypes and develop products",
            "Building pitch and presentation skills",
            "Developing teamwork and leadership skills",
            "Understanding the basics of marketing and resource management",
        ],
        "ar_outcomes": [
            "طالب يفكر بعقلية ريادية وابتكارية",
            "قدرة على تحويل الأفكار إلى مشاريع",
            "مهارات بناء نماذج أولية واختبارها",
            "مهارات عرض وتسويق المشاريع",
            "فهم أساسيات نموذج العمل التجاري",
            "قدرة على العمل ضمن فريق ريادي",
        ],
        "en_outcomes": [
            "A student who thinks with an entrepreneurial and innovative mindset",
            "Ability to turn ideas into projects",
            "Skills in building and testing prototypes",
            "Project presentation and marketing skills",
            "Understanding the basics of business models",
            "Ability to work within an entrepreneurial team",
        ],
        "ar_journey": [
            "الاكتشاف — رصد الفرص والحاجات",
            "الفكرة — توليد الأفكار واختيار الأفضل",
            "النموذج — بناء نموذج أولي قابل للتطبيق",
            "العرض — تقديم المشروع للمستثمرين",
            "الإطلاق — تشغيل المشروع وقياس الأثر",
        ],
        "en_journey": [
            "Discovery — spotting opportunities and needs",
            "Idea — generating ideas and selecting the best",
            "Prototype — building a workable prototype",
            "Pitch — presenting the project to investors",
            "Launch — running the project and measuring impact",
        ],
        "ar_activities": [
            "ورش اكتشاف الفرص والتحليل السوقي",
            "تدريبات العصف الذهني للأفكار",
            "بناء نماذج أولية بالمواد المتاحة",
            "يوم العرض الاستثماري (Pitch Day)",
            "زيارات لشركات ناشئة ورواد أعمال",
            "محاكاة إدارة مشروع صغير",
        ],
        "en_activities": [
            "Opportunity discovery and market analysis workshops",
            "Brainstorming exercises for ideas",
            "Building prototypes with available materials",
            "Pitch Day — investment presentation",
            "Visits to startups and entrepreneurs",
            "Small project management simulation",
        ],
        "ar_projects": [
            "بناء مشروع ريادي كامل من الفكرة للإطلاق",
            "نموذج عمل تجاري لمنتج مبتكر",
            "عرض استثماري احترافي (Pitch)",
            "سوق المشاريع الطلابية",
        ],
        "en_projects": [
            "Building a complete entrepreneurial project from idea to launch",
            "A business model for an innovative product",
            "A professional pitch presentation",
            "A student projects marketplace",
        ],
    },
    {
        "slug": "robotics-3d-printing", "number": "05",
        "ar_name": "الروبوت والطباعة ثلاثية الأبعاد", "en_name": "Robotics & 3D Printing",
        "color": "#7B5CFF",
        "icon": '<rect x="4" y="8" width="16" height="11" rx="2"/><path d="M12 4v4M9 13h.01M15 13h.01M9 16h6"/>',
        "ar_tagline": "برمج • صمّم • ابنِ • اصنع",
        "en_tagline": "Code • Design • Build • Make",
        "ar_desc": "دمج البرمجة والهندسة والتصميم والتصنيع الرقمي في تجارب عملية تجعل الطالب صانعًا للتكنولوجيا وليس مجرد مستخدم لها.",
        "en_desc": "Integrating programming, engineering, design, and digital fabrication into hands-on experiences that make students creators of technology, not just users of it.",
        "ar_about": "في عالم تسيطر عليه التكنولوجيا، لا يكفي أن نعلّم الطلاب كيف يستخدمونها — بل كيف يصنعونها. برنامج الروبوت والطباعة ثلاثية الأبعاد يدمج البرمجة والهندسة والتصميم والتصنيع الرقمي في تجارب عملية ومثيرة. يتعلم الطلاب كيف يبنون روبوتات ويبرمجونها، وكيف يصممون نماذج ثلاثية الأبعاد ويطبعونها، محولين أفكارهم من الشاشة إلى الواقع.",
        "en_about": "In a world dominated by technology, it's not enough to teach students how to use it — but how to create it. The Robotics & 3D Printing program integrates programming, engineering, design, and digital fabrication into exciting hands-on experiences. Students learn how to build and program robots, and how to design and print 3D models, transforming their ideas from screen to reality.",
        "ar_why": "الروبوتات والتصنيع الرقمي يشكلان مستقبل الصناعة والابتكار. الطالب الذي يتعلم كيف يصمم ويبني ويبرمج يكتسب مهارات القرن 21 الأساسية: التفكير الحاسوبي، حل المشكلات الهندسية، الإبداع التقني، والقدرة على تحويل الأفكار إلى منتجات ملموسة. هذا البرنامج يجعل الطالب صانعاً ومبتكراً، لا مجرد مستهلك للتكنولوجيا.",
        "en_why": "Robotics and digital fabrication shape the future of industry and innovation. A student who learns to design, build, and program acquires essential 21st century skills: computational thinking, engineering problem-solving, technical creativity, and the ability to turn ideas into tangible products. This program makes the student a creator and innovator, not just a consumer of technology.",
        "ar_objectives": [
            "تعلّم أساسيات البرمجة والتفكير الحاسوبي",
            "بناء وتجميع الروبوتات وبرمجتها",
            "تطوير مهارات التصميم ثلاثي الأبعاد",
            "إتقان استخدام الطابعات ثلاثية الأبعاد",
            "ربط التكنولوجيا بحل المشكلات الواقعية",
            "تنمية مهارات العمل الجماعي والهندسي",
        ],
        "en_objectives": [
            "Learning programming fundamentals and computational thinking",
            "Building, assembling, and programming robots",
            "Developing 3D design skills",
            "Mastering the use of 3D printers",
            "Linking technology to real-world problem-solving",
            "Developing teamwork and engineering skills",
        ],
        "ar_outcomes": [
            "طالب قادر على بناء وبرمجة الروبوتات",
            "مهارات تصميم نماذج ثلاثية الأبعاد",
            "قدرة على استخدام الطابعات ثلاثية الأبعاد",
            "فهم أساسيات التفكير الحاسوبي",
            "مهارات حل المشكلات الهندسية",
            "قدرة على تحويل الأفكار إلى منتجات ملموسة",
        ],
        "en_outcomes": [
            "A student able to build and program robots",
            "3D model design skills",
            "Ability to use 3D printers",
            "Understanding computational thinking fundamentals",
            "Engineering problem-solving skills",
            "Ability to turn ideas into tangible products",
        ],
        "ar_journey": [
            "الأساس — تعلّم البرمجة والمنطق",
            "البناء — تجميع الروبوت وتشغيله",
            "التصميم — نمذجة ثلاثية الأبعاد",
            "التصنيع — الطباعة والإنتاج",
            "الابتكار — مشروع متكامل يجمع المهارات",
        ],
        "en_journey": [
            "Foundations — learning programming and logic",
            "Building — assembling and running the robot",
            "Design — 3D modeling",
            "Fabrication — printing and production",
            "Innovation — an integrated project combining all skills",
        ],
        "ar_activities": [
            "ورش البرمجة الأساسية والمتقدمة",
            "تجميع وبرمجة الروبوتات التعليمية",
            "تدريبات التصميم ثلاثي الأبعاد",
            "جلسات الطباعة ثلاثية الأبعاد العملية",
            "تحديات الروبوت والمسابقات",
            "مشاريع تصنيع رقمي متكاملة",
        ],
        "en_activities": [
            "Basic and advanced programming workshops",
            "Assembling and programming educational robots",
            "3D design training exercises",
            "Practical 3D printing sessions",
            "Robotics challenges and competitions",
            "Integrated digital fabrication projects",
        ],
        "ar_projects": [
            "بناء وبرمجة روبوت كامل",
            "تصميم وطباعة نموذج ثلاثي الأبعاد",
            "مشروع حل مشكلة بالروبوت والتقنية",
            "المشاركة في مسابقة الروبوت",
        ],
        "en_projects": [
            "Building and programming a complete robot",
            "Designing and printing a 3D model",
            "A project solving a problem with robotics and technology",
            "Participating in a robotics competition",
        ],
    },
    {
        "slug": "stem", "number": "06",
        "ar_name": "STEM", "en_name": "STEM Education",
        "color": "#10C38B",
        "icon": '<ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"/><circle cx="12" cy="12" r="1.4"/>',
        "ar_tagline": "علوم • تكنولوجيا • هندسة • رياضيات",
        "en_tagline": "Science • Technology • Engineering • Mathematics",
        "ar_desc": "بيئة تعليمية تكاملية تجمع العلوم والتكنولوجيا والهندسة والرياضيات في مشروعات وتحديات واقعية.",
        "en_desc": "An integrated learning environment that brings together science, technology, engineering, and mathematics in real-world projects and challenges.",
        "ar_about": "STEM ليس مجرد اختصار لأربع مواد — بل فلسفة تعليمية تكاملية تكسر الحدود بين التخصصات. في بيئة STEM، لا يتعلم الطلاب العلوم والرياضيات بشكل منفصل، بل يوظفونها معاً لحل مشكلات وتحديات واقعية. البرنامج يبني التفكير العلمي والهندسي، ويجعل التعلم تجربة عملية ومترابطة وقابلة للتطبيق.",
        "en_about": "STEM is not just an acronym for four subjects — it's an integrated educational philosophy that breaks down the boundaries between disciplines. In a STEM environment, students don't learn science and mathematics separately, but use them together to solve real-world problems and challenges. The program builds scientific and engineering thinking, making learning a practical, interconnected, and applicable experience.",
        "ar_why": "أكثر المهن طلباً في المستقبل تتطلب فهماً تكاملياً للعلوم والتكنولوجيا والهندسة والرياضيات. تعليم STEM يربط بين المعرفة النظرية والتطبيق العملي، ويجعل الطلاب يرون كيف ترتبط المواد الدراسية ببعضها وبالواقع. هذا النهج يبني مهارات حل المشكلات والابتكار والتفكير التحليلي — مهارات لا غنى عنها في اقتصاد المستقبل.",
        "en_why": "The most in-demand future professions require an integrated understanding of science, technology, engineering, and mathematics. STEM education connects theoretical knowledge with practical application, and lets students see how subjects relate to each other and to reality. This approach builds problem-solving, innovation, and analytical thinking skills — essential for the future economy.",
        "ar_objectives": [
            "تطوير التفكير العلمي والهندسي المتكامل",
            "ربط العلوم والرياضيات بالتطبيق العملي",
            "بناء مهارات حل المشكلات الواقعية",
            "تنمية مهارات البحث والتجريب",
            "تعزيز العمل الجماعي متعدد التخصصات",
            "تطوير مهارات التحليل والتفكير النقدي",
        ],
        "en_objectives": [
            "Developing integrated scientific and engineering thinking",
            "Linking science and mathematics to practical application",
            "Building real-world problem-solving skills",
            "Developing research and experimentation skills",
            "Enhancing multidisciplinary teamwork",
            "Developing analysis and critical thinking skills",
        ],
        "ar_outcomes": [
            "طالب يفهم الترابط بين العلوم والرياضيات والتكنولوجيا",
            "قدرة على تطبيق المعرفة في مشاريع واقعية",
            "مهارات تفكير علمي وهندسي",
            "قدرة على العمل في فرق متكاملة",
            "مهارات بحث وتجريب وتحليل",
            "استعداد لمسارات أكاديمية ومهنية في مجالات STEM",
        ],
        "en_outcomes": [
            "A student who understands the interconnection between science, math, and technology",
            "Ability to apply knowledge in real-world projects",
            "Scientific and engineering thinking skills",
            "Ability to work in integrated teams",
            "Research, experimentation, and analysis skills",
            "Readiness for academic and career paths in STEM fields",
        ],
        "ar_journey": [
            "التحدي — استقبال مشكلة أو سؤال واقعي",
            "الاستكشاف — بحث وتجريب وتحليل",
            "التصميم — بناء حل أو نموذج",
            "الاختبار — تجربة الحل وتقييمه",
            "العرض — مشاركة النتائج والتحسين",
        ],
        "en_journey": [
            "Challenge — receiving a real-world problem or question",
            "Exploration — research, experimentation, and analysis",
            "Design — building a solution or model",
            "Testing — trying the solution and evaluating it",
            "Presentation — sharing results and improving",
        ],
        "ar_activities": [
            "مشاريع STEM متكاملة ومتعددة التخصصات",
            "تجارب علمية وهندسية عملية",
            "تحديات بناء وحل مشكلات",
            "زيارات للمراكز العلمية والتقنية",
            "ورش تجمع بين العلوم والتكنولوجيا",
            "مسابقات STEM ومعارض المشاريع",
        ],
        "en_activities": [
            "Integrated multidisciplinary STEM projects",
            "Practical scientific and engineering experiments",
            "Building challenges and problem-solving",
            "Visits to scientific and technical centers",
            "Workshops combining science and technology",
            "STEM competitions and project exhibitions",
        ],
        "ar_projects": [
            "مشروع STEM متكامل يحل مشكلة واقعية",
            "تجربة علمية هندسية مع تحليل بيانات",
            "بناء نموذج يجمع بين العلوم والرياضيات",
            "عرض في معرض STEM السنوي",
        ],
        "en_projects": [
            "An integrated STEM project solving a real-world problem",
            "A scientific engineering experiment with data analysis",
            "Building a model combining science and mathematics",
            "A presentation at the annual STEM exhibition",
        ],
    },
]

# ── Shared CSS (from index.html, plus subpage additions) ──
SHARED_CSS = r"""
  :root{
    --bg:#F5F6FC;--ink:#14173A;--muted:#565D8C;
    --glass:rgba(255,255,255,.66);--glass-edge:rgba(255,255,255,.95);
    --line:rgba(60,70,160,.14);
    --violet:#6D4BFF;--cyan:#0EA5D6;--green:#0E9F76;--orange:#E8790A;--pink:#E63E7C;
    --foil:linear-gradient(100deg,#6D4BFF 0%,#0EA5D6 20%,#0E9F76 40%,#E8790A 60%,#E63E7C 80%,#6D4BFF 100%);
    --display:'Sora','Noto Kufi Arabic','IBM Plex Sans Arabic',Tahoma,sans-serif;
    --body:'IBM Plex Sans Arabic','Sora',Tahoma,sans-serif;
    --wrap:1200px;--start:right;--flip:1;--fx:-1;
  }
  html[dir="ltr"]{--start:left;--flip:-1;--fx:1}
  *{box-sizing:border-box;margin:0;padding:0}
  html{scroll-behavior:smooth;scroll-padding-top:100px;overflow-x:clip}
  body{font-family:var(--body);background:var(--bg);color:var(--ink);line-height:1.85;font-size:17px;-webkit-font-smoothing:antialiased;overflow-x:clip}
  a{color:inherit;text-decoration:none}
  button{font:inherit;color:inherit;cursor:pointer}
  :focus-visible{outline:3px solid var(--violet);outline-offset:3px;border-radius:10px}
  .wrap{max-width:var(--wrap);margin-inline:auto;padding-inline:24px}
  .aurora{position:fixed;inset:-25%;z-index:-1;pointer-events:none;
    background:radial-gradient(40% 35% at 20% 25%,rgba(109,75,255,.22),transparent 70%),
      radial-gradient(35% 30% at 80% 20%,rgba(14,165,214,.20),transparent 70%),
      radial-gradient(38% 34% at 72% 80%,rgba(230,62,124,.16),transparent 70%),
      radial-gradient(34% 30% at 15% 85%,rgba(232,121,10,.14),transparent 70%);
    animation:drift 28s ease-in-out infinite alternate}
  @keyframes drift{to{transform:translate3d(4%,3%,0) rotate(6deg) scale(1.08)}}
  .nav{position:fixed;top:12px;left:50%;transform:translateX(-50%);z-index:60;
    width:min(1200px,calc(100% - 24px));height:66px;padding-inline:16px 12px;
    display:flex;align-items:center;justify-content:space-between;gap:12px;
    background:var(--glass);backdrop-filter:blur(18px) saturate(1.4);-webkit-backdrop-filter:blur(18px) saturate(1.4);
    border:1px solid var(--glass-edge);border-radius:22px;
    box-shadow:0 12px 36px -16px rgba(40,50,140,.35)}
  .logos{display:flex;align-items:center;gap:12px}
  .logos .sep{width:1px;height:30px;background:var(--line)}
  .logo{position:relative;display:inline-flex;align-items:center;justify-content:center;height:44px;min-width:44px}
  .logo img{height:44px;width:auto;display:block}
  .logo .ph{display:none;font-size:11.5px;line-height:1.3;color:var(--muted);text-align:center;
    border:1.5px dashed rgba(60,70,160,.35);border-radius:11px;padding:5px 10px;white-space:nowrap}
  .logo.missing img{display:none}
  .logo.missing .ph{display:block}
  .nav-right{display:flex;align-items:center;gap:6px}
  .nav-links{display:flex;align-items:center;gap:2px}
  .nav-links a{padding:8px 14px;border-radius:14px;font-size:15px;color:var(--muted);transition:background .2s,color .2s;white-space:nowrap}
  .nav-links a:hover{background:rgba(109,75,255,.09);color:var(--ink)}
  .lang{direction:ltr;display:inline-flex;align-items:center;padding:3px;border:0;border-radius:14px;
    background:rgba(20,23,58,.07);font-family:'Sora',sans-serif;font-weight:600;font-size:13px}
  .lang span{padding:6px 12px;border-radius:11px;color:var(--muted);transition:background .2s,color .2s}
  html[lang="ar"] .lang [data-l="ar"],html[lang="en"] .lang [data-l="en"]{background:var(--ink);color:#fff}
  .burger{display:none;width:44px;height:40px;border:0;border-radius:14px;background:rgba(20,23,58,.07);flex-direction:column;justify-content:center;align-items:center;gap:5px}
  .burger i{display:block;width:18px;height:2px;border-radius:2px;background:var(--ink);transition:transform .25s,opacity .2s}
  .burger[aria-expanded="true"] i:nth-child(1){transform:translateY(7px) rotate(45deg)}
  .burger[aria-expanded="true"] i:nth-child(2){opacity:0}
  .burger[aria-expanded="true"] i:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
  .menu{position:fixed;top:86px;left:50%;transform:translateX(-50%);z-index:59;width:min(1200px,calc(100% - 24px));
    display:grid;gap:2px;padding:10px;border-radius:22px;
    background:rgba(255,255,255,.9);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
    border:1px solid var(--glass-edge);box-shadow:0 24px 50px -24px rgba(40,50,140,.5)}
  .menu[hidden]{display:none}
  .menu a{padding:14px 18px;border-radius:14px;font-family:var(--display);font-weight:600;font-size:16px}
  .menu a:hover{background:rgba(109,75,255,.09)}
  @media (min-width:981px){.menu{display:none!important}}
  .hero{position:relative;padding:130px 0 70px;overflow:hidden}
  #fx{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
  .hero-grid{position:relative;display:grid;grid-template-columns:1fr 1.05fr;gap:28px;align-items:center}
  .hero-text{position:relative;z-index:2}
  .hero h1{font-family:var(--display);font-weight:900;font-size:clamp(38px,5.6vw,78px);line-height:1.32;margin-bottom:12px;text-wrap:balance;
    background-image:var(--foil);background-size:200% 100%;background-repeat:repeat-x;
    -webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent;
    animation:foil 10s linear infinite,rise .9s cubic-bezier(.2,.8,.2,1) both}
  @keyframes foil{to{background-position:200% 0}}
  @keyframes rise{from{opacity:0;transform:translateY(26px);filter:blur(10px)}to{opacity:1;transform:none;filter:none}}
  .hero-sub{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin-bottom:26px;font-family:var(--display);font-weight:600;color:var(--muted);font-size:clamp(14px,1.4vw,18px);animation:rise .9s .1s cubic-bezier(.2,.8,.2,1) both}
  .hero-sub .vbar{width:1.5px;height:1.1em;background:rgba(60,70,160,.3)}
  .duo{font-family:var(--display);line-height:1.6}
  .duo span{display:block}
  .duo .a{font-weight:300;color:var(--muted)}
  .duo .b{font-weight:900;color:var(--ink)}
  .hero .duo{font-size:clamp(20px,2.3vw,30px);margin-bottom:14px;animation:rise .9s .18s cubic-bezier(.2,.8,.2,1) both}
  .hero .lead{font-size:clamp(16px,1.5vw,19px);color:var(--muted);max-width:33em;margin-bottom:32px;animation:rise .9s .28s cubic-bezier(.2,.8,.2,1) both}
  .btns{display:flex;flex-wrap:wrap;gap:12px;animation:rise .9s .38s cubic-bezier(.2,.8,.2,1) both}
  .btn{display:inline-flex;align-items:center;gap:10px;font-family:var(--display);font-weight:600;font-size:16px;padding:15px 30px;border-radius:16px;transition:transform .2s,box-shadow .2s,background .2s}
  .btn.primary{color:#fff;background:linear-gradient(135deg,var(--violet),var(--pink));box-shadow:0 14px 30px -12px rgba(109,75,255,.7)}
  .btn.primary:hover{transform:translateY(-3px);box-shadow:0 20px 36px -12px rgba(230,62,124,.65)}
  .btn.ghost{background:var(--glass);border:1px solid var(--glass-edge);box-shadow:0 8px 24px -14px rgba(40,50,140,.4)}
  .btn.ghost:hover{background:#fff;transform:translateY(-3px)}
  .p-hero-orb{position:relative;z-index:2;display:grid;place-items:center;animation:rise .9s .2s cubic-bezier(.2,.8,.2,1) both}
  .p-hero-orb .ball{position:relative;display:grid;place-items:center;width:280px;height:280px;border-radius:50%;
    background:radial-gradient(circle at 32% 26%,color-mix(in srgb,var(--c) 40%,#fff) 0%,var(--c) 48%,color-mix(in srgb,var(--c) 72%,#14173A) 100%);
    box-shadow:0 40px 80px -20px color-mix(in srgb,var(--c) 75%,transparent),inset -14px -18px 30px rgba(20,23,58,.22),inset 8px 10px 18px rgba(255,255,255,.55)}
  .p-hero-orb .ball::after{content:"";position:absolute;top:9%;left:16%;width:34%;height:20%;border-radius:50%;background:linear-gradient(180deg,rgba(255,255,255,.85),rgba(255,255,255,0));transform:rotate(-24deg)}
  .p-hero-orb .ball svg{position:relative;z-index:1;width:50%;height:50%;stroke:#fff;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 4px 8px rgba(0,0,0,.28))}
  .p-hero-orb .pnum{position:absolute;bottom:-10px;font-family:var(--display);font-weight:900;font-size:120px;line-height:1;color:transparent;-webkit-text-stroke:2px color-mix(in srgb,var(--c) 50%,transparent);direction:ltr;pointer-events:none}
  .band{position:relative;z-index:3;transform:rotate(-1.6deg);margin:20px -3% 0;padding:16px 0;overflow:hidden;
    background:var(--foil);background-size:200% 100%;background-repeat:repeat-x;animation:foil 16s linear infinite;
    box-shadow:0 18px 40px -20px rgba(109,75,255,.6)}
  .track{display:flex;width:max-content;direction:ltr;animation:marq 42s linear infinite}
  .track span{display:inline-flex;align-items:center;gap:34px;padding-inline-end:34px;font-family:var(--display);font-weight:900;font-size:clamp(24px,3.4vw,44px);line-height:1.4;color:#fff;white-space:nowrap;direction:rtl}
  html[dir="ltr"] .track span{direction:ltr}
  .track span::after{content:"";width:14px;height:14px;background:rgba(255,255,255,.85);transform:rotate(45deg);border-radius:3px}
  @keyframes marq{to{transform:translateX(-50%)}}
  section{padding:96px 0}
  .sec-title{font-family:var(--display);font-weight:900;font-size:clamp(30px,4.4vw,56px);line-height:1.4;margin-bottom:14px;text-wrap:balance}
  .sec-sub{color:var(--muted);max-width:40em;font-size:clamp(16px,1.4vw,18.5px)}
  .sec-head{display:flex;align-items:center;gap:18px;margin-bottom:48px}
  .sec-head .gorb{--sz:56px;flex:none}
  .sec-head .sec-title{margin-bottom:0}
  .sec-head .en{font-family:var(--display);font-weight:600;font-size:14px;color:var(--muted);direction:ltr}
  .gorb{--sz:56px;position:relative;display:grid;place-items:center;width:var(--sz);height:var(--sz);border-radius:50%;flex:none;
    background:radial-gradient(circle at 32% 26%,color-mix(in srgb,var(--c) 40%,#fff) 0%,var(--c) 48%,color-mix(in srgb,var(--c) 72%,#14173A) 100%);
    box-shadow:0 12px 22px -10px color-mix(in srgb,var(--c) 75%,transparent),inset -5px -7px 12px rgba(20,23,58,.22),inset 3px 4px 8px rgba(255,255,255,.55)}
  .gorb::after{content:"";position:absolute;top:9%;left:16%;width:34%;height:20%;border-radius:50%;background:linear-gradient(180deg,rgba(255,255,255,.85),rgba(255,255,255,0));transform:rotate(-24deg)}
  .gorb svg{position:relative;z-index:1;width:46%;height:46%;stroke:#fff;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 2px 3px rgba(0,0,0,.28))}
  .gorb b{position:relative;z-index:1;font-family:var(--display);font-weight:900;font-size:calc(var(--sz) * .4);color:#fff;text-shadow:0 2px 6px rgba(20,23,58,.35);direction:ltr}
  .info-card{display:flex;flex-direction:column;gap:18px;padding:40px 36px;border-radius:30px;
    background:var(--glass);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);
    border:1px solid var(--glass-edge);box-shadow:0 22px 46px -30px rgba(40,50,140,.55);
    --rx:0deg;--ry:0deg;--ty:0px;--mx:50%;--my:0%;
    transform:perspective(900px) rotateX(var(--rx)) rotateY(var(--ry)) translateY(var(--ty));
    transition:transform .25s ease-out,box-shadow .3s,border-color .3s;isolation:isolate;overflow:hidden}
  .info-card::before{content:"";position:absolute;inset:0;z-index:-1;opacity:0;transition:opacity .3s;
    background:radial-gradient(360px circle at var(--mx,50%) var(--my,0%),color-mix(in srgb,var(--c) 22%,transparent),transparent 70%)}
  @media(hover:hover){.info-card:hover{--ty:-8px;border-color:color-mix(in srgb,var(--c) 50%,#fff);box-shadow:0 34px 60px -28px var(--c)}.info-card:hover::before{opacity:1}}
  .info-card .gorb{--sz:72px}
  .info-card h3{font-family:var(--display);font-weight:900;font-size:clamp(22px,2.2vw,29px);line-height:1.45}
  .info-card p{color:var(--muted);font-size:17px;line-height:1.9}
  .list-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;margin-top:48px}
  .lcard{position:relative;display:flex;gap:18px;align-items:flex-start;padding:28px 26px;border-radius:26px;
    background:var(--glass);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
    border:1px solid var(--glass-edge);box-shadow:0 18px 40px -28px rgba(40,50,140,.5);
    --rx:0deg;--ry:0deg;--ty:0px;--mx:50%;--my:0%;
    transform:perspective(900px) rotateX(var(--rx)) rotateY(var(--ry)) translateY(var(--ty));
    transition:transform .25s ease-out,box-shadow .3s,border-color .3s;isolation:isolate;overflow:hidden}
  .lcard::before{content:"";position:absolute;inset:0;z-index:-1;opacity:0;transition:opacity .3s;
    background:radial-gradient(280px circle at var(--mx,50%) var(--my,0%),color-mix(in srgb,var(--c) 20%,transparent),transparent 70%)}
  @media(hover:hover){.lcard:hover{--ty:-6px;border-color:color-mix(in srgb,var(--c) 50%,#fff);box-shadow:0 26px 44px -26px var(--c)}.lcard:hover::before{opacity:1}}
  .lcard .gorb{--sz:50px}
  .lcard p{font-size:16px;line-height:1.8;color:var(--ink)}
  .journey{position:relative;list-style:none;display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-top:64px}
  .journey::before{content:"";position:absolute;top:30px;inset-inline:calc(100% / 10);height:5px;border-radius:5px;
    background:var(--foil);background-size:200% 100%;background-repeat:repeat-x;
    transform:scaleX(0);transform-origin:var(--start) center;transition:transform 1.6s cubic-bezier(.6,0,.2,1)}
  .journey.on::before{transform:scaleX(1);animation:foil 12s linear infinite}
  .step{position:relative;display:flex;flex-direction:column;align-items:center;gap:16px;text-align:center}
  .step .gorb{--sz:64px;transform:scale(.3);opacity:0;transition:transform .7s cubic-bezier(.2,1.5,.4,1),opacity .4s;transition-delay:calc(var(--i) * .18s + .25s)}
  .step .s-label{font-family:var(--display);font-weight:800;font-size:clamp(14px,1.4vw,18px);line-height:1.4;opacity:0;transition:opacity .5s;transition-delay:calc(var(--i) * .18s + .45s)}
  .journey.on .gorb{transform:none;opacity:1}
  .journey.on .s-label{opacity:1}
  .bento{display:grid;grid-template-columns:repeat(12,1fr);grid-auto-rows:270px;gap:16px;margin-top:44px}
  .b-tile{position:relative;grid-column:span var(--span);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;
    padding:0;border:0;border-radius:26px;overflow:hidden;background:#e6e8f7;box-shadow:0 18px 38px -24px rgba(40,50,140,.6);font-family:var(--display)}
  .b-tile.ph{background:linear-gradient(145deg,color-mix(in srgb,var(--c) 16%,#fff),color-mix(in srgb,var(--c) 6%,#fff));border:1px dashed color-mix(in srgb,var(--c) 50%,#fff);box-shadow:none}
  .b-tile.ph b{font-weight:800;font-size:18px}
  .b-tile.ph .soon{font-size:13px;font-weight:600;color:color-mix(in srgb,var(--c) 65%,#14173A);background:color-mix(in srgb,var(--c) 14%,#fff);padding:2px 12px;border-radius:999px}
  .b-tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .7s}
  button.b-tile:hover img{transform:scale(1.06)}
  .b-tile .cap{position:absolute;inset-inline:0;bottom:0;padding:44px 18px 16px;color:#fff;font-weight:600;font-size:15px;text-align:start;background:linear-gradient(180deg,transparent,rgba(20,23,58,.82))}
  .b-tile .play{position:absolute;top:50%;left:50%;translate:-50% -50%;width:66px;height:66px;display:grid;place-items:center;border-radius:50%;background:rgba(255,255,255,.88);box-shadow:0 12px 28px -10px rgba(20,23,58,.6)}
  .b-tile .play svg{width:34px;height:34px;stroke:var(--ink);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
  button.b-tile{cursor:zoom-in}
  .lightbox{position:fixed;inset:0;z-index:100;display:flex;align-items:center;justify-content:center;padding:24px;background:rgba(245,246,252,.9);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
  .lightbox[hidden]{display:none}
  .lightbox figure{max-width:min(1100px,92vw);text-align:center}
  .lightbox img{max-width:100%;max-height:78vh;border-radius:22px;box-shadow:0 30px 70px -30px rgba(20,23,58,.6)}
  .lightbox video{max-width:100%;max-height:78vh;border-radius:22px;background:#000;box-shadow:0 30px 70px -30px rgba(20,23,58,.6)}
  .lightbox iframe{border:0;border-radius:22px;box-shadow:0 30px 70px -30px rgba(20,23,58,.6)}
  .lightbox figcaption{margin-top:14px;font-weight:600}
  .lightbox .x{position:absolute;top:18px;inset-inline-end:18px;width:46px;height:46px;border-radius:50%;border:0;background:var(--ink);color:#fff;font-size:22px;line-height:1}
  .back-section{padding:48px 0 96px;text-align:center}
  .back-section .btn{font-size:17px}
  footer{padding:36px 0 44px;color:var(--muted);font-size:15px}
  footer .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:16px;padding-block:22px;border-radius:24px;background:var(--glass);border:1px solid var(--glass-edge)}
  footer b{color:var(--ink);font-weight:600}
  @media(max-width:1080px){.nav-links a{padding:8px 10px;font-size:14px}}
  @media(max-width:980px){
    .hero{padding-top:110px}
    .hero-grid{grid-template-columns:1fr;gap:10px}
    .hero-text{text-align:center}
    .hero-sub{justify-content:center}
    .hero .lead{margin-inline:auto}
    .btns{justify-content:center}
    .p-hero-orb{order:-1}
    .p-hero-orb .ball{width:200px;height:200px}
    .p-hero-orb .pnum{font-size:80px}
    .nav-links{display:none}
    .burger{display:inline-flex}
    .journey{grid-template-columns:1fr;gap:26px;margin-top:44px}
    .journey::before{top:32px;bottom:32px;height:auto;width:5px;inset-inline:auto;inset-inline-start:30px;transform:scaleY(0);transform-origin:center top}
    .journey.on::before{transform:scaleY(1)}
    .step{flex-direction:row;text-align:start;gap:20px}
  }
  @media(max-width:620px){
    body{font-size:16px}
    section{padding:64px 0}
    .list-grid{grid-template-columns:1fr}
    .logo,.logo img{height:38px}
    .nav{height:60px}
    .band{padding:12px 0}
    .bento{grid-auto-rows:230px}
    .b-tile{grid-column:span 12}
  }
  @media(prefers-reduced-motion:reduce){
    html{scroll-behavior:auto}
    *,*::before,*::after{animation:none!important;transition:none!important}
    .journey::before{transform:none}
    .step .gorb,.step .s-label{opacity:1;transform:none}
  }
"""

# ── Shared JS template (uses __PLACEHOLDER__ markers) ──
JS_TEMPLATE = r"""
const I18N = __I18N_JSON__;
const PROGRAM_COLOR = "__COLOR__";
const OBJ_ICONS = __OBJ_ICONS__;
const OUT_ICONS = __OUT_ICONS__;
const ACT_ICONS = __ACT_ICONS__;
const PROJ_ICONS = __PROJ_ICONS__;
const BAND = I18N.ar.band;
const JOURNEY_COLORS = ["#6D4BFF","#16B8E0","#10C38B","#7BC62D","#FF9A1F","#FF4D8D","#7B5CFF","#E8482B"];

const LS = { get(k){try{return localStorage.getItem(k);}catch(e){return null;}}, set(k,v){try{localStorage.setItem(k,v);}catch(e){}} };
let LANG = "ar";
const T = (path, lang=LANG) => path.split(".").reduce((o,k)=> (o==null?o:o[k]), I18N[lang]);

function applyLang(lang){
  LANG = lang;
  const de = document.documentElement;
  de.lang = lang; de.dir = lang === "ar" ? "rtl" : "ltr";
  document.querySelectorAll("[data-t]").forEach(el=>{ const v = T(el.dataset.t); if(v != null) el.textContent = v; });
  document.querySelectorAll("[data-alt-lang]").forEach(el=>{ const o = lang === "ar" ? "en" : "ar"; el.lang = o; el.dir = o === "ar" ? "rtl" : "ltr"; });
  document.title = T("meta.title");
  const md = document.querySelector('meta[name="description"]'); if(md) md.content = T("meta.description");
  LS.set("lang", lang);
  buildDynamic();
}

function buildList(gridId, items, icons, color){
  const el = document.getElementById(gridId);
  if(!el) return;
  el.innerHTML = items.map((text,i)=>{
    const icon = icons[i % icons.length];
    return '<div class="lcard" style="--c:'+color+'"><span class="gorb"><svg viewBox="0 0 24 24" aria-hidden="true">'+icon+'</svg></span><p>'+text+'</p></div>';
  }).join("");
  attachTilt(el);
}

function buildJourney(){
  const el = document.getElementById("journeyList");
  if(!el) return;
  const steps = T("journey.steps");
  el.innerHTML = steps.map((s,i)=>{
    const c = JOURNEY_COLORS[i % JOURNEY_COLORS.length];
    return '<li class="step" style="--c:'+c+';--i:'+i+'"><span class="gorb"><b>'+(i+1)+'</b></span><span class="s-label">'+s+'</span></li>';
  }).join("");
  const io = new IntersectionObserver(es=>{ if(es[0].isIntersecting){ el.classList.add("on"); io.disconnect(); } }, {threshold:.3});
  io.observe(el);
}

/* ============================================================
   إعدادات المعرض التلقائي من Google Drive
   لتفعيل المعرض التلقائي:
   1. انسخ سكربت gallery-drive.gs إلى Google Apps Script وانشره كـ Web App
   2. ضع رابط النشر هنا ↓
   3. ضع معرّف مجلد Google Drive الخاص بهذا البرنامج هنا ↓
   (ابحث عن "folder ID" في رابط مجلد Google Drive)
   إذا تركت القيم فارغة، ستظهر بطاقات «قريبًا» تلقائياً
   ============================================================ */
const DRIVE_CONFIG = {
  scriptUrl: "",   // ← رابط Google Apps Script Web App
  folderId: ""     // ← معرّف مجلد Google Drive الخاص بهذا البرنامج
};

/* يمكنك أيضاً إضافة عناصر يدوياً هنا — تظهر بجانب ملفات Google Drive */
const GALLERY = [];

/* تحميل المعرض من Google Drive تلقائياً */
async function loadGalleryFromDrive(){
  if(!DRIVE_CONFIG.scriptUrl || !DRIVE_CONFIG.folderId) return;
  try{
    const url = DRIVE_CONFIG.scriptUrl + "?folderId=" + encodeURIComponent(DRIVE_CONFIG.folderId);
    const res = await fetch(url);
    if(!res.ok) return;
    const data = await res.json();
    if(!Array.isArray(data) || !data.length) return;
    const driveItems = data.map(f => ({
      type: f.type,
      src: f.type === "video" ? (f.previewUrl || f.viewUrl) : f.viewUrl,
      poster: f.type === "video" ? f.thumb : "",
      thumb: f.thumb,
      isDrive: true,
      ar: f.caption || f.eventName || f.name,
      en: f.caption || f.eventName || f.name
    }));
    GALLERY.push(...driveItems);
  }catch(e){ console.warn("Gallery: could not load from Google Drive", e); }
}

function buildBento(){
  const el = document.getElementById("bento");
  if(!el) return;
  const SPANS = [6,6,3,6,3,4,4,4];
  const COLORS = ["#6D4BFF","#FF4D8D","#16B8E0","#FF9A1F","#10C38B","#7B5CFF","#7BC62D","#E8482B"];
  const PROG = T("hero.name");
  const PHOTO_ICON = '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M21 16l-5-5-8 8"/>';
  const VIDEO_ICON = '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/>';
  const PLAY_ICON = '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/>';

  if(!GALLERY.length){
    const soon = LANG === "ar" ? "\\u0642\\u0631\\u064a\\u0628\\u064b\\u0627" : "Soon";
    const types = LANG === "ar"
      ? ["\\u0635\\u0648\\u0631\\u0629","\\u0641\\u062a\\u062f\\u064a\\u0648","\\u0635\\u0648\\u0631\\u0629","\\u0635\\u0648\\u0631\\u0629","\\u0641\\u062a\\u062f\\u064a\\u0648","\\u0635\\u0648\\u0631\\u0629","\\u0635\\u0648\\u0631\\u0629","\\u0641\\u062a\\u062f\\u064a\\u0648"]
      : ["Photo","Video","Photo","Photo","Video","Photo","Photo","Video"];
    el.innerHTML = types.map((t,i)=>{
      const span = SPANS[i % SPANS.length];
      const c = COLORS[i % COLORS.length];
      const ic = t.indexOf(LANG === "ar" ? "\\u0641\\u062a\\u062f" : "Vid") >= 0 ? VIDEO_ICON : PHOTO_ICON;
      return '<div class="b-tile ph" style="--span:'+span+';--c:'+c+'"><span class="gorb" style="--sz:64px"><svg viewBox="0 0 24 24" aria-hidden="true">'+ic+'</svg></span><b>'+t+' \\u2014 '+PROG+'</b><span class="soon">'+soon+'</span></div>';
    }).join("");
    return;
  }

  const esc = v => String(v||"").replace(/"/g,"&quot;");
  el.innerHTML = GALLERY.map((g,i)=>{
    const span = SPANS[i % SPANS.length];
    const c = COLORS[i % COLORS.length];
    const thumb = g.type === "video" ? (g.poster || "") : g.src;
    const cap = LANG === "ar" ? (g.ar || g.en || "") : (g.en || g.ar || "");
    return '<button class="b-tile" type="button" data-i="'+i+'" style="--span:'+span+';--c:'+c+'">'
      + (thumb ? '<img src="'+thumb+'" alt="" loading="lazy" crossorigin="anonymous">' : '')
      + (g.type === "video" ? '<span class="play"><svg viewBox="0 0 24 24" aria-hidden="true">'+PLAY_ICON+'</svg></span>' : '')
      + '<span class="cap">'+esc(cap)+'</span>'
      + '</button>';
  }).join("");

  const box = document.getElementById("mediaBox"), fig = document.getElementById("mediaFig"), xBtn = box.querySelector(".x");
  function close(){ box.hidden = true; fig.innerHTML = ""; }
  box.addEventListener("click", e=>{ if(e.target === box || e.target === xBtn) close(); });
  document.addEventListener("keydown", e=>{ if(e.key === "Escape" && !box.hidden) close(); });
  el.querySelectorAll("button.b-tile").forEach(b=>b.addEventListener("click", ()=>{
    const g = GALLERY[+b.dataset.i];
    const cap = b.querySelector(".cap").textContent;
    if(g.isDrive && g.type === "video"){
      fig.innerHTML = '<iframe src="'+g.src+'" allow="autoplay" allowfullscreen style="width:min(90vw,1100px);height:min(70vh,620px);border:0;border-radius:22px"></iframe>';
    } else if(g.type === "video"){
      fig.innerHTML = '<video src="'+g.src+'" '+(g.poster ? 'poster="'+g.poster+'"' : '')+' controls autoplay playsinline></video>';
    } else {
      fig.innerHTML = '<img src="'+g.src+'" alt="">';
    }
    const fc = document.createElement("figcaption"); fc.textContent = cap; fig.appendChild(fc);
    box.hidden = false; xBtn.focus();
  }));
}

function buildBand(){
  const el = document.getElementById("track");
  if(!el) return;
  const one = BAND.map((_,i)=>'<span data-t="band.'+i+'"></span>').join("");
  el.innerHTML = one + one;
}

function buildDynamic(){
  buildBand();
  buildList("objGrid", T("objectives.items"), OBJ_ICONS, PROGRAM_COLOR);
  buildList("outGrid", T("outcomes.items"), OUT_ICONS, PROGRAM_COLOR);
  buildList("actGrid", T("activities.items"), ACT_ICONS, PROGRAM_COLOR);
  buildList("projGrid", T("projects.items"), PROJ_ICONS, PROGRAM_COLOR);
  buildJourney();
  buildBento();
}

function attachTilt(container){
  if(!matchMedia("(hover:hover) and (pointer:fine)").matches) return;
  container.querySelectorAll(".lcard, .info-card").forEach(c=>{
    if(c.dataset.tilt) return;
    c.dataset.tilt = "1";
    c.addEventListener("pointermove", e=>{
      const r = c.getBoundingClientRect();
      const x = (e.clientX - r.left)/r.width, y = (e.clientY - r.top)/r.height;
      c.style.setProperty("--mx", (x*100).toFixed(1)+"%");
      c.style.setProperty("--my", (y*100).toFixed(1)+"%");
      c.style.setProperty("--rx", ((0.5 - y)*6).toFixed(2)+"deg");
      c.style.setProperty("--ry", ((x - 0.5)*6).toFixed(2)+"deg");
    });
    c.addEventListener("pointerleave", ()=>{ c.style.setProperty("--rx","0deg"); c.style.setProperty("--ry","0deg"); });
  });
}

(function heroFx(){
  const cv = document.getElementById("fx"), hero = document.getElementById("top");
  if(!cv || !hero) return;
  const ctx = cv.getContext("2d");
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const colors = ["#6D4BFF","#0EA5D6","#0E9F76","#E8790A","#E63E7C",PROGRAM_COLOR];
  let W=0,H=0,pts=[],mouse={x:-999,y:-999},visible=true;
  function resize(){
    const dpr = Math.min(window.devicePixelRatio||1, 2);
    W = hero.clientWidth; H = hero.clientHeight;
    cv.width = W*dpr; cv.height = H*dpr;
    ctx.setTransform(dpr,0,0,dpr,0,0);
    const n = Math.round(Math.min(70, W*H/15000));
    pts = Array.from({length:n}, ()=>({
      x:Math.random()*W, y:Math.random()*H,
      vx:(Math.random()-.5)*.35, vy:(Math.random()-.5)*.35,
      r:1.6+Math.random()*2.6, c:colors[(Math.random()*colors.length)|0]
    }));
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    for(const p of pts){
      if(!reduce){
        p.x += p.vx; p.y += p.vy;
        if(p.x<0||p.x>W) p.vx*=-1;
        if(p.y<0||p.y>H) p.vy*=-1;
        const dx=p.x-mouse.x, dy=p.y-mouse.y, d2=dx*dx+dy*dy;
        if(d2<150*150 && d2>1){ const d=Math.sqrt(d2), f=(150-d)/150*1.6; p.x+=dx/d*f; p.y+=dy/d*f; }
      }
    }
    for(let i=0;i<pts.length;i++){
      const a=pts[i];
      for(let j=i+1;j<pts.length;j++){
        const b=pts[j], dx=a.x-b.x, dy=a.y-b.y, d=Math.sqrt(dx*dx+dy*dy);
        if(d<130){
          ctx.strokeStyle="rgba(80,90,190,"+(0.2*(1-d/130)).toFixed(3)+")";
          ctx.lineWidth=1; ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
        }
      }
    }
    for(const p of pts){
      ctx.globalAlpha=.16; ctx.fillStyle=p.c; ctx.beginPath(); ctx.arc(p.x,p.y,p.r*3,0,6.283); ctx.fill();
      ctx.globalAlpha=.85; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,6.283); ctx.fill();
    }
    ctx.globalAlpha=1;
  }
  function loop(){ if(visible) draw(); requestAnimationFrame(loop); }
  resize();
  window.addEventListener("resize", resize);
  if(reduce){ draw(); }
  else {
    loop();
    new IntersectionObserver(es=>{ visible = es[0].isIntersecting; }).observe(hero);
  }
  hero.addEventListener("pointermove", e=>{ const r = hero.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
  hero.addEventListener("pointerleave", ()=>{ mouse.x = mouse.y = -999; });
})();

(function(){
  const b = document.getElementById("burger"), m = document.getElementById("menu");
  function set(open){ m.hidden = !open; b.setAttribute("aria-expanded", String(open)); }
  b.addEventListener("click", ()=> set(m.hidden));
  m.querySelectorAll("a").forEach(a=>a.addEventListener("click", ()=> set(false)));
  document.addEventListener("keydown", e=>{ if(e.key === "Escape") set(false); });
  document.addEventListener("click", e=>{ if(!m.hidden && !m.contains(e.target) && !b.contains(e.target)) set(false); });
  window.addEventListener("resize", ()=>{ if(window.innerWidth > 980) set(false); });
})();

document.getElementById("langBtn").addEventListener("click", ()=> applyLang(LANG === "ar" ? "en" : "ar"));
(async function(){
  const q = new URLSearchParams(location.search).get("lang");
  const pick = [q, LS.get("lang")].find(v => v === "ar" || v === "en") || "ar";
  await loadGalleryFromDrive();
  applyLang(pick);
  attachTilt(document);
})();
"""

# Icons
CHECK_ICON = '<path d="M20 6L9 17l-5-5"/>'
TARGET_ICON = '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4"/>'
STAR_ICON = '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>'
LIGHTBULB_ICON = '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>'
FLASK_ICON = '<path d="M9 2v6l-4 6v8h14v-8l-4-6V2"/><path d="M9 2h6"/>'
PEN_ICON = '<path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/>'
TOOL_ICON = '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'
BUILD_ICON = '<path d="M2 20h20M5 20V8l5-4 5 4v12M14 20v-6h4v6"/>'
ROCKET_ICON = '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91 0z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 12a22.35 22.35 0 0 1-4 1z"/>'

OBJ_ICONS = [TARGET_ICON, CHECK_ICON, STAR_ICON, LIGHTBULB_ICON, ROCKET_ICON, BUILD_ICON]
OUT_ICONS = [CHECK_ICON, STAR_ICON, FLASK_ICON, TOOL_ICON, ROCKET_ICON, BUILD_ICON]
ACT_ICONS = [LIGHTBULB_ICON, FLASK_ICON, PEN_ICON, TOOL_ICON, BUILD_ICON, ROCKET_ICON]
PROJ_ICONS = [ROCKET_ICON, BUILD_ICON, STAR_ICON, LIGHTBULB_ICON]

def generate_page(p):
    slug = p["slug"]
    color = p["color"]
    icon = p["icon"]
    num = p["number"]

    band_ar = ["التفكير الناقد","الإبداع","التعاون","التواصل","حل المشكلات","الابتكار","ريادة الأعمال","القيادة"]
    band_en = ["Critical Thinking","Creativity","Collaboration","Communication","Problem Solving","Innovation","Entrepreneurship","Leadership"]

    i18n = {
        "ar": {
            "meta": {"title": f"{p['ar_name']} | وحدة مهارات القرن 21", "description": p["ar_desc"]},
            "nav": {"home":"الرئيسية","about":"عن الوحدة","why":"لماذا الوحدة؟","programs":"البرامج","journey":"الرحلة","achievements":"الإنجازات","gallery":"المعرض"},
            "hero": {"name": p["ar_name"], "altName": p["en_name"], "num": f"برنامج {num}", "tagline": p["ar_tagline"], "cta1": "تعرّف على البرنامج", "cta2": "كل البرامج"},
            "about": {"title":"عن البرنامج","en":"About the Program","desc": p["ar_about"]},
            "why": {"title":"لماذا نُدرّس هذا البرنامج؟","en":"Why It Matters","desc": p["ar_why"]},
            "objectives": {"title":"الأهداف","en":"Objectives","items": p["ar_objectives"]},
            "outcomes": {"title":"مخرجات تعلّم الطالب","en":"Student Outcomes","items": p["ar_outcomes"]},
            "journey": {"title":"رحلة التعلّم","en":"Learning Journey","steps": p["ar_journey"]},
            "activities": {"title":"الأنشطة","en":"Activities","items": p["ar_activities"]},
            "projects": {"title":"المشاريع","en":"Projects","items": p["ar_projects"]},
            "gallery": {"title":"معرض الصور والفيديوهات","en":"Gallery","sub":"صور وفيديوهات من قلب البرنامج والفعاليات."},
            "back":"العودة لمنظومة البرامج",
            "footer": {"name":"وحدة مهارات القرن 21","by":"إعداد وإشراف: اسم مسؤول الوحدة"},
            "band": band_ar,
        },
        "en": {
            "meta": {"title": f"{p['en_name']} | 21st Century Skills Unit", "description": p["en_desc"]},
            "nav": {"home":"Home","about":"About","why":"Why?","programs":"Programs","journey":"Journey","achievements":"Achievements","gallery":"Gallery"},
            "hero": {"name": p["en_name"], "altName": p["ar_name"], "num": f"Program {num}", "tagline": p["en_tagline"], "cta1": "Learn More", "cta2": "All Programs"},
            "about": {"title":"About the Program","en":"About the Program","desc": p["en_about"]},
            "why": {"title":"Why We Teach This Program","en":"Why It Matters","desc": p["en_why"]},
            "objectives": {"title":"Objectives","en":"Objectives","items": p["en_objectives"]},
            "outcomes": {"title":"Student Outcomes","en":"Student Outcomes","items": p["en_outcomes"]},
            "journey": {"title":"Learning Journey","en":"Learning Journey","steps": p["en_journey"]},
            "activities": {"title":"Activities","en":"Activities","items": p["en_activities"]},
            "projects": {"title":"Projects","en":"Projects","items": p["en_projects"]},
            "gallery": {"title":"Gallery","en":"Gallery","sub":"Photos and videos from the heart of the program and events."},
            "back":"Back to Programs",
            "footer": {"name":"21st Century Skills Unit","by":"Prepared and supervised by: Unit Lead Name"},
            "band": band_en,
        }
    }

    i18n_json = json.dumps(i18n, ensure_ascii=False)

    # Build the JS by replacing placeholders
    js = JS_TEMPLATE
    js = js.replace("__I18N_JSON__", i18n_json)
    js = js.replace("__COLOR__", color)
    js = js.replace("__OBJ_ICONS__", json.dumps(OBJ_ICONS, ensure_ascii=False))
    js = js.replace("__OUT_ICONS__", json.dumps(OUT_ICONS, ensure_ascii=False))
    js = js.replace("__ACT_ICONS__", json.dumps(ACT_ICONS, ensure_ascii=False))
    js = js.replace("__PROJ_ICONS__", json.dumps(PROJ_ICONS, ensure_ascii=False))

    # Build HTML using template with placeholders
    html = HTML_TEMPLATE
    html = html.replace("__SLUG__", slug)
    html = html.replace("__COLOR__", color)
    html = html.replace("__ICON__", icon)
    html = html.replace("__NUM__", num)
    html = html.replace("__AR_NAME__", p["ar_name"])
    html = html.replace("__EN_NAME__", p["en_name"])
    html = html.replace("__AR_DESC__", p["ar_desc"])
    html = html.replace("__CSS__", SHARED_CSS)
    html = html.replace("__JS__", js)

    return html

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__AR_NAME__ | وحدة مهارات القرن 21</title>
<meta name="description" content="__AR_DESC__">
<meta name="theme-color" content="#F5F6FC">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Noto+Kufi+Arabic:wght@300;600;900&family=Sora:wght@400;600;800&display=swap" rel="stylesheet">
<style>
__CSS__
</style>
</head>
<body>
<div class="aurora" aria-hidden="true"></div>

<!-- Nav -->
<header class="nav">
  <div class="logos">
    <a href="../index.html" class="logo"><img src="../assets/school-logo.png" alt="School logo" onerror="this.parentNode.classList.add('missing')"><span class="ph">School<br>Logo</span></a>
    <span class="sep" aria-hidden="true"></span>
    <a href="../index.html" class="logo"><img src="../assets/unit-logo.png" alt="Unit logo" onerror="this.parentNode.classList.add('missing')"><span class="ph">Unit<br>Logo</span></a>
  </div>
  <div class="nav-right">
    <nav class="nav-links" aria-label="Main">
      <a href="../index.html" data-t="nav.home"></a>
      <a href="../index.html#about" data-t="nav.about"></a>
      <a href="../index.html#programs" data-t="nav.programs"></a>
      <a href="../index.html#journey" data-t="nav.journey"></a>
      <a href="../index.html#achievements" data-t="nav.achievements"></a>
      <a href="../index.html#gallery" data-t="nav.gallery"></a>
    </nav>
    <button class="lang" id="langBtn" type="button" aria-label="Change language / تغيير اللغة"><span data-l="ar">AR</span><span data-l="en">EN</span></button>
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Menu"><i></i><i></i><i></i></button>
  </div>
</header>

<!-- Mobile menu -->
<nav class="menu" id="menu" aria-label="Menu" hidden>
  <a href="../index.html" data-t="nav.home"></a>
  <a href="../index.html#about" data-t="nav.about"></a>
  <a href="../index.html#programs" data-t="nav.programs"></a>
  <a href="../index.html#journey" data-t="nav.journey"></a>
  <a href="../index.html#achievements" data-t="nav.achievements"></a>
  <a href="../index.html#gallery" data-t="nav.gallery"></a>
</nav>

<main>
<!-- Hero -->
<section class="hero" id="top">
  <canvas id="fx" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="hero-text">
      <p class="hero-sub"><span data-t="hero.num"></span><i class="vbar" aria-hidden="true"></i><span data-t="hero.altName" data-alt-lang></span></p>
      <h1 data-t="hero.name"></h1>
      <p class="duo"><span class="a" data-t="hero.tagline"></span></p>
      <div class="btns">
        <a class="btn primary" href="#about" data-t="hero.cta1"></a>
        <a class="btn ghost" href="../index.html#programs" data-t="hero.cta2"></a>
      </div>
    </div>
    <div class="p-hero-orb" style="--c:__COLOR__">
      <div class="ball">
        <svg viewBox="0 0 24 24" aria-hidden="true">__ICON__</svg>
        <span class="pnum">__NUM__</span>
      </div>
    </div>
  </div>
</section>

<!-- Skills band -->
<div class="band" aria-hidden="true"><div class="track" id="track"></div></div>

<!-- About -->
<section id="about">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true">__ICON__</svg></span>
      <div><div class="en" data-t="about.en"></div><h2 class="sec-title" data-t="about.title"></h2></div>
    </div>
    <div class="info-card" style="--c:__COLOR__">
      <p data-t="about.desc"></p>
    </div>
  </div>
</section>

<!-- Why -->
<section id="why">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg></span>
      <div><div class="en" data-t="why.en"></div><h2 class="sec-title" data-t="why.title"></h2></div>
    </div>
    <div class="info-card" style="--c:__COLOR__">
      <p data-t="why.desc"></p>
    </div>
  </div>
</section>

<!-- Objectives -->
<section id="objectives">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4"/></svg></span>
      <div><div class="en" data-t="objectives.en"></div><h2 class="sec-title" data-t="objectives.title"></h2></div>
    </div>
    <div class="list-grid" id="objGrid"></div>
  </div>
</section>

<!-- Outcomes -->
<section id="outcomes">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg></span>
      <div><div class="en" data-t="outcomes.en"></div><h2 class="sec-title" data-t="outcomes.title"></h2></div>
    </div>
    <div class="list-grid" id="outGrid"></div>
  </div>
</section>

<!-- Learning Journey -->
<section id="journey">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg></span>
      <div><div class="en" data-t="journey.en"></div><h2 class="sec-title" data-t="journey.title"></h2></div>
    </div>
    <ol class="journey" id="journeyList"></ol>
  </div>
</section>

<!-- Activities -->
<section id="activities">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/></svg></span>
      <div><div class="en" data-t="activities.en"></div><h2 class="sec-title" data-t="activities.title"></h2></div>
    </div>
    <div class="list-grid" id="actGrid"></div>
  </div>
</section>

<!-- Projects -->
<section id="projects">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/></svg></span>
      <div><div class="en" data-t="projects.en"></div><h2 class="sec-title" data-t="projects.title"></h2></div>
    </div>
    <div class="list-grid" id="projGrid"></div>
  </div>
</section>

<!-- Gallery -->
<section id="gallery">
  <div class="wrap">
    <div class="sec-head">
      <span class="gorb" style="--c:__COLOR__"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M21 16l-5-5-8 8"/></svg></span>
      <div><div class="en" data-t="gallery.en"></div><h2 class="sec-title" data-t="gallery.title"></h2></div>
    </div>
    <p class="sec-sub" data-t="gallery.sub"></p>
    <div class="bento" id="bento"></div>
  </div>
</section>

<!-- Back -->
<section class="back-section">
  <div class="wrap">
    <a class="btn ghost" href="../index.html#programs">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="transform:scaleX(var(--flip))"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      <span data-t="back"></span>
    </a>
  </div>
</section>

<!-- Lightbox -->
<div class="lightbox" id="mediaBox" hidden><button class="x" aria-label="إغلاق">×</button><figure id="mediaFig"></figure></div>
</main>

<footer>
  <div class="wrap">
    <div><b data-t="footer.name"></b></div>
    <div data-t="footer.by"></div>
  </div>
</footer>

<script>
__JS__
</script>
</body>
</html>"""

# Generate all pages
for p in PROGRAMS:
    html = generate_page(p)
    filepath = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {filepath}")

print(f"\nDone! Generated {len(PROGRAMS)} program pages.")
