#Use this sql cmd to average the day's moisture.

SELECT Avg(Moist) as Average from plant_log where Date(DateTime) = CURDATE();
