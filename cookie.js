// n.d
function d(t, e, n) {
    i.o(t, e) || Object.defineProperty(t, e, {
        enumerable: !0,
        get: n
    })
}
e={}


function r(t, e, n, r, o) {
    var i = "".concat(t, "=").concat(escape(e));
    if (null != n && "" != n) {
        0 == n && (n = 5256e4);
        var a = new Date;
        a.setTime(a.getTime() + 60 * n * 1e3),
        i += "; expires=".concat(a.toGMTString())
    }
    r && (i += "; path=".concat(r)),
    o && (i += "; domain=".concat(o)),
    document.cookie = i
}



function co1(t, e, n) {
    "use strict";
    function r(t, e, n, r, o) {
        var i = "".concat(t, "=").concat(escape(e));
        if (null != n && "" != n) {
            0 == n && (n = 5256e4);
            var a = new Date;
            a.setTime(a.getTime() + 60 * n * 1e3),
            i += "; expires=".concat(a.toGMTString())
        }
        r && (i += "; path=".concat(r)),
        o && (i += "; domain=".concat(o)),
        document.cookie = i
    }
    function o(t) {
        var e = new RegExp("(^| )".concat(t, "=([^;]*)(;|$)"),"gi").exec(unescape(document.cookie));
        return e ? e[2] : null
    }
    function i(t, e, n) {
        document.cookie = "".concat(t, "=").concat(e ? "; path=".concat(e) : "").concat(n ? "; domain=".concat(n) : "", "; expires=Thu, 01-Jan-70 00:00:01 GMT")
    }
    n.r(e),
    n.d(e, "setCookie", (function() {
        return r
    }
    )),
    n.d(e, "getCookie", (function() {
        return o
    }
    )),
    n.d(e, "delCookie", (function() {
        return i
    }
    ))
}

console.log("anchor-task-tips","vistived",5256000)


