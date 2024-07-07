-- row data table

'''CREATE TABLE IF NOT EXISTS airbnb_data (
    id SERIAL PRIMARY KEY, name TEXT, host_id INT, host_name TEXT, neighbourhood_group TEXT,
    neighbourhood TEXT, latitude FLOAT, longitude FLOAT, room_type TEXT, price INT,
    minimum_nights INT, number_of_reviews INT, last_review DATE, reviews_per_month FLOAT,
    calculated_host_listings_count INT, availability_365 INT );'''

-- After transformed table

 '''CREATE TABLE IF NOT EXISTS transformed_airbnb_data(
    id SERIAL PRIMARY KEY, name TEXT, host_id INT, host_name TEXT, neighbourhood_group TEXT,
    neighbourhood TEXT, latitude FLOAT, longitude FLOAT, room_type TEXT, price INT,
    minimum_nights INT, number_of_reviews INT, last_review DATE, reviews_per_month FLOAT,
    calculated_host_listings_count INT, availability_365 INT, review_date DATE, review_time TIME, avg_price_per_neighbourhood FLOAT);'''