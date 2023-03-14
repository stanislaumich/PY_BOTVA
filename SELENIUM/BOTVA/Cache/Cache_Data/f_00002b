var Logging;
(function (Logging) {
    var Logger = (function () {
        function Logger(level) {
            if (level === void 0) { level = 0; }
            this.level = level;
        }
        Logger.write = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            try {
                var func = args.shift();
                if (window.console && console[func]) {
                    var t = '[' + (((new Date()).getTime() - Logger.logStartTime) / 1000) + '] ';
                    args.unshift(t);
                    switch (func) {
                        case 'info':
                            console.info.apply(console, args);
                            break;
                        case 'error':
                            console.error.apply(console, args);
                            break;
                        case 'warn':
                            console.warn.apply(console, args);
                            break;
                        default:
                            console.log.apply(console, args);
                            break;
                    }
                }
            }
            catch (e) {
            }
        };
        Logger.prototype.debug = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            if (this.level < 4)
                return;
            args.unshift('debug');
            Logger.write.apply(this, args);
        };
        Logger.prototype.info = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            if (this.level < 3)
                return;
            args.unshift('info');
            Logger.write.apply(this, args);
        };
        Logger.prototype.warn = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            if (this.level < 2)
                return;
            args.unshift('warn');
            Logger.write.apply(this, args);
        };
        Logger.prototype.error = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            if (this.level < 1)
                return;
            args.unshift('error');
            Logger.write.apply(this, args);
        };
        Logger.logStartTime = (new Date()).getTime();
        return Logger;
    })();
    Logging.Logger = Logger;
})(Logging || (Logging = {}));
var Utils;
(function (Utils) {
    function getTimestamp() {
        return Math.floor(new Date().getTime() / 1000);
    }
    Utils.getTimestamp = getTimestamp;
    function getParameterFromQueryString(name, queryString) {
        if (queryString === void 0) { queryString = location.search; }
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)");
        var results = regex.exec(queryString);
        return results === null ? undefined : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    function getParameterByName(name) {
        var value = getParameterFromQueryString(name);
        if (typeof value !== 'undefined')
            return value;
        var hashString = getParameterFromQueryString("hash");
        if (typeof hashString !== 'undefined') {
            hashString = '?' + hashString;
            value = getParameterFromQueryString(name, hashString);
            if (typeof value !== 'undefined')
                return value;
        }
    }
    Utils.getParameterByName = getParameterByName;
    function toDate(timestamp) {
        return new Date(timestamp * 1000);
    }
    Utils.toDate = toDate;
    function getXMLHttpRequest() {
        if (typeof XMLHttpRequest != 'undefined') {
            return new XMLHttpRequest;
        }
        else {
            try {
                return new ActiveXObject("MSXML2.XMLHTTP");
            }
            catch (ex) {
                return null;
            }
        }
    }
    function getJSON(params) {
        var request = getXMLHttpRequest();
        if (request != null) {
            var sendArray = [];
            for (var k in params.data) {
                if (params.data.hasOwnProperty(k)) {
                    sendArray.push(encodeURIComponent(k) + "=" + encodeURIComponent(params.data[k]));
                }
            }
            var sendString = sendArray.join('&');
            var url = sendString.length ? params.url + '?' + sendString : params.url;
            var async = typeof params.async != 'undefined' ? params.async : true;
            request.open("GET", url, async);
            request.onreadystatechange = function handler() {
                if (request.readyState != 4)
                    return;
                if (request.status == 200) {
                    var response = JSON.parse(request.responseText);
                    if (params.done)
                        params.done.apply(this, [response]);
                }
                else {
                    if (params.fail)
                        params.fail.apply(this, [request.statusText, request.statusMessage, request.statusCode]);
                }
            };
        }
        request.send();
    }
    Utils.getJSON = getJSON;
})(Utils || (Utils = {}));
var Cookies;
(function (Cookies) {
    function getCookie(name) {
        var matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }
    Cookies.getCookie = getCookie;
    function setCookie(name, value, options) {
        var expires = options.expires;
        if (typeof expires == "number" && expires) {
            var d = new Date();
            d.setTime(d.getTime() + expires * 1000);
            expires = options.expires = d;
        }
        if (expires && expires.toUTCString) {
            options.expires = expires.toUTCString();
        }
        value = encodeURIComponent(value.toString());
        var updatedCookie = name + "=" + value;
        for (var propName in options) {
            if (options.hasOwnProperty(propName)) {
                updatedCookie += "; " + propName;
                var propValue = options[propName];
                if (propValue !== true) {
                    updatedCookie += "=" + propValue;
                }
            }
        }
        document.cookie = updatedCookie;
    }
    Cookies.setCookie = setCookie;
    function deleteCookie(name, options) {
        if (getCookie(name)) {
            document.cookie = name + "=" +
                ((options.path) ? ";path=" + options.path : "") +
                ((options.domain) ? ";domain=" + options.domain : "") +
                ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
        }
    }
    Cookies.deleteCookie = deleteCookie;
    var Storage = (function () {
        function Storage(storage_options) {
            this.storage_options = storage_options;
            this.prefix = '_lbn_';
        }
        Storage.prototype.setItem = function (key, value, options) {
            var _options = {};
            updateObject(_options, this.storage_options, options);
            Cookies.setCookie(this.prefix + key, value, _options);
        };
        Storage.prototype.getItem = function (key) {
            return Cookies.getCookie(this.prefix + key);
        };
        Storage.KEYS = {
            LAST_SEEN: 'l',
            REF_CODE: 'rt',
            REFERRER: 'rf',
            REF_CODE_CREATION_DATE: 'd'
        };
        return Storage;
    })();
    Cookies.Storage = Storage;
    function updateObject(obj) {
        var params = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            params[_i - 1] = arguments[_i];
        }
        for (var i = 0, l = params.length; i < l; i++) {
            for (var prop in params[i]) {
                if (params[i].hasOwnProperty(prop)) {
                    var val = params[i][prop];
                    if (typeof val == "object")
                        updateObject(obj[prop], val);
                    else
                        obj[prop] = val;
                }
            }
        }
        return obj;
    }
})(Cookies || (Cookies = {}));
/*
    Используемые термины:
    - реферал / реферальный код / рефкод /ref code -- уникальный ключ(md5 hash) клика. Передается в проект в GET параметрах.
        Например rt=rt_ace8af043412482b59390a8c25d8a917c
    - органика / organic -- это пользователь, пришедший на проект
        не от партнеров, а либо из поисовых систем, либо пришедшие напрямую (вбили сайт в адресную строку).
        Т.е. при первом переходе на сайт у пользователя отсутсвовал реферальный код
    - органический реферал -- уникальный ключ органического пользователя
    - клик -- переход на проект с баннера. Сопровождается уникальным реферальнм кодом.
 */
/// <reference path='./logging.ts' />
/// <reference path='./utils.ts' />
/// <reference path='./cookies.ts' />
var Marketing;
(function (Marketing) {
    var ORGANIC_TIMEOUT = 90 * 24 * 60 * 60;
    var NON_ORGANIC_TIMEOUT = 90 * 24 * 60 * 60;
    var DEFAULT_COOKIES_EXPIRES = 60 * 60 * 24 * 365 * 2;
    var DEFAULT_EXPIRATION_REF_CODE_SECONDS = 60 * 24 * 60 * 60;
    var DEFAULT_EXPIRATION_ORGANIC_REF_CODE_SECONDS = 90 * 24 * 60 * 60;
    var OPENLEAD_IDS = {
        'tera': 'ol35'
    };
    var Handlers = (function () {
        function Handlers(logger) {
            this.logger = logger;
        }
        Handlers.prototype.registration = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            this.logger.debug('Registration:', args);
            window.destinyScopeHandlerRegistration.apply(this, args);
        };
        Handlers.prototype.levelup = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            this.logger.debug('Level up:', args);
            window.destinyScopeHandlerLevelup.apply(this, args);
        };
        Handlers.prototype.purchase = function () {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i - 0] = arguments[_i];
            }
            this.logger.debug('Purchase money:', args);
            window.destinyScopeHandlerPurchase.apply(this, args);
        };
        return Handlers;
    })();
    var Arbitration = (function () {
        function Arbitration(options) {
            this.options = options;
            this.CREATE_REFERRAL_URL = '//lbn2.ddestiny.ru/arbitration/save_referral/';
            this.IS_REF_CODE_ORGANIC_URL = '//lbn2.ddestiny.ru/arbitration/is_ref_code_organic/';
            this.UPDATE_OPENLEADID_URL = '//lbn2.ddestiny.ru/openlead/update/';
            this.options = this.options || {};
            this.options.ref_code_name = this.options.ref_code_name || 'rt';
            this.options.cookie_options = this.options.cookie_options || {};
            this.options.cookie_options.expires = this.options.cookie_options.expires || DEFAULT_COOKIES_EXPIRES;
            this.options.cookie_options.path = this.options.cookie_options.path || '/';
            if (options.dev) {
                this.CREATE_REFERRAL_URL = '//dev.lbn2.ddestiny.ru/arbitration/save_referral/';
                this.IS_REF_CODE_ORGANIC_URL = '//dev.lbn2.ddestiny.ru/arbitration/is_ref_code_organic/';
            }
            this.initOpenlead();
            this.logger = new Logging.Logger(this.options.debug);
            this.storage = new Cookies.Storage(this.options.cookie_options);
            this.main();
            this.storage.setItem(Cookies.Storage.KEYS.LAST_SEEN, Utils.getTimestamp().toString());
            this.handlers = new Handlers(this.logger);
            if (typeof window.destinyScopeInitialized == 'function') {
                window.destinyScopeInitialized.apply(this);
            }
        }
        Arbitration.prototype.initOpenlead = function () {
            var self = this;
            if (!OPENLEAD_IDS.hasOwnProperty(this.options.project))
                return;
            var projectId = OPENLEAD_IDS[this.options.project];
            var jsElm = document.createElement("script");
            jsElm.type = "text/javascript";
            jsElm.src = 'https://openlead.net/s/ol.js?id=' + projectId;
            jsElm.onload = function () {
                self.updateOpenleadId();
            };
            document.body.appendChild(jsElm);
        };
        Arbitration.prototype.isRegistered = function () {
            return !!this.options.account_id && !!this.options.account_ref_code;
        };
        Arbitration.prototype.hasNoActivity = function (seconds) {
            var lastSeenTimestamp = parseInt(this.storage.getItem(Cookies.Storage.KEYS.LAST_SEEN)) || 0;
            return Utils.getTimestamp() - lastSeenTimestamp >= seconds;
        };
        Arbitration.prototype.hasVisited = function () {
            return typeof this.storage.getItem(Cookies.Storage.KEYS.LAST_SEEN) != 'undefined'
                || this.isRegistered();
        };
        Arbitration.prototype.hasRefCodeInQueryString = function () {
            return typeof Utils.getParameterByName(this.options.ref_code_name) != 'undefined';
        };
        Arbitration.prototype.hasExpiredRefCode = function () {
            return typeof this.storage.getItem(Cookies.Storage.KEYS.REF_CODE) == 'undefined';
        };
        Arbitration.prototype.isCurrentRefCodeOrganic = function (callback) {
            var self = this;
            this.logger.debug('-> isCurrentRefCodeOrganic');
            if (!this.options.account_id) {
                this.logger.error('[isCurrentRefCodeOrganic] options.account_id is undefined');
                return false;
            }
            if (!this.options.account_ref_code) {
                this.logger.error('[isCurrentRefCodeOrganic] options.account_ref_code is undefined');
                return false;
            }
            Utils.getJSON({
                url: this.IS_REF_CODE_ORGANIC_URL,
                data: {
                    account_id: this.options.account_id,
                    account_ref_code: this.options.account_ref_code
                },
                done: function (response) {
                    if (response['status'] === 'ok') {
                        callback.apply(self, [response['response']['organic']]);
                    }
                    else {
                        self.logger.error('[isCurrentRefCodeOrganic] сервер вернул ответ с ошибкой:', response['error']);
                    }
                },
                fail: function (statusText, statusMessage, statusCode) {
                    self.logger.error('[isCurrentRefCodeOrganic] ошибка при запросе:', statusText, statusMessage, statusCode);
                }
            });
        };
        Arbitration.prototype.createReferral = function (params) {
            var self = this;
            this.logger.debug(("-> createReferral(account_id[" + params.account_id + "],")
                + (" account_ref_code[" + params.account_ref_code + "])")
                + (" ref_code[" + params.ref_code + "])"));
            var getData = {
                project: this.options.project
            };
            if (params.account_id) {
                getData['account_id'] = params.account_id;
                getData['account_ref_code'] = params.account_ref_code;
            }
            if (params.ref_code)
                getData['ref_code'] = params.ref_code;
            if (params.link_id)
                getData['link_id'] = params.link_id;
            if (params.source)
                getData['source'] = params.source;
            if (params.vk_referrer)
                getData['vk_referrer'] = params.vk_referrer;
            var _openlead = Cookies.getCookie('_openlead');
            if (_openlead)
                getData['_openlead'] = _openlead;
            Utils.getJSON({
                url: this.CREATE_REFERRAL_URL,
                data: getData,
                done: function (response) {
                    self.logger.debug('[createReferral] ответ от сервера:', response);
                    if (params.callback)
                        params.callback.apply(this, [response]);
                },
                fail: function (statusText, statusMessage, statusCode) {
                    self.logger.error('[createReferral] ошибка при запросе:', statusText, statusMessage, statusCode);
                }
            });
        };
        Arbitration.isVkTargeting = function () {
            var apiUrl = Utils.getParameterByName('api_url'), referrer = Utils.getParameterByName('referrer'), isPlatformVk = typeof apiUrl == 'string' && apiUrl.indexOf('vk.com') != -1, isAdReferrer = typeof referrer == 'string' && referrer.indexOf('ad_') == 0;
            return isPlatformVk && isAdReferrer;
        };
        Arbitration.prototype.saveRefCookie = function (response) {
            var _cookie_options = {
                expires: DEFAULT_EXPIRATION_ORGANIC_REF_CODE_SECONDS
            };
            this.storage.setItem(Cookies.Storage.KEYS.REF_CODE, response['response']['ref_code'], _cookie_options);
            this.storage.setItem(Cookies.Storage.KEYS.REF_CODE_CREATION_DATE, response['response']['ref_code_creation_date'], _cookie_options);
            this.storage.setItem(Cookies.Storage.KEYS.REFERRER, document.referrer, _cookie_options);
        };
        Arbitration.prototype.createOrganicReferral = function () {
            var self = this;
            this.logger.debug('-> createOrganicReferral');
            this.createReferral({
                link_id: this.options.link_id,
                source: this.options.source,
                callback: function (response) {
                    self.saveRefCookie.call(self, response);
                }
            });
        };
        Arbitration.prototype.createTargetingReferral = function (vk_referrer) {
            var self = this;
            this.logger.debug('-> createTargetingReferral');
            this.createReferral({
                link_id: this.options.link_id,
                source: this.options.source,
                vk_referrer: vk_referrer,
                callback: function (response) {
                    self.saveRefCookie.call(self, response);
                }
            });
        };
        Arbitration.prototype.moveCurrentReferralToOrganic = function () {
            this.logger.debug('-> moveCurrentReferralToOrganic');
            this.createReferral({
                account_id: this.options.account_id,
                account_ref_code: this.options.account_ref_code
            });
        };
        Arbitration.prototype.moveCurrentReferralToNewReferral = function () {
            this.logger.debug('-> moveCurrentReferralToNewReferral');
            var ref_code = Utils.getParameterByName(this.options.ref_code_name);
            if (typeof ref_code == 'undefined') {
                this.logger.error('[moveCurrentReferralToNewReferral] Trying to save undefined ref code');
                return;
            }
            this.createReferral({
                account_id: this.options.account_id,
                account_ref_code: this.options.account_ref_code,
                ref_code: ref_code
            });
        };
        Arbitration.prototype.main = function () {
            var self = this;
            this.logger.debug('[*] Текущее время:', new Date());
            this.logger.debug('[*] Текущий реферал:', this.storage.getItem(Cookies.Storage.KEYS.REF_CODE));
            this.logger.debug('[*] Дата создания текущего реферала:', this.storage.getItem(Cookies.Storage.KEYS.REF_CODE_CREATION_DATE), '->', Utils.toDate(parseInt(this.storage.getItem(Cookies.Storage.KEYS.REF_CODE_CREATION_DATE))));
            this.logger.debug('[*] Новый реферал:', Utils.getParameterByName(this.options.ref_code_name));
            this.logger.info('---- Старт блока арбитража ----');
            if (this.hasVisited()) {
                this.logger.debug('Сайт уже был посещен');
                if (this.isRegistered()) {
                    this.logger.debug('Пользователь зарегистрирован');
                    var hasNoActivityAsUsual = this.hasNoActivity(NON_ORGANIC_TIMEOUT);
                    var hasNoActivityAsOrganic = this.hasNoActivity(ORGANIC_TIMEOUT);
                    var checkForOrganicCallback = function (isOrganic) {
                        this.logger.debug('Пользователь органика:', isOrganic);
                        var hasNoActivity = isOrganic ? hasNoActivityAsOrganic : hasNoActivityAsUsual;
                        if (hasNoActivity) {
                            this.logger.debug('Пользователь был не активен');
                            if (this.hasRefCodeInQueryString()) {
                                this.moveCurrentReferralToNewReferral();
                            }
                            else {
                                this.moveCurrentReferralToOrganic();
                            }
                        }
                        else {
                            this.logger.debug('Пользователь все еще активен');
                        }
                    };
                    if (hasNoActivityAsUsual) {
                        this.isCurrentRefCodeOrganic(checkForOrganicCallback);
                    }
                    else {
                        this.logger.debug('Пользователь все еще активен');
                    }
                }
                else {
                    this.logger.debug('Пользователь не зарегистрирован');
                    if (this.hasExpiredRefCode()) {
                        this.logger.debug('Текущий рефкод протух');
                        this.saveReferral();
                    }
                    else {
                        this.logger.debug('Текущий рефкод еще не протух');
                    }
                }
            }
            else {
                this.logger.debug('Сайт еще не был посещен');
                this.saveReferral();
            }
        };
        Arbitration.prototype.saveReferral = function () {
            this.logger.debug('-> saveReferral');
            if (this.hasRefCodeInQueryString()) {
                this.logger.debug('Есть новый рефкод в QUERY_STRING -- сохраняем его в куках');
                var ref_code = Utils.getParameterByName(this.options.ref_code_name);
                var _cookie_options = {
                    expires: parseInt(Utils.getParameterByName('_exp')) || DEFAULT_EXPIRATION_REF_CODE_SECONDS
                };
                this.storage.setItem(Cookies.Storage.KEYS.REF_CODE, ref_code, _cookie_options);
                this.storage.setItem(Cookies.Storage.KEYS.REF_CODE_CREATION_DATE, Utils.getTimestamp(), _cookie_options);
                this.storage.setItem(Cookies.Storage.KEYS.REFERRER, document.referrer, _cookie_options);
            }
            else {
                if (Arbitration.isVkTargeting()) {
                    this.logger.debug('Нового рефкода нет, таргетинговая реклама -- присваиваем реферал "Таргетинг"');
                    this.createTargetingReferral(Utils.getParameterByName('referrer'));
                }
                else {
                    this.logger.debug('Нового рефкода нет -- присваиваем реферал "Органика"');
                    this.createOrganicReferral();
                }
            }
        };
        Arbitration.prototype.getRefCode = function () {
            return this.storage.getItem(Cookies.Storage.KEYS.REF_CODE) || null;
        };
        Arbitration.prototype.getReferrer = function () {
            return this.storage.getItem(Cookies.Storage.KEYS.REFERRER) || null;
        };
        Arbitration.prototype.updateOpenleadId = function () {
            var self = this;
            if (!this.hasRefCodeInQueryString())
                return;
            var ref_code = Utils.getParameterByName(this.options.ref_code_name);
            var _openlead = Cookies.getCookie('_openlead') || '';
            Utils.getJSON({
                url: this.UPDATE_OPENLEADID_URL + ref_code + '/',
                data: { '_openlead': _openlead },
                done: function (response) {
                    self.logger.debug('[updateOpenleadId] ответ от сервера:', response);
                },
                fail: function (statusText, statusMessage, statusCode) {
                    self.logger.error('[updateOpenleadId] ошибка при запросе:', statusText, statusMessage, statusCode);
                }
            });
        };
        return Arbitration;
    })();
    Marketing.Arbitration = Arbitration;
})(Marketing || (Marketing = {}));
if (typeof destinyScopeOptions == 'undefined') {
    var destinyScopeOptions = {};
}
var DestinyScope = Marketing.Arbitration;
var destiny_scope = new DestinyScope(destinyScopeOptions);
