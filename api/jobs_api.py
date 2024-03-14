import flask

from data.db_session import create_session
from data.jobs import Jobs
from flask import jsonify, make_response

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


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict()
        }
    )
