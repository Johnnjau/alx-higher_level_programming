-- Genres lists from database hbtn_0d_tvshows along with no of
-- shows linked to each.
-- Doesnt display genres without shows linked.
-- Records order descending nSELECT g.`name` AS `genre`,
SELECT g.`name` AS `genre`,
	COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
