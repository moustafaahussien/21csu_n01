# وحدة مهارات القرن 21 | 21st Century Skills Unit

**Empowering Students for the Future**

موقع تعريفي احترافي لوحدة مهارات القرن 21 — منظومة تعليمية متكاملة تبني مهارات المستقبل.

---

## الهيكل · Structure

```
21st-century-skills/
│
├── index.html                 الصفحة الرئيسية
│
├── programs/                  صفحات البرامج الستة
│   ├── emotional-intelligence.html
│   ├── scientific-research.html
│   ├── design-for-change.html
│   ├── entrepreneurship.html
│   ├── robotics-3d-printing.html
│   └── stem.html
│
├── css/
│   └── style.css              التصميم الكامل (Dark/Light mode)
│
├── js/
│   └── main.js                التفاعلات (Theme, Navbar, Counters, Gallery, Canvas)
│
├── assets/
│   └── images/                ضع هنا الشعارات والصور
│       ├── logos/             شعار المدرسة + شعار الوحدة
│       ├── hero/              صور الخلفية
│       ├── programs/          صور كل برنامج
│       └── gallery/           صور المعرض
│
├── tools/
│   └── generate_pages.py      سكريبت توليد صفحات البرامج (أداة تطوير)
│
└── README.md
```

---

## البرامج الستة · Programs

| # | البرنامج | Program |
|---|---------|---------|
| 01 | الذكاء العاطفي | Emotional Intelligence |
| 02 | البحث العلمي | Scientific Research |
| 03 | التصميم من أجل التغيير | Design for Change |
| 04 | ريادة الأعمال | Entrepreneurship |
| 05 | الروبوت والطباعة ثلاثية الأبعاد | Robotics & 3D Printing |
| 06 | STEM | STEM Education |

---

## كيفية الرفع على GitHub Pages

### الخطوة 1: إنشاء مستودع
1. اذهب إلى [github.com/new](https://github.com/new)
2. اسم المستودع: `21st-century-skills` (أو أي اسم تريده)
3. اختر **Public**
4. اضغط **Create repository**

### الخطوة 2: رفع الملفات
#### الطريقة الأولى: عبر المتصفح
1. اضغط **uploading an existing file** في صفحة المستودع
2. اسحب وأفلت جميع الملفات (index.html, programs/, css/, js/, assets/)
3. اكتب رسالة commit ثم اضغط **Commit changes**

#### الطريقة الثانية: عبر Git CLI
```bash
git clone https://github.com/USERNAME/21st-century-skills.git
cd 21st-century-skills
# انسخ جميع الملفات هنا
git add .
git commit -m "Initial website"
git push origin main
```

### الخطوة 3: تفعيل GitHub Pages
1. في صفحة المستودع، اذهب إلى **Settings**
2. في القائمة الجانبية، اضغط **Pages**
3. في قسم **Source**، اختر **Deploy from a branch**
4. اختر الفرع `main` واختر `/ (root)`
5. اضغط **Save**
6. انتظر دقيقة — ستحصل على رابط مثل:
   ```
   https://USERNAME.github.io/21st-century-skills/
   ```

---

## التخصيص · Customization

### استبدال الشعارات
- ضع شعار المدرسة في `assets/images/logos/school-logo.png`
- ضع شعار الوحدة في `assets/images/logos/unit-logo.png`
- ثم استبدل placeholder في `index.html`:
```html
<!-- بدلاً من -->
<div class="hero-logo"><span>شعار المدارس</span></div>
<!-- استخدم -->
<div class="hero-logo"><img src="assets/images/logos/school-logo.png" alt="شعار المدرسة"></div>
```

### استبدال صور المعرض
- ضع الصور في `assets/images/gallery/`
- استبدل الـ placeholders في قسم `#gallery` بـ:
```html
<div class="gallery-item">
  <img src="assets/images/gallery/photo1.jpg" alt="وصف الصورة">
</div>
```

### تعديل الأرقام والإحصائيات
- في `index.html`، ابحث عن قسم `stats` وعدّل القيم

### تعديل ألوان الهوية
- في `css/style.css`، عدّل المتغيرات في `:root`:
```css
--color-primary: #06b6d4;  /* اللون الأساسي */
--color-secondary: #8b5cf6; /* اللون الثانوي */
```

### تعديل محتوى صفحات البرامج
- كل صفحة في `programs/` تحتوي على محتوى قابل للتعديل مباشرة
- يمكن إعادة توليد الصفحات باستخدام `tools/generate_pages.py`

---

## التقنيات · Tech Stack

- HTML5
- CSS3 (Grid, Flexbox, Variables, Glassmorphism, Animations)
- Vanilla JavaScript (Canvas, Intersection Observer, No frameworks)
- الخطوط: Cairo + Tajawal (Google Fonts) + Clash Display (Fontshare)
- لا حاجة لأي Backend أو قاعدة بيانات
- جاهز لـ GitHub Pages مباشرة

---

© 2026 وحدة مهارات القرن 21 — Empowering Students for the Future
