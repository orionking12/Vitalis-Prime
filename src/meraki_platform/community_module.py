import logging
from typing import Dict, List, Any

# =====================================================================
# MERAKI SMILE DENTAL: COMMUNITY & MARKETING
# SHARE MARKETING CAMPAIGNS ACROSS THE MEXICAN NETWORK
# =====================================================================

logger = logging.getLogger("MerakiCommunity")

class CommunityModule:
    def __init__(self):
        # Global marketing feed
        self.marketing_feed: List[Dict[str, Any]] = []

    def post_marketing(self, dentist_id: str, content: str, title: str):
        """Allows a dentist to share marketing material with the community."""
        post = {
            "dentist_id": dentist_id,
            "title": title,
            "content": content,
            "timestamp": "2026-03-02",
            "likes": 0
        }

        self.marketing_feed.append(post)
        logger.info(f"Dentist {dentist_id} shared a marketing post in Meraki Smile Dental community.")
        return post

    def get_community_feed(self):
        """Returns the latest marketing and community posts."""
        return sorted(self.marketing_feed, key=lambda x: x['timestamp'], reverse=True)

# Export instance
meraki_community = CommunityModule()
