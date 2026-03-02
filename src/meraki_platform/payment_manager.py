import logging
from typing import Dict, List, Any

# =====================================================================
# MERAKI SMILE DENTAL: PATIENT PAYMENT MANAGER
# HANDLING MEXICAN DENTAL CLINIC PAYMENTS
# =====================================================================

logger = logging.getLogger("MerakiPayments")

class PaymentManager:
    def __init__(self):
        # Maps dentist_id -> list of patients and their payments
        self.patient_records: Dict[str, List[Dict[str, Any]]] = {}

    def add_patient_payment(self, dentist_id: str, patient_name: str, amount: float, method: str):
        """Register a payment for a patient."""
        if dentist_id not in self.patient_records:
            self.patient_records[dentist_id] = []

        payment_entry = {
            "patient_name": patient_name,
            "amount": amount,
            "method": method,
            "timestamp": "2026-03-02", # Placeholder for real datetime
            "status": "PAID"
        }

        self.patient_records[dentist_id].append(payment_entry)
        logger.info(f"Registered payment of {amount} MXN for {patient_name} (Dentist: {dentist_id})")
        return payment_entry

    def get_dentist_ledger(self, dentist_id: str):
        """Returns the list of payments for a dentist."""
        return self.patient_records.get(dentist_id, [])

# Export instance
meraki_payment_manager = PaymentManager()
