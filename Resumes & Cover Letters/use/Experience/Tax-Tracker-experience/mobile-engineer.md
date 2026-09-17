# Mobile Engineer

**Project scored:** TaxTacker (this repository only)  
**Score:** 8.0 / 10  
**Band:** Strong  
**Application guidance:** Target now

This project is primary evidence for the role.

---

## What this job title usually means

Mobile engineers ship iOS/Android apps: navigation, device APIs, store requirements, offline-ish UX, and native build pipelines.

## What you actually did in this project

Expo 57 app with EAS profiles, iOS/Android Firebase apps, App Attest / Play Integrity App Check notes, Face ID/Touch ID lock, expo-iap subscriptions, AdMob banners for free users, Crashlytics config plugins, image/document pickers, and store-review seed accounts. You wrote Expo config plugins that patch Gradle (force play-services-ads 24.6.0 / UMP 3.2.0 because Ads SDK 25.x Kotlin 2.3 metadata broke EAS; Crashlytics iOS dSYM upload; App Check iOS). That is native-adjacent Android/iOS build-system work, not a Swift/Kotlin product codebase. App Store Guideline 2.3.10 copy fix (remove Play references on iOS), review accounts that skip email verification and get seeded Diamond demo data, store listing placeholders, EAS submit profiles. You handled the mobile-only surface area: biometrics, push tokens, AdMob, IAP, Crashlytics, App Check, EAS, store copy, review accounts.

## How that work applies to this title

Cross-platform mobile engineer (React Native/Expo) is a direct match. You did not stop at UI — you fought store and native SDK reality, which is most of professional mobile work.

## Gaps (be ready to say these out loud)

Not a native mobile specialist. No SwiftUI/Jetpack Compose app code. Offline is a banner, not a local-first sync engine. Some IAP server verification is still a documented follow-on.

## Interview / resume angle

Tell the AdMob/Kotlin 2.3 vs Expo Kotlin 2.1 story and the App Store 2.3.10 story. Mobile interviewers trust people who have been burned by store and Gradle.

## Verdict

Strong for React Native / Expo mobile roles. Good supporting evidence for 'mobile' on a full-stack team.

---

*Generated from repository evidence (web app, `mobile/`, `functions/`, Firebase rules, CI, ops/store docs). Scores are role-fit, not years of employment.*
