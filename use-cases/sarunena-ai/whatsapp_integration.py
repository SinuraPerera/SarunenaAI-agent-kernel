"""
SaruNena AI - WhatsApp Integration using Agent Kernel

This module provides WhatsApp integration for the SaruNena multi-agent system,
allowing farmers to interact via WhatsApp messages.
"""

import logging
import os
from flask import Flask, request, jsonify
from sarunena_kernel import SaruNenaOrchestrator, orchestrator

logger = logging.getLogger(__name__)


class WhatsAppIntegration:
    """
    WhatsApp integration handler for SaruNena using Agent Kernel.
    Processes incoming WhatsApp messages and routes them through the multi-agent system.
    """
    
    def __init__(self, app: Flask, orchestrator: SaruNenaOrchestrator):
        self.app = app
        self.orchestrator = orchestrator
        self.verify_token = os.getenv("WHATSAPP_VERIFY_TOKEN", "sarunena_verify_token")
        self._setup_routes()
        
    def _setup_routes(self):
        """Setup WhatsApp webhook routes."""
        
        @self.app.route("/webhook/whatsapp", methods=["GET"])
        def verify_webhook():
            """Verify WhatsApp webhook."""
            mode = request.args.get("hub.mode")
            token = request.args.get("hub.verify_token")
            challenge = request.args.get("hub.challenge")
            
            if mode == "subscribe" and token == self.verify_token:
                logger.info("Webhook verified successfully")
                return challenge, 200
            else:
                logger.warning("Webhook verification failed")
                return "Forbidden", 403
        
        @self.app.route("/webhook/whatsapp", methods=["POST"])
        async def handle_message():
            """Handle incoming WhatsApp messages."""
            try:
                data = request.get_json()
                
                # Extract message data
                entry = data.get("entry", [{}])[0]
                changes = entry.get("changes", [{}])[0]
                value = changes.get("value", {})
                
                messages = value.get("messages", [])
                
                if messages:
                    for message in messages:
                        await self._process_message(message, value)
                
                return jsonify({"status": "ok"}), 200
                
            except Exception as e:
                logger.error(f"Error handling WhatsApp message: {e}")
                return jsonify({"status": "error"}), 500
    
    async def _process_message(self, message: dict, value: dict):
        """Process individual WhatsApp message through the multi-agent system."""
        try:
            # Extract phone number and message content
            phone_number = message.get("from")
            message_id = message.get("id")
            
            # Get message text
            if message.get("type") == "text":
                text_obj = message.get("text", {})
                user_query = text_obj.get("body", "")
            else:
                logger.info(f"Received non-text message type: {message.get('type')}")
                user_query = "I sent an image/file. Please help me with my farming question."
            
            # Use phone number as farmer ID
            farmer_id = f"whatsapp_{phone_number}"
            
            logger.info(f"Processing message from {farmer_id}: {user_query}")
            
            # Process through SaruNena multi-agent system
            response = await self.orchestrator.process_farmer_query(farmer_id, user_query)
            
            # Send response back via WhatsApp
            await self._send_whatsapp_message(phone_number, response)
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
    
    async def _send_whatsapp_message(self, phone_number: str, message: str):
        """Send response message via WhatsApp API."""
        try:
            # In production, this would call the actual WhatsApp Business API
            # For now, we'll log the message that would be sent
            logger.info(f"WhatsApp Response to {phone_number}: {message}")
            
            # TODO: Implement actual WhatsApp API call
            # import requests
            # url = f"https://graph.facebook.com/v17.0/{os.getenv('WHATSAPP_PHONE_NUMBER_ID')}/messages"
            # headers = {
            #     "Authorization": f"Bearer {os.getenv('WHATSAPP_ACCESS_TOKEN')}",
            #     "Content-Type": "application/json"
            # }
            # data = {
            #     "messaging_product": "whatsapp",
            #     "to": phone_number,
            #     "text": {"body": message}
            # }
            # response = requests.post(url, json=data, headers=headers)
            # response.raise_for_status()
            
        except Exception as e:
            logger.error(f"Error sending WhatsApp message: {e}")


def setup_whatsapp_integration(app: Flask, orchestrator: SaruNenaOrchestrator):
    """
    Setup WhatsApp integration for the Flask app.
    
    Args:
        app: Flask application instance
        orchestrator: SaruNena orchestrator instance
    """
    return WhatsAppIntegration(app, orchestrator)
