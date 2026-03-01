var I18N={
en:{
"nav.features":"Features","nav.skills":"Skills","nav.blog":"Blog","nav.showcase":"Showcase","nav.store":"🛒 Store","nav.community":"Community",
"blog.title":"Yuki & Claw: The Build Log","blog.subtitle":"A founder and her AI lobster — building, breaking, and evolving together.",
"blog.log1":"Founder's Log #1",
"blog.title1":"I Built This Site with Ima Claw. It Deleted the Lobster's Face.",
"blog.desc1":"2 hours, zero lines of code, and a lobster that had an existential crisis. The real story of how the founder built this site with Vibe Coding — crashes included.",
"blog.readmore":"Read More →",
"sk.page.title":"Skill Market","sk.page.desc":"Vetted · Plug & play · Zero config · One-click install",
"sk.cat.image":"Image Generation","sk.cat.video":"Video Production","sk.cat.music":"Music Creation","sk.cat.allinone":"All-in-One","sk.cat.social":"Social Media","sk.cat.writing":"Writing","sk.cat.research":"Research","sk.cat.info":"Info & Tools","sk.cat.feishu":"Feishu","sk.cat.system":"System","sk.cat.other":"Other",
"sk.install":"Install","sk.items":"skills","sk.footer.note":"All skills are security-vetted. Install with one click inside your Claw."
},
es:{
"nav.features":"Funciones","nav.skills":"Skills","nav.blog":"Blog","nav.showcase":"Galería","nav.store":"🛒 Tienda","nav.community":"Comunidad",
"blog.title":"Yuki & Claw: Diario de Creación","blog.subtitle":"Una fundadora y su langosta IA — construyendo y evolucionando juntas.",
"blog.log1":"Diario de Fundadora #1",
"blog.title1":"Hice este sitio con Ima Claw. Borró la cara de la langosta.",
"blog.desc1":"2 horas, cero líneas de código y una langosta con crisis existencial. La historia real de cómo la fundadora creó este sitio con Vibe Coding — incluidos los desastres.",
"blog.readmore":"Leer Más →",
"sk.page.title":"Mercado de Skills","sk.page.desc":"Verificados · Plug & play · Sin configuración · Un clic",
"sk.cat.image":"Generación de Imágenes","sk.cat.video":"Producción de Video","sk.cat.music":"Creación Musical","sk.cat.allinone":"Todo en Uno","sk.cat.social":"Redes Sociales","sk.cat.writing":"Escritura","sk.cat.research":"Investigación","sk.cat.info":"Info y Herramientas","sk.cat.feishu":"Feishu","sk.cat.system":"Sistema","sk.cat.other":"Otros",
"sk.install":"Instalar","sk.items":"skills","sk.footer.note":"Todos los skills están verificados. Instálalos con un clic en tu Claw."
},
ja:{
"nav.features":"機能","nav.skills":"スキル","nav.blog":"ブログ","nav.showcase":"作品集","nav.store":"🛒 ストア","nav.community":"コミュニティ",
"blog.title":"Yuki & Claw の創作日誌","blog.subtitle":"創業者とAIロブスター、一緒にプロダクトを作る記録。",
"blog.log1":"創業者ログ #1",
"blog.title1":"Ima Clawでこのサイトを作った。ロブスターの顔が消えた。",
"blog.desc1":"2時間、コードゼロ行、存在危機に陥ったロブスター。創業者がVibe Codingで公式サイトを作った実話——全事故現場付き。",
"blog.readmore":"続きを読む →",
"sk.page.title":"スキルマーケット","sk.page.desc":"審査済み · すぐ使える · 設定不要 · ワンクリック",
"sk.cat.image":"画像生成","sk.cat.video":"動画制作","sk.cat.music":"音楽制作","sk.cat.allinone":"オールインワン","sk.cat.social":"SNS","sk.cat.writing":"ライティング","sk.cat.research":"リサーチ","sk.cat.info":"情報＆ツール","sk.cat.feishu":"Feishu","sk.cat.system":"システム","sk.cat.other":"その他",
"sk.install":"インストール","sk.items":"スキル","sk.footer.note":"全スキル審査済み。Clawでワンクリックインストール。"
},
ar:{
"nav.features":"الميزات","nav.skills":"المهارات","nav.blog":"المدونة","nav.showcase":"المعرض","nav.store":"🛒 المتجر","nav.community":"المجتمع",
"blog.title":"يوكي وكلو: سجل البناء","blog.subtitle":"مؤسسة وجرادها البحري الذكي — يبنيان ويتطوران معاً.",
"blog.log1":"سجل المؤسسة #1",
"blog.title1":"بنيتُ هذا الموقع بـ Ima Claw. حذف وجه الجراد البحري.",
"blog.desc1":"ساعتان، صفر أسطر كود، وجراد بحر في أزمة وجودية. القصة الحقيقية لبناء هذا الموقع بـ Vibe Coding — بكل الكوارث.",
"blog.readmore":"اقرأ المزيد →",
"sk.page.title":"متجر المهارات","sk.page.desc":"مُراجَع · جاهز للاستخدام · بدون إعدادات · نقرة واحدة",
"sk.cat.image":"توليد الصور","sk.cat.video":"إنتاج الفيديو","sk.cat.music":"إبداع موسيقي","sk.cat.allinone":"الكل في واحد","sk.cat.social":"وسائل التواصل","sk.cat.writing":"الكتابة","sk.cat.research":"البحث","sk.cat.info":"أدوات ومعلومات","sk.cat.feishu":"فيشو","sk.cat.system":"النظام","sk.cat.other":"أخرى",
"sk.install":"تثبيت","sk.items":"مهارات","sk.footer.note":"كل المهارات مُراجعة أمنيًا. ثبّتها بنقرة واحدة في Claw الخاص بك."
}
};
var ZH={};
function setLang(l){
  document.documentElement.lang=l;
  var m={'zh-CN':'🇨🇳 中文','en':'🇺🇸 EN','es':'🇪🇸 ES','ja':'🇯🇵 JA','ar':'🇸🇦 AR'};
  var t=document.querySelector('.lang-trigger');
  if(t)t.textContent='🌐 '+(m[l]||l)+' ▾';
  document.querySelectorAll('.lang-dropdown').forEach(function(d){d.classList.remove('open')});
  document.querySelectorAll('[data-i18n]').forEach(function(el){
    var k=el.getAttribute('data-i18n');
    if(!ZH[k])ZH[k]=el.innerHTML;
    if(l==='zh-CN'){el.innerHTML=ZH[k]}
    else if(I18N[l]&&I18N[l][k]){el.textContent=I18N[l][k]}
  });
  document.documentElement.style.direction=l==='ar'?'rtl':'ltr';
}
