SELECT game, count(*) as viewers, strftime('%Y-%m-%d', time) as date
FROM stream
WHERE strftime('%Y-%m-%d', time) >= '2015-01-01'
      AND strftime('%Y-%m-%d', time) < '2015-01-02'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;