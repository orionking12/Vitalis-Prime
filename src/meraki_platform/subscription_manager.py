import os
import logging
from datetime import datetime, timedelta
from typing import Dict, Any

# =====================================================================
# MERAKI SMILE DENTAL: SUBSCRIPTION & TRIAL MANAGER
# ADAPTED FOR THE MEXICAN MARKET
# =====================================================================

logger = logging.getLogger("MerakiSubscription")

class SubscriptionManager:
    def __init__(self):
        # In a real scenario, this would be a database connection
        self.subscribers: Dict[str, Dict[str, Any]] = {}

    def register_dentist(self, dentist_id: str, email: str):
        """Register a new dentist and provide a 1-month free trial."""
        trial_end = datetime.now() + timedelta(days=30)

        self.subscribers[dentist_id] = {
            "email": email,
            "tier": "PREMIUM_TRIAL",
            "trial_expires": trial_end.isoformat(),
            "status": "ACTIVE",
            "widgets": [],
            "payment_methods_enabled": True
        }

        logger.info(f"Registered {dentist_id} for Meraki Smile Dental (1-month trial until {trial_end})")
        return self.subscribers[dentist_id]

    def check_access(self, dentist_id: str) -> bool:
        """Check if the dentist has active premium/trial access."""
        sub = self.subscribers.get(dentist_id)
        if not sub:
            return False

        expires = datetime.fromisoformat(sub["trial_expires"])
        if datetime.now() < expires:
            return True

        # If expired, downgrade or deactivate
        sub["tier"] = "FREE"
        sub["status"] = "EXPIRED"
        return False

    def update_widgets(self, dentist_id: str, widgets: list):
        """Allows dentists to customize their page with widgets."""
        if dentist_id in self.subscribers:
            self.subscribers[dentist_id]["widgets"] = widgets
            return True
        return False

# Export instance
meraki_sub_manager = SubscriptionManager()
