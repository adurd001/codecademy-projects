SELECT *
FROM stream
JOIN chat
	ON stream.device_id = chat.device_id;