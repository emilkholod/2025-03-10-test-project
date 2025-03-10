WITH cte_phrases_delta_views as (
    SELECT
        phrase,
        toHour(dt) AS hour,
        (
            last_value(views) OVER (PARTITION BY phrase, toHour(dt) ORDER BY dt ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)
            - first_value(views) OVER (PARTITION BY phrase, toHour(dt) ORDER BY dt ROWS BETWEEN 1 PRECEDING AND CURRENT ROW)
        ) as views_by_ten_minutes,
        not toBool(
            6 - count() OVER (PARTITION BY phrase, toHour(dt))
        ) as full_hour
    FROM phrases_views final
    WHERE campaign_id = 1111111
        AND dt >= toDate('2025-01-01')
        AND dt < toDate('2025-01-01') + 1
    ORDER BY phrase, hour DESC
), cte_phrases_views_by_hours as (
    SELECT
        phrase,
        hour,
        sum(views_by_ten_minutes) as delta
    FROM cte_phrases_delta_views
    where full_hour
    group by phrase, hour
    order by phrase, hour desc
)

SELECT
    phrase,
    groupArray((hour, delta)) AS views_by_hour
FROM cte_phrases_views_by_hours
GROUP BY phrase
