from flask import Blueprint
from flask import current_app as app

home_bp = Blueprint('home', __name__,
    template_folder='templates',
    static_folder='static')

@home_bp.route('/')
def index():
    return 'MUHU welcomes you!'