import fitbit

if __name__ == "__main__":
    CLIENT_ID =  "22CYHK"
    CLIENT_SECRET  = "05ed6d78d685730df215d2d4fcb3fc01"
    ACCESS_TOKEN =  "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkNZSEsiLCJzdWIiOiI2U1c1QkciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTQxMTM0NzQxLCJpYXQiOjE1NDA1Mjk5OTd9.8xl4EAi3f5YambKMmlQN7fzASN7kgM28Me0Lgi5H4xY"
    REFRESH_TOKEN =  "48ac76489cbd1a5fd55475f42752067d15c62440e5beab8961eb6882eb7f712c"


    DATE = input("input date > ")
    start_time = "10:00"
    end_time = "10:01"

    authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='1min', start_time=start_time, end_time=end_time) #'1sec', '1min', or '15min'
    heart_sec = data_sec["activities-heart-intraday"]["dataset"]
    heart_sec[:10]
    print(heart_sec)