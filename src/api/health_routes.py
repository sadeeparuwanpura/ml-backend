from flask import Blueprint, jsonify
from src.models.model_registry import model_registry

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    try:
        # Check if models are loaded
        components = model_registry.get_irrigation_components()
        models_loaded = all(v is not None for v in components.values())
        
        return jsonify({
            'status': 'healthy' if models_loaded else 'unhealthy',
            'models_loaded': models_loaded
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500