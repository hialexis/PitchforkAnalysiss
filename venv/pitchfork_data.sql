SELECT r.reviewid, REPLACE(title, " ep", "") AS album, artist, score, best_new_music, author, pub_day, pub_month, pub_year, g.genre, group_concat(label) as music_labels
FROM reviews r
LEFT JOIN labels l
ON r.reviewid = l.reviewid
LEFT JOIN genres g
ON r.reviewid = g.reviewid
GROUP BY r.reviewid, r.title
ORDER BY r.artist