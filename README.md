# podcast-crawler

![diagram](https://user-images.githubusercontent.com/933676/222932397-21b1a5f6-1a6c-4844-b521-c80d5cc79bc4.png)

## Fetch Genres Function
- GCP Function will fetch the genre index page
- It will then parse the text content for top genres IDs
- For each genre ID, publish that ID to the `genres` GCP topic
- This function can be triggered from an automated scheduler such as cron, either through HTTP or event-driven

## Fetch Podcasts Function
- GCP Function will recursively fetch each paginated page for each letter of a given genre ID
- It will parse the text content for podcast IDs
- For each podcast ID, publish that ID to the `podcasts` GCP topic!!

## Fetch Feed Function
- GCP Function will fetch podcast JSON for a given podcast ID
- Will fetch the XML RSS feed given the feed location in the JSON
- For each item in the feed, parse write the metadata to a CloudSQL table
- For each item in the feed, fetch the audio file and write to file Storage
