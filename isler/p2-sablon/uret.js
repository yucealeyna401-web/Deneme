// sablon.html -> deneme.pdf (700x900 mm) + onizleme.png
// Kullanım: node uret.js [girdi.html] [cikti.pdf] [onizleme.png]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp = 'sablon.html', pdf = 'deneme.pdf', png = 'onizleme.png'] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(inp));
  await page.pdf({ path: pdf, width: '700mm', height: '900mm', printBackground: true, preferCSSPageSize: true });
  // Taşma denetimi: içerik sayfa yüksekliğini aşıyor mu
  const tasma = await page.evaluate(() => {
    const mm = 96 / 25.4, sinir = 900 * mm;
    return { sayfa: Math.round(document.documentElement.scrollHeight / mm), tasiyor: document.documentElement.scrollHeight > sinir + 1 };
  });
  console.log('yukseklik_mm', tasma.sayfa, 'tasiyor', tasma.tasiyor);
  await browser.close();
})();
