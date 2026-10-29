// Renders infrastructure-plan.html to PDF. Usage: node render_pdf.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(__dirname, 'infrastructure-plan.html'), { waitUntil: 'networkidle' });
  await p.pdf({ path: path.join(__dirname, 'Studio-Infrastructure-Funding-Launch-Plan.pdf'), format: 'Letter', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font:8px Helvetica;color:#888;width:100%;text-align:center"><span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
  await b.close();
})();
