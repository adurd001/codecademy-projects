Select  game,
	case game
		when 'League of Legends' then 'MOBA'
		when 'Dota 2' then 'MOBA'
		when 'Heroes of the Storm' then 'MOBA'
		when 'Counter-Strike: Global Offensive' then 'FPS'
		when 'DayZ' then 'Survival'
		when 'Survival Evolved' then 'Survival'
		ELSE 'Other'
		End AS 'genre',
		COUNT(*)
 FROM stream
 GROUP BY 1
 ORDER BY 3 DESC;