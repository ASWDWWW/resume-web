# Android Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 6.0 / 10  
**Band:** Good  
**Application guidance:** Stretch

This project is credible evidence; name the gaps in interviews.

---

## What this job title usually means

Android engineers write Kotlin/Java, Gradle modules, Jetpack, Play policies, and often deal with OEM/Play Integrity quirks.

## What you actually did in this project

You wrote Expo config plugins that patch Gradle (force play-services-ads 24.6.0 / UMP 3.2.0 because Ads SDK 25.x Kotlin 2.3 metadata broke EAS; Crashlytics iOS dSYM upload; App Check iOS). That is native-adjacent Android/iOS build-system work, not a Swift/Kotlin product codebase. Additional Android evidence: `google-services.json`, Play Integrity App Check, Play Billing via expo-iap (offer tokens), AdMob Android app/unit IDs, JDK 17 pin for Gradle, FCM V1 for push.

## How that work applies to this title

You have more Android *build-system* scars than iOS language scars. Forcing Ads SDK versions through Gradle resolutionStrategy is real Android engineering, even inside Expo.

## Gaps (be ready to say these out loud)

No Kotlin app code, no Jetpack Compose, no custom Views. Play Console data-safety is documented as a checklist, not proven completed in-repo.

## Interview / resume angle

Lead with Gradle/Ads/Play Integrity/IAP, then be clear the UI is React Native. Some Android teams (RN shops, brownfield) will like that; AOSP-style teams will not.

## Verdict

Better Android evidence than iOS evidence, still not a native Android IC portfolio.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
