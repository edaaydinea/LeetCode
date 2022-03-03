SELECT w.id
FROM Weather w
         JOIN Weather p
              ON w.recordDate = DATE_ADD(p.recordDate, INTERVAL 1 DAY) AND
                 w.Temperature > p.Temperature