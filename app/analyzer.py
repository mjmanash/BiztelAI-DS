class ChatAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_summary(self):
        return {"total_transcripts": len(self.data)}

    def analyze_transcript(self, transcript_id):
        transcript = self.data.get(transcript_id)
        if not transcript:
            return {"error": "Transcript not found"}
        agent1_msgs = sum(1 for m in transcript["content"] if m["agent"] == "agent_1")
        agent2_msgs = sum(1 for m in transcript["content"] if m["agent"] == "agent_2")
        agent1_sentiments = list({m["sentiment"] for m in transcript["content"] if m["agent"] == "agent_1"})
        agent2_sentiments = list({m["sentiment"] for m in transcript["content"] if m["agent"] == "agent_2"})
        return {
            "article_url": transcript["article_url"],
            "agent_1_message_count": agent1_msgs,
            "agent_2_message_count": agent2_msgs,
            "agent_1_sentiments": agent1_sentiments,
            "agent_2_sentiments": agent2_sentiments
        }
