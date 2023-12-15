from youtube_transcript_api import YouTubeTranscriptApi as yta

video_id = 'BmytbT9cim8'

try:
    data = yta.get_transcript(video_id, languages=['pt'])

    transcript = ' '.join([value['text'] for value in data])

    keyword_theme = input("Enter the desired theme: ").lower()

    occurrences_theme = [occurrence for occurrence in transcript.split('.') if keyword_theme in occurrence.lower()]

    with open(f"content_{keyword_theme.replace(' ', '_')}.txt", "w", encoding="utf-8") as file:
        file.write('\n'.join(occurrences_theme))

    print(f"Content related to the theme '{keyword_theme}' successfully saved in 'content_{keyword_theme.replace(' ', '_')}.txt'.")

except Exception as e:
    print(f"Error while obtaining transcript: {e}")
