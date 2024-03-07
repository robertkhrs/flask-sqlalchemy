import flask

from data.db_session import create_session
from data.jobs import Jobs
from flask import jsonify

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    session = create_session()
    _jobs = session.query(Jobs).all()
    return jsonify({
        'data': [item.to_dict() for item in _jobs]
    })
