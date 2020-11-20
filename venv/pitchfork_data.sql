SELECT reviewid, title AS album, artist, score, best_new_music, author, pub_day, pub_month, pub_year, genre, label
FROM reviews
LEFT JOIN genres
ON reviews.reviewid = genres.reviewid
LEFT JOIN labels
ON reviews.reviewid = labels.reviewid
