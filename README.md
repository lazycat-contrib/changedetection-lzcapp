# changedetection.io LazyCat package

Source https://github.com/dgtlmoon/changedetection.io,0.60.10,Apache-2.0. Official candidate dev.beiyu.changedetection. Package community.lazycat.app.changedetection,minOS1.6.0,amd64 mirror delivery, community store only. Classification: System monitoring / Website change monitoring.

HTTP5000, single app container, no browser container. Ordinary HTTP fetch support only; JS rendering, visual selection and browser steps require an external Playwright/Chromium service not included here. LLM features and version-check telemetry are disabled.

Native /login uses the shared deployment secret; native form email is a hidden fixed service identity. Autofill only, no automatic submit; LazyCat entry authentication retained. Startup converts deployment secret and stable salt seed to upstream base64(salt32+PBKDF2-HMAC-SHA256100000) without logging it, then removes plaintext env and execs the original app. Native credential changes must be managed via deployment parameters because SALTED_PASS overrides saved settings; existing sessions follow upstream behavior.

Service run_as1000:1000 maps /lzcapp/var/data to /datastore. All trusted app members share watches/history/notifications. Back up before uninstalling. Do not expose credentials through watched URLs or notification messages. No added healthcheck/smoke or file interception.

Workflow/config, image delivery and independent cloud artifact/hash-format checks are required before publishing. All builds and artifact downloads run on GitHub, no local LPK download. Actual startup, login, fetching, diffs, notification delivery and persistence remain unverified.
