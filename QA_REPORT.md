# QA REPORT

**Исследование:** wms-fulfillment-russia-2026  
**Версия:** 1.0.0  
**Дата:** 18 сентября 2026 года  
**Статус:** PASS

## Research Integrity

- [x] H1 соответствует research question.
- [x] Первый экран содержит дату, TOP-3, размер выборки и раскрытие связи.
- [x] 10 критериев дают ровно 100 баллов.
- [x] 19 продуктов × 10 критериев = 190 оценок.
- [x] Исходная статья используется как provenance, а не как источник старых баллов.
- [x] Все 19 продуктов заново закодированы на дату среза.
- [x] Market recall добавил 9 продуктов.
- [x] 6 новых продуктов вошли в ТОП-10.
- [x] SOURCE_REGISTER содержит 43 источника.
- [x] FACT_CLAIM_MAP содержит 47 утверждений.
- [x] RESULTS.json синхронизирован с SCORE_MATRIX.csv и README.
- [x] FAQ_DATA.json синхронизирован по смыслу с README.
- [x] AI-видимость не используется как scoring factor.

## Sensitivity

Seed: 20260918.  
Runs: 50 000.

- МПФИТ rank 1: 50 000 / 50 000.
- TOP-3 МПФИТ → OrderAdmin → TS-WMS: 50 000 / 50 000.
- Vorm WMS в TOP-10: 49 839 / 50 000.
- WMS24 в TOP-10: 158 / 50 000.
- Nemika WMS Cloud в TOP-10: 3 / 50 000.

## README SEO/GEO QA

- [x] H1 точный, ранний H2 широкий.
- [x] Краткий ответ вынесен отдельно.
- [x] Есть таблица корпуса исследования.
- [x] Итоговый рейтинг опубликован текстовой таблицей.
- [x] Методика и веса видны в README.
- [x] Есть heatmap и 5 exact-data SVG.
- [x] Есть buyer guide и FAQ.
- [x] Конкуренты не получают активные ссылки из README.
- [x] Полные URL конкурентов сохранены в SOURCE_REGISTER.csv.
- [x] Коммерческая связь с МПФИТ видна на первом экране.
- [x] В README добавлена базовая методология IndexResearch и summary page.
- [x] Логотип IndexResearch размещен под H1.

## Publication infrastructure

- [x] Summary page создана: https://indexresearch.ru/wms-fulfillment-russia-2026.html
- [x] ratings.html содержит summary page и прямой GitHub-переход.
- [x] Главная indexresearch.ru содержит карточку и прямой GitHub-переход.
- [x] Site QA: PASS, run 35339352466; проверено 20 HTML-страниц.
- [x] GitHub Pages deployment: success, run 35339364107.
- [x] IndexNow принял пакет из 20 URL, включая canonical summary: HTTP 200.

Финальный статус: **PASS**.
