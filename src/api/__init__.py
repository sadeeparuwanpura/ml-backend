from flask import Blueprint
from src.api.irrigation_routes import irrigation_bp
from src.api.health_routes import health_bp

def init_app(app):
    """Initialize all API routes"""
    # Register blueprints
    app.register_blueprint(irrigation_bp, url_prefix='/api/irrigation')
    app.register_blueprint(health_bp, url_prefix='/api/health')