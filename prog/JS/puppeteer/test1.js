const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://www.baidu.com/');
    await page.screenshot({
        path: 'example.png'
    });

    await browser.close();
})();
//var pt=require('puppeteer');
//const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        headless: false
    });
    const page = await browser.newPage();
    await page.goto('https://www.baidu.com', {
        waitUntil: 'networkidle2'
    });
    // await page.pdf({   //此功能未实现
    //     path: 'hn.pdf',
    //     format: 'A4'
    // });

    await browser.close();
})();