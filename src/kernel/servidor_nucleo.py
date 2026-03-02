import os
import sys
import time
import threading
import logging
import signal
from collections import deque
from typing import Dict, Any

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from dotenv import load_dotenv

# Meraki Platform Modules
# Using relative imports or adjusting sys.path carefully
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from meraki_platform.subscription_manager import meraki_sub_manager
from meraki_platform.payment_manager import meraki_payment_manager
from meraki_platform.community_module import meraki_community
from meraki_platform.home_service_engine import meraki_home_service

# Load environment variables
load_dotenv()

# =====================================================================
# VITALIS-PRIME: NEURO-HYBRID KERNEL (V2.0 PRO)
# ARCHITECT: JORGE HUMBERTO DAVALOS GONZALEZ
# ORGANIZATION: ORZWORKNET FOUNDATION
# =====================================================================

# Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
PORT = int(os.getenv("KERNEL_PORT", 5000))
DRIFT_THRESHOLD = float(os.getenv("DRIFT_THRESHOLD", 0.8))

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("VitalisKernel")

class AdvancedGenerator(nn.Module):
    """Deep latent representation extractor."""
    def __init__(self, input_dim: int, latent_dim: int, output_dim: int):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128), nn.ReLU(),
            nn.Linear(128, latent_dim), nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64), nn.ReLU(),
            nn.Linear(64, output_dim)
        )
    def forward(self, x):
        latent = self.encoder(x)
        logits = self.decoder(latent)
        return logits, latent

class LatentTransformer(nn.Module):
    """Aligns latent space with classical outputs."""
    def __init__(self, latent_dim: int, transformed_dim: int):
        super().__init__()
        self.transform = nn.Sequential(
            nn.Linear(latent_dim, transformed_dim),
            nn.LayerNorm(transformed_dim), nn.ReLU()
        )
    def forward(self, latent):
        return self.transform(latent)

class AttentionModule(nn.Module):
    """Dynamic model arbitration module."""
    def __init__(self, feature_dim: int, output_dim: int, n_models=2):
        super().__init__()
        self.attention = nn.Sequential(
            nn.Linear(feature_dim * n_models, 64), nn.Tanh(),
            nn.Linear(64, n_models), nn.Softmax(dim=1)
        )
        self.final_projection = nn.Linear(feature_dim, output_dim)

    def forward(self, features):
        combined = features.view(features.size(0), -1)
        weights = self.attention(combined)
        weighted_features = (features * weights.unsqueeze(2)).sum(dim=1)
        final_logits = self.final_projection(weighted_features)
        return final_logits, weights

class NeuroHybridSynchronizer:
    def __init__(self, input_dim: int, latent_dim: int, classical_dim: int, output_dim: int):
        self.generator = AdvancedGenerator(input_dim, latent_dim, output_dim)
        self.transformer = LatentTransformer(latent_dim, classical_dim)
        self.classical_model = RandomForestClassifier(n_estimators=50, warm_start=True)
        self.attention_module = AttentionModule(feature_dim=classical_dim, output_dim=output_dim)
        self.scaler = StandardScaler()

        self.optimizer = optim.Adam([
            {'params': self.generator.parameters()},
            {'params': self.transformer.parameters()},
            {'params': self.attention_module.parameters()}
        ], lr=0.005)
        self.criterion = nn.CrossEntropyLoss()

class VitalisKernelApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.dim_entrada = 3
        self.dim_latente = 8
        self.dim_clasica = 2
        self.dim_salida = 2

        self.sync = NeuroHybridSynchronizer(self.dim_entrada, self.dim_latente, self.dim_clasica, self.dim_salida)
        self.feedback_queue = deque()
        self.mem_x = deque(maxlen=2000)
        self.mem_y = deque(maxlen=2000)

        self.stats = {
            'batches': 0,
            'atn_gen': 0.5,
            'atn_rf': 0.5,
            'loss': 0.0,
            'running': True
        }

        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/api/v1/telemetria/feedback', methods=['POST'])
        def feedback():
            data = request.get_json(force=True, silent=True)
            if not data: return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400
            self.feedback_queue.append(data)
            return jsonify({'status': 'queued'}), 202

        @self.app.route('/api/v1/sistema/estado', methods=['GET'])
        def state():
            return jsonify({
                'queue_size': len(self.feedback_queue),
                'hybrid_metrics': {
                    'batches_processed': self.stats['batches'],
                    'atn_gen': self.stats['atn_gen'],
                    'atn_rf': self.stats['atn_rf'],
                    'current_loss': self.stats['loss']
                },
                'classical_memory_size': len(self.mem_x)
            })

        # --- Meraki Platform Endpoints ---

        @self.app.route('/api/v1/meraki/dentist/register', methods=['POST'])
        def meraki_register():
            data = request.get_json()
            d_id = data.get('dentist_id')
            email = data.get('email')
            if not d_id or not email:
                return jsonify({'status': 'error', 'message': 'Missing data'}), 400

            sub = meraki_sub_manager.register_dentist(d_id, email)
            return jsonify({'status': 'registered', 'subscription': sub}), 201

        @self.app.route('/api/v1/meraki/dentist/widgets', methods=['PUT'])
        def meraki_widgets():
            data = request.get_json()
            d_id = data.get('dentist_id')
            widgets = data.get('widgets', [])

            if not d_id or not meraki_sub_manager.check_access(d_id):
                return jsonify({'status': 'error', 'message': 'Access denied or missing ID'}), 403

            if meraki_sub_manager.update_widgets(d_id, widgets):
                return jsonify({'status': 'updated', 'widgets': widgets}), 200
            return jsonify({'status': 'error', 'message': 'Dentist not found'}), 404

        @self.app.route('/api/v1/meraki/patient/payment', methods=['POST'])
        def meraki_payment():
            data = request.get_json()
            d_id = data.get('dentist_id')
            p_name = data.get('patient_name')
            amount = data.get('amount')
            method = data.get('method', 'CASH')

            if not d_id or not meraki_sub_manager.check_access(d_id):
                return jsonify({'status': 'error', 'message': 'Access denied or missing ID'}), 403

            payment = meraki_payment_manager.add_patient_payment(d_id, p_name, amount, method)
            return jsonify({'status': 'payment_recorded', 'payment': payment}), 201

        @self.app.route('/api/v1/meraki/patient/ledger', methods=['GET'])
        def meraki_ledger():
            d_id = request.args.get('dentist_id')
            if not d_id or not meraki_sub_manager.check_access(d_id):
                return jsonify({'status': 'error', 'message': 'Access denied or missing ID'}), 403

            ledger = meraki_payment_manager.get_dentist_ledger(d_id)
            return jsonify({'status': 'success', 'ledger': ledger}), 200

        @self.app.route('/api/v1/meraki/community/post', methods=['POST'])
        def meraki_post():
            data = request.get_json()
            d_id = data.get('dentist_id')
            title = data.get('title')
            content = data.get('content')

            if not d_id or not meraki_sub_manager.check_access(d_id):
                return jsonify({'status': 'error', 'message': 'Access denied or missing ID'}), 403

            post = meraki_community.post_marketing(d_id, content, title)
            return jsonify({'status': 'posted', 'post': post}), 201

        @self.app.route('/api/v1/meraki/community/feed', methods=['GET'])
        def meraki_feed():
            return jsonify({'status': 'success', 'feed': meraki_community.get_community_feed()}), 200

        @self.app.route('/api/v1/meraki/home_service/find', methods=['GET'])
        def meraki_home_find():
            d_id = request.args.get('dentist_id')
            if not d_id or not meraki_sub_manager.check_access(d_id):
                return jsonify({'status': 'error', 'message': 'Access denied or missing ID'}), 403

            matches = meraki_home_service.find_matches(d_id)
            return jsonify({'status': 'success', 'matches': matches}), 200

        @self.app.route('/api/v1/meraki/home_service/offer', methods=['POST'])
        def meraki_home_offer():
            data = request.get_json()
            d_id = data.get('dentist_id')
            r_id = data.get('request_id')

            if not d_id or not meraki_sub_manager.check_access(d_id):
                return jsonify({'status': 'error', 'message': 'Access denied or missing ID'}), 403

            if meraki_home_service.offer_service(d_id, r_id):
                return jsonify({'status': 'offered', 'request_id': r_id}), 200
            return jsonify({'status': 'error', 'message': 'Service not found'}), 404

    def _worker_loop(self):
        logger.info("Kernel Synchronizer Worker active.")

        # Initial cold start
        x_init = np.random.rand(10, self.dim_entrada)
        y_init = np.random.randint(0, self.dim_salida, 10)
        self.sync.scaler.fit(x_init)
        self.sync.classical_model.fit(self.sync.scaler.transform(x_init), y_init)

        while self.stats['running']:
            if len(self.feedback_queue) >= 64:
                batch = [self.feedback_queue.popleft() for _ in range(64)]

                try:
                    x_batch = [[i['metricas_internas'].get('temperatura_q', 0),
                                i['metricas_internas'].get('entropia_shannon', 0),
                                i['metricas_internas'].get('amplitud_base', 0)] for i in batch]
                    y_batch = [1 if i['resultado_real'] == 'colapso_estable' else 0 for i in batch]

                    x_np = np.array(x_batch, dtype=np.float32)
                    y_np = np.array(y_batch, dtype=np.int64)

                    self.mem_x.extend(x_np)
                    self.mem_y.extend(y_np)

                    # Re-train classical every 10 batches
                    if self.stats['batches'] % 10 == 0:
                        x_h = self.sync.scaler.fit_transform(np.array(self.mem_x))
                        self.sync.classical_model.fit(x_h, np.array(self.mem_y))

                    x_t = torch.tensor(x_np)
                    y_t = torch.tensor(y_np)

                    # Model Fusion Inference & Training
                    probs_rf = self.sync.classical_model.predict_proba(self.sync.scaler.transform(x_np))
                    if probs_rf.shape[1] < self.dim_salida:
                        probs_rf = np.pad(probs_rf, ((0,0), (0, self.dim_salida - probs_rf.shape[1])), mode='constant')

                    c_feats = torch.tensor(probs_rf, dtype=torch.float32)

                    self.sync.generator.train()
                    self.sync.attention_module.train()
                    self.sync.optimizer.zero_grad()

                    logits_gen, latent = self.sync.generator(x_t)
                    trans_latent = self.sync.transformer(latent)

                    combined = torch.stack([trans_latent, c_feats], dim=1)
                    final_logits, attn_w = self.sync.attention_module(combined)

                    loss = self.sync.criterion(final_logits, y_t) + 0.4 * self.sync.criterion(logits_gen, y_t)
                    loss.backward()
                    self.sync.optimizer.step()

                    # Update Stats
                    self.stats['loss'] = round(loss.item(), 4)
                    weights = attn_w.detach().mean(axis=0).numpy()
                    self.stats['atn_gen'] = round(float(weights[0]), 3)
                    self.stats['atn_rf'] = round(float(weights[1]), 3)
                    self.stats['batches'] += 1

                    logger.debug(f"Batch {self.stats['batches']} | Loss: {self.stats['loss']} | Gen/RF Attention: {self.stats['atn_gen']}/{self.stats['atn_rf']}")

                    if self.stats['loss'] > DRIFT_THRESHOLD:
                        print(f"CRITICAL_DRIFT: {self.stats['loss']}") # Captured by Node.js spawn

                except Exception as e:
                    logger.error(f"Worker Error: {e}")
            else:
                time.sleep(0.1)

    def run(self):
        threading.Thread(target=self._worker_loop, daemon=True).start()
        logger.info(f"Vitalis-Prime Kernel starting on port {PORT}")
        self.app.run(port=PORT, debug=False, host='0.0.0.0')

if __name__ == "__main__":
    kernel = VitalisKernelApp()
    kernel.run()
