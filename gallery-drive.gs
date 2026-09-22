/**
 * ============================================================
 *  سكربت المعرض التلقائي من Google Drive
 *  وحدة مهارات القرن 21 — 21st Century Skills Unit
 * ============================================================
 *
 *  التعليمات:
 *  1. افتح script.google.com و أنشئ مشروعاً جديداً
 *  2. الصق هذا الكود كاملاً (احذف أي كود افتراضي)
 *  3. اضغط Deploy → New deployment
 *  4. اختر Type: Web app
 *  5. Execute as: Me (your email)
 *  6. Who has access: Anyone with the link
 *  7. انسخ رابط الـ Web App URL
 *  8. ضعه في كل صفحة برنامج في المتغير DRIVE_CONFIG.scriptUrl
 *
 *  بنية المجلدات على Google Drive:
 *
 *  المنصة/                          ← المجلد الرئيسي (اختياري)
 *    ├── الذكاء العاطفي/            ← مجلد البرنامج (ضع معرّفه في folderId)
 *    │   ├── ورشة الصف السابع/      ← مجلد الفعالية
 *    │   │   ├── photo1.jpg
 *    │   │   ├── photo2.jpg
 *    │   │   └── video1.mp4
 *    │   ├── محاضرة الوعي الذاتي/
 *    │   │   ├── photo1.jpg
 *    │   │   └── photo2.jpg
 *    │   └── (يمكن أيضاً وضع صور مباشرة بدون مجلد فرعي)
 *    │
 *    ├── البحث العلمي/              ← مجلد برنامج آخر
 *    │   ├── معرض العلوم/
 *    │   │   └── ...
 *    │   └── ...
 *    └── ...
 *
 *  ملاحظات:
 *  - جميع المجلدات يجب أن تكون مشتركة (Anyone with the link can view)
 *  - الصور المدعومة: jpg, png, gif, webp, bmp, svg
 *  - الفيديوهات المدعومة: mp4, webm, mov, avi, mkv
 *  - اسم مجلد الفعالية يظهر كعنوان للصورة/الفيديو
 *  - إذا لم تجد السكربت أي ملفات، تظهر بطاقات «قريبًا» تلقائياً
 * ============================================================
 */

function doGet(e) {
  var folderId = (e && e.parameter && e.parameter.folderId) ? e.parameter.folderId : '';

  if (!folderId) {
    return jsonOut({ error: 'missing folderId parameter', hint: 'Add ?folderId=YOUR_FOLDER_ID to the URL' });
  }

  try {
    var folder = DriveApp.getFolderById(folderId);
  } catch (err) {
    return jsonOut({ error: 'folder not found', detail: err.message });
  }

  var results = [];

  // 1) الملفات المباشرة في مجلد البرنامج (بدون مجلد فرعي)
  collectFiles(folder, '', results);

  // 2) الملفات داخل مجلدات الفعاليات
  var eventFolders = folder.getFolders();
  while (eventFolders.hasNext()) {
    var eventFolder = eventFolders.next();
    var eventName = eventFolder.getName();
    collectFiles(eventFolder, eventName, results);
  }

  return jsonOut(results);
}

function collectFiles(folder, eventName, results) {
  var files = folder.getFiles();
  while (files.hasNext()) {
    var file = files.next();
    var mime = file.getMimeType() || '';
    var name = file.getName();
    var ext = name.split('.').pop().toLowerCase();

    var isImage = mime.indexOf('image/') === 0 || ['jpg','jpeg','png','gif','webp','bmp','svg'].indexOf(ext) >= 0;
    var isVideo = mime.indexOf('video/') === 0 || ['mp4','webm','mov','avi','mkv','m4v','ogv'].indexOf(ext) >= 0;

    if (!isImage && !isVideo) continue;

    var fileId = file.getId();
    var caption = eventName ? eventName : name.replace(/\.[^.]+$/, '');

    results.push({
      type: isVideo ? 'video' : 'photo',
      id: fileId,
      name: name,
      eventName: eventName,
      caption: caption,
      // صورة مصغّرة (تعمل للصور والفيديوهات)
      thumb: 'https://drive.google.com/thumbnail?id=' + fileId + '&sz=w1000',
      // رابط العرض المباشر
      viewUrl: 'https://drive.google.com/uc?export=view&id=' + fileId,
      // رابط المعاينة (للفيديوهات في iframe)
      previewUrl: 'https://drive.google.com/file/d/' + fileId + '/preview'
    });
  }
}

function jsonOut(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
